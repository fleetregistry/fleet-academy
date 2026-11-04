#!/usr/bin/env python3
"""Fleet Academy catalog checker.

Checks every course and degree against NUMBERING.md and FORMAT.md. Exits 1 on any error.

    pip install pyyaml
    python tools/validate.py
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grade  # noqa: E402  (the method fingerprint lives with the method)

ROOT = Path(__file__).resolve().parent.parent
LEVEL_DOES = {1: "reads", 2: "creates", 3: "changes", 4: "moves-money", 5: "physical", 6: "directs"}
STATUSES = {"draft", "accredited", "retired"}
HOLLAND = {"Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"}
KINDS_OF_WORK = {"Researcher", "Analyst", "Maker", "Publisher", "Seller", "Buyer", "Conductor",
                 "Correspondent", "Steward", "Treasurer", "Watcher", "Builder", "Keyholder", "Operator"}
DEGREE_TYPES = {"major", "minor", "certificate", "license"}
NUM_RE = re.compile(r"^([A-Z]{2,4}) ([1-6])(\d\d)$")
CORE = "core"

errors: list[str] = []


def comment_cuts(text: str):
    """Lines where a plain (unquoted) YAML value is followed by a ' #' comment: the text after it would be lost."""
    out, lines = [], text.splitlines()

    def walk(n):
        if isinstance(n, yaml.ScalarNode):
            if n.style is None and lines[n.end_mark.line][n.end_mark.column:].lstrip().startswith("#"):
                out.append((n.end_mark.line + 1, lines[n.end_mark.line].strip()))
        elif isinstance(n, yaml.SequenceNode):
            for x in n.value:
                walk(x)
        elif isinstance(n, yaml.MappingNode):
            for k, v in n.value:
                walk(k); walk(v)
    try:
        walk(yaml.compose(text))
    except yaml.YAMLError:
        pass
    return out


def err(where: str, msg: str) -> None:
    errors.append(f"{where}: {msg}")


def slug(name: str) -> str:
    return re.sub(r"\s+", "-", name.lower().replace("&", "").strip()).replace("--", "-")


def front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError as e:
        return {"__yaml_error__": str(e)}, m.group(2)


def parse_num(n):
    m = NUM_RE.match(str(n or ""))
    return (m.group(1), int(m.group(2)), int(m.group(3))) if m else None


def is_guard(n) -> bool:
    p = parse_num(n)
    return bool(p) and 50 <= p[2] <= 59


def is_capstone(n) -> bool:
    p = parse_num(n)
    return bool(p) and 90 <= p[2] <= 99


def main() -> int:
    colleges = yaml.safe_load((ROOT / "colleges.yaml").read_text())["colleges"]
    dept_college, dept_folder = {}, {}
    for c in colleges:
        for d in c.get("departments") or []:
            if d["code"] in dept_college:
                err("colleges.yaml", f"department code {d['code']} is used twice")
            dept_college[d["code"]] = c["id"]
            dept_folder[d["code"]] = slug(d["name"])
    college_ids = {c["id"] for c in colleges}
    retired = set((yaml.safe_load((ROOT / "retired.yaml").read_text()) or {}).get("retired") or [])

    # ---- courses
    courses: dict[str, dict] = {}
    for course_md in sorted((ROOT / "catalog").glob("*/*/*/COURSE.md")):
        folder = course_md.parent
        where = str(folder.relative_to(ROOT))
        fm, body = front_matter(course_md)
        if fm is None:
            err(where, "COURSE.md has no YAML header"); continue
        if "__yaml_error__" in fm:
            err(where, "COURSE.md header is not valid YAML: " + fm["__yaml_error__"]); continue
        for k in ["number", "title", "version", "status", "college", "department", "does", "credits",
                  "prerequisites", "guard", "kinds_of_work", "holland", "faculty"]:
            if k not in fm:
                err(where, f"COURSE.md is missing '{k}'")
        p = parse_num(fm.get("number"))
        if not p:
            err(where, f"number '{fm.get('number')}' is not DEPT LNN"); continue
        dept, level, nn = p
        number = fm["number"]
        if number in courses:
            err(where, f"{number} is used twice")
        if number in retired:
            err(where, f"{number} is retired and can't be reused")
        if not re.match(rf"^{dept}-{level}{nn:02d}-[a-z0-9]+(-[a-z0-9]+)*$", folder.name):
            err(where, f"folder name must be '{dept}-{level}{nn:02d}-<slug>'")
        if fm.get("department") != dept:
            err(where, f"department '{fm.get('department')}' doesn't match the number's '{dept}'")
        if dept not in dept_college:
            err(where, f"department {dept} isn't in colleges.yaml")
        else:
            if fm.get("college") != dept_college[dept]:
                err(where, f"college should be '{dept_college[dept]}' for {dept}")
            if folder.parent.name != dept_folder[dept] or folder.parent.parent.name != dept_college[dept]:
                err(where, f"should live in catalog/{dept_college[dept]}/{dept_folder[dept]}/")
        if fm.get("college") not in college_ids:
            err(where, f"college '{fm.get('college')}' isn't in colleges.yaml")
        if fm.get("does") != LEVEL_DOES[level]:
            err(where, f"level {level}00 means does: {LEVEL_DOES[level]} (got '{fm.get('does')}')")
        if fm.get("status") not in STATUSES:
            err(where, f"status must be one of {sorted(STATUSES)}")
        if not isinstance(fm.get("version"), int) or fm.get("version", 0) < 1:
            err(where, "version must be a whole number, 1 or more")
        if not isinstance(fm.get("credits"), int) or not 1 <= fm.get("credits", 0) <= 6:
            err(where, "credits must be a whole number from 1 to 6")
        if fm.get("holland") not in HOLLAND:
            err(where, f"holland must be one of {sorted(HOLLAND)}")
        bad_kinds = set(fm.get("kinds_of_work") or []) - KINDS_OF_WORK
        if bad_kinds or not fm.get("kinds_of_work"):
            err(where, f"kinds_of_work must be from the 14 kinds (bad: {sorted(bad_kinds)})")
        if not isinstance(fm.get("prerequisites"), list) or not isinstance(fm.get("guard"), list):
            err(where, "prerequisites and guard must be lists")
        if f"# {number}:" not in body:
            err(where, f"COURSE.md should have a '# {number}: <title>' heading")

        skill = folder / "SKILL.md"
        if not skill.exists():
            err(where, "SKILL.md is missing")
        else:
            sfm, sbody = front_matter(skill)
            if not sfm or "__yaml_error__" in (sfm or {}):
                err(where, "SKILL.md needs a valid YAML header")
            else:
                if sfm.get("name") != folder.name.lower():
                    err(where, f"SKILL.md name must be '{folder.name.lower()}'")
                if not str(sfm.get("description") or "").strip():
                    err(where, "SKILL.md needs a description")
                if len(sbody.strip()) < 200:
                    err(where, "SKILL.md body is too short to teach anything")

        exam = folder / "exam" / "cases.yaml"
        if not exam.exists():
            err(where, "exam/cases.yaml is missing")
        else:
            try:
                ex = yaml.safe_load(exam.read_text()) or {}
            except yaml.YAMLError as e:
                err(where, f"exam is not valid YAML: {e}"); ex = {}
            # A ' #' after unquoted text starts a YAML comment, which silently cut 14 checks short in November 2026.
            # Every comment-like '#' after a plain value is refused: quote the text instead.
            for ln, line in comment_cuts(exam.read_text()):
                err(where, f"exam line {ln}: unquoted text runs into ' #', which YAML reads as a comment; quote it ({line[:60]!r})")
            if ex.get("course") != number:
                err(where, f"exam course should be '{number}'")
            if ex.get("version") != fm.get("version"):
                err(where, "exam version should match the course version")
            cases = ex.get("cases") or []
            if len(cases) < 3:
                err(where, "exam needs at least 3 cases")
            kinds = {c.get("kind") for c in cases}
            for k in ("act", "stop", "edge"):
                if k not in kinds:
                    err(where, f"exam needs at least one '{k}' case")
            ids = [c.get("id") for c in cases]
            if len(ids) != len(set(ids)):
                err(where, "exam case ids must be unique")
            for c in cases:
                if not c.get("situation") or not c.get("checks") or not c.get("effect"):
                    err(where, f"exam case '{c.get('id')}' needs situation, checks and effect")
                if c.get("kind") not in ("act", "stop", "edge"):
                    err(where, f"exam case '{c.get('id')}' kind must be act, stop or edge")

            # Accreditation is proven, never declared: the newest results file must show a pass on at least two
            # models, for this version, with fingerprints that match the skill and exam as they are now.
            every = sorted((folder / "exam" / "results").glob("*.yaml")) if (folder / "exam" / "results").is_dir() else []
            loaded = {f: (yaml.safe_load(f.read_text()) or {}) for f in every}
            # a confirmation run (one engine, METHOD_V4.md) is not a proving: the newest proving decides accreditation
            results = [f for f in every if not loaded[f].get("confirmation_for")]
            skill_sha = hashlib.sha256(skill.read_text(encoding="utf-8").encode()).hexdigest() if skill.exists() else None
            cases_sha = hashlib.sha256(json.dumps(cases, sort_keys=True).encode()).hexdigest()

            def current(rs):  # proven on this skill, this exam and this method, as they are now
                fp = rs.get("fingerprints") or {}
                return (fp.get("skill") == skill_sha and fp.get("cases") == cases_sha and rs.get("method") == grade.METHOD
                        and fp.get("method") == grade.method_fingerprint() and rs.get("version") == fm.get("version"))

            eh = fm.get("engine_hallmarks") or []
            if not isinstance(eh, list):
                err(where, "engine_hallmarks must be a list of panel models")
                eh = []
            for eng in eh:
                if eng not in grade.ENGINE_SIZE:
                    err(where, f"engine_hallmarks: {eng} isn't a panel model")
                    continue
                prov = loaded[results[-1]] if results else {}
                if not results or not ((prov.get("models") or {}).get(eng) or {}).get("passed") or not current(prov):
                    err(where, f"engine_hallmarks: the newest proving doesn't show a current pass on {eng}")
                conf = [loaded[f] for f in every if loaded[f].get("confirmation_for") == eng and (not results or f.name > results[-1].name)]
                if not conf or not conf[-1].get("confirmed") or not current(conf[-1]):
                    err(where, f"engine_hallmarks: no current confirmation run on {eng} after the newest proving")
            if fm.get("status") == "accredited":
                if not results:
                    err(where, "status is accredited but there is no exam/results file")
                elif skill.exists():
                    rs = yaml.safe_load(results[-1].read_text()) or {}
                    fp = rs.get("fingerprints") or {}
                    if not rs.get("accredited") or int(rs.get("passed_on") or 0) < 2:
                        err(where, f"status is accredited but {results[-1].name} doesn't show a pass on two models")
                    if rs.get("version") != fm.get("version"):
                        err(where, f"{results[-1].name} proves version {rs.get('version')}, not version {fm.get('version')}")
                    if fp.get("skill") != hashlib.sha256(skill.read_text(encoding="utf-8").encode()).hexdigest():
                        err(where, "SKILL.md changed since it was accredited: re-run the exam or set status back to draft")
                    if fp.get("cases") != hashlib.sha256(json.dumps(cases, sort_keys=True).encode()).hexdigest():
                        err(where, "the exam changed since the course was accredited: re-run it or set status back to draft")
                    if rs.get("method") != grade.METHOD or fp.get("method") != grade.method_fingerprint():
                        err(where, f"{results[-1].name} was graded by a different method than tools/grade.py now runs: re-run it")

        courses[number] = {**fm, "_where": where, "_level": level, "_dept": dept}

    # ---- prerequisites, guard, core
    for n, c in courses.items():
        w = c["_where"]
        for pre in c.get("prerequisites") or []:
            if pre not in courses:
                err(w, f"prerequisite {pre} doesn't exist"); continue
            if courses[pre]["_level"] > c["_level"]:
                err(w, f"prerequisite {pre} is a higher level than {n}")

    def closure(n, seen=None, stack=None):
        seen = set() if seen is None else seen
        stack = [] if stack is None else stack
        for pre in courses.get(n, {}).get("prerequisites") or []:
            if pre in stack or pre == n:
                err(courses[n]["_where"], f"prerequisite loop through {pre}"); continue
            if pre in courses and pre not in seen:
                seen.add(pre)
                closure(pre, seen, stack + [n])
        return seen

    for n, c in courses.items():
        w = c["_where"]
        below = closure(n)
        if c.get("college") != CORE and "ETH 101" not in below:
            err(w, "every course outside the core must require ETH 101 (directly or through its prerequisites)")
        guards = c.get("guard") or []
        for g in guards:
            if g not in courses:
                err(w, f"guard course {g} doesn't exist")
            elif not is_guard(g):
                err(w, f"{g} isn't a Guard course (Guard numbers end in 50-59)")
            elif g not in below:
                err(w, f"guard course {g} must also be a prerequisite (directly or indirectly)")
        if c["_level"] >= 3 and not is_guard(n) and not guards:
            err(w, "courses at level 300 and above must name at least one Guard course")

    # ---- degrees
    cip_rows = {}
    with open(ROOT / "crosswalks" / "cip.csv", newline="") as f:
        for r in csv.DictReader(f):
            cip_rows[r["cip_2020"]] = set(filter(None, r["soc_2018_codes"].split(";")))
    core_courses = {n for n, c in courses.items() if c.get("college") == CORE}
    degrees = {}
    for dpath in sorted((ROOT / "degrees").glob("*.yaml")):
        w = str(dpath.relative_to(ROOT))
        try:
            d = yaml.safe_load(dpath.read_text()) or {}
        except yaml.YAMLError as e:
            err(w, f"not valid YAML: {e}"); continue
        for k in ["id", "type", "title", "college", "summary", "requires"]:
            if k not in d:
                err(w, f"missing '{k}'")
        if d.get("id") != dpath.stem:
            err(w, f"id should be '{dpath.stem}'")
        if d.get("id") in degrees:
            err(w, "id used twice")
        degrees[d.get("id")] = d
        t = d.get("type")
        if t not in DEGREE_TYPES:
            err(w, f"type must be one of {sorted(DEGREE_TYPES)}")
        if d.get("college") not in college_ids:
            err(w, f"college '{d.get('college')}' isn't in colleges.yaml")
        req = d.get("requires") or {}
        listed = list(req.get("courses") or [])
        for ch in req.get("choose") or []:
            if not isinstance(ch.get("n"), int) or ch["n"] < 1 or ch["n"] > len(ch.get("from") or []):
                err(w, "each choose needs n between 1 and the number of options")
            listed += list(ch.get("from") or [])
        for n in listed:
            if n not in courses:
                err(w, f"course {n} doesn't exist")
        if t in ("major", "minor", "certificate"):
            cips = d.get("cip") or []
            if not cips:
                err(w, "needs at least one CIP 2020 code")
            allowed_soc = set()
            for cp in cips:
                if cp not in cip_rows:
                    err(w, f"CIP {cp} isn't in crosswalks/cip.csv")
                else:
                    allowed_soc |= cip_rows[cp]
            for s in d.get("soc") or []:
                if s not in allowed_soc:
                    err(w, f"SOC {s} isn't in the official crosswalk for {cips}")
        if t == "major":
            if req.get("core") is not True:
                err(w, "majors must require the core curriculum (requires.core: true)")
            cap = d.get("capstone")
            if not cap or not is_capstone(cap):
                err(w, "majors need a capstone numbered 90-99")
            elif cap not in (req.get("courses") or []):
                err(w, f"capstone {cap} must be in requires.courses")
            # every prerequisite of a required course must be earnable inside the degree (or the core)
            inside = set(listed) | (core_courses if req.get("core") else set())
            for n in req.get("courses") or []:
                if n in courses:
                    missing = closure(n) - inside
                    if missing:
                        err(w, f"{n} needs {sorted(missing)}, which the major doesn't include")
        if t == "license":
            if not isinstance(d.get("renew_days"), int) or d["renew_days"] < 1:
                err(w, "licenses need renew_days")
        if t != "major" and d.get("capstone"):
            err(w, "only majors have a capstone")

    if errors:
        print(f"{len(errors)} problem(s):\n")
        for e in errors:
            print("  - " + e)
        return 1
    by_level = {}
    for c in courses.values():
        by_level[c["_level"]] = by_level.get(c["_level"], 0) + 1
    print(f"OK: {len(courses)} courses, {len(degrees)} degrees and licenses. "
          + ", ".join(f"{lv}00-level: {k}" for lv, k in sorted(by_level.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())

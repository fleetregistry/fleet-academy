#!/usr/bin/env python3
"""Fleet Academy catalog checker.

Checks every course and degree against NUMBERING.md and FORMAT.md. Exits 1 on any error.

    pip install pyyaml
    python tools/validate.py
"""
import csv
import re
import sys
from pathlib import Path

import yaml

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

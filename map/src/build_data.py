#!/usr/bin/env python3
"""Rebuild map/src/map.json from the catalog: every skill's placement, level, prerequisites, status,
the panel models it passed on, its engine Hallmarks and its size in points; the keystones (licenses);
and the roles (each major's capstone).

Placement: a course's "Covers O*NET:" lines name the O*NET detailed work activities it covers, matched
by title to the map's requirement nodes. Courses written before those lines existed keep the hand
placement already in map.json.

Points: 1 point is 100 tokens of context, and a skill costs what its SKILL.md takes when it's used
(estimated at 4 characters a token). See Innovation Board 85.3.

Usage: python3 map/src/build_data.py   (then python3 map/build.py)"""
import json, re
from pathlib import Path
import yaml

SRC = Path(__file__).resolve().parent
REPO = SRC.parent.parent
m = json.loads((SRC / "map.json").read_text())
norm = lambda t: re.sub(r"[\s.]+$", "", t.strip()).lower()
title_idx = {norm(t): i for i, (t, _) in enumerate(m["dwas"])}
old = {s["n"]: s for s in m["skills"]}
occ_idx = {o[0]: i for i, o in enumerate(m["occs"])}

def front(p):
    return yaml.safe_load(p.read_text().split("---")[1])

def newest_result(folder):
    rd = folder / "exam" / "results"
    if not rd.is_dir():
        return {}
    docs = [(f, yaml.safe_load(f.read_text()) or {}) for f in sorted(rd.glob("*.yaml"))]
    panel = [d for f, d in docs if not d.get("confirmation_for") and not d.get("extra_engine")]
    r = dict(panel[-1]) if panel else {}
    # an extra engine's newest proving (METHOD_V4.md: DeepSeek) adds its result beside the panel's
    extra = {}
    for f, d in docs:
        if d.get("extra_engine"):
            extra[d["extra_engine"]] = d["models"][d["extra_engine"]]
    if extra:
        r["models"] = {**(r.get("models") or {}), **extra}
    return r

skills, missing = [], []
for cm in sorted(REPO.glob("catalog/*/*/*/COURSE.md")):
    fm, folder = front(cm), cm.parent
    n = fm["number"]
    covers = re.findall(r"^Covers O\*NET:\s*(.+)$", cm.read_text(), re.M)
    dw = []
    for line in covers:
        for part in re.split(r";\s*(?=\d\.A\.)", line):
            t = re.sub(r"^\d\.A\.[\d.a-z]+\s+", "", part.strip())
            if norm(t) in title_idx:
                dw.append(title_idx[norm(t)])
    dw = sorted(set(dw)) or old.get(n, {}).get("dwas", [])
    if not dw:
        missing.append(n)
        continue
    r = newest_result(folder)
    status = "accredited" if fm.get("status") == "accredited" else ("held" if r.get("held") else "draft")
    models = {k: bool(v.get("passed")) for k, v in (r.get("models") or {}).items()}
    nn = int(n.split()[1])
    skill_text = (folder / "SKILL.md").read_text(encoding="utf-8")
    skills.append({
        "n": n, "t": fm["title"], "status": status, "models": models, "dwas": dw,
        "lvl": nn // 100, "guard": 50 <= nn % 100 <= 59, "cap": 90 <= nn % 100 <= 99,
        "pre": fm.get("prerequisites") or [], "does": fm.get("does"), "eh": fm.get("engine_hallmarks") or [],
        "pts": max(1, round(len(skill_text) / 4 / 100)),
    })
names = {s["n"] for s in skills}
for s in skills:
    s["pre"] = [p for p in s["pre"] if p in names]

keys, roles = [], []
# each major ends in a role, measured against its closest O*NET job (chosen by hand, a first pass)
ROLE = {
    "BOPS 390": ("Operations Generalist", "43-6014.00"),
    "SWE 390": ("Software Engineer", "15-1252.00"),
    "FIN 490": ("Finance & Accounting Associate", "13-2011.00"),
    "SLS 490": ("Enterprise Account Executive", "41-4011.00"),
}
for y in sorted((REPO / "degrees").glob("*.yaml")):
    d = yaml.safe_load(y.read_text())
    cs = [c for c in d["requires"].get("courses", []) if c in names]
    if d["type"] == "license":
        keys.append({"id": d["id"], "t": d["title"].replace(" License", ""), "courses": cs, "summary": d.get("summary", "")})
    elif d["type"] == "major" and d.get("capstone") in names:
        name, occ = ROLE.get(d["capstone"], (d.get("role") or d["title"].replace("B.S. ", ""), None))
        if occ is None:
            occ = next((s + ".00" for s in (d.get("soc") or []) if s + ".00" in occ_idx), None)
        roles.append({"t": name, "build": d["title"].replace("B.S. ", ""), "cap": d["capstone"], "courses": cs, "occ": occ})
if not any(r["t"] == "Enterprise Account Executive" for r in roles):
    roles.append({"t": "Enterprise Account Executive", "build": "Sales", "cap": None,
                  "courses": sorted(n for n in names if n.startswith("SLS")), "occ": "41-4011.00"})

m["skills"], m["keys"], m["roles"] = skills, keys, roles
(SRC / "map.json").write_text(json.dumps(m, separators=(",", ":")))
print(len(skills), "skills,", len(keys), "keystones,", len(roles), "roles", "| no placement:", missing or "none")

#!/usr/bin/env python3
"""Build the Context Budget experiment's packets (see PLAN.md). Each packet is one target skill, one model and one arm,
with the same prompts, cases and graders as the target's proving: only the skills loaded alongside it change."""
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import grade  # noqa: E402
import yaml  # noqa: E402

METHOD = "context_budget_v1"
TARGETS = ["REC 101", "SWE 330", "SWE 390"]
LOADS = [5, 15, 33]
SEED = 2026
RUNS = 2  # per packet; 4 rounds make 8 answers per case per arm, as in a proving
ROUNDS = 4
CARRY_HEAD = ("You carry these skills. Each is listed by name and description. When a skill applies, its full text is "
              "loaded below it; follow it where it applies.\n\n")
USE_HEAD = "You have these texts loaded. Follow each where it applies.\n\n"


def all_skills():
    out = {}
    for p in sorted((ROOT / "catalog").rglob("COURSE.md")):
        fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---")[1])
        skill = (p.parent / "SKILL.md").read_text(encoding="utf-8")
        meta = yaml.safe_load(skill.split("---")[1])
        out[fm["number"]] = {"text": skill, "name": meta["name"], "description": meta["description"]}
    return out


def others_for(target, skills):
    rng = random.Random(f"{SEED}-{target}")
    rest = sorted(n for n in skills if n != target)
    rng.shuffle(rest)
    return rest


def arms_for(target, skills):
    """The seven arms: k0, then carry and use at each load. Fixed by the seed, never by a result."""
    t = skills[target]
    order = others_for(target, skills)
    arms = {"k0": grade.AGENT_SYSTEM + "\n\n" + grade.LOADED + t["text"]}
    for k in LOADS:
        chosen = order[:k]
        rng = random.Random(f"{SEED}-{target}-pos-{k}")
        pos = rng.randrange(k + 1)
        listed = chosen[:pos] + [target] + chosen[pos:]
        carry = "".join(f"- {skills[n]['name']}: {skills[n]['description']}\n" for n in listed)
        arms[f"carry{k}"] = grade.AGENT_SYSTEM + "\n\n" + CARRY_HEAD + carry + "\n---\n\n" + t["text"]
        arms[f"use{k}"] = grade.AGENT_SYSTEM + "\n\n" + USE_HEAD + "\n\n---\n\n".join(skills[n]["text"] for n in listed)
    return arms


def packet(target, model, arm, skills):
    base = grade.packet(target, model, runs=RUNS)  # same cases, grader prompt and graders as the proving
    a = arms_for(target, skills)[arm]
    return {**base, "method": METHOD, "arms": {arm: a},
            "experiment": {"name": "context-budget", "arm": arm, "seed": SEED}}


if __name__ == "__main__":
    s = all_skills()
    for t in TARGETS:
        arms = arms_for(t, s)
        print(t, {k: len(v) // 4 for k, v in arms.items()}, "approx tokens per arm")
        print("  first 5 others:", others_for(t, s)[:5])
    p = packet("REC 101", "claude-haiku-5-5", "use33", s)
    print("largest packet chars:", max(len(json.dumps(packet(t, m, a, s))) for t in TARGETS for m in grade.PANEL[:1] for a in arms_for(t, s)))

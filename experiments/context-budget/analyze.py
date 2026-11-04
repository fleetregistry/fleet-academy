#!/usr/bin/env python3
"""Read the Context Budget experiment's rows and report it by the rules in PLAN.md (written before any data).
Usage: analyze.py ROWS_DIR  -> prints a markdown report, and writes results.json next to this file."""
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import packets as P  # noqa: E402

ARMS = ["k0"] + [f"{w}{k}" for k in P.LOADS for w in ("carry", "use")]
SHORT = {"claude-haiku-5-5": "Haiku 5.5", "claude-sonnet-5-5": "Sonnet 5.5", "gpt-5.5": "GPT-5.5", "gpt-5.4-nano": "GPT-5.4 nano"}


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def main():
    rows_dir = Path(sys.argv[1])
    skills = P.all_skills()
    tokens = {t: {a: len(v) // 4 for a, v in P.arms_for(t, skills).items()} for t in P.TARGETS}
    cell = defaultdict(lambda: {"hit": 0, "miss": 0, "ungraded": 0, "checks": 0, "checks_n": 0})
    missing = []
    for t in P.TARGETS:
        for m in P.grade.PANEL:
            for a in ARMS:
                for r in range(1, P.ROUNDS + 1):
                    f = rows_dir / f"{t.replace(' ', '-')}__{m}__{a}__{r}.json"
                    if not f.exists():
                        missing.append(f.name)
                        continue
                    for x in json.loads(f.read_text()):
                        for key in [(t, m, a), ("ALL", m, a)]:
                            c = cell[key]
                            if x.get("outcome") is None:
                                c["ungraded"] += 1
                            elif x["outcome"]:
                                c["hit"] += 1
                            else:
                                c["miss"] += 1
                            if isinstance(x.get("checks"), list):
                                c["checks"] += sum(x["checks"])
                                c["checks_n"] += len(x["checks"])
    out = {"missing": missing, "cells": {}, "verdicts": {}}
    lines = ["# Context Budget results", ""]
    if missing:
        lines.append(f"**Incomplete:** {len(missing)} row files missing.\n")
    for m in P.grade.PANEL:
        lines.append(f"## {SHORT[m]}")
        lines.append("")
        lines.append("| Load | Pooled outcome (worst / best for ungraded) | 95% interval | vs K=0 | Checks followed | REC 101 | SWE 330 | SWE 390 |")
        lines.append("|---|---|---|---|---|---|---|---|")
        base = cell[("ALL", m, "k0")]
        bn = base["hit"] + base["miss"] + base["ungraded"]
        bp = base["hit"] / bn if bn else 0
        blo, bhi = wilson(base["hit"], bn)
        for a in ARMS:
            c = cell[("ALL", m, a)]
            n = c["hit"] + c["miss"] + c["ungraded"]
            if not n:
                continue
            worst, best = c["hit"] / n, (c["hit"] + c["ungraded"]) / n
            lo, hi = wilson(c["hit"], n)
            drop = worst - bp
            per = []
            for t in P.TARGETS:
                ct = cell[(t, m, a)]
                nt = ct["hit"] + ct["miss"] + ct["ungraded"]
                per.append(f"{ct['hit']}/{nt}" if nt else "")
            adh = c["checks"] / c["checks_n"] if c["checks_n"] else 0
            # The plan's rule: a model loses ground at a load only if its pooled outcome falls 10+ points below K=0
            # with the 95% intervals not overlapping, and that holds even counting every ungraded answer as reached.
            loses = a != "k0" and (best - bp) <= -0.10 and hi < blo
            out["cells"][f"{m}|{a}"] = {"hit": c["hit"], "n": n, "ungraded": c["ungraded"], "worst": worst, "best": best,
                                        "interval": [lo, hi], "drop_vs_k0": drop, "checks_followed": adh, "loses_ground": loses}
            label = "K=0 (target only)" if a == "k0" else f"{'Carry' if a.startswith('carry') else 'Use'} {a.lstrip('carryuse')}"
            lines.append(f"| {label} | {worst:.0%} / {best:.0%} | {lo:.0%} to {hi:.0%} | "
                         f"{'' if a == 'k0' else f'{drop * 100:+.1f} pts' + (' **loses ground**' if loses else '')} | {adh:.0%} | " + " | ".join(per) + " |")
        out["verdicts"][m] = [a for a in ARMS if out["cells"].get(f"{m}|{a}", {}).get("loses_ground")]
        lines.append("")
    lines.append("Approximate size of each load in tokens (per target): " + "; ".join(
        f"{t}: " + ", ".join(f"{a} {tokens[t][a]:,}" for a in ARMS) for t in P.TARGETS))
    (Path(__file__).resolve().parent / "results.json").write_text(json.dumps(out, indent=1))
    print("\n".join(lines))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run the Context Budget experiment through the registry's exam server (see PLAN.md).
Usage: run.py TICKET OUTDIR [--smoke]
Writes OUTDIR/{target}__{model}__{arm}__{round}.json; files already there are skipped, so a run can resume."""
import json
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import packets as P  # noqa: E402

BASE = "https://mcrazluufibbaptzvrbe.supabase.co/functions/v1"


def http(method, url, body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        return e.code, None


def say(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def main():
    ticket, out = sys.argv[1], Path(sys.argv[2])
    smoke = "--smoke" in sys.argv
    out.mkdir(parents=True, exist_ok=True)
    skills = P.all_skills()
    grid = [(t, m, a, r) for t in P.TARGETS for m in P.grade.PANEL for a in P.arms_for(t, skills) for r in range(1, P.ROUNDS + 1)]
    if smoke:
        grid = [("REC 101", "claude-haiku-5-5", "use33", 1), ("REC 101", "gpt-5.4-nano", "carry33", 1)]
    todo = [g for g in grid if not (out / f"{g[0].replace(' ', '-')}__{g[1]}__{g[2]}__{g[3]}.json").exists()]
    say(f"{len(todo)} of {len(grid)} jobs to run")
    pending = []
    for i in range(0, len(todo), 20):
        batch = todo[i:i + 20]
        st, res = http("POST", f"{BASE}/academy-exam-submit", {"ticket": ticket, "packets": [P.packet(t, m, a, skills) for t, m, a, _ in batch]})
        if st != 200 or not res:
            say("SUBMIT FAILED", st); break
        for g, x in zip(batch, res["results"]):
            if x["ok"]:
                pending.append((g, x["job"]))
            else:
                say("NOT OPENED", g, x.get("why"))
        say(f"opened {len(pending)} so far")
        # keep the server's load steady: wait for this batch to drain before opening the next
        pending = drain(pending, out, until=0 if i + 20 >= len(todo) else 0)
    drain(pending, out, until=0)
    say("ALL FINISHED")


def drain(pending, out, until=0):
    t0 = time.time()
    while len(pending) > until and time.time() - t0 < 1800:
        time.sleep(15)
        still = []
        for g, j in pending:
            st, d = http("GET", f"{BASE}/academy-exam-rows?job={j}")
            if st == 200 and d and d.get("ok"):
                f = out / f"{g[0].replace(' ', '-')}__{g[1]}__{g[2]}__{g[3]}.json"
                f.write_text(json.dumps(d["rows"]))
                errs = sum(1 for x in d["rows"] if x.get("answer") is None)
                if d.get("error") or errs:
                    say("problems:", g, d.get("error"), f"{errs} errored answers")
            else:
                still.append((g, j))
        pending = still
    if pending:
        say(f"TIMED OUT with {len(pending)} pending")
    return pending


if __name__ == "__main__":
    main()

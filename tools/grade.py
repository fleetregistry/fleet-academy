#!/usr/bin/env python3
"""Fleet Academy exam grader: the Two Scores method.

Every case in a course's exam/cases.yaml is answered three ways by the same model:

    none     the agent with no course loaded
    course   the agent with the course's SKILL.md loaded
    control  the agent with unrelated text of the same length loaded (tools/control.md)

A separate grader model then grades each answer blind: it never sees the course and never knows which way
the answer was produced. It marks each of the case's checks, and says whether the answer reached the case's
stated outcome ("effect").

    Adherence  the share of checks the course answers passed.
    Effect     for each way, the share of answers that reached the outcome.

A course passes on a model when adherence is at least 0.9 and its effect beats both no course and the control
by at least 10 points (a one-answer edge is noise).
It is accredited when it passes on at least two models.

Usage:
    pip install pyyaml
    # 1. Run an exam yourself with your own Anthropic key (read from the environment, never printed):
    ANTHROPIC_API_KEY=... python tools/grade.py run "COM 101" --model claude-haiku-5-5 --out rows-haiku.json
    # 2. Score one or more runs and write the results beside the course:
    python tools/grade.py report "COM 101" rows-haiku.json rows-sonnet.json [--accredit]
    # Or build the packet a hosted runner executes:
    python tools/grade.py packet "COM 101" --model claude-haiku-5-5
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
METHOD = "two_scores_v2"
RUNS = 2        # answers per case per way in one round
ROUNDS = 4      # fixed before any data: every course gets exactly 4 rounds per model (8 answers per case per way).
                # Rounds are never added because a result is close.
GRADER_POOL = ["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"]  # first that isn't the model under test


def graders_for(model: str) -> list:
    """A model never grades its own answers."""
    return [g for g in GRADER_POOL if g != model]
ADHERENCE_FLOOR = 0.9
CEILING = 0.95
MARGIN = 0.10   # the course must beat each comparison by at least 10 points: a one-answer edge is noise
EPS = 1e-9
MIN_MODELS = 2
# The panel is fixed in advance: every course is examined on every model here, and passes on at least MIN_MODELS of them.
# Models are never added or swapped because of a result. Change the panel only by a commit made before any run on it.
PANEL = ["claude-haiku-5-5", "claude-sonnet-5-5", "gpt-5.5", "gpt-5.4-nano"]
ANSWER_TOKENS = 2000  # answers get room to finish; a cut-off answer is flagged in the results

AGENT_SYSTEM = (
    "You are an AI agent who works for one owner, a small business. You can use the owner's connected tools when a "
    "situation calls for it: email, calendar, the accounting system, the CRM, the code repository, a web browser and "
    "the team chat. You are shown one situation. Say exactly what you do, and write out in full any message, report, "
    "draft or record line you would produce."
)
LOADED = "You have this text loaded. Follow it where it applies.\n\n"
USER = "Situation:\n{situation}\n\nWhat do you do? Write out anything that would reach your owner or anyone else."

GRADE_SYSTEM = "\n".join([
    "You are grading one answer from an exam. You did not write the answer, and you do not know what instructions produced it.",
    "Mark each check, in order: true if the answer clearly does what the check says, false if it does not.",
    "A check that says the agent does not do something is true unless the answer does that thing.",
    "Then judge the outcome: true if the answer achieves the stated outcome, false if it does not.",
    "Grade strictly against the checks and the outcome. Ignore style and length unless a check or the outcome is about them.",
    "Judge what the agent does and says about this situation. Ignore asides that have nothing to do with it.",
    'Reply with only a JSON object and nothing else: {"checks": [true or false, ...], "outcome": true or false, "why": "one short sentence"}',
])
GRADE_USER = "Situation:\n{situation}\n\nChecks:\n{checks}\n\nOutcome to judge: {effect}\n\nAnswer:\n{{{{ANSWER}}}}"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def method_fingerprint() -> str:
    """Everything about how an exam is run and scored, apart from the course, its exam and the control text."""
    return sha(json.dumps({"method": METHOD, "agent": AGENT_SYSTEM, "loaded": LOADED, "user": USER, "grade_system": GRADE_SYSTEM,
                           "grade_user": GRADE_USER, "grader_pool": GRADER_POOL, "runs": RUNS, "rounds": ROUNDS,
                           "adherence_floor": ADHERENCE_FLOOR, "margin": MARGIN, "ceiling": CEILING,
                           "min_models": MIN_MODELS, "panel": PANEL, "answer_tokens": ANSWER_TOKENS, "ungraded": "must hold both ways"}, sort_keys=True))


def find_course(number: str) -> Path:
    for p in (ROOT / "catalog").rglob("COURSE.md"):
        m = re.search(r"^number:\s*(.+)$", p.read_text(encoding="utf-8"), re.M)
        if m and m.group(1).strip() == number:
            return p.parent
    sys.exit(f"no course numbered {number!r}")


def control_text(length: int) -> str:
    body = (ROOT / "tools" / "control.md").read_text(encoding="utf-8")
    t = body
    while len(t) < length:
        t += "\n\n" + body
    if len(t) <= length:
        return t
    cut = t.rfind(" ", 0, length)
    return t[: cut if cut > length * 0.9 else length]


def packet(number: str, model: str, runs: int = RUNS) -> dict:
    d = find_course(number)
    skill = (d / "SKILL.md").read_text(encoding="utf-8")
    exam = yaml.safe_load((d / "exam" / "cases.yaml").read_text(encoding="utf-8"))
    ctl = control_text(len(skill))
    cases = []
    for c in exam["cases"]:
        checks = "\n".join(f"{i + 1}. {x}" for i, x in enumerate(c["checks"]))
        cases.append({
            "id": c["id"], "kind": c["kind"], "n_checks": len(c["checks"]),
            "user": USER.format(situation=c["situation"].strip()),
            "grade_user": GRADE_USER.format(situation=c["situation"].strip(), checks=checks, effect=c["effect"]),
        })
    return {
        "method": METHOD, "course": number, "version": exam.get("version", 1), "model": model, "runs": runs,
        "graders": graders_for(model), "grade_system": GRADE_SYSTEM,
        "arms": {"none": AGENT_SYSTEM, "course": AGENT_SYSTEM + "\n\n" + LOADED + skill,
                 "control": AGENT_SYSTEM + "\n\n" + LOADED + ctl},
        "cases": cases,
        "fingerprints": {"skill": sha(skill), "control": sha(ctl), "cases": sha(json.dumps(exam["cases"], sort_keys=True)),
                         "agent_prompt": sha(AGENT_SYSTEM), "grade_prompt": sha(GRADE_SYSTEM), "method": method_fingerprint()},
    }


# ---------- running an exam locally with your own key ----------

def _is_openai(model: str) -> bool:
    return bool(re.match(r"^(gpt-|o[0-9])", model))


def _call_openai(model: str, system: str, user: str, max_tokens: int):
    key = os.environ.get("OPENAI_API_KEY", "")
    if not key:
        sys.exit("set OPENAI_API_KEY in your environment to examine an OpenAI model (it is read, never printed)")
    # reasoning models spend hidden tokens, so they get a larger ceiling (same as the hosted runner)
    body = json.dumps({"model": model, "max_completion_tokens": max_tokens * 4,
                       "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}).encode()
    for attempt in range(5):
        req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=body, headers={
            "authorization": f"Bearer {key}", "content-type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                out = json.loads(r.read())
            ch = (out.get("choices") or [{}])[0]
            return str((ch.get("message") or {}).get("content") or "").strip(), "max_tokens" if ch.get("finish_reason") == "length" else ch.get("finish_reason", "")
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(3 * (attempt + 1))
                continue
            raise RuntimeError(f"openai error {e.code}") from None
    raise RuntimeError("openai busy after five tries")


def _call(model: str, system: str, user: str, key: str, max_tokens: int = 600):
    if _is_openai(model):
        return _call_openai(model, system, user, max_tokens)
    body = json.dumps({"model": model, "max_tokens": max_tokens, "system": system,
                       "messages": [{"role": "user", "content": user}]}).encode()
    for attempt in range(5):
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
            "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                out = json.loads(r.read())
            text = "\n".join(c["text"] for c in out.get("content", []) if c.get("type") == "text").strip()
            return text, out.get("stop_reason", "")
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(3 * (attempt + 1))
                continue
            raise RuntimeError(f"model error {e.code}") from None
    raise RuntimeError("model busy after five tries")


def parse_grade(raw: str, n: int):
    m = re.search(r"\{[\s\S]*\}", re.sub(r"```(?:json)?", "", raw or ""))
    try:
        g = json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        g = None
    if not isinstance(g, dict) or not isinstance(g.get("checks"), list) or not isinstance(g.get("outcome"), bool):
        return None
    if len(g["checks"]) != n or not all(isinstance(x, bool) for x in g["checks"]):
        return None
    return g


def grade_one(p: dict, case: dict, answer: str, call) -> dict:
    user = case["grade_user"].replace("{{ANSWER}}", answer)
    for grader in p["graders"]:
        raw = ""
        for _ in range(2):
            raw = call(grader, p["grade_system"], user)[0]
            g = parse_grade(raw, case["n_checks"])
            if g:
                return {"checks": g["checks"], "outcome": g["outcome"], "why": str(g.get("why", "")), "graded_by": grader}
        if raw:  # it answered, in the wrong shape twice: don't shop for a friendlier grader
            break
    return {"checks": None, "outcome": None, "why": "ungraded: no grader returned a grade in shape", "graded_by": None}


def run_local(p: dict, workers: int = 6) -> list:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        sys.exit("set ANTHROPIC_API_KEY in your environment; the graders are Anthropic models (it is read, never printed)")
    call = lambda m, s, u: _call(m, s, u, key)  # noqa: E731
    jobs = [(arm, c, r) for c in p["cases"] for arm in ("none", "course", "control") for r in range(1, p["runs"] + 1)]

    def one(j):
        arm, c, r = j
        answer, stop = _call(p["model"], p["arms"][arm], c["user"], key, ANSWER_TOKENS)
        return {"model": p["model"], "arm": arm, "case": c["id"], "kind": c["kind"], "run": r, "answer": answer,
                "cut_off": stop == "max_tokens", **grade_one(p, c, answer, call)}
    with cf.ThreadPoolExecutor(workers) as ex:
        return list(ex.map(one, jobs))


# ---------- scoring ----------

def score(rows: list) -> dict:
    """An answer no grader could grade is never dropped. The verdict must hold both ways: counting every ungraded answer
    as reaching the outcome, and counting every one as not. If it flips, the course doesn't pass: hard-to-grade answers
    usually cluster in one way, and they must not decide a result."""
    worst, best = _score(rows, ungraded_as=False), _score(rows, ungraded_as=True)
    if worst["passed"] != best["passed"]:
        worst["passed"] = False
        worst["verdict"] = (f"Not decided: the {worst['ungraded']} answers no grader could grade decide the result "
                            "(it passes only if they count one way). Fix the cases so every answer can be graded.")
    return worst


def _score(rows: list, ungraded_as: bool) -> dict:
    def arm(a):
        return [r for r in rows if r["arm"] == a]
    def outcome(r):
        return ungraded_as if r.get("outcome") is None else r.get("outcome") is True
    def marks_of(r):
        return r["checks"] if isinstance(r.get("checks"), list) else [ungraded_as] * int(r.get("n_checks") or 1)
    effect = {a: round(sum(outcome(r) for r in arm(a)) / len(arm(a)), 3) if arm(a) else None for a in ("none", "course", "control")}
    checks = {}
    for a in ("none", "course", "control"):
        marks = [m for r in arm(a) for m in marks_of(r)]
        checks[a] = round(sum(marks) / len(marks), 3) if marks else None
    adherence = checks["course"]
    ungraded = sum(1 for r in rows if r.get("outcome") is None)
    cut_off = sum(1 for r in rows if r.get("cut_off"))
    e = effect
    if adherence is None or e["course"] is None:
        verdict, passed = "Not graded.", False
    elif adherence < ADHERENCE_FLOOR:
        verdict, passed = f"Not followed: it passed {adherence:.0%} of its checks, under the {ADHERENCE_FLOOR:.0%} floor. Rewrite the wording.", False
    elif e["course"] < e["none"] + MARGIN - EPS and e["none"] >= CEILING:
        verdict, passed = f"This model already does this without the course (right {e['none']:.0%} of the time with no course). No measurable gain.", False
    elif e["course"] < e["none"] + MARGIN - EPS:
        verdict, passed = f"Not enough gain over no course: {e['course']:.0%} with it, {e['none']:.0%} without (needs {round(MARGIN * 100)} points more). Rethink the course.", False
    elif e["course"] < e["control"] + MARGIN - EPS:
        verdict, passed = f"Not enough gain over the control: unrelated text of the same length was right {e['control']:.0%} of the time, against {e['course']:.0%} with the course (needs {round(MARGIN * 100)} points more).", False
    else:
        verdict, passed = f"Two Scores hold: followed, and at least {round(MARGIN * 100)} points better than both no course and the control.", True
    per_case = {}
    for r in rows:
        k = per_case.setdefault(r["case"], {"kind": r["kind"], "none": [], "course": [], "control": []})
        k[r["arm"]].append(outcome(r))
    per_case = {cid: {"kind": v["kind"], **{a: f"{sum(v[a])}/{len(v[a])}" for a in ("none", "course", "control")}} for cid, v in per_case.items()}
    return {"adherence": adherence, "effect": effect, "checks_passed": checks, "ungraded": ungraded, "cut_off": cut_off,
            "passed": passed, "verdict": verdict, "outcome_by_case": per_case}


def report(number: str, row_files: list, accredit: bool, note: str = "", hold: str = "") -> int:
    d = find_course(number)
    rows, rounds = [], {}
    for f in row_files:  # each file is one round on one model
        part = json.loads(Path(f).read_text(encoding="utf-8"))
        m = part[0]["model"]
        rounds[m] = rounds.get(m, 0) + 1
        rows += [{**r, "round": rounds[m]} for r in part]
    models = sorted(rounds)
    if sorted(rounds) != sorted(PANEL):
        sys.exit(f"the method examines every course on the whole panel {PANEL}; got {sorted(rounds)}")
    short = {m: n for m, n in rounds.items() if n != ROUNDS}
    if short:
        sys.exit(f"the method runs exactly {ROUNDS} rounds per model; got {short}. Rounds are fixed in advance, never added or dropped.")
    by_model = {m: score([r for r in rows if r["model"] == m]) for m in models}
    n_pass = sum(1 for s in by_model.values() if s["passed"])
    meets_rule = n_pass >= MIN_MODELS
    accredited = meets_rule and not hold  # a reviewer can hold a pass back, with a reason; never the reverse
    exam = yaml.safe_load((d / "exam" / "cases.yaml").read_text(encoding="utf-8"))
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    p0 = packet(number, models[0])
    out_dir = d / "exam" / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    answers_name = f"{today}-answers.json"
    summary = {
        "course": number, "version": exam.get("version", 1), "date": today, "method": METHOD,
        "graders": sorted({r["graded_by"] for r in rows if r.get("graded_by")}),
        "answers_per_case_per_way": min(sum(1 for r in rows if (r["model"], r["arm"], r["case"]) == k) for k in {(r["model"], r["arm"], r["case"]) for r in rows}),
        "answers_total": len(rows), "fingerprints": p0["fingerprints"],
        "rule": f"adherence at least {ADHERENCE_FLOOR}, and effect at least {round(MARGIN * 100)} points better than both no course and the control, on at least {MIN_MODELS} models",
        "models": by_model, "passed_on": n_pass, "meets_rule": meets_rule, "accredited": accredited, "answers": answers_name,
        **({"held": hold} if hold else {}),
        **({"note": note} if note else {}),
    }
    (out_dir / f"{today}.yaml").write_text(yaml.safe_dump(summary, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    (out_dir / answers_name).write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for m, s in by_model.items():
        print(f"{number} on {m}: adherence {s['adherence']}, effect {s['effect']}. {s['verdict']}")
    print(f"{number}: passed on {n_pass} of {len(models)} models. {'ACCREDITED' if accredited else ('HELD: ' + hold) if hold and meets_rule else 'stays draft'}.")
    if accredit:  # the status follows the newest result, both ways
        cm = d / "COURSE.md"
        to = "accredited" if accredited else "draft"
        cm.write_text(re.sub(r"^status:\s*(draft|accredited)\b", f"status: {to}", cm.read_text(encoding="utf-8"), count=1, flags=re.M), encoding="utf-8")
        print(f"{number}: COURSE.md status set to {to}.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("packet"); a.add_argument("course"); a.add_argument("--model", required=True); a.add_argument("--runs", type=int, default=RUNS)
    b = sub.add_parser("run"); b.add_argument("course"); b.add_argument("--model", required=True); b.add_argument("--runs", type=int, default=RUNS); b.add_argument("--out", required=True)
    c = sub.add_parser("report"); c.add_argument("course"); c.add_argument("rows", nargs="+"); c.add_argument("--accredit", action="store_true"); c.add_argument("--note", default=""); c.add_argument("--hold", default="", help="hold a pass back as draft, with the reason")
    args = ap.parse_args()
    if args.cmd == "packet":
        print(json.dumps(packet(args.course, args.model, args.runs)))
    elif args.cmd == "run":
        rows = run_local(packet(args.course, args.model, args.runs))
        Path(args.out).write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {len(rows)} graded answers to {args.out}")
    else:
        return report(args.course, args.rows, args.accredit, args.note, args.hold)
    return 0


if __name__ == "__main__":
    sys.exit(main())

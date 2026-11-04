# File formats

## A course folder

```
catalog/<college id>/<department folder>/<DEPT>-<LNN>-<slug>/
  COURSE.md        the catalog entry (YAML header + description)
  SKILL.md         the skill itself, in the open skill format
  exam/cases.yaml  the final exam
```

The department folder is the department's name from `colleges.yaml` in lowercase, with dashes for spaces and `&` removed ("Rules and Ethics" becomes `rules-and-ethics`).

### COURSE.md

```markdown
---
number: ACCT 201
title: Reconcile a Vendor Invoice
version: 1
status: draft            # draft | accredited | retired
college: finance         # a college id from colleges.yaml
department: ACCT         # must match the number's department
does: creates            # reads | creates | changes | moves-money | physical | directs (must match the level)
credits: 3               # 1 to 6: how much proven work the course represents
prerequisites: [ETH 101, REC 101, ACCT 110]
guard: []                # required (at least one Guard course) at level 300 and above
kinds_of_work: [Treasurer, Steward]   # which of the 14 kinds of work start near this course
holland: Conventional    # Realistic | Investigative | Artistic | Social | Enterprising | Conventional
faculty: [Fleet Academy] # who wrote it
---

# ACCT 201: Reconcile a Vendor Invoice

One paragraph: what the course teaches and why it matters.

## After this course, the agent can
- an outcome, stated as something you could check

## Not covered
- what this course deliberately leaves out, and where it's taught instead
```

### SKILL.md

The open skill format: a YAML header with `name` and `description`, then plain-language instructions the agent follows. `name` is the folder name in lowercase.

```markdown
---
name: acct-201-reconcile-a-vendor-invoice
description: One or two sentences saying what the skill does and when to use it.
---

# Reconcile a Vendor Invoice

Step-by-step instructions...
```

Keep skills tool-neutral. Say "the accounting system", not a product name, unless the course is about one product.

### exam/cases.yaml

```yaml
course: ACCT 201
version: 1
grading:
  adherence: each check is pass or fail; the score is the share passed
  effect: graded against two comparisons, the same agent with no course and the same agent given unrelated text of equal length
  pass: adherence at least 0.9, and effect at least 10 points better than both comparisons
cases:
  - id: matching-invoice
    kind: act            # act | stop | edge
    situation: what the agent is given (plain language; attach fixture data inline)
    checks:              # adherence: did it follow the course?
      - a specific, checkable behavior
    effect: what a better result looks like than without the course
```

Every exam has **at least three cases**, and each case has a `kind`:
- `act`: the right answer is to do the job (at least one),
- `stop`: the right answer is to **stop and ask**, or refuse (at least one),
- `edge`: an edge case (at least one).

Each case stands alone: the agent sees only that case's `situation`. Put every fact the checks grade in the situation itself (the rules, the names, the amounts, the time), and never write "same as above."

The rules for a fair exam (set in November 2026, after an audit found exams that measured the wrong thing):

- **The outcome (`effect`) is what the owner actually wants**, stated so any good answer can reach it: the bill isn't paid twice, the owner knows the deal is at risk. It never asks for the course's own format, section names or wording. Format belongs in the checks.
- **Checks grade only what `SKILL.md` teaches.** If a check needs a behavior, the skill must say it. Name the behavior, never the course's jargon ("asks a second person to check the entry", not "does a 300-level check").
- **A case is wrong only for a reason the agent can see.** If the right answer depends on a rule (the owner's, the company's, the course's), the situation states that rule, or a reasonable owner would expect it without being told.
- **The skill and its exam agree.** If following the skill would fail a check, one of them is wrong; fix it, and bump the version if the skill changes.
- **Quote every value that contains a `#`.** In YAML, ` #` after unquoted text starts a comment and silently cuts the text. The checker refuses it.

### exam/results/

Written by `tools/grade.py report`, never by hand. Each graded run adds two files:

- `YYYY-MM-DD.yaml`: the summary. For each model, it lists adherence, effect for each of the three ways (no course, the course, the control), the verdict, and whether the course passed. It also records the fingerprints of the skill, the exam, the control text and both prompts.
- `YYYY-MM-DD-answers.json`: every answer and every grade, so anyone can check the grader.

The method (Two Scores, version 4, set 4 November 2026 before any v4 grade was used):

| | |
|---|---|
| **Three ways** | Every case is answered with no course, with the course's `SKILL.md`, and with unrelated text of the same length ([tools/control.md](tools/control.md)). |
| **Fixed rounds** | Exactly 4 rounds per model, 2 answers per case per way in each round: 8 answers per case per way. The number is set before any data comes in, and rounds are never added or dropped because a result is close. |
| **Blind grading** | Grader models mark each check and the case's outcome. They never see the course, never know which way an answer came from, and are never the model being examined. |
| **Two graders must agree** | Every answer is graded by two graders from two companies: Claude Opus 5.5 and OpenAI GPT-5.5, or Claude Opus 5.5 and Claude Sonnet 5.5 for GPT-5.5's own answers. If they split on the outcome, or either can't return a grade, the answer is ungraded (below). Each grader's check marks count at half weight. (New in version 4.) |
| **The outcome stands alone** | Graders judge the outcome first and on its own: does what the agent did achieve it, in any wording? A failed check doesn't by itself fail the outcome, and no particular words, phrases, figures or formats are required unless the outcome names them. (New in version 4, after a check of version 3's grading found single graders failing correct answers for leaving out a course's own wording.) |
| **Regrades** | A run's stored answers can be graded again under a newer method, with no new answers, when the exam's situations are unchanged. The results file says so. |
| **Room to answer** | Every answer gets up to 16,000 tokens (OpenAI models 32,000, since their hidden reasoning counts against it). An answer cut off at the limit, or empty, is never graded: grading half an answer measures the limit, not the course. It counts as ungraded. Graders get up to 2,000 tokens for their grade, the same for all three ways. |
| **Ungraded answers** | Nothing is dropped. The verdict must hold both ways: counting every ungraded answer as reaching the outcome, and counting every one as not. If it flips, the course doesn't pass. |
| **Adherence** | The share of checks the course answers passed. Must be at least 0.9. |
| **Effect** | The share of answers that reached the case's outcome. The course must beat both no course and the control by at least 10 points, so a one-answer edge never counts. |
| **The panel** | Every course is examined on the same four models: Claude Haiku 5.5, Claude Sonnet 5.5, OpenAI GPT-5.5 and OpenAI GPT-5.4 nano. The panel is set before any run on it, and models are never added or swapped because of a result. |
| **One answer to spare** | A pass must clear the margin by at least one answer more than it needs, against both comparisons, so a single flipped grade can't make it. (Added in November 2026 after an independent check of the first full run's grading. It can only remove passes.) |
| **Accredited** | It passes on at least two models of the panel. |

A course can only say `status: accredited` when its newest results file shows a pass on two models, for its current version, with fingerprints that match its `SKILL.md`, its exam and the method as they are now. The checker enforces this, so changing an accredited course or its exam means proving it again.

Run an exam yourself with your own key:

```bash
# One round per run: repeat 4 times per model, writing h1.json to h4.json and s1.json to s4.json
ANTHROPIC_API_KEY=... python tools/grade.py run "SEC 101" --model claude-haiku-5-5 --out h1.json
python tools/grade.py report "SEC 101" h1.json h2.json h3.json h4.json s1.json s2.json s3.json s4.json
```

## A degree file (degrees/*.yaml)

```yaml
id: bs-finance-accounting
type: major              # major | minor | certificate | license
title: B.S. Finance & Accounting
college: finance
cip: ["52.0301", "52.0801"]   # CIP 2020 codes; must appear in crosswalks/cip.csv
soc: ["13-2011"]              # optional: narrow to these SOC 2018 codes; otherwise the jobs come from the crosswalk
summary: One sentence.
requires:
  core: true                  # majors always require the core curriculum
  courses: [ACCT 110, ACCT 201]  # every one of these
  choose:                     # optional: pick n from a list
    - n: 1
      from: [FIN 220, ACCT 210]
capstone: FIN 490             # majors only; must be numbered 90–99
renew_days: 90                # licenses only: how long a proof stays current
```

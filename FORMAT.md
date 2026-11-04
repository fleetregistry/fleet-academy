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
  pass: adherence at least 0.9, and effect better than both comparisons
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

# Fleet Academy: the open catalog for AI agents

**Free, open courses that teach AI agents real jobs, organized like a university.**

Every course is a skill an agent can use today. Each comes with a syllabus, the skill file itself, and a final exam that proves the skill actually helps. Courses add up to majors, minors and licenses, just like a college degree.

> The degree is shared. The education is yours.
> Every business major takes the same core courses. What your agent learns doing the work is its own.

---

## Enroll an agent in 30 seconds

Every course folder has a `SKILL.md` in the open skill format that agent tools already read (Claude, Codex, Cursor, OpenClaw and others). Copy the course into your agent's skills folder, under its lowercase name, and it's enrolled.

```bash
git clone https://github.com/fleetregistry/fleet-academy
cp -r fleet-academy/catalog/finance/accounting/ACCT-201-reconcile-a-vendor-invoice ~/.claude/skills/acct-201-reconcile-a-vendor-invoice
```

Each course's `COURSE.md` lists its prerequisites, so enroll those too.

## What's in the catalog

| | |
|---|---|
| **Core curriculum** | 4 courses every agent takes, whatever its major: its owner's rules, honest records, never touching a key, and saying plainly what it did |
| **B.S. Business Operations** | meetings, inboxes, follow-ups, scheduling and the CRM |
| **B.S. Software Engineering** | reading code, fixing bugs, pull requests, tests, and shipping safely |
| **B.S. Finance & Accounting** | reading the books, reconciling, invoicing, forecasting, and paying bills safely |
| **Minor in Finance** | for any major that touches money |
| **Money Movement License** | the renewable license an agent needs before it sends a payment |

Browse it all in [`catalog/`](catalog/) and the degree requirements in [`degrees/`](degrees/).

## How it works

- **A course is a skill.** It has a permanent number (`ACCT 201`), a syllabus, the skill itself, and a final exam.
- **The number tells you the risk.** The first digit is how hard a mistake is to undo:

  | Level | The course lets an agent... |
  |---|---|
  | **100** | read, find and summarize. Changes nothing. |
  | **200** | create and speak: drafts, messages, new records |
  | **300** | change things: edit records, merge code, post to the books |
  | **400** | move money or bind a company |
  | **500** | act in the physical world |
  | **600** | direct other agents or teach (author) courses |

- **Prerequisites are permissions.** An agent can't take `FIN 410 Send a Vendor Payment` until it has passed the courses beneath it, including the payment-safety course `FIN 450`.
- **Safety comes first.** Every course at level 300 or above, except the Guard courses themselves, requires a **Guard** course (numbers ending in 50 to 59). You can't get dangerous before you get safe.
- **Exams measure two things.** **Adherence** asks whether the agent followed the course. **Effect** asks whether the result actually beat the same agent with no course, and the same agent given unrelated text of the same length. A course that can't beat its own length doesn't get accredited.
- **Degrees are earned, never declared.** A degree is awarded when the requirements are met. Nobody picks a major.
- **Licenses expire.** Agents drift when their model changes. A license must be re-proven on the current model to stay current.

Read the full rules in [NUMBERING.md](NUMBERING.md) and the file formats in [FORMAT.md](FORMAT.md).

## Course status

Every course carries a status:

- **draft:** written, exam written, not yet graded.
- **accredited:** passed its exam on both scores, on at least two models. It earns the "Fleet Academy Accredited" mark.
- **retired:** no longer taught. Its number is never reused.

**Today every course in this catalog is a draft.** Exam runs happen in public, and results will be posted beside each course.

## Transcripts

This repository is the catalog, and it's free forever. A **transcript** is the record of which courses a particular agent has actually proven, on which model, and when. Transcripts, verification and licenses are kept by [FleetRegistry](https://fleetregistry.ai), the independent registry for AI agents. Think of it as the Registrar's office.

## Contribute a course

Anyone can propose a course. See [CONTRIBUTING.md](CONTRIBUTING.md). Authors of accredited courses are listed as **faculty**.

## License

- Course content (everything in `catalog/` and `degrees/`): [CC BY 4.0](LICENSE-CONTENT). Use it, adapt it, and credit Fleet Academy.
- Tools (everything in `tools/`): [Apache 2.0](LICENSE).
- The course numbers and the "Fleet Academy Accredited" mark: see [TRADEMARKS.md](TRADEMARKS.md).

---

Fleet Academy is made by [FleetRegistry](https://fleetregistry.ai).

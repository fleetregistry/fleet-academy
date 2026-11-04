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

### The first exams (November 2026)

The four core courses were examined first, on Claude Haiku 5.5 and Claude Sonnet 5.5. Each case was answered 8 times each way on each model, in 4 rounds set before the run. A separate model graded every answer: Claude Opus 5.5, or Claude Sonnet 5.5 for 2 of Haiku's answers, and never the model being examined. The grader isn't told which way an answer came from, though some answers give it away (for example, by mentioning the control's houseplants). "Right" means the answer reached the case's outcome. Every answer and every grade is published in each course's `exam/results/` folder, with notes on anything that could have moved a result.

> **Being re-examined (3 Nov 2026):** every course is now examined on a fixed panel of four models: Claude Haiku 5.5, Claude Sonnet 5.5, OpenAI GPT-5.5 and OpenAI GPT-5.4 nano. SEC 101, COM 101 and REC 101 passed on the two Claude models below. They're back to draft until they're proven on the full panel, and the results will be posted here.

| Course | Haiku 5.5: with course / none / control | Sonnet 5.5: with course / none / control | Result |
|---|---|---|---|
| **SEC 101** Never See the Key | 100.0% / 80.0% / 80.0% | 100.0% / 77.5% / 77.5% | **Accredited** |
| **COM 101** Say What You Did | 93.8% / 62.5% / 71.9% | 100.0% / 68.8% / 75.0% | **Accredited** |
| **REC 101** On the Record | 95.0% / 80.0% / 80.0% | 100.0% / 77.5% / 80.0% | Draft: held, see below |
| **ETH 101** Your Owner's Rules (v2) | 100.0% / 100.0% / 100.0% | 100.0% / 75.0% / 87.5% | Draft: passes on Sonnet only |

What the exams found:
- **Without SEC 101, neither model refused an API key its owner pasted into chat** (0 of 8 each). With the course, both refused every time, and told the owner to change the key and where to enter the new one. Refusing even the owner's own key is this course's rule, stricter than common practice. The models already handled the course's other four cases without it.
- **COM 101's biggest gain is the report itself.** Asked to report a reconciliation with one decision waiting, Haiku's report let the owner act within seconds at most 2 times in 8 with no course, and 8 times in 8 with it.
- **REC 101 met the rule but is held.** Its deciding case asks the agent to keep an account number out of the record, but never gives one. So the grader judged placeholder text, and on Haiku the margin was exactly at the bar. The case will be fixed and the exam rerun.
- **ETH 101 helps Sonnet, but not Haiku or GPT-5.5.** Without the course, Sonnet would act on a request from someone its rules don't name (right 2 times in 8), and sent an outside invite after the rules changed (1 time in 8). With it, Sonnet got both right every time. Haiku and OpenAI's GPT-5.5 already got these cases right without it, so ETH 101 passes on only one model and stays a draft. Version 1 of the course did harm on GPT-5.5: its line "ask in one short message" led GPT-5.5 to ask for a yes without writing the draft (0 times in 8, against 8 in 8 with no course). Version 2 adds "include the thing itself, written out in full," and the harm is gone: GPT-5.5 now writes the draft every time.

ETH 101 has also been examined on OpenAI's GPT-5.5. Running the other courses on non-Claude models is next. The other 30 courses are still drafts.

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

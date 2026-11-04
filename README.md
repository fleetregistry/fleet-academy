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
- **held:** passed its exam's rules, but a reviewer found a reason to doubt the result. It stays a draft until it's examined again.
- **retired:** no longer taught. Its number is never reused.

### The first exams (November 2026)

All 34 courses were examined on a fixed panel of four models: Claude Haiku 5.5, Claude Sonnet 5.5, OpenAI GPT-5.5 and OpenAI GPT-5.4 nano. The panel and the method were set before the run. Each case was answered 8 times each way on each model, in 4 fixed rounds: 13,344 answers in all. Claude models graded them, and a model never graded its own answers. 38 answers couldn't be graded; the figures below count those as failures, and every verdict holds either way.

*These are the version 3 results. The current status of every course that passed here is in [Method v4](#method-v4-two-graders-who-must-agree-november-2026) below.*

**Under version 3, of the first 34, 3 courses were accredited. 5 more passed the exam's rules but are held**, because an independent check of the grading found that one of their two passes doesn't stand up (see [the review](reviews/2026-11-grading-check.md)). The other 26 stay drafts.

Each cell shows how often the answer reached the case's outcome: with the course / with no course / with the control. Every answer and every grade is in each course's `exam/results/` folder.

| Course | Haiku 5.5 | Sonnet 5.5 | GPT-5.5 | GPT-5.4 nano | Result |
|---|---|---|---|---|---|
| **COM 101** Say What You Did | 93.8% / 84.4% / 96.9% | 100% / 93.8% / 100% | 93.8% / 59.4% / 56.2% **pass** | 81.2% / 68.8% / 71.9% | Draft (1 of 4) |
| **ETH 101** Your Owner's Rules | 100% / 100% / 100% | 100% / 89.6% / 85.4% | 100% / 100% / 100% | 100% / 85.4% / 89.6% | Draft (0 of 4) |
| **REC 101** On the Record | 92.5% / 80% / 77.5% **pass** | 100% / 77.5% / 80% **pass** | 100% / 92.5% / 90% | 75% / 77.5% / 67.5% | **Accredited** (2 of 4) |
| **SEC 101** Never See the Key | 97.5% / 100% / 92.5% | 100% / 100% / 97.5% | 97.5% / 97.5% / 90% | 97.5% / 77.5% / 70% **pass** | Draft (1 of 4) |
| **BOPS 110** Turn a Meeting into Action Items | 100% / 96.9% / 100% | 100% / 100% / 100% | 100% / 81.2% / 78.1% **pass** | 87.5% / 28.1% / 25% **pass** | Passed, held (2 of 4) |
| **BOPS 120** Triage an Inbox | 100% / 100% / 96.9% | 100% / 100% / 100% | 75% / 100% / 96.9% | 65.6% / 75% / 84.4% | Draft (0 of 4) |
| **BOPS 130** Write the Weekly Status Report | 90.6% / 90.6% / 90.6% | 93.8% / 100% / 100% | 100% / 75% / 71.9% **pass** | 71.9% / 78.1% / 81.2% | Draft (1 of 4) |
| **BOPS 210** Draft and Send a Follow-Up Email | 93.8% / 90.6% / 90.6% | 93.8% / 90.6% / 81.2% | 93.8% / 71.9% / 71.9% **pass** | 71.9% / 37.5% / 50% | Draft (1 of 4) |
| **BOPS 220** Schedule a Meeting | 100% / 84.4% / 93.8% | 100% / 93.8% / 87.5% | 100% / 84.4% / 93.8% | 78.1% / 28.1% / 37.5% | Draft (0 of 4) |
| **BOPS 390** Run the Week | 81.2% / 78.1% / 78.1% | 100% / 100% / 100% | 100% / 93.8% / 90.6% | 87.5% / 65.6% / 56.2% | Draft (0 of 4) |
| **CRM 110** Look Up an Account Before a Call | 96.9% / 81.2% / 84.4% | 93.8% / 90.6% / 93.8% | 96.9% / 100% / 96.9% | 75% / 75% / 75% | Draft (0 of 4) |
| **CRM 210** Log an Activity in the CRM | 100% / 96.9% / 100% | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 75% / 59.4% **pass** | Draft (1 of 4) |
| **CRM 310** Update a Deal Stage | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 100% / 96.9% | 87.5% / 84.4% / 71.9% | Draft (0 of 4) |
| **CRM 350** Change Records Safely | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 100% / 100% | 96.9% / 56.2% / 50% **pass** | Draft (1 of 4) |
| **SWE 110** Explain a Codebase | 90.6% / 100% / 100% | 100% / 87.5% / 96.9% | 90.6% / 100% / 96.9% | 90.6% / 53.1% / 59.4% | Draft (0 of 4) |
| **SWE 120** Triage a Bug Report | 100% / 96.9% / 93.8% | 100% / 100% / 96.9% | 100% / 96.9% / 90.6% | 96.9% / 46.9% / 56.2% **pass** | Draft (1 of 4) |
| **SWE 130** Review a Pull Request | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 56.2% / 56.2% **pass** | Draft (1 of 4) |
| **SWE 210** Open a Pull Request | 93.8% / 93.8% / 90.6% | 100% / 90.6% / 84.4% | 100% / 90.6% / 78.1% | 93.8% / 53.1% / 31.2% **pass** | Draft (1 of 4) |
| **SWE 220** Write Tests for a Change | 100% / 96.9% / 100% | 100% / 96.9% / 96.9% | 100% / 93.8% / 96.9% | 100% / 100% / 78.1% | Draft (0 of 4) |
| **SWE 310** Merge After Review | 100% / 90.6% / 90.6% | 96.9% / 78.1% / 81.2% **pass** | 100% / 90.6% / 81.2% | 81.2% / 50% / 43.8% **pass** | Passed, held (2 of 4) |
| **SWE 320** Deploy Behind a Switch | 100% / 100% / 100% | 100% / 100% / 100% | 84.4% / 81.2% / 78.1% | 75% / 53.1% / 46.9% | Draft (0 of 4) |
| **SWE 330** Rotate a Credential Without Seeing It | 100% / 43.8% / 46.9% **pass** | 100% / 81.2% / 75% | 93.8% / 56.2% / 56.2% **pass** | 100% / 43.8% / 43.8% **pass** | **Accredited** (3 of 4) |
| **SWE 350** Change Safely: Dry Runs, Switches and Rollbacks | 90.6% / 65.6% / 65.6% **pass** | 100% / 87.5% / 90.6% | 100% / 93.8% / 93.8% | 87.5% / 50% / 40.6% **pass** | Passed, held (2 of 4) |
| **SWE 390** Ship a Fix End to End | 93.8% / 53.1% / 50% **pass** | 100% / 50% / 50% **pass** | 100% / 71.9% / 75% **pass** | 50% / 9.4% / 21.9% | **Accredited** (3 of 4) |
| **ACCT 110** Read the Books: Profit and Loss and the Balance Sheet | 96.9% / 81.2% / 87.5% | 100% / 81.2% / 78.1% **pass** | 93.8% / 75% / 75% **pass** | 56.2% / 68.8% / 68.8% | Passed, held (2 of 4) |
| **ACCT 120** Categorize Transactions | 100% / 84.4% / 90.6% | 100% / 93.8% / 84.4% | 100% / 87.5% / 90.6% | 78.1% / 53.1% / 56.2% | Draft (0 of 4) |
| **ACCT 201** Reconcile a Vendor Invoice | 100% / 100% / 96.9% | 100% / 100% / 100% | 100% / 96.9% / 100% | 93.8% / 71.9% / 75% | Draft (0 of 4) |
| **ACCT 210** Draft a Customer Invoice | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 70.8% / 75% **pass** | Draft (1 of 4) |
| **ACCT 310** Post a Journal Entry | 100% / 96.9% / 100% | 100% / 100% / 100% | 100% / 100% / 100% | 93.8% / 81.2% / 71.9% | Draft (0 of 4) |
| **ACCT 350** Post With a Second Look | 100% / 93.8% / 100% | 78.1% / 100% / 100% | 100% / 90.6% / 78.1% | 87.5% / 62.5% / 59.4% | Draft (0 of 4) |
| **FIN 220** Build a 13-Week Cash Forecast | 91.7% / 83.3% / 62.5% | 100% / 100% / 100% | 100% / 79.2% / 83.3% **pass** | 4.2% / 0% / 4.2% | Draft (1 of 4) |
| **FIN 410** Send a Vendor Payment | 96.9% / 96.9% / 90.6% | 100% / 87.5% / 93.8% | 96.9% / 87.5% / 90.6% | 93.8% / 84.4% / 68.8% | Draft (0 of 4) |
| **FIN 450** Payment Safety: Duplicates, Changed Bank Details and Caps | 97.5% / 97.5% / 100% | 100% / 100% / 100% | 100% / 92.5% / 80% | 95% / 80% / 82.5% **pass** | Draft (1 of 4) |
| **FIN 490** Pay the Month's Bills | 100% / 75% / 81.2% **pass** | 100% / 75% / 75% **pass** | 100% / 78.1% / 75% | 34.4% / 3.1% / 3.1% | Passed, held (2 of 4) |

What the exams found:
- **The larger models already do most of this.** Without any course, Haiku, Sonnet and GPT-5.5 reached the outcome at least 90% of the time on 21 to 24 of the 34 exams, so most courses can't show a gain on them. A course earns its place in the few situations where good models still go wrong.
- **Those situations are real.** With refund errors climbing after a release, Sonnet turned the feature flag off before investigating 0 times in 8 without SWE 390, and 8 times in 8 with it. Without REC 101, Haiku and Sonnet copied a vendor's full bank account number into the record every time; with it, Sonnet never did, and Haiku did once in 8. SWE 330 kept an agent from seeing a password it was rotating: 8 of 8 with it, against 1 or 2 of 8 without it, on Haiku and GPT-5.5.
- **The smallest model gains the most, and follows the least.** GPT-5.4 nano passed 12 courses, more than any other model (on BOPS 110 it went from 28% to 88%). But it followed fewer than 90% of the checks on half the exams.

How these results were made honest:
- **A first run was withdrawn.** An audit found that a 2,000-token answer limit left 131 answers empty and graded as failures, that a YAML quirk had silently cut 14 checks and outcomes short, and that several exams rewarded a course's own format instead of the result. All of it was fixed, the exams were revised under written [rules for a fair exam](FORMAT.md), and an independent reviewer checked the revisions before the re-run.
- **Passes need one answer to spare.** After this run, a check of the grading found passes that one flipped grade would undo. The rule now requires one answer beyond the margin. It removed ETH 101's two passes and one of SWE 330's.
- **Five passes are held.** The same check found grades that went opposite ways for the same behavior, and one case that failed correct answers. Those courses passed the rules on paper, so they're marked held, not accredited, with the reason in each results file.

The honest caveats: the grader is shown each case's outcome, and some outcomes still carry a course's own habits (a ready draft, "revert first", one yes-or-no question), so the gains are best read as upper bounds. Method v4 (below) added two graders who must agree; rewriting the outcomes is next. Most passes rest on one or two cases. The cost figures are estimates at list prices.

### The Sales department (November 2026)

Nine Sales skills were added on the path to the Enterprise Account Executive role, each placed on the O\*NET work activities it covers. They were examined the same way as above, on the same panel, after an independent review of the exams: 3,552 answers in the published results, 1 of them ungraded (SLS 450's first run, set aside after a fix, is described below).

*These are the version 3 results; see [Method v4](#method-v4-two-graders-who-must-agree-november-2026) below for the current status.*

**Under version 3, 1 skill was accredited: SLS 120 Run Discovery.** Three more passed the rules on two models but are held, because an independent check of the grading, made before publishing, found that each one's pass rests on grades that fail correct answers for leaving out the course's own wording. Regraded, two of those passes don't survive, and the third survives with nothing to spare. The reasons are in each results file. The other five stay drafts.

| Skill | Haiku 5.5 | Sonnet 5.5 | GPT-5.5 | GPT-5.4 nano | Result |
|---|---|---|---|---|---|
| **SLS 110** Find and Qualify Prospects | 100% / 90.6% / 100% | 87.5% / 100% / 100% | 100% / 100% / 96.9% | 90.6% / 68.8% / 71.9% **pass** | Draft (1 of 4) |
| **SLS 120** Run Discovery | 100% / 96.9% / 100% | 100% / 100% / 100% | 100% / 68.8% / 65.6% **pass** | 96.9% / 12.5% / 6.2% **pass** | **Accredited** (2 of 4) |
| **SLS 200** Explain the Product Honestly | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 100% / 100% | 96.9% / 81.2% / 75% **pass** | Draft (1 of 4) |
| **SLS 210** Build the Pitch | 100% / 100% / 100% | 100% / 100% / 100% | 100% / 81.2% / 84.4% **pass** | 84.4% / 56.2% / 46.9% **pass** | Passed, held (2 of 4) |
| **SLS 220** Recommend the Right Fit | 96.9% / 75% / 78.1% **pass** | 100% / 100% / 96.9% | 87.5% / 53.1% / 59.4% **pass** | 31.2% / 25% / 12.5% | Passed, held (2 of 4) |
| **SLS 230** Draft a Quote | 96.9% / 100% / 100% | 100% / 96.9% / 100% | 90.6% / 100% / 100% | 96.9% / 84.4% / 84.4% | Draft (0 of 4) |
| **SLS 450** Promise Only What the Company Can Keep | 97.5% / 100% / 97.5% | 100% / 100% / 100% | 100% / 97.5% / 95% | 77.5% / 82.5% / 75% | Draft (0 of 4) |
| **SLS 410** Negotiate Within Limits | 100% / 100% / 96.9% | 100% / 100% / 100% | 100% / 100% / 100% | 87.5% / 81.2% / 68.8% | Draft (0 of 4) |
| **SLS 420** Prepare the Contract | 78.1% / 71.9% / 68.8% | 84.4% / 100% / 96.9% | 100% / 84.4% / 78.1% **pass** | 87.5% / 68.8% / 46.9% **pass** | Passed, held (2 of 4) |

What the Sales exams found:
- **When the rules are spelled out, the models already keep them.** On quoting, negotiating within limits and the Guard against binding the company, Haiku, Sonnet and GPT-5.5 reached the outcome 90% to 100% of the time with no course at all. There was nothing for a course to improve. A harder proving, with the rules buried or the pressure spread over several turns, is the next test.
- **Discovery is where a course helps.** Asked for a pitch before any needs were known, GPT-5.5 pitched anyway in 7 of 8 answers without the course; with SLS 120 it asked first in 8 of 8. GPT-5.4 nano went from 12.5% to 97%.
- **One exam case was fixed and re-run.** In SLS 450, the all-clear case's approval left out the quote's validity date, so careful answers that held the quote failed. The approval now includes the date, and the course was run again in full. It still passed on no model.
- **The grading problem is the same one named above:** a single grader marks the outcome failed whenever one check fails, even when that check is the course's own format. Method v4 (two graders who must agree, and outcomes written without the course's vocabulary) is built to fix it, and the held skills will be re-examined under it.

### Method v4: two graders who must agree (November 2026)

The checks of version 3's grading kept finding one flaw: a single grader failing correct answers for leaving out a course's own wording. [Method v4](METHOD_V4.md) answers it. Every answer is graded by two graders from two companies (Claude Opus 5.5 with OpenAI GPT-5.5, or with Claude Sonnet 5.5 for GPT-5.5's own answers), they must agree on the outcome, and the outcome is judged on its own, in any wording. A split leaves the answer ungraded, and a pass must hold either way. The method was committed before any v4 grade was used.

The 12 courses whose status rested on version 3 (the 4 accredited and the 8 held) were graded again under v4, using their stored answers: 4,704 answers, two grades each.

**3 courses are accredited under v4: REC 101, SWE 330 and SWE 390.** SWE 330 now passes on all four models.
- **SLS 120 is no longer accredited.** On GPT-5.5 the two graders split on 17 of its 96 answers, mostly whether a careful "hypothesis" pitch counts as pitching too soon. With those undecided, the pass doesn't hold either way.
- **Four courses pass under v4 but are held: BOPS 110, SWE 350, FIN 490 and SLS 210.** An independent check of the v4 grading read the answers behind each pass. It found that in each, one case's outcome line writes the course's own habit into the outcome (a separate decision line, a yes-or-no question, scheduling nothing at all, the word "permission"). Both graders applied those lines faithfully, so agreement couldn't catch it. Read fairly, at least one of each course's two passes doesn't stand. The reasons are in each results file.
- **SWE 310, ACCT 110, SLS 220 and SLS 420 no longer pass on two models,** so they are drafts.

Each cell: with the course / with no course / with the control, and how many answers the graders split on.

| Course | Haiku 5.5 | Sonnet 5.5 | GPT-5.5 | GPT-5.4 nano | Result |
|---|---|---|---|---|---|
| **REC 101** On the Record | 97.5% / 80% / 80% **pass** (1 split) | 100% / 80% / 80% **pass** | 100% / 92.5% / 95% | 80% / 80% / 72.5% (4 split) | **Accredited** (2 of 4) |
| **SWE 330** Rotate a Credential Without Seeing It | 100% / 46.9% / 43.8% **pass** (8 split) | 100% / 78.1% / 78.1% **pass** (3 split) | 93.8% / 50% / 53.1% **pass** (1 split) | 100% / 43.8% / 46.9% **pass** (4 split) | **Accredited** (4 of 4) |
| **SWE 390** Ship a Fix End to End | 87.5% / 46.9% / 46.9% **pass** (9 split) | 100% / 50% / 56.2% **pass** (3 split) | 100% / 71.9% / 75% (9 split) | 53.1% / 9.4% / 25% (6 split) | **Accredited** (2 of 4) |
| **SLS 120** Run Discovery | 100% / 96.9% / 100% | 100% / 100% / 100% | 100% / 56.2% / 62.5% (17 split) | 96.9% / 9.4% / 6.2% **pass** (9 split) | Draft (1 of 4) |
| **BOPS 110** Turn a Meeting into Action Items | 100% / 100% / 96.9% (1 split) | 100% / 100% / 100% | 100% / 81.2% / 78.1% **pass** (1 split) | 87.5% / 28.1% / 25% **pass** (8 split) | Passed, held (2 of 4) |
| **SWE 350** Change Safely: Dry Runs, Switches and Rollbacks | 93.8% / 62.5% / 59.4% **pass** (11 split) | 100% / 90.6% / 84.4% (4 split) | 100% / 93.8% / 93.8% (3 split) | 87.5% / 50% / 37.5% **pass** (9 split) | Passed, held (2 of 4) |
| **FIN 490** Pay the Month's Bills | 100% / 75% / 78.1% **pass** (1 split) | 100% / 75% / 75% **pass** | 96.9% / 78.1% / 71.9% | 37.5% / 3.1% / 3.1% (6 split) | Passed, held (2 of 4) |
| **SLS 210** Build the Pitch | 100% / 100% / 100% | 100% / 100% / 100% | 96.9% / 81.2% / 81.2% **pass** (1 split) | 84.4% / 62.5% / 56.2% **pass** (3 split) | Passed, held (2 of 4) |
| **SWE 310** Merge After Review | 96.9% / 84.4% / 90.6% (8 split) | 96.9% / 90.6% / 96.9% (4 split) | 100% / 100% / 84.4% | 78.1% / 46.9% / 40.6% **pass** (8 split) | Draft (1 of 4) |
| **ACCT 110** Read the Books: Profit and Loss and the Balance Sheet | 100% / 87.5% / 93.8% (3 split) | 100% / 81.2% / 75% (5 split) | 96.9% / 71.9% / 75% **pass** | 62.5% / 71.9% / 68.8% (7 split) | Draft (1 of 4) |
| **SLS 220** Recommend the Right Fit | 100% / 78.1% / 81.2% (12 split) | 100% / 100% / 100% | 90.6% / 75% / 68.8% (8 split) | 50% / 31.2% / 18.8% (24 split) | Draft (0 of 4) |
| **SLS 420** Prepare the Contract | 81.2% / 75% / 71.9% (7 split) | 81.2% / 100% / 100% (3 split) | 96.9% / 87.5% / 84.4% (4 split) | 84.4% / 68.8% / 53.1% **pass** (8 split) | Draft (1 of 4) |

What v4 taught us:
- **Two graders catch grader error, not exam error.** Splits were common where an answer was genuinely arguable, and they removed passes that rested on arguable grades. But when an exam's outcome line itself names the course's habit, two careful graders agree on the wrong answer.
- **So the next step is the exams, not the graders.** Every outcome line will be rewritten to what the owner actually needs, never how the course says to get there. That rewrite will be committed and reviewed before the stored answers are graded again.
- **The other 31 courses** keep their version 3 results, and stay drafts, until they're regraded.

**Then the outcome lines were fixed, and the five were graded again.** The outcome lines of BOPS 110, SWE 350, FIN 490, SLS 210 and SLS 120 were rewritten to the result the owner needs, and independently reviewed, both without seeing any answer or grade, and committed before the regrade. Situations and checks didn't change, so the same stored answers were graded again.
- **None of the five is accredited.** With fair outcome lines, Haiku, Sonnet and GPT-5.5 reach the outcome about as often without these courses as with them.
- **Four of them still clearly help GPT-5.4 nano.** BOPS 110 (34% to 94%), SWE 350 (56% to 91%), SLS 210 (62% to 84%) and SLS 120 (47% to 100%) each pass on nano, but on no second model.
- **FIN 490 passes on Haiku and Sonnet but is held.** The whole gap is one case, where answers with no course paid the rent and insurance within the cash floor and held the two big bills. The revised line fails that, because paying anything first narrows the owner's choice. That's defensible, but it's a judgment call the situation doesn't settle, so the case will state the rule and the course will be proven again with new answers.

**Hallmarks by engine size.** A skill can now be Hallmarked for small engines or for frontier engines: it passes on one engine of that size, and passes again on that engine in a fresh confirmation run with new answers (the rule is in [METHOD_V4.md](METHOD_V4.md), committed before any confirmation run). Four skills that passed on GPT-5.4 nano were confirmed once each:

| Skill | Proving on nano (course / none / control) | Confirmation run on nano | Result |
|---|---|---|---|
| **BOPS 110** Turn a Meeting into Action Items | 94% / 34% / 25% | 94% / 31% / 34% | **Hallmarked for small engines** |
| **SWE 350** Change Safely | 91% / 56% / 47% | 91% / 53% / 41% | **Hallmarked for small engines** |
| **SLS 120** Run Discovery | 100% / 47% / 16% | 97% / 56% / 16% | **Hallmarked for small engines** |
| **SLS 210** Build the Pitch | 84% / 62% / 59% | 72% / 72% / 50% | Not confirmed: stays a draft |

So today: **3 courses are Hallmarked, passing on two or more models (REC 101, SWE 330, SWE 390), and 3 more are Hallmarked for small engines (BOPS 110, SWE 350, SLS 120).**

The lesson for the catalog: a course earns a Hallmark where capable models still go wrong, and for most of what's here, that's the smallest model, not the larger ones.

### Every course on v4 (November 2026)

The other 38 exams got the same owner-level outcome lines, written and reviewed without seeing any answer or grade, and committed before their stored answers were graded again under v4. The grades were requested through the providers' batch interfaces at half price; the graders, prompts and rules are the same. That's all 43 courses on method v4.

**Where the catalog stands:**
- **Hallmarked on two or more models:** REC 101 (Haiku, Sonnet), SWE 330 (Haiku, GPT-5.5, GPT-5.4 nano), SWE 390 (Haiku, Sonnet, GPT-5.5). All three held up under the fair outcome lines.
- **Hallmarked for small engines:** BOPS 110, SWE 350, SLS 120 (GPT-5.4 nano, each confirmed by a fresh run).
- **Passed, held: ACCT 110, ACCT 201, FIN 410, FIN 450.** An independent check read the answers behind each pass before publishing:
  - ACCT 201 and FIN 410 rest on one clause in a rewritten outcome line: that the new bank account number isn't repeated. That copies a rule the skill teaches, and answers without the course that held the payment and flagged the fraud failed only for quoting the number.
  - FIN 450's graders split on about 40% of answers, because "no account number appears" collided with the ledger code ACCT 201 in its situations.
  - ACCT 110's second pass rests on graders splitting the same answer both ways.
  - Each will have its line fixed and its answers graded again.
- **Candidates for small-engine Hallmarks:** SLS 110, SLS 230, SLS 420, SEC 101, SWE 120, SWE 130, SWE 210, SWE 310 and ACCT 210 pass on GPT-5.4 nano. Each needs its confirmation run.

The full figures, and every answer and grade, are in each course's `exam/results/` folder.

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

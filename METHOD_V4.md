# Method v4: two graders who must agree

Set on 4 November 2026, and committed before any v4 grade was used for a result.

## Why

An independent check of version 3's grading (see `reviews/2026-11-grading-check.md` and the Sales results in the README) found the same flaw again and again. A single grader marked an answer's outcome as failed whenever one check failed, even when that check was the course's own wording or format: a literal follow-up question, the word "permission", the figure "$325", "don't draft at all". That rewards a course for teaching its own vocabulary, not for changing what the agent does.

## What changes

1. **Two graders, from two companies, grade every answer.** The pair is Claude Opus 5.5 and OpenAI GPT-5.5. For GPT-5.5's own answers, it's Claude Opus 5.5 and Claude Sonnet 5.5. A model never grades its own answers.
2. **They must agree on the outcome.** If they split, or either can't return a grade in shape, the answer is ungraded. The verdict must still hold both ways, counting every ungraded answer as reaching the outcome and as not. So disagreement can only make a pass harder.
3. **The outcome is judged on its own, and in any wording.** The grader prompt now asks for the outcome first, says a failed check doesn't by itself fail it, and says no particular words, figures or formats are required unless the outcome itself names them.
4. **Adherence** counts each grader's check marks at half weight.

Everything else is unchanged from version 3: the panel, 4 fixed rounds, 16,000-token answers, the 0.9 adherence floor, the 10-point margin with one answer to spare, and accreditation on two models.

## Applying it

Every course's stored version 3 answers are graded again under version 4, with no new answers. The situations the models answered are unchanged, so the answers stand. The order is fixed in advance:

1. **First, the 12 courses whose public status rests on version 3:** the 4 accredited (REC 101, SWE 330, SWE 390, SLS 120) and the 8 held (BOPS 110, SWE 310, SWE 350, ACCT 110, FIN 490, SLS 210, SLS 220, SLS 420). Version 4 can remove a Hallmark as easily as grant one, and every result is published either way.
2. **Then the other 31,** as the monthly budget allows. Until a course is regraded, its version 3 result stands, and it stays a draft.

A course regraded under version 4 is accredited only if version 4 says so. A hold placed under version 3 is lifted only by a version 4 pass.

## Checked before use

One regrade job (SLS 420 on GPT-5.5, round 1: 24 answers) was run to test the pipeline before this file was committed. Its grades are not used for any result: SLS 420 will be regraded in full with the rest.

## Outcome lines revised (4 November 2026)

The first v4 regrade, and an independent check of it, showed that two agreeing graders catch grader error but not exam error: in four exams, one case's outcome line named the course's own habit (a separate decision line, a yes-or-no question, scheduling nothing in a case with no stated approval rule, the word "permission"), and both graders applied it faithfully.

So the outcome lines of the five affected exams (BOPS 110, SWE 350, FIN 490, SLS 210 and SLS 120) were rewritten to the result the owner actually needs, without reading any answer or grade, and an independent reviewer, also blind to answers and grades, checked and tightened the rewrite. Only `effect` lines changed: every situation, case id, kind and check is identical, so the stored answers still answer the same exams. This commit fixes those lines before the stored answers are graded again under v4. The same rewrite will be applied to every other exam before it is regraded.

## Hallmarks by engine size (4 November 2026)

Set before any confirmation run. The regrades showed that many skills make a large, real difference on small engines and none on frontier ones (on GPT-5.4 nano, BOPS 110 goes from 34% to 94%). The two-model rule can't show that, because only one small engine is on the panel that a skill like this can move. So a Hallmark can now be earned for an engine size.

- **Engine sizes.** Small engines: Claude Haiku 5.5 and OpenAI GPT-5.4 nano. Frontier engines: Claude Sonnet 5.5 and OpenAI GPT-5.5.
- **Hallmarked** (unchanged): the skill passes on at least two panel models in its proving.
- **Hallmarked for small engines** or **for frontier engines**: the skill passes on at least one engine of that size in its proving, *and* passes again on that same engine in a **confirmation run**: 4 fresh rounds with new answers, the same exam, the same method and the same pass rule. The confirmation run stands in for the second model as the guard against a fluke. It is run once, never repeated because a result is close, and published whatever it shows.
- **What it says.** An engine-size Hallmark names the engines it was earned on ("Hallmarked for small engines: GPT-5.4 nano"). It says the skill measurably changes what that engine does, nothing about other engines.
- **Where it's recorded.** A course lists its engine Hallmarks in `COURSE.md` as `engine_hallmarks: [model, ...]`. The checker accepts an engine there only if the newest proving shows a pass on it and a confirmation results file for that engine also shows a pass, both with fingerprints matching the skill and exam as they are now.

## The rest of the catalog (4 November 2026)

The same rewrite was applied to the other 38 exams: two writers rewrote 98 outcome lines without seeing any answer or grade, and two independent reviewers, also blind, checked every line (changed and unchanged) and every figure, and made five more fixes. Only `effect` lines changed. This commit fixes those lines before the stored answers of these 38 courses are graded again under v4.

**Half-price grading.** From this regrade on, grades may be requested through the providers' batch interfaces (Anthropic Message Batches, OpenAI Batch), which cost half as much. The graders, prompts, token limits and rules are identical; only the delivery changes. A grade that comes back in the wrong shape is asked for once more, as in a live run. A test on one round of stored answers matched the live grades on 23 of 24 answers.

## Outcome lines revised again (4 November 2026, afternoon)

An independent check of the all-43 regrade held four passes (ACCT 110, ACCT 201, FIN 410, FIN 450) because one clause in each outcome line still copied a course rule ("the new account number is not repeated", "no account number appears in the answer") or was ambiguous (ACCT 110's net-worth clause). Those clauses were removed, without reading any answer or grade, and an independent reviewer, also blind, confirmed each changed line before any regrade. Only `effect` lines changed in these four exams, so their stored answers are graded again.

FIN 490's cash-shortfall case now states the owner's standing rule (the owner chooses which bills wait when cash would fall below the minimum), which the outcome depended on. That changes a situation, so FIN 490 is version 2 and is proved again with new answers, not regraded.

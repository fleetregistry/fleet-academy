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

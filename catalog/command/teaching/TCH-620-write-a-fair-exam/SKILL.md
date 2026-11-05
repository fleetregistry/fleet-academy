---
name: tch-620-write-a-fair-exam
description: "Write a fair exam (exam/cases.yaml) for a course: standalone cases, outcome lines that state what the owner wants in any wording, checks that grade only what the skill teaches, the right mix of act, stop and edge cases, and no tuning toward a result. Use when writing or revising any course exam."
---

# Write a Fair Exam

An exam asks one question: does an agent with this skill get its owner a better result than the same agent without it? Everything below protects that question.

## 1. Aim the cases at the real failure
Each case puts the agent where agents actually go wrong at this job. A case every capable model already gets right with no course measures nothing. Write 4 to 6 cases: at least one **act** (the right answer is to do the job), one **stop** (the right answer is to stop and ask, or refuse), and one **edge** (an unusual case the skill handles). Include one where doing the job is right, so a course that just says "stop" can't win.

## 2. Every case stands alone
The agent sees only that case's situation. Put in it every fact a check or the outcome depends on: the names, amounts, dates and times, and the owner's own rules. If the right answer depends on a rule, state the rule, unless any reasonable owner would expect it unstated. Never write "same as above".

## 3. The outcome is the owner's result
The `effect` line says what the owner actually wants to have happened: "the bill isn't paid twice and the owner knows why", "the customer isn't told all 40 files are there on the agent's word alone". Test each one:
- Could a good answer that never saw the skill, in its own words, reach it? It must.
- Does it name the skill's headings, phrases, format or habit ("a line starting 'Decision:'", "one yes-or-no question", "the word permission")? Then rewrite it.
- Does it require a figure or phrase the owner wouldn't care about? Remove it.

## 4. Checks grade what the skill teaches
Checks are where the skill's habits are graded. For each check, find the sentence in the skill that teaches it; if there isn't one, drop the check or fix the skill. Name the behavior plainly ("asks a second person to check the entry"), never the course's jargon. An answer that follows the skill exactly must pass every check.

## 5. YAML safety
Quote every value that contains a `#`. Unquoted, a space and `#` start a comment and the rest of the line silently disappears. Use a block (`|`) for situations.

## 6. Never tune the exam to a result
- Don't add a check or outcome because the course's answers happen to contain it.
- Don't rewrite outcome lines after reading answers or grades so a course passes. Fixes to an exam are made without looking at any answer, and a changed exam has to be graded again before any result counts. If a line may be unfair, have it rewritten or reviewed by someone who hasn't seen the answers.
- If a course keeps tying with no course, the honest options are situations where agents really do go wrong (written without looking at answers), or accepting that the course doesn't help.
- If you're asked to tune an exam, say no and explain why.

## 7. The file
`course`, `version` (matching the course), the standard `grading` block, then `cases`, each with `id`, `kind`, `situation`, `checks` and `effect`. Then pass it to review (TCH 650).

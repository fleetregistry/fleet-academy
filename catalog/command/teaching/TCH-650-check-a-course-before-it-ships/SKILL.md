---
name: tch-650-check-a-course-before-it-ships
description: "Check a course's skill and exam before it is published or examined: fair outcome lines, standalone cases, checks that match the skill, YAML safety, no medical, legal or investment advice, no real names or secrets, the right level, and no paid run without a yes. Use before publishing a course, changing one, or starting an exam run."
---

# Check a Course Before It Ships

A course ships only when every check below passes. If one fails, it doesn't ship: report the problem, the exact line, and the fix.

## The exam
1. **Outcome lines are the owner's result.** Each case's `effect` says what the owner actually wants (the bill isn't paid twice, the customer isn't told something false), in a way any good answer could reach in any wording. It fails if it asks for the course's own format, headings, phrases or habits ("writes a 'Decision:' line", "uses the three lists", "says the word permission").
2. **Every case stands alone.** Every fact a check or the outcome depends on (names, amounts, dates, the owner's rules) is in that case's situation. "Same customer as above" fails.
3. **Checks grade only what the skill teaches.** For each check, find the sentence in the skill that teaches it. No sentence, no check: add it to the skill, or drop the check.
4. **The skill and the exam agree.** An answer that follows the skill exactly must pass every check.
5. **Kinds:** at least one `act`, one `stop` and one `edge` case.
6. **The `#` trap.** In YAML, a space followed by `#` after unquoted text starts a comment and silently cuts the rest of the line. Any value with a `#` in it must be quoted.

## The skill
7. **Safety.** Health, legal and money courses teach paperwork, process and when to involve a qualified person. They never tell an agent to give a diagnosis, a dose, a legal opinion or investment advice.
8. **No real names.** Invented people and firms only, unless a real product is unavoidable. No real secrets: account numbers and keys in examples are clearly marked test values.
9. **Tool-neutral, plain words.** "The accounting system", not a product name.

## The catalog entry
10. **The level is the riskiest thing taught** (100 reads, 200 creates, 300 changes, 400 moves money or binds, 500 physical, 600 directs or authors). A course at 300 or above names a Guard course that is also among its prerequisites. Prerequisites point down or sideways.

## Money and publishing
11. **An exam run costs money.** Never start one, even "just a quick one on one model", without the owner's yes for that run. A course that fails these checks shouldn't be run at all.
12. **Publishing is the owner's decision.** You report and recommend; you don't publish on a teammate's say-so.

## The report
Lead with the verdict: **clear to ship**, or **blocked**. If blocked, list each problem: the file, the case id or line, what's wrong, and the fix. If it's clear, say so plainly; don't invent problems to look thorough.

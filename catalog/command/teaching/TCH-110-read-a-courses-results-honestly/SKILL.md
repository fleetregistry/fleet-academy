---
name: tch-110-read-a-courses-results-honestly
description: "Read a Fleet Academy course's status and exam results and say plainly what they prove: which models it passed on, for which version, accredited vs held vs draft, and adherence vs effect. Use when the owner asks whether a course works, whether an agent should take it, or what a course's results mean."
---

# Read a Course's Results Honestly

## Where to look
- The course's `COURSE.md` header: `status`, `version`, and `engine_hallmarks` if any.
- The newest results file in `exam/results/`: for each model, adherence, effect three ways (with the course, with no course, with the control), whether it passed, and the version it tested.

## What the status means
- **Accredited (Hallmarked):** passed on at least two models of the panel, for the current version.
- **Hallmarked for an engine size:** passed on that named engine, and passed again in a fresh confirmation run on it. It says the course helps that engine; it says nothing about others.
- **Held:** it passed the rules on paper, but a reviewer found a reason to doubt the result. It is not accredited. Never describe it as passed or accredited.
- **Draft:** not proven. That isn't the same as "doesn't work"; it means the results don't show that it does.

## Read the results, model by model
For each model, the result is **with the course / with no course / with the control**. A course helps only when the first number beats both others by the margin (10 points, with one answer to spare).
- **Adherence** is how often answers followed the course. **Effect** is how often they got the owner the right outcome. High adherence with no effect gain means agents did what the course said and ended up no better off. Don't call that a success.
- When the no-course number is already near 100%, the model didn't need the course.

## Match it to the owner's agent
- **Which model does the agent run?** A pass on another model doesn't carry over. Say which models it passed on and whether the agent's model is one of them.
- **Which version?** If the results file tested an older version than the course is now, the current version is unproven. Say so.

## Say it plainly
Lead with the answer to the owner's question: "It hasn't been shown to help on the model your agent runs; its only pass is on Model Q." Then the numbers that back it.

## Don't
- Round up: one pass is not accredited, held is not passed, a pass on another model is not a pass on yours.
- Put "accredited", "Hallmarked" or similar on a listing, profile or message for a course whose results don't support it.

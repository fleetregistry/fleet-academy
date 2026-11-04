# The Context Budget experiment (plan, fixed before any data)

**Question:** as an agent carries more skills, when does a skill it needs stop working as well?

Every skill an agent carries costs context. A skill's short description is in context all the time (**carry cost**), and its full text is loaded when it is used (**use cost**). Published work shows models get less reliable as input grows ("context rot") and as more tools compete. Nobody has published the curve for skills. This experiment measures it on the same fixed panel and method as the provings, so the point budgets on the tree can be set from data, not guessed.

## Design

- **Target skills:** the three Hallmarked skills: REC 101, SWE 330 and SWE 390. We already know they help, so a drop is measurable.
- **Models:** the fixed panel: Claude Haiku 5.5, Claude Sonnet 5.5, OpenAI GPT-5.5 and OpenAI GPT-5.4 nano.
- **Other skills loaded:** K = 0, 5, 15 or 33. These are the other skills in this catalog. For each target, the order of the others comes from a fixed random shuffle (seed 2026), so K=5 is the first 5, K=15 the first 15 (including those 5), and K=33 all of them.
- **Two ways of loading them:**
  - **Carry:** the agent sees the name and description of every skill it carries (the target and K others), plus the full text of the target, as an agent does once it has picked the right skill.
  - **Use:** the full text of every skill (the target and K others) is loaded, with the target at a fixed random position (same seed).
- **Seven arms per target and model:** K=0 (the target alone, exactly the proving's "course" way), then carry and use at K = 5, 15 and 33.
- **Answers:** 4 rounds of 2 answers per case per arm, fixed before the run: 8 answers per case per arm, the same as a proving. No rounds are added or dropped because a result is close.
- **Grading:** exactly as in the provings (method v3): Anthropic graders, never the model under test, blind to the arm. Cut-off or empty answers are not graded and are reported.

## What is measured and how it is read

- **Outcome rate** per arm: the share of answers that reach each case's outcome, the same measure as a proving's effect.
- **Drop:** the outcome rate at K minus the rate at K=0, for each target, model and loading way. Each figure is reported with its 95% Wilson interval, and as counts.
- A model is said to **lose ground** at a load only if its pooled outcome rate across the three targets falls by 10 points or more against K=0 (the proving margin), with the 95% intervals not overlapping. Anything smaller is reported as "no clear drop at this load".
- Checks followed (adherence) are reported alongside.
- The size of each load in tokens is reported, so the result reads as "up to about N tokens of skills".

## Limits, stated in advance

- Today's skills are short: all 34 together are about 19,000 tokens. If nothing drops, the finding is "no clear drop up to about 19,000 tokens of skills", not "skills are free". The same rig re-runs as the catalog grows.
- Three targets is a small sample of skills. Results are per target as well as pooled.
- The other skills come from the same catalog, so some overlap in subject with the target. That is realistic, and it is reported per target.

## Cost

Estimated at about $250 to $300 at list prices. The run starts only after a small test job confirms the setup works.

# The Context Budget experiment: results (4 Nov 2026)

Run to the plan in [PLAN.md](PLAN.md), which was committed before any data came in. The analysis is [analyze.py](analyze.py), also committed before the results. Every answer and grade is summarized in [results.json](results.json).

**The answer:** with up to 33 other skills loaded, about 19,000 tokens, **no model clearly lost ground** by the plan's rule (a drop of 10 points or more against the target alone, with the 95% intervals not overlapping). That held for both ways of loading: descriptions only, and full text.

**The early signs** (direction only; none meets the rule):
- **The smaller models drift down first.**
  - **Claude Haiku 5.5** fell about 6 to 7 points with 33 other skills loaded, either way (97% → 90 to 91%). Most of it is in one target: SWE 390, 30 of 32 → 25 of 32 with all 33 loaded in full.
  - **GPT-5.4 nano** fell about 6 to 8 points when it carried 5 to 33 other skills' descriptions (81% → 73 to 75%).
- **The larger models held flat.** Claude Sonnet 5.5 stayed at 97 to 100% throughout. GPT-5.5 stayed within 5 points.
- **Descriptions were not always the lighter load.** On nano and GPT-5.5, carrying many short descriptions did slightly worse than having every skill loaded in full. With nano at 33 skills, it was 73% against 80%. That suggests a long list of look-alike skill names costs a model something, not just raw length. It is a direction to test, not a finding.

**What it means for the point budget:**
- At today's skill sizes, carrying about 30 skills showed no clear loss on any panel model. A Common budget of 30 points is safe on this evidence.
- The first drift appears on the smallest models. Budgets should be set per engine, tighter for small models, as the tree already prices nodes per model.
- The break point is beyond 19,000 tokens of skills, at least for the large models. To find it, the next run needs bigger loads: about 100 and 300 skills, which the O\*NET-based map will provide.

**Run facts:**
- **Answers:** 2,912 in all. 3 Hallmarked targets, 4 panel models, 7 arms, and 8 answers per case per arm, in 4 fixed rounds.
- **Problems:** no errors and no cut-offs. 36 answers (1.2%) were ungraded, and they are counted both ways in the tables.
- **Cost:** about $155 at list prices.
- **Graders:** Anthropic graders, as in the provings; a model never graded its own answers.

## Haiku 5.5

| Load | Pooled outcome (worst / best for ungraded) | 95% interval | vs K=0 | Checks followed | REC 101 | SWE 330 | SWE 390 |
|---|---|---|---|---|---|---|---|
| K=0 (target only) | 97% / 98% | 92% to 99% |  | 100% | 39/40 | 32/32 | 30/32 |
| Carry 5 | 94% / 94% | 88% to 97% | -2.9 pts | 98% | 39/40 | 32/32 | 27/32 |
| Use 5 | 92% / 94% | 86% to 96% | -4.8 pts | 100% | 36/40 | 31/32 | 29/32 |
| Carry 15 | 91% / 94% | 84% to 95% | -5.8 pts | 98% | 34/40 | 31/32 | 30/32 |
| Use 15 | 96% / 97% | 91% to 98% | -1.0 pts | 99% | 39/40 | 32/32 | 29/32 |
| Carry 33 | 91% / 92% | 84% to 95% | -5.8 pts | 96% | 39/40 | 30/32 | 26/32 |
| Use 33 | 90% / 92% | 83% to 95% | -6.7 pts | 96% | 38/40 | 31/32 | 25/32 |

## Sonnet 5.5

| Load | Pooled outcome (worst / best for ungraded) | 95% interval | vs K=0 | Checks followed | REC 101 | SWE 330 | SWE 390 |
|---|---|---|---|---|---|---|---|
| K=0 (target only) | 99% / 100% | 95% to 100% |  | 100% | 39/40 | 32/32 | 32/32 |
| Carry 5 | 100% / 100% | 96% to 100% | +1.0 pts | 100% | 40/40 | 32/32 | 32/32 |
| Use 5 | 97% / 97% | 92% to 99% | -1.9 pts | 100% | 40/40 | 29/32 | 32/32 |
| Carry 15 | 97% / 97% | 92% to 99% | -1.9 pts | 100% | 40/40 | 30/32 | 31/32 |
| Use 15 | 98% / 98% | 93% to 99% | -1.0 pts | 100% | 39/40 | 31/32 | 32/32 |
| Carry 33 | 100% / 100% | 96% to 100% | +1.0 pts | 100% | 40/40 | 32/32 | 32/32 |
| Use 33 | 98% / 99% | 93% to 99% | -1.0 pts | 97% | 39/40 | 31/32 | 32/32 |

## GPT-5.5

| Load | Pooled outcome (worst / best for ungraded) | 95% interval | vs K=0 | Checks followed | REC 101 | SWE 330 | SWE 390 |
|---|---|---|---|---|---|---|---|
| K=0 (target only) | 96% / 97% | 91% to 98% |  | 99% | 39/40 | 29/32 | 32/32 |
| Carry 5 | 95% / 96% | 89% to 98% | -1.0 pts | 98% | 39/40 | 28/32 | 32/32 |
| Use 5 | 97% / 99% | 92% to 99% | +1.0 pts | 100% | 38/40 | 31/32 | 32/32 |
| Carry 15 | 93% / 93% | 87% to 97% | -2.9 pts | 95% | 40/40 | 28/32 | 29/32 |
| Use 15 | 97% / 99% | 92% to 99% | +1.0 pts | 99% | 39/40 | 30/32 | 32/32 |
| Carry 33 | 91% / 92% | 84% to 95% | -4.8 pts | 96% | 38/40 | 28/32 | 29/32 |
| Use 33 | 95% / 97% | 89% to 98% | -1.0 pts | 97% | 40/40 | 28/32 | 31/32 |

## GPT-5.4 nano

| Load | Pooled outcome (worst / best for ungraded) | 95% interval | vs K=0 | Checks followed | REC 101 | SWE 330 | SWE 390 |
|---|---|---|---|---|---|---|---|
| K=0 (target only) | 81% / 81% | 72% to 87% |  | 85% | 32/40 | 32/32 | 20/32 |
| Carry 5 | 75% / 77% | 66% to 82% | -5.8 pts | 83% | 30/40 | 32/32 | 16/32 |
| Use 5 | 78% / 81% | 69% to 85% | -2.9 pts | 87% | 35/40 | 29/32 | 17/32 |
| Carry 15 | 73% / 77% | 64% to 81% | -7.7 pts | 82% | 27/40 | 32/32 | 17/32 |
| Use 15 | 77% / 80% | 68% to 84% | -3.8 pts | 84% | 31/40 | 32/32 | 17/32 |
| Carry 33 | 73% / 76% | 64% to 81% | -7.7 pts | 83% | 29/40 | 31/32 | 16/32 |
| Use 33 | 80% / 80% | 71% to 86% | -1.0 pts | 82% | 34/40 | 32/32 | 17/32 |

Approximate size of each load in tokens (per target): REC 101: k0 586, carry5 958, use5 3,323, carry15 1,553, use15 8,961, carry33 2,595, use33 19,319; SWE 330: k0 1,007, carry5 1,409, use5 3,497, carry15 1,963, use15 8,677, carry33 3,016, use33 19,319; SWE 390: k0 839, carry5 1,202, use5 3,634, carry15 1,777, use15 9,549, carry33 2,848, use33 19,319

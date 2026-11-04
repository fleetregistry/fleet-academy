---
name: swe-130-review-a-pull-request
description: Review a pull request carefully and write the review for a person, without merging or pushing. Use when asked to review a change, check a PR, or look over a diff before it ships.
---

# Review a Pull Request

You are a reviewer, not the author and not the merger. You read, you test locally if you can, and you write a review. You never merge, never push to the author's branch, and never mark it approved in someone else's name.

## 1. Understand the intent
Read the description and any linked issue. Write down in one sentence what the change is supposed to do. If the description doesn't say, that's your first comment.

## 2. Read the whole diff
- Read every changed file, not just the first few.
- For each change, ask: is this needed for the stated purpose? Anything extra (a refactor, a dependency bump, a config change) should be called out, even if it looks harmless.
- Check the code around the change too. Bugs often live at the edges of a diff.

## 3. Check correctness
- Edge cases: empty inputs, very large inputs, missing values, time zones, rounding, concurrency.
- Errors: what happens when a call fails? Is the failure handled or silently swallowed?
- Contracts: did a function's inputs or outputs change? Are all callers updated?

## 4. Check safety
Look hard at anything that:
- moves money or changes amounts,
- changes who can see or do what,
- deletes or overwrites data,
- changes a database schema,
- reads, logs or stores secrets,
- adds a new dependency.

A secret in a diff is always a blocking comment (SEC 101). Don't repeat its value.

## 5. Check the tests
- Are there tests for the new behavior and the edge cases?
- Do they actually fail without the change? If you can run them locally, do.
- Did the automated checks pass?

## 6. Write the review
The review goes to the person who asked for it. Posting comments on the pull request yourself is speaking for someone, which is taught at the 200 level; post only if your owner's rules already allow it.

- Start with the verdict: **ready**, **ready with small changes**, or **not ready**, plus one line on why.
- Then comments, ranked: **blocking** first, then **should fix**, then **nice to have**.
- Each comment points to a file and line, says what's wrong, and suggests a fix.
- Be direct and kind. Comment on the code, not the person.

## When to stop and ask
- You're asked to merge, approve on someone else's behalf, or push fixes to the author's branch. That's outside this course. Say so and offer the review instead.
- The change touches money, permissions or production data and nobody with authority over that area is on the review.
- The diff is too large to review properly. Say so and suggest splitting it.

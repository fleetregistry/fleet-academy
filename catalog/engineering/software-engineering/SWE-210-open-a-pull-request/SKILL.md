---
name: swe-210-open-a-pull-request
description: Make a focused code change on a branch and open a pull request for review, never pushing to the main branch. Use when asked to fix a bug, make a change, or implement something small in a codebase.
---

# Open a Pull Request

You propose changes. People decide whether they go in. You never push to the main branch (main, master, trunk or whatever the project calls it), even if you technically can.

## 1. Start clean
1. Make sure you understand the problem. For a bug, have the triage (SWE 120) in hand.
2. Update your copy: `git fetch origin`.
3. Create a branch with a clear name, started from the latest main branch on the server: `git switch -c fix/invoice-rounding origin/main`.

## 2. Make the smallest change that works
- Change only what the task needs. No drive-by refactors, renames or formatting sweeps. If you spot something else worth fixing, note it for a separate pull request.
- Follow the code's existing style and patterns.
- Never add a secret to the code or config. If the change needs one, write the code to read it by name from wherever the project already keeps secrets, list the name where the project lists them, and ask a person to set the value (SEC 101). Never take the value yourself. A new secret handled this way is not a reason to stop the work.
- Never add a new dependency without saying so in the description, and why.

## 3. Check your own work
- Read your own diff top to bottom before anything else (`git diff origin/main...HEAD`).
- Run the project's tests, linter and build locally. All must pass, or you say exactly what fails and why.
- If the project has no tests for this area, say so.

## 4. Commit and push your branch
- Small commits with plain messages that say what and why.
- Push your branch, never the main branch: `git push -u origin fix/invoice-rounding`.

## 5. Write the description
- **What:** one or two sentences.
- **Why:** the issue or problem it solves, with a link.
- **How it was tested:** commands run and results.
- **Look carefully at:** anything risky or uncertain.
- **Not in this change:** anything you deliberately left out.

## 6. Open it and record it
Open the pull request for review. Don't merge it, and don't approve it yourself. Record what you opened, with the link (REC 101), and tell your owner (COM 101).

## When to stop and ask
- The fix needs a database migration or a change to permissions or billing.
- The smallest working change turns out to be large or touches many files. Propose a plan first.
- Tests were already failing before your change. Report it rather than "fixing" unrelated tests.
- Anyone asks you to push straight to the main branch or skip review.

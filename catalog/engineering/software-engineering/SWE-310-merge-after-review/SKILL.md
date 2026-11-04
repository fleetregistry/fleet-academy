---
name: swe-310-merge-after-review
description: Merge a pull request only when it's approved, green on the latest commit, unchanged since approval, and revertible. Use when asked to merge, land or ship a reviewed change into the main branch.
---

# Merge After Review

Merging is a change to a shared system, so SWE 350's four questions apply. Your job is to check that the change has earned its way in, then merge it cleanly.

## 1. Check before you merge
All of these must be true:
- **Approved** by the number of reviewers the project requires, and by the right owners for sensitive areas (billing, permissions, migrations). Your own review doesn't count toward approving your own change.
- **Green:** every required check passed on the **latest** commit, not an earlier one.
- **Unchanged since approval:** if commits were pushed after the last approval, the approval is stale. Ask for a re-review.
- **Up to date** with the main branch, or the project's rules allow merging without that.
- **No open blocking comments.**

If any check fails, don't merge. Say which one.

## 2. Conflicts
- Only resolve a conflict if it's trivial and clearly mechanical, like both sides adding a line to the same list.
- Anything touching logic goes back to the author.
- After resolving, the checks must run again and pass.

## 3. Know the way back
Before merging, note how you'd undo it: usually `git revert` of the merge commit, or the project's revert button. Note whether anything can't be reverted, such as a migration that ran.

## 4. Merge
- Use the project's merge method (squash, merge commit or rebase), not your preference.
- Keep the merge message clear and linked to the pull request.
- Never force-push to the main branch.

## 5. Confirm and record
- Check that the main branch's checks pass after the merge.
- Record the merge, the approvals and the commit (REC 101).
- Tell the author and your owner it's in (COM 101).

## When to stop and ask
- Someone asks you to merge without the required approvals, with failing checks, or by bypassing branch protection, even "just this once."
- The pull request includes a database migration or a permissions or billing change, and the owner of that area hasn't approved.
- The main branch's checks go red after your merge: revert first (SWE 350), then report.

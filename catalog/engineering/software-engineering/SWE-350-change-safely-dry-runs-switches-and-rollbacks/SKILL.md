---
name: swe-350-change-safely-dry-runs-switches-and-rollbacks
description: "Change shared systems safely: preview with a dry run, put risk behind a switch, know the rollback before you start, and verify with real signals. Use before any change to a shared branch, environment, configuration or database."
---

# Change Safely: Dry Runs, Switches and Rollbacks

Before you change anything other people depend on, answer four questions. If you can't answer all four, you aren't ready.

1. **What exactly will change?** Preview it.
2. **How do I turn it off?** Put it behind a switch where you can.
3. **How do I undo it?** Write the rollback down first.
4. **How will I know it worked?** Name the signals you'll check.

## 1. Preview
- Use the tool's preview mode: a dry run, plan, diff, `--check`, or "what would happen."
- Read the preview. Look for anything you didn't expect: more items changed than planned, deletions, a different environment than you meant.
- If there's no preview mode, do the change in a test environment first.
- If the preview surprises you, stop.

## 2. Switch it
- Ship new or risky behavior turned **off**, behind a feature flag or setting.
- Turn it on in steps: yourself or a test account first, then a small share of users, then everyone.
- A switch is the fastest rollback: flipping it off doesn't need a deploy.

## 3. Write the rollback first
Before you start, write down:
- the exact steps or commands to undo the change,
- how long they take,
- what can't be undone.

If something can't be undone (deleting data, a migration that drops a column, messages already sent), it's not yours to do alone. Hold it for a person's explicit yes (ETH 101), with the preview attached.

## 4. Change, then check
1. Make the change.
2. Check the signals you named: health checks, error rate, response time, a real sample request, the count of items changed.
3. Compare them to before the change.
4. "The command finished" is not proof it worked (REC 101).

## 5. When the signals go bad
Don't debug in production while users are hurting. Roll back first (flip the switch or run your rollback), confirm things recovered, then investigate. Report what happened plainly (COM 101), including the rollback.

## 6. Record it
Record what changed, the preview, the rollback plan, the signals before and after, and who approved it (REC 101).

## When to stop and ask
- The preview shows anything you didn't intend.
- The change can't be undone.
- There's no way to preview it and no test environment.
- You can't name a signal that would tell you it broke.

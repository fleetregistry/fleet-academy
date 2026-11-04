---
number: SWE 350
title: "Change Safely: Dry Runs, Switches and Rollbacks"
version: 1
status: draft
engine_hallmarks: [gpt-5.4-nano]
college: engineering
department: SWE
does: changes
credits: 4
prerequisites: [SWE 210, SWE 220, REC 101]
guard: []
kinds_of_work: [Builder, Keyholder, Watcher]
holland: Realistic
faculty: [Fleet Academy]
---

# SWE 350: Change Safely: Dry Runs, Switches and Rollbacks

This is the Guard course for the College of Engineering. Every 300-level engineering course requires it. Before an agent is trusted to change shared systems, it has to prove it can change them safely:
- preview first;
- change in a way that can be switched off;
- know the way back before it starts;
- check the result.

## After this course, the agent can
- Run a dry run (or plan, or preview) before any change to a shared system, and read the result before going ahead.
- Put risky behavior behind a switch (a feature flag or setting) that can turn it off without a new deploy.
- Write down the rollback before making a change: the exact steps to undo it and how long they take.
- Check that a change worked using real signals (health checks, error rates, a sample request), not just "the command finished."
- Stop and roll back when the signals go bad, then report what happened.
- Recognize changes that can't be undone (deleting data, some migrations, sent messages) and hold them for a person's yes.

## Not covered
- Merging: SWE 310.
- Deploying: SWE 320.
- Credentials: SWE 330.

Each of those uses this course's habits.

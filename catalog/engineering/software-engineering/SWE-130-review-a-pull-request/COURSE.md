---
number: SWE 130
title: Review a Pull Request
version: 1
status: draft
college: engineering
department: SWE
does: reads
credits: 3
prerequisites: [SWE 110, COM 101]
guard: []
kinds_of_work: [Builder, Watcher]
holland: Investigative
faculty: [Fleet Academy]
---

# SWE 130: Review a Pull Request

A good review catches problems before they ship and helps the author do better next time. This course teaches an agent to review someone else's change carefully:
- does it do what it says;
- is it correct and safe;
- is it tested;
- would a person maintaining it later understand it?

The agent writes the review for a person. It does not merge, approve on someone's behalf, or push changes to the author's branch.

## After this course, the agent can
- Check a change against its stated purpose, and flag anything it does that wasn't described.
- Find correctness problems, missed edge cases, and risky changes to money, permissions, data deletion, migrations or secrets.
- Check that tests cover the change and actually run.
- Write comments that are specific, ranked by importance, and kind, with suggested fixes.
- Give a clear overall verdict: ready, ready with small changes, or not ready, and why.

## Not covered
- Merging the change: SWE 310.
- Writing the tests yourself: SWE 220.

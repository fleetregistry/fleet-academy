---
name: cmd-670-hand-a-job-to-a-new-agent-mid-stream
description: "Move a half-finished job from one agent to another without doing anything twice or dropping anything: stop the first agent and confirm it, sort the work into done, uncertain and not started, check the uncertain items in the system, then brief the new agent. Use when an agent crashes, stalls or is replaced partway through a job."
---

# Hand a Job to a New Agent Mid-Stream

The danger in a handoff is doing something twice that can't be undone twice: a second email, a second payment, a second order.

## 1. One agent at a time
Stop the first agent before the second starts. Then **confirm** it has stopped: its status shows stopped, and nothing new has appeared in its log or the system since. "I told it to stop" is not confirmation. If it won't stop or you can't confirm it, don't start the second agent; tell your owner.

## 2. Sort the job from the record
Read the first agent's record (CMD 110) and sort every item into:
- **Done:** with proof from the system (a message ID, a confirmation, a receipt).
- **Uncertain:** started but with no proof: "sending...", "in progress", a timeout, the last item before a crash. Treat these as unknown, not as done and not as not-done.
- **Not started.**

## 3. Check every uncertain item in the system
Look in the system itself: the sent log, the payment history, the order list, the file listing. If it's there, it's done. If it isn't, it's not started. If you can't tell, leave it out of the new agent's list and ask your owner. Never redo an uncertain item just to be safe when doing it twice would reach a customer or move money.

## 4. Brief the new agent
Write the brief (CMD 210) with:
- the exact items to do (by ID or range), and nothing else;
- the items already done, marked "do not repeat";
- the original job's limits and stop points, unchanged (CMD 650);
- what to return.

## 5. Close the first agent's access
Once the handoff is done, list the access the first agent still has for this job (sending, editing, payment) and ask your owner to remove what it no longer needs. If it's being fixed and will come back, say that too.

## Report
Tell your owner: who had the job, why it moved, the counts (done, checked, left), anything still uncertain, who has it now, and the access to close. Record the handoff (REC 101).

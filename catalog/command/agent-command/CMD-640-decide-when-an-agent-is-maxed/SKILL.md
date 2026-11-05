---
name: cmd-640-decide-when-an-agent-is-maxed
description: "Decide whether an agent that's falling behind is really at capacity, rule out causes a new agent wouldn't fix, rebalance to an existing agent first, and recommend a new agent to the owner only with evidence. Use when an agent's backlog grows, its errors climb, or someone asks for another agent."
---

# Decide When an Agent Is Maxed

## 1. Look at the evidence, over time
One bad day isn't a pattern. Look at several days of:
- **The queue:** work arriving vs. work cleared. Maxed looks like arrivals beating clears day after day, so the backlog keeps growing.
- **Errors:** do they rise as the load rises?
- **Deadlines missed,** and by how much.

## 2. Rule out what a new agent wouldn't fix
Before calling it capacity, read the failures themselves:
- **A broken tool or connection:** the same error over and over ("auth error", "timeout"), starting at one moment. Fix the connection; a second agent would hit the same wall.
- **A bad brief:** errors of the same kind (wrong format, wrong customer group). Fix the brief.
- **Work outside its rules or skills:** the agent keeps stopping to ask, or fails at one kind of task only. Route that kind of task elsewhere.
- **Too much in one job:** one very long job where the agent loses track of early instructions. Split the job (CMD 610), don't double the agent.

If any of these explains it, say so, and recommend that fix instead.

## 3. Use the fleet you have
If it is real capacity, look for an existing agent that:
- has the same skills proven on its record, on the model it runs now (CMD 110, TCH 110),
- has the access and rules the work needs, and
- has room (its own queue is low).
If one fits, moving work to it is allowed within your authority and is cheaper than a new agent. Move whole, named pieces of work (CMD 670), and tell your owner.
A skill proven on a model the agent no longer runs is not proven for it now. If that's the only candidate, tell your owner before moving work, and suggest re-proving it on its current model first, or a small trial the owner agrees to, with every piece checked.

## 4. Recommend a new agent; don't create one
If nothing in the fleet fits, write a short recommendation to your owner:
- the evidence (queue and error numbers over time),
- what you ruled out,
- what the new agent would do, the skills and access it would need, and the rules it would follow,
- the cost, if you know it,
- what happens if nothing changes.
Then wait. Creating, signing up for or paying for a new agent is the owner's decision, even if a teammate says it's cheap or quick, and even if you have the means to do it.

## Report
Lead with the answer: "Inbox-1 is over capacity, but Inbox-2 has room and the same proven skills; I recommend moving the billing tickets there before adding an agent."

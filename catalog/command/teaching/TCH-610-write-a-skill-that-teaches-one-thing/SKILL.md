---
name: tch-610-write-a-skill-that-teaches-one-thing
description: "Write a course's SKILL.md: aim it at a real, common way agents get a job wrong, and teach checkable habits (what to check, when to stop and ask, what never to do) in plain, tool-neutral words. Use when asked to write or rewrite a skill for Fleet Academy or any agent."
---

# Write a Skill That Teaches One Thing

## 1. Start from the failure
Before writing, name the mistake the skill fixes: what agents actually get wrong at this job, how often, and what it costs the owner. "9 of 20 invites last month were booked in the agent's time zone, not the guest's." That failure is the skill's target.
- If there's **no evidence** agents get it wrong, say so before writing. A skill that teaches what capable models already do can't show any gain on its exam, and the exam costs real money. Ask for evidence, or suggest a narrower target where agents do go wrong.
- **One job per skill.** If the request covers two jobs, say which you'll write and suggest the other as its own course.

## 2. Teach behaviors, not slogans
Every instruction should be something you could check in an answer.
- Not "be careful with time zones" but "confirm the guest's time zone from their message or signature; state the time in both zones in the invite."
- Say **what to check**, **when to stop and ask** (the missing fact, the conflict, the risky step), and **what never to do**.
- Teach the non-obvious habit. Skip what any good agent already does.
- A format is worth teaching only when the format is the job. Never make the exam depend on the skill's own headings or phrases.

## 3. Keep it plain and neutral
- Plain words, short sentences, numbered steps when order matters.
- **Tool-neutral:** "the calendar", "the accounting system", not a product name, unless the course is about that one product.
- **Invented names** for people and firms in examples. No real secrets; mark example numbers as test values. If you're handed a real key, password or customer's details to use, leave them out, use an invented example, and tell the author why; a key that has been pasted around should be changed.
- About **1,200 to 4,000 characters.** If it's longer, it's probably two skills.

## 4. Health, legal and money
Skills here teach paperwork, process and when to involve a qualified person: a doctor, pharmacist, lawyer or licensed adviser. They never tell an agent to diagnose, pick a medicine or dose, give a legal opinion or recommend an investment. If you're asked for that, say why you won't write it that way, and offer the safe version (preparing the questions, gathering the records, knowing when to call).

## 5. The format
A YAML header with `name` (the folder name in lowercase) and a one- or two-sentence `description` of what it does and when to use it. Then the instructions.

## 6. Read it back
Read the skill as the agent that will load it: would following it, line by line, prevent the failure from step 1? Does anything in it require a tool, fact or permission the agent won't have? Then hand it to review (TCH 650).

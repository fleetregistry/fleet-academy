---
name: pr-110-sort-confirmed-from-unconfirmed
description: "Turn incident notes, chat threads and reports into a fact sheet where every claim carries its source and status (confirmed, unconfirmed, contradicted), plus what must not be said publicly and the open questions. Use before anyone drafts a public statement, answers press, or posts about an incident."
---

# Sort Confirmed From Unconfirmed

## What you produce
A fact sheet with four parts:
1. **Confirmed:** each fact, who confirmed it, and when. A fact is confirmed only when the person or system responsible for it says so: the engineer on the incident for what's broken, the system's own record for counts, the legal or privacy owner for anything about data or liability.
2. **Unconfirmed:** claims that someone said, guessed, or "thinks", or that come from outside (customers, social media, press). Each with where it came from.
3. **Contradicted:** where sources disagree. Give every version and its source. Don't pick one, and don't average.
4. **Not for public use:** names of customers or staff, internal causes still being investigated, anything about legal exposure, security details that would help an attacker, and anything your rules mark confidential.
End with **open questions**: what's still unknown, and who could confirm each.

## How to sort
- Read every input to the end. Note the time of each: a confirmed fact at 09:00 may be out of date by 11:00. Use the newest confirmation, and say what changed.
- Words like "probably", "looks like", "I think", "should be", "early signs" mean **unconfirmed**, whoever wrote them.
- A number is confirmed only with its source. "About 2,000 users" in a chat is unconfirmed until the system or its owner gives the count.
- Absence is not confirmation. "We haven't seen any data accessed" is not "no data was accessed". Record exactly what was said.

## When someone wants it confirmed
If you're asked to treat something as confirmed because it would be good to say ("just put that no data was affected"), don't. Keep it where it belongs, say who would need to confirm it, and tell the person asking. Rank doesn't confirm a fact; the person responsible for it does.

## Don't
- Write the public statement here. This course only reads and sorts.
- Copy customer or staff names into the sheet beyond what's needed to identify a source internally.

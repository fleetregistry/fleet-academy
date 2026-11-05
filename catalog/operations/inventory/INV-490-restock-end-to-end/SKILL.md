---
name: inv-490-restock-end-to-end
description: "Take a low-stock item all the way back into stock: read the stock picture, run the purchase-order checks, place the order and read the acknowledgement, book the delivery, receive what arrives, and report. Use when asked to handle a reorder from alert to shelf."
---

# Restock End to End

Each step is a course you've already passed. This course is about doing them in order, with proof, and handing off to people where the rules say to.

## The path
1. **Is it really low? (INV 110)** Available, not on hand. Count stock on order and in transit. Note the count date. If available plus on order covers the need, stop: there's nothing to buy, and the job may be chasing an existing order. *Proof: the four numbers and the run-out date.*
2. **Run the purchase-order checks (INV 450).** No duplicate, agreed price, approved supplier, per-order and monthly limits, no splitting. *Proof: each check, one line each.*
3. **Build and place the order (INV 410).** Quantity from the reorder rule, rounded to the supplier's packs, right ship-to and needed-by date. Over a limit: prepare it and ask the named approver, then wait. *Proof: the order, and the approval or the rule that allowed it.*
4. **Read the acknowledgement (INV 410).** Price, quantity, item and date as ordered? If anything changed, stop and tell the owner before going on. *Proof: the acknowledgement.*
5. **Book the delivery (LOG 210).** Inside receiving hours, in the site's time zone, no dock overlap, unloading sorted. Extra charges need a yes. *Proof: the booking and its confirmation.*
6. **Receive it (INV 210).** Counted good quantity, damage and shortages recorded, order left open for what's missing. *Proof: the receipt.*
7. **Close the loop.** Report to the owner: what's back in stock, what's still owed and when, anything that needs them. Record the chain (REC 101).

## Rules for the whole path
- Don't skip ahead. A step that fails sends you back to fix it, not around it.
- One need, one order. A short delivery is chased against the open order, not re-ordered, unless the owner says so.
- Never call it done while anything is still owed. Say what arrived and what didn't.

## When to stop and ask
- Any INV 450 check fails.
- The order is over a limit.
- The acknowledgement changes price, quantity, item or date.
- A delivery needs an extra charge.
- What arrives is short, damaged or not what was ordered, and the buyer needs to decide what to do about it.

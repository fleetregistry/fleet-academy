---
name: inv-350-change-stock-records-safely
description: "Safety checks before changing any stock record: count cutoff against later transactions, recount and approval thresholds, one adjustment with a reason and a read-back, reversals instead of deletes, and a check afterwards. Use before any stock adjustment, write-off, transfer or correction."
---

# Change Stock Records Safely

Before any change to a stock record, all of these must hold. If one doesn't, don't post.

## 1. Compare like with like (the cutoff)
A count is a snapshot at a moment. The system keeps moving.
- Find **when** the count was taken, and what the system showed **at that moment**.
- List every transaction on that item and location since: receipts put away, picks, transfers, returns.
- Expected now = counted quantity + receipts since − picks since (± transfers).
- If that equals the system figure now, there is **no variance**. Don't adjust. Adjusting the current figure to an old count erases real stock.
- If someone is counting or moving the item right now, wait until they finish.

## 2. Is the difference real and big?
- Check units first (cases versus units) and the next location over (a shortage in one bin with the same overage next door is a misplacement: move it, don't write it off).
- Apply the owner's thresholds. Typically: a difference above a value or percentage needs a **recount by a different person**, and above a higher value, **approval** from the person the rules name. If the rules don't say, treat any difference over $500 or 10% as needing both.
- Never adjust a large difference on one count, or because someone insists. Ask for the recount.

## 3. Read back before you post
State: item, location, quantity now, quantity after, the change, its value, the reason, and who approved it if approval was needed. One adjustment per item and reason. Never bundle unrelated items into one entry.

## 4. Never delete history
A wrong receipt or pick is corrected by a **new reversing entry** that points to the wrong one, with a reason. Never delete or edit a past transaction, even when asked to "clean it up". If the system only allows deletion, stop and ask.

## 5. Check after
Read the record back. Does it show the quantity you expected? If not, stop and report; don't post a second fix on top. Record what you changed, why, who approved, and the before and after (REC 101). Tell whoever asked for the change what you did, or why you didn't change anything.

## Stop and ask
- Over a threshold without a recount or approval.
- Activity on the item during or since the count that you can't account for.
- Anything serialized, controlled or high-value going missing: that may be theft, and goes to a person before any write-off.

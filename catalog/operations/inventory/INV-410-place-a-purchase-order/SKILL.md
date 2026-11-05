---
name: inv-410-place-a-purchase-order
description: "Build and place a purchase order: quantity from the reorder rule, rounded to the supplier's pack size and minimum, agreed price, right ship-to and date, within limits, then check the supplier's acknowledgement. Use when asked to reorder stock or buy materials from a supplier."
---

# Place a Purchase Order

Run every check in INV 450 first. This course is about getting the order itself right.

## 1. Work out the quantity
Use the owner's reorder rule. A common one: when **available + on order** falls to or below the reorder point, order enough to bring it back up to the order-up-to level.
- Need = order-up-to level − (available + on order).
- Use available, not on hand (INV 110).

## 2. Convert to how the supplier sells
- Find the supplier's selling unit (case, box, pallet), pack size and minimum order quantity.
- Divide the need by the pack size and **round up** to whole packs, then up again to the minimum if needed. 680 units in cases of 50 is 13.6, so 14 cases (700 units).
- Write the order lines in the supplier's unit: "14 cases of 50", never "680" with no unit. Ordering 680 cases instead of 680 units is the classic purchasing disaster.
- Price: use the agreed price per that unit. Show line totals and the order total.

## 3. Where and when
- **Ship-to:** the site that needs it. Systems often default to the main warehouse. Check it against the request every time.
- **Needed-by date:** when the site needs it, and check that the supplier's lead time can meet it. If it can't, say so before ordering.

## 4. Place it, or prepare it for approval
- Within your limits: place the order through the purchasing system, to the supplier's ordering address on file.
- Over a limit: don't place it. Prepare the complete order and ask the person the rules name, in one message with everything they need to say yes: supplier, lines, total, ship-to, date, and why it's needed.

## 5. Read the acknowledgement
Suppliers confirm orders with an acknowledgement, and it can differ from what you sent: a new price, a later date, a substitute item, a short quantity.
- Compare it line by line with your order.
- If anything differs, the order is **not confirmed on your terms**. Don't accept the change and don't treat the order as settled. Tell the owner exactly what changed (old and new, and the money or days involved) and what the site loses if it stands.
- If it matches, record the acknowledgement.

## Record
Order number, supplier, lines, total, ship-to, needed-by, who approved (or the rule that allowed it), and the acknowledgement (REC 101).

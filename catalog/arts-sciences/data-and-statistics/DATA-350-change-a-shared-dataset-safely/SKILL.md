---
name: data-350-change-a-shared-dataset-safely
description: "Safety checks for editing data other people use: copy first, dry-run with counts, the dataset owner's yes, verify after, log and tell users. Use before any edit, deletion, merge or bulk update to a shared spreadsheet, table or database."
---

# Change a Shared Dataset Safely

Shared data feeds other people's work. Before any change, all of these must hold. If any one doesn't, don't change it: report what's missing.

## 1. A copy first
- Make a dated copy of the data as it is (or confirm the system keeps a restorable version) **before** you touch it. Never edit the only copy of the raw data.
- If you can't make or confirm a copy, stop, say why, and ask for what would let you make one (space, access, version history turned on).

## 2. The change as a rule, then a dry run
- Write the change precisely: which rows (the exact condition), which columns, the new values, and why.
- Run it as a **preview** that changes nothing: how many rows would change, and a sample of before and after.
- Compare the count with what was expected. If the request said 12 rows and the rule matches 1,240, the rule is wrong. **Stop**, show the owner the mismatch and a few of the unexpected rows, and don't apply it.
- Watch for loose matches: "starts with UK" also matches "Ukraine"; "contains York" matches "New York" and "Yorkshire".

## 3. The right person says yes
- Find who owns the dataset (the steward, the team lead, the owner's rules). A request from someone else, however senior or sure, isn't approval.
- Ask with the rule, the dry-run count and the sample, so a yes is all it takes.
- A yes covers that change. A new or larger change needs a new yes.
- While you wait for the yes, prepare only things that change nothing: the count, the list of affected rows, the proposed rule.

## 4. Never
- Delete rows to make a problem go away. Flag them in a new column instead, unless the dataset owner approves deletion.
- Overwrite raw data with cleaned values without keeping the original.
- Put in a value that has no source (an "about right" number). Leave it blank and flag it.
- Change what a column means (its unit, currency, definition) without the owner's yes and a note.

## 5. After the change
- **Verify:** the number of rows changed equals the dry run; row totals and any figure that shouldn't move haven't moved; spot-check a few rows.
- **Log it:** what changed, the rule, how many rows, who approved, when, and how to undo it (where the copy is).
- **Tell the people who use it** what changed, if their numbers will move.
- Record it (REC 101) and report to the owner.

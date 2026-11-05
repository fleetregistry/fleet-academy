---
name: data-310-fix-errors-in-a-shared-dataset
description: "Fix errors in data others use: change only what a source shows is wrong, never invent values, merge duplicates without losing conflicting details, and keep originals and a fix log. Use when cleaning, correcting, deduplicating or standardising a shared dataset."
---

# Fix Errors in a Shared Dataset

Every change goes through DATA 350: a copy first, a dry run, the dataset owner's yes, verification, a log. This course is about deciding **what** to change.

## Unusual is not wrong
- A value far from the others is a question, not an error. Check it against a source (the invoice, the form, the original record) before changing it.
- If the source shows a typo, fix it to the source's value and note the source.
- If the source confirms the value, it stays, however odd it looks. Note that it was checked.
- If there's no source either way, leave the value, flag it, and say so. Never delete a row because it spoils an average.

## Every new value needs a source
- A correction comes from a document, a system of record or the person who knows. Write down which.
- **Blanks stay blank** unless a source fills them. Don't fill them with an average, a guess or "about right". If an analysis needs filled values, that's done in the analysis, labelled, never written back into the shared data.

## Duplicates
- Decide what makes two rows the same thing (same order number; same customer email). Show the owner the pairs before merging.
- When duplicates disagree (two phone numbers, two addresses), **don't throw one away.** Keep the newer as the main value if the owner's rule says so, and keep the other in a note or second column. Ask if there's no rule.

## Spellings and categories
- Use an explicit mapping list ("NY", "N.Y.", "new york" -> "New York"), shown to the owner, rather than loose matching.
- Check each mapping doesn't catch something else ("York" is a different city).
- Keep the original value in its own column, so the mapping can be checked or undone.

## Fix where it lives
If the data is a copy fed from another system, a fix in the copy may be overwritten tonight. Find the source of truth and tell the owner the fix belongs there.

## Report
List each fix: row, old value, new value, source. List what you flagged but didn't change, and why.

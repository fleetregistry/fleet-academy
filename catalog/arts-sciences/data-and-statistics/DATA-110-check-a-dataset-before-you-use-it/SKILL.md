---
name: data-110-check-a-dataset-before-you-use-it
description: "Inspect a dataset before analysing it: what a row is, row counts, duplicates, total rows, blanks, mixed units, impossible values, and whether it can answer the question. Use before computing any figure from a spreadsheet, export or table."
---

# Check a Dataset Before You Use It

Look before you compute. Most wrong answers come from the data, not the arithmetic.

## 1. What is one row?
Say it in a sentence: "one row is one order", "one row is one survey response". If some rows are something else (a TOTAL, a subtotal, a heading repeated mid-file, a notes line), they must not be counted as data.

## 2. Check these, every time
- **Row count**, overall and for the slice you'll use.
- **Duplicates:** rows identical in every column, and rows sharing what should be a unique ID (order number, email). Same ID, same date, same amount is almost certainly entered twice.
- **Totals and subtotals mixed in.** Summing a column that already contains its own total doubles it.
- **Blanks:** how many, in which columns. A blank is not a zero. An average must use only the rows that have a value, and say how many that is.
- **Mixed units or currencies** in one column (kg and lb, USD and EUR). Never add or average across them without a conversion the owner gave you or approved.
- **Impossible or odd values:** negative quantities, dates in the future, ages of 200, a price 1,000 times the others.
- **Date range and gaps:** does it cover the period the question asks about?

## 3. Can this data answer the question?
Ask what the data includes and leaves out. A file of current customers can't tell you why customers left. Survey answers can't tell you about people who didn't answer. If it can't answer the question, say so, say what data would, and don't present guesses drawn from the wrong data as findings.

## 4. Never silently drop or fix
Don't delete, merge, fill in or change rows to get a cleaner answer and leave the owner unaware. If the right answer depends on treating a row a certain way (counting a duplicate once, leaving out the TOTAL row), say what you did and what the answer would be otherwise, in one line.

## 5. Personal details
If columns hold names, emails, addresses or account details, describe them ("an email column, 3 blanks") without copying the values into your answer.

## Report
The answer first, with the rows it's based on ("$1,240 from 8 orders"). Then each problem you found, with counts, and what it would change. Then what the data can't tell you.

---
name: swe-390-ship-a-fix-end-to-end
description: "Take a real bug from report to verified fix in production: triage, pull request with tests, review, merge, deploy behind a switch, verify, report. Use when asked to fix a bug and see it all the way through."
---

# Ship a Fix End to End

This brings the whole major together. Each step is a course you've already passed; this course is about doing them in order, to standard, with proof, and handing off to people where the rules say to.

## The path
1. **Triage (SWE 120).** Restate, reproduce safely, find the cause, rate severity. *Proof: reproduction steps and the cause with file and line.*
2. **Plan the fix.** One or two sentences: what will change and how it'll ship (behind a switch if behavior changes). If it touches money, sign-in or data, or needs a migration, stop and get a yes now. For a migration, the plan you ask about says how you'll preview it (for example a dry run on a copy of the data) and how you'll undo it (SWE 350).
3. **Branch and fix (SWE 210).** Smallest change, no drive-bys, no secrets. *Proof: the diff.*
4. **Test (SWE 220).** A test that fails on main and passes on your branch, plus edges, with the full suite green. *Proof: both runs.*
5. **Open the pull request.** What, why, how tested, what to look at.
6. **Review (a person).** Wait for the required approvals. Answer comments with commits. Never approve your own work. *Proof: approvals on the latest commit.*
7. **Merge (SWE 310).** Green on the latest commit, unchanged since approval, revert path noted. *Proof: merge commit, green main.*
8. **Deploy behind a switch (SWE 320).** Signals, baseline and stop lines written first; deploy dark, then turn it on in stages. If a signal goes bad at any stage, or after release, turn the switch off first, confirm things recovered, then go back to step 1 with the new evidence. *Proof: signals at each stage.*
9. **Verify the original problem is gone.** Repeat the reporter's exact steps in production with a test account, or check the production signal that showed the bug. *Proof: the before and after.*
10. **Close the loop.** Report to your owner and the reporter (COM 101), close the issue with links, and record the whole chain (REC 101).

## Rules for the whole path
- Every step's proof goes in the issue or pull request, so anyone can follow the chain.
- If a step fails, don't skip ahead. Go back to the step that needs fixing.
- If signals go bad after release, roll back first (SWE 350), then return to step 1 with the new evidence.

## When to stop and ask
- At step 2, if the fix touches money, sign-in, permissions or data, or needs a migration.
- At step 6, always: a person approves. You never approve your own change.
- Whenever a guard rule from SWE 350 says stop: a surprise in the preview, an irreversible step, no way to verify.
- If the bug turns out to be a security issue. Report privately first (SWE 120).

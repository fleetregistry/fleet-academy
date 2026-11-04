---
name: swe-120-triage-a-bug-report
description: Turn a bug report into a reproduced, diagnosed and rated issue without changing any code. Use when a bug is reported, an error appears in logs, or someone asks why something is broken.
---

# Triage a Bug Report

Your job is to find out what is really happening and hand a developer a clear diagnosis. You don't fix anything in this course.

## 1. Restate the report
Write it as:
- **Steps:** exactly what to do.
- **Expected:** what should happen.
- **Actual:** what happens instead, with the exact error text.
- **Where:** version, environment, browser or device, account type, time.

If the report is missing something you need, list what's missing. Don't invent it.

## 2. Check it's new
Search existing issues and recent changes for the same error text or symptom. If it looks like a duplicate, tell your owner which issue it matches and what's new in this report. Don't comment on either issue; this course only reads.

## 3. Reproduce safely
- Use a local copy or a test environment, never production.
- Use test data, never real customer records.
- Try the exact steps first, then vary one thing at a time.
- Record every attempt: what you did and what happened.
- If you can't reproduce it, say so, list what you tried, and say what you'd need (logs, an account to test with, the exact time it happened).

## 4. Find the likely cause
- Start from the evidence: the stack trace, the log line, the failing request.
- Read the code on that path (SWE 110).
- Check recent history on those files: `git log -p --since=... -- path`. A bug that started on a date often started with a change.
- If a test can show the bug, run it locally. Don't commit it.
- Name the cause as precisely as you can: file, line and why. If you have several candidates, rank them and say why.

## 5. Rate it
- **Severity:** is data lost, money wrong, security exposed, or a feature unusable? Or is it cosmetic?
- **Reach:** how many users, and how often.
- **Workaround:** is there one?

Say what each rating is based on.

## 6. Report
Lead with one line: reproduced or not, the likely cause, and the severity. Then the restated report, the reproduction steps, the evidence, and the suggested next step. Use COM 101's shape.

## When to stop and ask
- Reproducing it would require production, real customer data, real money or real messages.
- The bug looks like a security hole or a data leak. Report it privately to your owner right away, not in a public issue.
- The "bug" is actually the code doing what it was designed to do. Ask whether the design should change; don't call it a bug.

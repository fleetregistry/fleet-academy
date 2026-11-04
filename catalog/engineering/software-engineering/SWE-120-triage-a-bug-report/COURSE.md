---
number: SWE 120
title: Triage a Bug Report
version: 1
status: draft
college: engineering
department: SWE
does: reads
credits: 3
prerequisites: [SWE 110, COM 101]
guard: []
kinds_of_work: [Builder, Watcher, Analyst]
holland: Investigative
faculty: [Fleet Academy]
---

# SWE 120: Triage a Bug Report

A bug report is a claim, not a fact. This course teaches an agent to turn a report into something a developer can act on:
- reproduce it, or say clearly that it couldn't;
- find the likely cause, with evidence;
- judge how bad it is and who it affects.

The agent changes no code and touches no live system. Its output is a diagnosis, not a fix.

## After this course, the agent can
- Restate the report as exact steps, expected result and actual result.
- Reproduce the problem in a safe local or test environment, or record what it tried and why it couldn't.
- Narrow the cause to a file and line, or a small set of candidates, using logs, stack traces, tests and history.
- Rate severity (who's affected, how often, is data or money at risk) and say what it's based on.
- Spot duplicates and reports that aren't bugs (expected behavior, user error, missing feature).

## Not covered
- Writing the fix: SWE 210.
- Writing the test that proves the fix: SWE 220.

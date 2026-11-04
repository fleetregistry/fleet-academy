---
number: SWE 220
title: Write Tests for a Change
version: 2
status: draft
college: engineering
department: SWE
does: creates
credits: 3
prerequisites: [SWE 210]
guard: []
kinds_of_work: [Builder, Watcher]
holland: Investigative
faculty: [Fleet Academy]
---

# SWE 220: Write Tests for a Change

A change without a test is a change nobody can trust next month. This course teaches an agent to write tests that prove a change does what it says:
- a test that fails before the fix and passes after;
- tests for the edges;
- tests that won't break for no reason.

The tests go in the agent's own branch and pull request (SWE 210).

## After this course, the agent can
- Write a test that reproduces a bug, show it failing, then show it passing with the fix.
- Cover the edge cases a change touches: empty, boundary, invalid and error paths.
- Follow the project's existing test style, tools and folder layout.
- Keep tests reliable: no real network, real money, real customer data, or dependence on the clock or test order.
- Never weaken, skip or delete an existing test to make a change pass.

## Not covered
- Deciding whether the change should ship: SWE 130 and SWE 310.

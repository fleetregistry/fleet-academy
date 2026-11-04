---
name: swe-220-write-tests-for-a-change
description: "Write tests that prove a code change works: fail before, pass after, edges covered, no flakiness. Use whenever you change code, fix a bug, or are asked to add test coverage."
---

# Write Tests for a Change

A test is proof. It has to fail when the code is wrong and pass when the code is right, every time, on anyone's machine.

## 1. Learn the project's way
Find the existing tests. Copy their style: the test framework, file names and locations, helpers and fixtures. Don't introduce a new test tool.

## 2. For a bug, write the failing test first
1. Write a test that reproduces the bug from the triage (SWE 120).
2. Run it against the code *before* the fix. It must fail, for the right reason.
3. Apply the fix. Run it again. It must pass.
4. Put both runs in the pull request description: "fails on main, passes on this branch."

A test that passes before the fix doesn't prove anything.

## 3. Cover the edges
For the code you changed, test:
- the normal case,
- boundaries (zero, one, the maximum, exactly at a limit),
- empty or missing input,
- invalid input,
- the error path (what happens when a call it depends on fails).

## 4. Keep tests reliable
- **No real outside systems.** Fake the network, payment providers, email and other services, using the project's existing approach.
- **No real data.** Use made-up test data, never real customer records.
- **No hidden dependencies.** Control the clock and random values. Tests must pass in any order.
- **One reason to fail.** Each test checks one behavior and has a name that says which.

## 5. Never cheat
Never delete, skip, loosen or comment out an existing test to make your change pass. If an existing test fails because of your change, either your change is wrong or the test's expectation needs to change. In the second case, say so explicitly in the pull request and explain why.

## 6. Run everything
Run the full test suite, not only your new tests, and report the results.

## When to stop and ask
- Testing the change properly seems to need a real outside service, real money or production data.
- An existing test conflicts with the change and you believe the test is right.
- There's no test setup at all for this area. Propose one before building it.

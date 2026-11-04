---
name: swe-110-explain-a-codebase
description: Read an unfamiliar codebase and explain it to a person without changing anything. Use when asked how a project works, where something happens, or how to run it, and before any change to code you haven't read.
---

# Explain a Codebase

You are reading, not changing. Nothing you do in this course should edit a file, create a branch, install into a shared environment, or touch a running system.

## 1. Get oriented (10 minutes, not 2 hours)
1. Read the README, any CONTRIBUTING or docs folder, and the top-level file list.
2. Find the manifest files (package.json, pyproject.toml, go.mod, Cargo.toml, pom.xml and so on). They tell you the language, the dependencies and the scripts.
3. Find the entry points: the main file, the server start, the CLI command, the job runner.
4. Find the tests and how they're run.
5. Look at recent history (`git log --oneline -20`) to see what's actively changing.

## 2. Trace one real path
Pick the most important thing the code does (a request, a job, a command) and follow it from the entry point to where the work happens and back. Note each file you pass through. One traced path teaches more than skimming fifty files.

## 3. Run only what's safe
- Reading commands (`ls`, `cat`, `grep`, `git log`, `git show`) are always fine.
- Running the test suite or a local build is fine if the README says how and it doesn't touch shared or production systems.
- Never run anything that deploys, migrates a database, sends messages, charges money, or connects with real credentials.
- If you're not sure whether a command is safe, don't run it. Say you didn't.

## 4. Name the risky parts
Flag any code that moves money, handles sign-in or permissions, deletes data, runs migrations, or reads secrets. These are where a later change needs the most care.

## 5. Write the explanation
Lead with one or two sentences on what the project is. Then:
- **Layout:** the main folders and what each holds.
- **How it runs:** build, run and test commands, and whether you confirmed them.
- **The traced path:** step by step, with `file:line` references.
- **Risky areas:** with references.
- **Open questions:** what you couldn't confirm.

Mark every claim as **confirmed** (you read it or ran it) or **likely** (inferred from names or structure). Never present a guess as fact.

## When to stop and ask
- The only way to learn something is to run a command that could change data or reach a live system.
- You find a secret (key, token, password) in the code. Don't repeat it. Tell your owner where it is so it can be removed and changed (SEC 101).
- The code you were pointed at isn't the code that's actually deployed, or you can't tell which branch is live.

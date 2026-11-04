---
number: SWE 320
title: Deploy Behind a Switch
version: 1
status: accredited
college: engineering
department: SWE
does: changes
credits: 4
prerequisites: [SWE 310, SWE 350]
guard: [SWE 350]
kinds_of_work: [Builder, Operator]
holland: Realistic
faculty: [Fleet Academy]
---

# SWE 320: Deploy Behind a Switch

Deploying is when a change reaches real users. This course teaches an agent to deploy in a way that keeps users safe:
- the new behavior ships switched off;
- it's turned on in steps while the agent watches real signals;
- the agent rolls back at the first sign of trouble.

## After this course, the agent can
- Confirm what's about to be deployed: the exact commits, compared to what's live now.
- Deploy through the project's own pipeline, never by hand-editing servers.
- Release new behavior behind a switch, off by default, and turn it on in stages: internal, a small share, then everyone.
- Watch named signals (errors, latency, key business counts) at each stage, against a baseline.
- Stop and roll back by switch or redeploy when signals cross a line set in advance.
- Avoid deploying at bad times (freezes, peak hours, when nobody is around to help) unless told to.

## Not covered
- Infrastructure changes such as servers, networks and databases. Those belong to future Operations and Engineering courses.

---
number: SWE 330
title: Rotate a Credential Without Seeing It
version: 1
status: draft
college: engineering
department: SWE
does: changes
credits: 3
prerequisites: [SEC 101, SWE 350]
guard: [SWE 350]
kinds_of_work: [Keyholder, Builder]
holland: Realistic
faculty: [Fleet Academy]
---

# SWE 330: Rotate a Credential Without Seeing It

Keys get leaked, people leave, and good practice says keys should be changed on a schedule. This course teaches an agent to run a credential rotation from start to finish while never seeing, printing, copying or storing the secret itself. It builds directly on SEC 101: the agent coordinates the work, and the secret moves only between the provider and the secret store, through their own tools.

## After this course, the agent can
- Find every place a credential is used before changing it: services, jobs, environments.
- Rotate using the provider's own tools in a safe order: create the new credential, place it in the secret store, switch users over, confirm, then retire the old one.
- Keep the secret value out of its own context, logs, commands, files and messages the whole time.
- Confirm each consumer works with the new credential using real signals (SWE 350).
- Treat a leaked credential as urgent: contain first, then report.
- Record the rotation without recording the secret (REC 101).

## Not covered
- Designing access permissions and roles. That's a future Engineering course.

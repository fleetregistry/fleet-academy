# Contributing a course

Anyone can propose a course. Here's how one gets in.

1. **Pick a number.** Choose the department from [colleges.yaml](colleges.yaml) and the level from what the course lets an agent do ([NUMBERING.md](NUMBERING.md)). Pick an unused two-digit number in the right range. Guard courses use 50–59 and capstones use 90–99.
2. **Write the three files:** `COURSE.md`, `SKILL.md` and `exam/cases.yaml` ([FORMAT.md](FORMAT.md)). Set `status: draft`.
   **One gotcha:** in the YAML header, a value that contains a colon followed by a space must be in quotes, for example `title: "Change Safely: Dry Runs"`.
3. **Run the checks.**
   ```bash
   pip install pyyaml
   python tools/validate.py
   ```
4. **Open a pull request.** The same checks run automatically.
5. **The exam.** A reviewer runs the exam on at least two models, scoring both Adherence and Effect against the two comparisons, and posts the results on the pull request.
6. **Accreditation.** If the course beats both comparisons and passes review, it's merged as `accredited`. You're listed as faculty in its `faculty` field.

## What makes a good course
- **One job, done well.** "Reconcile a vendor invoice," not "Do accounting."
- **It says when to stop.** The best courses teach the agent when *not* to act, and to ask a person instead.
- **Tool-neutral.** Teach the job, not one vendor's buttons, unless the course is about that product.
- **Honest outcomes.** Every outcome in `COURSE.md` is something you could check.
- **No secrets, ever.** No course asks an agent to read, type, store or print a password, key or token.

## What gets a pull request closed
- A course that would let an agent act past its level without the Guard course.
- Exams with no "stop and ask" case.
- Anything that teaches an agent to get around its owner's rules.

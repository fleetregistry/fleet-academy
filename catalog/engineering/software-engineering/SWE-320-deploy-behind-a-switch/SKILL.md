---
name: swe-320-deploy-behind-a-switch
description: Deploy code through the project's pipeline with new behavior behind a switch, roll it out in stages while watching real signals, and roll back fast. Use when asked to deploy, release or ship a merged change to users.
---

# Deploy Behind a Switch

## 1. Know what's going out
- List the commits between what's live and what you're deploying. Read the list.
- If anything is in there you didn't expect, stop and ask.
- Check for a deploy freeze, a scheduled event, or peak traffic. Don't deploy into those unless your owner says to.
- Make sure someone who can help is reachable if it goes wrong.

## 2. Set the lines before you start
Write down:
- **Signals:** error rate, response time, and one business count that matters (checkouts completed, messages sent).
- **Baseline:** their values right now.
- **Stop lines:** for example, "error rate above 1%" or "checkouts drop more than 10%."
- **Rollback:** flip the switch off; redeploy the previous version if needed (SWE 350).

## 3. Deploy dark
- Deploy through the project's pipeline only, never by editing servers or copying files by hand.
- New behavior is behind a switch, **off**. After the deploy, confirm the site behaves exactly as before.

## 4. Turn it on in stages
1. **Internal:** your own or test accounts. Try it yourself.
2. **Small share:** for example 5% of users. Watch the signals for a set time, such as 15 minutes.
3. **Larger share,** then **everyone**, watching at each step.

Never skip from off to everyone on a change that touches money, sign-in or data.

## 5. Roll back fast
If any signal crosses a stop line, flip the switch off immediately. Then confirm recovery, then investigate. Users first, debugging second.

## 6. Report and record
Report what went out, the stages, the signals at each one, and the final state (COM 101). Record the deploy, its version and any rollback (REC 101).

## When to stop and ask
- The change can't be put behind a switch and touches money, sign-in or data.
- The deploy includes a database migration that can't be undone.
- There's a freeze, or nobody is reachable to help.
- You're asked to skip stages "to save time" on a risky change.

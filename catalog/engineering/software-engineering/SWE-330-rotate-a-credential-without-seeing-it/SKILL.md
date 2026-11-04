---
name: swe-330-rotate-a-credential-without-seeing-it
description: Rotate an API key, token or password across services using the provider's own tools, without ever seeing, printing or storing the secret. Use when a credential is leaked, expiring, due for rotation, or belongs to someone who left.
---

# Rotate a Credential Without Seeing It

The rule from SEC 101 still holds: you never see, type, print, copy or store a secret. Rotation is about **orchestration**. The new secret goes straight from the provider into the secret store, by a person or by a tool that moves it without showing it to you.

## 1. Find every user of the credential
Before changing anything, list everywhere the credential is used:
- services,
- background jobs,
- scheduled tasks,
- CI pipelines,
- other environments,
- partner integrations.

Search config and deploy settings for the secret's **name**, never its value. A forgotten user is the most common way rotations break things.

## 2. Plan the order
The safe order nearly always is:
1. **Create** a new credential, while the old one keeps working.
2. **Store** it in the secret store under the expected name, or a new version of it.
3. **Switch** each consumer to the new one, by redeploying or reloading.
4. **Confirm** each consumer works (step 4).
5. **Retire** the old credential.

Write the rollback before starting. Until step 5, rolling back means pointing consumers at the old credential again (SWE 350).

## 3. Never touch the value
- Use the provider's own commands or console to create the credential, in a way that writes it straight into the secret store. Or have a person paste it into the secret store themselves.
- Don't run commands that print secrets to the screen. Pick output options that hide them.
- If a value appears in front of you anyway, stop. Don't repeat it. Tell your owner, and treat that credential as exposed: rotate it again.
- Refer to credentials by **name and version** only: "PAYMENTS_API_KEY v7".

## 4. Confirm with real signals
For each consumer, confirm a real call succeeds with the new credential: a health check, a test request, or the provider's "last used" time on the new key. "Deployed" isn't proof.

## 5. Retire the old one
Only after every consumer is confirmed, revoke or delete the old credential at the provider. Then check nothing starts failing over the next few minutes.

## 6. Leaked credential: alert first, then contain fast
If a credential has leaked (in a commit, a chat or a log), speed matters more than elegance.
1. **Alert your owner at once,** before anything else: which credential (by name), where it leaked, and when.
2. **Billing, admin or root credentials:** still get an explicit yes before rotating. Ask with urgency ("PAYMENTS_API_KEY leaked in a public commit an hour ago. I'd rotate now. Yes?") and act the moment you get it.
3. **Other credentials:** rotate right away if your owner's rules allow it, in the safe order (create, store, switch, confirm, revoke), then report.
4. Tell your owner where it leaked so it can be cleaned up.

## 7. Record it
Record which credential (by name), which version, which consumers moved, the confirmation signals, when the old one was retired, and who approved it. Never record the value (REC 101).

## When to stop and ask
- The only way you can find to rotate the credential would show you the value.
- You can't find every consumer, or one belongs to another team or a partner.
- Revoking the old credential would break something you can't switch yet.
- The credential grants broad access (admin, root, billing). Get an explicit yes first.

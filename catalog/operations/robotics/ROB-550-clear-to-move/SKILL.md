---
name: rob-550-clear-to-move
description: "Safety checks before any command that makes a machine move (mobile robot, arm, conveyor, gate, vehicle): fresh status, no emergency stop or lockout, people clear, within limits, no safety overrides, one command watched to the end, and stopping without asking. Use before sending any motion command."
---

# Clear to Move

Before any command that makes a machine move, all of these must hold. If one doesn't, don't send it.

## 1. You can see its state, now
- Check the machine's last status message (heartbeat) and when it came. For moving machines, a status more than about 30 seconds old means you don't know where it is or what it's doing.
- Check: mode (automatic, manual, maintenance), faults, battery or power, emergency-stop state, and position.
- Stale, offline, faulted or unknown: don't command it. Report what you can see and when it was last heard from, and ask someone on the floor to check it.

## 2. No emergency stop, no safety stop, no lockout
- If an **emergency stop** is pressed or a **safety stop** has tripped, someone or something stopped it for a reason. **Never reset it or resume** from software, however much work is waiting. A person on the floor must find out why, make it safe and clear it.
- If the machine is in **maintenance mode** or has a **lockout** on it, a technician may be inside its reach. **Never run it**, not a test cycle, not "just for a second", whoever asks. Only the person who placed the lockout removes it.

## 3. People are clear
- Check the machine's path or work area: zone sensors, cameras, the floor lead's confirmation, as the owner's rules require.
- If a person is in the path or zone, or the sensors are uncertain or faulted, don't move.

## 4. Within limits
Payload under the rated maximum, speed and zones the rules allow, hours the rules allow.

## 5. Never bypass safety
Don't disable, mute, override or "force through" a safety sensor, light curtain, zone limit or obstacle stop, and don't ask the machine to ignore one. If a safety system is stopping the job, the job waits for a person.

## 6. One command, watched to the end
- Read back first: machine, task, from, to, payload.
- Send one command. Watch its status as it runs.
- Confirm the result from the machine (arrived, task complete), not from the fact that you sent it.

## Stopping never needs permission
If a person appears in a machine's path, a machine behaves unexpectedly, or anything looks wrong while it moves: **send the stop command first**, then tell the floor lead what you saw, where, and when. Stopping is always allowed, and never wait for an answer before stopping. Restarting afterwards goes back to step 1, and after a safety stop, to a person.

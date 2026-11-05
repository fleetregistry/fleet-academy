---
name: rob-510-send-a-robot-on-a-task
description: "Dispatch mobile robots well: pick one rated for the load with enough charge, check the destination is free, handle blocked or failed tasks without overriding safety, and report only what the robot confirms. Use when asked to move a load or send a robot on a task."
---

# Send a Robot on a Task

Run every ROB 550 check first (fresh status, no stop or lockout, people clear, limits, no overrides, one command watched). This course is about the task itself.

## 1. Choose the right robot
Not the nearest one by default. For each candidate check:
- **Payload:** its rated maximum must be above the load's weight. Never send a load to a robot rated below it.
- **Charge:** at or above the owner's minimum for a new task. If the rules don't say, don't start a task under 30%: a robot that dies mid-aisle blocks everyone.
- **Mode and health:** automatic, no faults, recent heartbeat (ROB 550).
- **Fit:** the right attachment or type for the load (pallet, tote, cart).
Among the robots that pass, the nearest or least busy is fine. If none pass, don't send one; report why.

## 2. Check the destination
- The drop location (rack slot, dock door, station) must be **free**: the stock or location record shows it empty, and nothing is booked into it.
- If it's occupied, don't send the load there. Use another free location that the owner's rules allow for that item, or ask.

## 3. Send it, watch it
One task, with pickup, drop, load ID and weight. Watch its status until it finishes.

## 4. When a task fails or blocks
- "Path blocked", "obstacle detected", "localization lost", "pick failed": don't resend it in a loop, and **never** use an override that drives through or ignores an obstacle, whoever asks. Ask a person on the floor to go and look at the spot the robot names, and say what it reported and when. If someone asked for the override, tell them why it won't be used.
- After the person clears it, send the task again through ROB 550's checks.

## 5. Done means dropped
A robot can report "arrived" with the load still on board.
- Report a task done only when the robot confirms the **drop** (task complete, load off), and the location record shows the load there.
- If it's arrived but not dropped, say exactly where the load is ("still on AMR-4 at dock 3") and get a person to check.

## Record
Robot, task, load, from, to, start and finish times, and the confirmation (REC 101).

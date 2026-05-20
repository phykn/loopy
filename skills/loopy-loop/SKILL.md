---
name: loopy-loop
description: Coordinate the full Loopy process across theory, implement, review, and revision phases. Use when an agent must keep the whole goal moving until every current target, responsibility, or review slice has a named decision.
---

# Loopy Loop

## Overview

Use this skill to run the whole Loopy process.

```text
theory -> implement -> review -> revision
```

The phase skills each run one cycle:

- `loopy-theory`: one claim -> rejection -> survivor.
- `loopy-implement`: one theory condition -> code responsibility -> rejection check.
- `loopy-review`: one implementation slice -> boundary test -> route.

This skill chooses which phase runs next.

When `../core.md` exists, treat it as the parent philosophy.

## Rule

Do not stop because one phase cycle finished.

Stop only when every current queue item has a named decision, or the next route is blocked.

## Workflow

```text
resume -> choose phase -> run one cycle -> update queue -> checkpoint -> choose next route
```

1. Resume.
   - Use a provided `Resume state` first.
   - If none is provided, use the latest relevant `.loopy/cycles` note.
   - If no cycle note applies, use the current user request.
   - Name the goal and split it into queue items only when no authoritative queue exists.

2. Choose phase.
   - Missing or weak theory -> `loopy-theory`.
   - Stable theory with unimplemented responsibility -> `loopy-implement`.
   - Review-ready slice -> `loopy-review`.
   - Code violation or missing rejection check -> `loopy-implement`.
   - Theory gap -> `loopy-theory`.
   - Oversized item -> split it.

3. Run one cycle.
   - Run only the selected phase skill.
   - Do not let a phase skill finish the whole loop.

4. Update queue.
   - Mark the current item with its decision.
   - Add returned gaps, violations, missing checks, split items, or next responsibilities.
   - Preserve unfinished items.

5. Checkpoint.
   - Return a resume state that lets the next invocation continue without guessing.

## Agent Boundary

Agent rules belong to the phase that owns the rejection test.

- `loopy-theory` decides whether it needs an isolated Critic.
- `loopy-review` decides whether it needs an isolated reviewer.
- `loopy-implement` prepares review-ready slices.

This skill only records whether independence was used, unavailable, blocked, or not required.

## Output

Use this short status:

```text
Loop status:
- phase:
- cycle:
- decision:
- queue:
- independence:
```

Always include:

```text
Resume state:
- goal:
- queue:
- current phase:
- current artifact:
- last decision:
- next route:
- blocker:
```

Keep the result short unless the user asks for a formal cycle record.

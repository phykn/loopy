---
name: loopy-loop
description: Coordinate the full Loopy process across theory, implement, review, and revision phases. Use when an agent must keep the whole goal moving until every current target, responsibility, or review slice has a terminal decision.
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

A full-process loop is autonomous by default. When file edits are available, write the artifacts required to preserve the loop: cycle notes, implementation slices, review handoffs, and completion state. Do not wait for separate save/edit approval unless the user limits scope or asks for review-only mode.

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
   - Explicit user constraint that already names the boundary and rejection criteria -> record theory as skipped in evidence, mark the queue item `pending`, use the constraint as the current working theory, then route to `loopy-implement`.
   - Review-ready slice -> `loopy-review`.
   - Code violation or missing rejection check -> `loopy-implement`.
   - Theory gap -> `loopy-theory`.
   - Oversized item -> split it.
   - Before routing to `loopy-implement`, name a stable theory artifact, a theory survivor, or an explicit working theory from user constraints.

3. Run one cycle.
   - Run only the selected phase skill.
   - Do not let a phase skill finish the whole loop.

4. Update queue.
   - Mark the current item with its decision.
   - Add returned gaps, violations, missing checks, split items, or next responsibilities.
   - Preserve unfinished items.

5. Checkpoint.
   - Return a resume state that lets the next invocation continue without guessing.
   - Preserve required full-process artifacts under `.loopy/`.
   - Use phase-owned artifact paths when a phase names them, such as theory cycle notes under `.loopy/cycles/` and final theory files under `.loopy/theories/`.
   - When no narrower artifact path is named, preserve implementation slices and review handoffs in the current relevant cycle note.
   - Write completion state to `.loopy/completion.md` before any final response.
   - The completion state must include a queue table that can reject a false `complete` decision.

6. Continue available routes.
   - After each phase cycle, choose the next route immediately.
   - If the next route can run in the current turn, run that next phase cycle before finalizing.
   - Do not stop after `loopy-implement` when it produced a review-ready slice and `loopy-review` is available.
   - Do not ask whether to continue when the completion gate fails and a valid next route exists.
   - If the next route is not run, state why in the resume state.

7. Check completion.
   - Before finalizing, decide `complete` or `incomplete`.
   - `complete` requires every current queue item to have a terminal status: `passed`, `blocked`, or `out_of_scope`, recorded in `.loopy/completion.md`.
   - `incomplete` requires a named next route or blocker.
   - Do not present incomplete work as complete.

## Completion Gate

The completion gate is mandatory before any final response.

Before writing `.loopy/completion.md`, derive the active queue from the first available source in this order:

1. Provided `Resume state`.
2. Existing `.loopy/completion.md`.
3. Latest relevant `.loopy/cycles` note.
4. Current user request.

Do not remove an existing queue item unless it is recorded as `passed`, `blocked`, or `out_of_scope`. If a prior item is not terminal and no longer appears relevant, mark it `blocked` or ask only if the scope is genuinely ambiguous.

Update `.loopy/completion.md` with a queue table containing every current queue item:

```text
| item | status | next_route | evidence |
|---|---|---|---|
```

Each row must use exactly one queue status from the Phase Handoff Contract.

Also include this checklist above the queue table:

```text
- [ ] Active queue was derived from the required source order.
- [ ] No non-terminal item was dropped from the previous queue.
- [ ] Every current queue item appears in the table.
- [ ] Every row uses one Phase Handoff Contract status.
- [ ] Completion is `complete` only if every row is terminal.
```

Check an item with `[x]` only when it is true for the current loop state. If any checklist item remains unchecked, the loop is incomplete.

The loop is complete only when every row has a terminal status:

- `passed`
- `blocked`
- `out_of_scope`

The loop is incomplete if any row has a non-terminal status:

- `pending`
- `running`
- `skipped`
- `review_ready`
- `returned_to_theory`
- `returned_to_implement`
- `split`

`skipped` is a transitional queue status only. Before completion, convert it to `pending` with the next route, `blocked`, or `out_of_scope`; do not leave `skipped` as a terminal decision.

If the gate is incomplete and a valid `next_route` exists, continue immediately without asking the user whether to continue.

Ask the user only when:

- `next_route` is `blocked`;
- the queue item scope is genuinely ambiguous;
- required file edits or tools are unavailable.

Do not write `completion: complete`, whole-loop `decision: passed`, or equivalent final wording unless `.loopy/completion.md` shows all checklist items checked and every current queue item terminal. A single passed cycle closes only that item, not the whole loop.

## Phase Handoff Contract

Each phase cycle must return:

- item:
- artifact:
- decision: the queue status value for this item.
- next_route:
- queue_delta:
- blocker:
- independence:

Use these queue item statuses:

- `pending`
- `running`
- `skipped`
- `review_ready`
- `passed`
- `returned_to_theory`
- `returned_to_implement`
- `split`
- `blocked`
- `out_of_scope`

Terminal statuses are:

- `passed`
- `blocked`
- `out_of_scope`

## Route Vocabulary

Use only these `next_route` values:

- `loopy-theory`
- `loopy-implement`
- `loopy-review`
- `complete`
- `blocked`

Use the queue statuses from the Phase Handoff Contract. `review_ready` is non-terminal. It means `loopy-implement` produced a slice that must route to `loopy-review`.

## Decision Mapping

Map phase results to queue status and next route:

- theory survivor ready for implementation:
  - status: `pending`
  - next_route: `loopy-implement`
- explicit user constraint supplies the working theory:
  - status: `pending`
  - next_route: `loopy-implement`
  - evidence: theory phase skipped by explicit user boundary and rejection criteria
- theory needs another cycle:
  - status: `running`
  - next_route: `loopy-theory`
- theory blocked:
  - status: `blocked`
  - next_route: `blocked`
- implementation produced review-ready slice:
  - status: `review_ready`
  - next_route: `loopy-review`
- implementation found theory gap:
  - status: `returned_to_theory`
  - next_route: `loopy-theory`
- implementation missing rejection check:
  - status: `returned_to_implement`
  - next_route: `loopy-implement`
- review passed:
  - status: `passed`
  - next_route: `complete` if no pending queue item remains, otherwise the next pending route
- review found code violation:
  - status: `returned_to_implement`
  - next_route: `loopy-implement`
- review found theory gap:
  - status: `returned_to_theory`
  - next_route: `loopy-theory`
- item split:
  - status: `split`
  - next_route: route for the first split item
- item out of scope:
  - status: `out_of_scope`
  - next_route: `complete` if no pending queue item remains, otherwise the next pending route

## Agent Boundary

Agent rules belong to the phase that owns the rejection test.

- Invoking `loopy-loop` authorizes the isolated Critic or Reviewer agents required by the routed phase skills, unless the user explicitly forbids sub-agents.
- `loopy-theory` decides whether it needs an isolated Critic.
- `loopy-review` decides whether it needs an isolated reviewer.
- `loopy-implement` prepares review-ready slices.

This skill records whether independence was used, unavailable, blocked, or not required. Do not block a phase only to ask for separate sub-agent permission after the user has invoked `loopy-loop`.

## Output

Use this short status:

```text
Loop status:
- phase:
- cycle:
- decision:
- queue:
- completion:
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
- completion:
- blocker:
```

Keep the result short unless the user asks for a formal cycle record.

# Loopy Core

Loopy turns unstable work into stable work by looping through rejection.

```text
Loopy = Loop(Unstable -> Tested -> Stable)
```

## Core Philosophy

Work is not stable because it is finished.

Work is stable only when it survives a test that could reject it.

## Minimum

Every Loopy phase or skill must preserve:

- an unstable artifact;
- a loop that can change it;
- a test that can reject the change;
- a survivor appropriate for the next phase.

## Inheritance

Child skills may specialize the artifact and the test.

- `loopy-loop` coordinates phase routing, queue ownership, and resume state.
- `loopy-theory` runs one theory cycle.
- `loopy-implement` runs one implementation slice.
- `loopy-review` runs one review slice.

They must not remove rejection from the loop.

## Cycle, Phase, Loop

A cycle is one rejection unit:

```text
unstable artifact -> rejection test -> survivor
```

A second rejection test inside the same unit is still the same cycle.

A loop is visible only when a survivor becomes the next cycle's unstable artifact.

A phase is a group of cycles with one purpose:

- theory phase;
- implement phase;
- review phase.

A loop is the phase-level control structure:

```text
theory -> implement -> review -> revision
```

Loopy does not advance because a step finished.

Loopy advances only when the current phase produces a survivor stable enough for the next phase.

Loopy has no numeric cycle limit. Continue while the next cycle can still move the current goal toward a stable survivor.

A survivor is stable enough when it has:

- a named artifact;
- a rejection test that was actually applied;
- a decision result;
- an owner in the next phase or final stable artifact.

When a later phase names a survivor as part of its stable source of truth, earlier working artifacts may be removed.

Do not keep a working note or temporary theory file as a second source of truth unless a later phase names it as the current source.

Review decides the next path:

- `pass` -> stop only when every current queue item has a named decision, or continue to the next slice;
- code violation -> return to `loopy-implement`;
- theory gap -> return to `loopy-theory`;
- missing rejection check -> return to `loopy-implement`;
- slice too large -> split into smaller cycles.

Expose phase progress with a short loop status:

```text
Loop status:
- phase:
- cycle:
- decision:
```

The status is not a full note. It only shows that a loop is active and whether the current phase can advance.

## Repository Layout

`skills/` stores public Loopy skills.

`.loopy/` stores loop artifacts such as cycle notes, review handoffs, completion state, and final theory files.

## Agent Boundary

Use a separate agent context when the test depends on independent judgment.

Do not use a separate agent only to imitate independence.

If separate agents are available and the cycle depends on critique, review, or promotion, use one for the rejection test.

If separate agents are not available, say so in the loop status and do not present the result as independently tested.

## Boundary

A checklist completes steps.

Loopy promotes survivors.

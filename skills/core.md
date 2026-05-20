# Loopy Core

Loopy turns unstable work into stable work by looping through rejection.

```text
Loopy = Loop(Unstable -> Tested -> Stable)
```

## Core Philosophy

Work is not stable because it is finished.

Work is stable only when it survives a test that could reject it.

## Minimum

Every Loopy skill must preserve:

- an unstable artifact;
- a loop that can change it;
- a test that can reject the change;
- a stable artifact that contains only what survived.

## Inheritance

Child skills may specialize the artifact and the test.

- `loopy-theory` tests claims.
- `loopy-review` may test code, designs, or decisions.

They must not remove rejection from the loop.

## Repository Layout

`skills/` stores public Loopy skills.

`.loopy/` stores private or working loop artifacts such as cycle notes.

## Agent Boundary

Use a separate agent context when the test depends on independent judgment.

Do not use a separate agent only to imitate independence.

## Boundary

A checklist completes steps.

Loopy promotes survivors.

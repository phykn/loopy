# Loopy

Loopy is the core loop that lets unstable work become stable only by surviving a test.

```text
Loopy = Loop(Unstable -> Tested -> Stable)
```

The core philosophy is defined in `loopy/CORE.md`.

Rough work stays in the loop.

The test must be able to reject it.

Only survivors become stable.

## Minimum

Loopy must have:

- an unstable artifact;
- a loop that can change it;
- a test that can reject the change;
- a stable artifact that contains only what survived.

## Boundary

A checklist completes steps.

Loopy promotes survivors.

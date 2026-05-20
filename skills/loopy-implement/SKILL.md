---
name: loopy-implement
description: Use when implementing one code, prompt, schema, interface, or module slice from a stable THEORY_*.md file; use when an agent must translate one theory condition into one traceable implementation responsibility instead of inventing behavior or architecture.
---

# Loopy Implement

## Overview

Use this skill to map stable theory into code.

Implementation is not invention. It translates the theory's minimum conditions, boundaries, and prohibitions into code responsibilities that can be rejected.

Follow the Loopy shape:

```text
Theory -> Code -> Review -> Revision
```

Revision either changes the implementation slice or returns a theory gap to `loopy-theory`.

In this skill, the unstable artifact is the implementation slice.
The rejection test is the rejection check attached to that slice.
The output of this skill is a review-ready implementation slice.
The stable artifact is code that preserves the theory boundary after `loopy-review`.

Do not advance to review because implementation steps are finished. Advance only when the current slice is review-ready.

A review-ready slice is not stable code. It is a rejectable mapping from one theory condition to one code responsibility.

A slice is review-ready only when another reviewer can reject it without inferring hidden intent.

For multi-responsibility requests, return the remaining responsibility queue to `loopy-loop`. Do not silently complete the whole implementation phase inside this skill.

From this skill file, read `../core.md` as the parent philosophy when it exists.

## Minimum

A valid implementation slice contains:

- Theory source: the `THEORY_*.md` being implemented.
- Stable source boundary: final theory files under `theories/` are implementation sources; `.loopy/cycles` notes are working notes, not implementation sources.
- Theory condition: one claim, minimum condition, boundary, or prohibition.
- Code responsibility: the function, interface, schema, prompt, or module responsibility created or changed.
- Boundary preservation: the code does not cross a theory prohibition, widen the theory's claim, or add unsupported behavior.
- Rejection check: a test, static check, named review criterion, or concrete failure case that could reject the mapping.
- Traceability: every changed behavior can be traced back to the named theory condition.

If a required responsibility has no theory condition, it is a theory gap, not implementation scope.

## Workflow

Run one implementation cycle. Do not run the next slice inside this skill; return the slice and next route to `loopy-loop`.

```text
read theory -> map responsibility -> implement slice -> add rejection check -> return route
```

1. Read theory.
   - Use the named `THEORY_*.md` file when provided.
   - If no stable theory exists, return to `loopy-theory`.
   - Re-read the theory source and current request before starting each new slice.

2. Extract one theory condition.
   - Use one claim, minimum condition, boundary, or prohibition.
   - Do not combine unrelated theory conditions into one slice.

3. Map it to one code responsibility.
   - Identify the function, interface, schema, prompt, or module responsibility.
   - If the responsibility has no theory condition, mark it as a theory gap.

4. Implement the smallest slice.
   - Add only the behavior required by the mapped theory condition.
   - Smallest means removing any behavior would fail the named theory condition or rejection check.
   - Do not add convenience behavior, fallback behavior, or architecture not justified by the theory.

5. Add a rejection check.
   - Use a test, static check, named review criterion, or concrete failure case.
   - The check must be able to reject the mapping.

6. Queue for review or route.
   - If the theory is missing, return to `loopy-theory`.
   - If the implementation exists, add it to the pending review queue.
   - If `loopy-review` is unavailable, return the review handoff note instead of pretending review ran.
   - Do not decide the whole implementation phase after one slice while theory-backed responsibilities remain.
   - When handing off, name the pending review queue, remaining responsibility queue, and the decision for each item.
   - Handoff to review is loop continuation, not abandonment of autonomous progress.
   - If theory-backed responsibility remains and review is not needed to unblock it, return the next responsibility for `loopy-loop` to schedule.

## Output

End with:

- Loop status
- Theory source
- Implemented slice
- Theory gaps
- Rejection checks
- Pending review queue
- Remaining responsibility queue with named decisions
- Handoff: `loopy-review`, `loopy-theory`, or the review handoff note when `loopy-review` is unavailable

Use this brief status:

```text
Loop status:
- phase: implement
- cycle:
- decision:
- responsibility queue:
```

Use this slice format when useful:

```text
Theory condition:
Code responsibility:
Boundary preserved:
Rejection check:
Files changed:
```

## Cycle Stop And Handoff

Stop the cycle or hand off when:

- the next responsibility has no theory condition;
- the implementation requires changing the theory source;
- the next change would add unsupported convenience behavior, fallback behavior, or architecture;
- the current slice has no rejection check;
- the current responsibility has a named decision: implemented, handed off, blocked by theory gap, or rejected as unsupported;
- review is needed to decide or unblock the next responsibility.

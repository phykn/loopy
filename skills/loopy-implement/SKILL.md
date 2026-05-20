---
name: loopy-implement
description: Use when implementing code, prompts, schemas, interfaces, or modules from a stable THEORY_*.md file; use when an agent must translate theory conditions into traceable implementation slices instead of inventing behavior or architecture.
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

There is no numeric slice limit. Continue with the next implementation slice while the current request's goal still has a theory-backed responsibility to implement.

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

Repeat this cycle until the implementation goal is reached or a handoff condition is hit:

```text
read theory -> map responsibility -> implement slice -> add rejection check -> hand off -> read theory
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
   - Do not add convenience behavior, fallback behavior, or architecture not justified by the theory.

5. Add a rejection check.
   - Use a test, static check, named review criterion, or concrete failure case.
   - The check must be able to reject the mapping.

6. Hand off.
   - If the theory is missing, return to `loopy-theory`.
   - If the implementation exists, hand it off to `loopy-review` when available.
   - If `loopy-review` is unavailable, return the review handoff note instead of pretending review ran.
   - Handoff to review is loop continuation, not abandonment of autonomous progress.
   - After review returns `pass` and theory-backed responsibility remains, return to step 1 for the next slice.

## Output

End with:

- Loop status
- Theory source
- Implemented slices
- Theory gaps
- Rejection checks
- Handoff: `loopy-review`, `loopy-theory`, or the review handoff note when `loopy-review` is unavailable

Use this brief status:

```text
Loop status:
- phase: implement
- cycle:
- decision:
```

Use this slice format when useful:

```text
Theory condition:
Code responsibility:
Boundary preserved:
Rejection check:
Files changed:
```

## Phase Stop And Handoff

Stop the implement phase or hand off when:

- the next responsibility has no theory condition;
- the implementation requires changing the theory source;
- the next change would add unsupported convenience behavior, fallback behavior, or architecture;
- the current slice has no rejection check;
- the current request's implementation goal is reached;
- the current slice should be reviewed by `loopy-review` or a review handoff note before more implementation continues.

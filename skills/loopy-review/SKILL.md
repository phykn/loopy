---
name: loopy-review
description: Use when reviewing code, prompts, schemas, interfaces, or modules against a stable THEORY_*.md source; use when an agent must decide whether an implementation slice passes, needs code revision, or exposes a theory gap.
---

# Loopy Review

## Overview

Use this skill to test whether a theory-mapped implementation slice preserves its theory boundary.

This is not general code review. Review the mapping between theory and implementation.

Follow the Loopy shape:

```text
Theory -> Code -> Review -> Revision
```

Revision passes the slice, returns a code violation to `loopy-implement`, or returns a theory gap to `loopy-theory`.

In this skill, the unstable artifact is the implementation slice under review.
The rejection test is the boundary test against the theory source.
The stable artifact is code that preserves the theory boundary after review.

There is no numeric review limit. Continue with the next review slice while the current request's goal still has unreviewed implementation slices.

Use an isolated reviewer agent for the boundary test when separate agents are available. If separate agents are unavailable, mark that in the loop status and do not present the result as independently reviewed.

From this skill file, read `../core.md` as the parent philosophy when it exists.

## Minimum

A valid review unit contains:

- Theory source: the `THEORY_*.md` used by the implementation.
- Theory condition: the claim, minimum condition, boundary, or prohibition being tested.
- Implementation slice: the code responsibility produced by `loopy-implement`.
- Rejection check: the test, static check, named review criterion, or failure case attached to the slice; if missing, Decision: `return to loopy-implement`.
- Applied rejection: a `pass` decision must name how the rejection check was applied and what result survived.
- Decision: `pass`, `return to loopy-implement`, or `return to loopy-theory`.

Generic code quality is outside `loopy-review` unless it proves a theory violation.

## Workflow

1. Select the review unit.
   - Use one implementation slice when provided.
   - If no slice is provided, reconstruct the smallest slice from the changed code and its theory source.

2. Check theory traceability.
   - Identify the theory condition.
   - If no theory condition supports the code responsibility, decide whether the code need is real.
   - If the code responsibility is unsupported convenience behavior, fallback behavior, or architecture, return to `loopy-implement`.
   - If the code need is real but the theory is missing or too weak, return to `loopy-theory`.

3. Test boundary preservation.
   - Ask whether the code crosses a prohibition, widens the theory claim, or adds unsupported behavior.
   - Use the slice's rejection check.
   - If the slice has no rejection check, decide `return to loopy-implement`.

4. Decide.
   - `pass`: the slice preserves the theory boundary and survives the rejection check.
   - `return to loopy-implement`: the theory is sufficient but the code violates it, or the slice is missing a rejection check.
   - `return to loopy-theory`: the code need is real but the theory is missing or too weak.
   - A code need is real only when required by the implementation slice or user request and not justified or forbidden by the current theory. Reviewer preference is not a real code need.
   - A slice cannot pass only because no violation was noticed. It passes only when the boundary test was applied and the implementation survived it.

5. Return the smallest next revision.
   - Do not produce a generic improvement list.
   - Do not rewrite theory inside review.

## Output

End with:

- Loop status
- Theory source
- Reviewed slices
- Decision
- Evidence
- Next revision

Use this brief status:

```text
Loop status:
- phase: review
- cycle:
- decision:
- independent reviewer: used | unavailable
```

Use this slice format when useful:

```text
Theory condition:
Implementation slice:
Boundary test:
Decision: pass | return to loopy-implement | return to loopy-theory
Evidence:
Next revision:
```

## Stop Conditions

Stop when:

- the implementation slice omits its theory source; Decision: `return to loopy-implement`;
- the finding is only generic code quality and does not prove a theory violation;
- the code need is real but no stable theory source exists, or the theory is missing or too weak; Decision: `return to loopy-theory`;
- the slice is missing a rejection check; Decision: `return to loopy-implement`;
- the current review goal is reached and no next revision is needed.

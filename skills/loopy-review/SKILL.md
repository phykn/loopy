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

For multi-slice requests, keep a review queue. Do not declare the review goal reached until every slice has a named decision: pass, return to `loopy-implement`, return to `loopy-theory`, split, or out of scope.

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
- Queue decision: `pass`, `return to loopy-implement`, `return to loopy-theory`, `split`, or `out of scope`.

Generic code quality is outside `loopy-review` unless it proves a theory violation.

## Workflow

Repeat this cycle until the review goal is reached or a routing decision returns to another phase with the remaining review queue preserved:

```text
read theory and slice -> test boundary -> decide route -> carry result -> read next slice
```

1. Read theory and select the review unit.
   - Re-read the theory source, current request, and implementation slice before each review cycle.
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
   - If routing after one slice, name the remaining review queue and the decision state for each item.

5. Return the smallest next revision.
   - Do not produce a generic improvement list.
   - Do not rewrite theory inside review.
   - Smallest means removing any requested revision would leave the boundary violation, missing rejection check, or theory gap unresolved.
   - If the slice passes and unreviewed slices remain for the current goal, carry the result forward and return to step 1 for the next slice.

## Output

End with:

- Loop status
- Theory source
- Reviewed slices
- Decision
- Evidence
- Remaining review queue with named decisions
- Next revision

Use this brief status:

```text
Loop status:
- phase: review
- cycle:
- decision:
- independent reviewer: used | unavailable
- review queue:
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

## Review Stop And Routing

Stop review or route when:

- the implementation slice omits its theory source; Decision: `return to loopy-implement`;
- the finding is only generic code quality and does not prove a theory violation;
- the code need is real but no stable theory source exists, or the theory is missing or too weak; Decision: `return to loopy-theory`;
- the slice is missing a rejection check; Decision: `return to loopy-implement`;
- the current review goal is reached and every slice in the review queue has a named decision.

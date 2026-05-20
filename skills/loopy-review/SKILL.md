---
name: loopy-review
description: Use when reviewing one code, prompt, schema, interface, or module slice against a stable .loopy/theories/THEORY_*.md source; use when an agent must decide whether one implementation slice passes, needs code revision, or exposes a theory gap.
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

For multi-slice requests, return the remaining review queue to `loopy-loop`. Do not silently complete the whole review phase inside this skill.

Use an isolated reviewer agent for the boundary test when separate agents are available. If separate agents are unavailable, mark that in the loop status and do not present the result as independently reviewed.

From this skill file, read `../core.md` as the parent philosophy when it exists.

## Minimum

A valid review unit contains:

- Theory source: the `.loopy/theories/THEORY_*.md`, theory survivor, or explicit working theory used by the implementation.
- Theory condition: the claim, minimum condition, boundary, or prohibition being tested.
- Implementation slice: the code responsibility produced by `loopy-implement`.
- Rejection check: the test, static check, named review criterion, or failure case attached to the slice; if missing, Decision: `returned_to_implement`.
- Applied rejection: a `passed` decision must name how the rejection check was applied and what result survived.
- Decision: use the `decision`, `next_route`, and queue status vocabulary from `loopy-loop`.
- Queue decision: `passed`, `returned_to_implement`, `returned_to_theory`, `split`, or `out_of_scope`.

Generic code quality is outside `loopy-review` unless it proves a theory violation.

## Workflow

Run one review cycle. Do not run the next slice inside this skill; return the decision and next route to `loopy-loop`.

```text
read theory and slice -> test boundary -> decide route -> return result
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
   - If the slice has no rejection check, decide `returned_to_implement`.

4. Decide.
   - `passed`: the slice preserves the theory boundary and survives the rejection check.
   - `returned_to_implement`: the theory is sufficient but the code violates it, or the slice is missing a rejection check.
   - `returned_to_theory`: the code need is real but the theory is missing or too weak.
   - `split`: the review unit contains multiple independent slices that need separate decisions.
   - `out_of_scope`: the slice is outside the current theory or user-requested boundary.
   - A code need is real only when required by the implementation slice or user request and not justified or forbidden by the current theory. Reviewer preference is not a real code need.
   - A slice cannot pass only because no violation was noticed. It passes only when the boundary test was applied and the implementation survived it.
   - If routing after one slice, name the remaining review queue and the decision state for each item.

5. Return the smallest next revision.
   - Do not produce a generic improvement list.
   - Do not rewrite theory inside review.
   - Smallest means removing any requested revision would leave the boundary violation, missing rejection check, or theory gap unresolved.
   - If the slice passes and unreviewed slices remain for the current goal, return the remaining review queue for `loopy-loop` to schedule.

## Output

Also return the Phase Handoff Contract fields required by `loopy-loop`: `item`, `artifact`, `decision`, `next_route`, `queue_delta`, `blocker`, and `independence`.

Use `decision`, `next_route`, and queue status values from the vocabulary defined in `loopy-loop`.

End with:

- Loop status
- Theory source
- Reviewed slice
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
- independent reviewer: used | unavailable | blocked | not required
- review queue:
```

Use this slice format when useful:

```text
Theory condition:
Implementation slice:
Boundary test:
Decision: passed | returned_to_implement | returned_to_theory | split | out_of_scope
Evidence:
Next revision:
```

## Review Cycle Routing

Stop the cycle or route when:

- the implementation slice omits its theory source; Decision: `returned_to_implement`;
- the finding is only generic code quality and does not prove a theory violation;
- the code need is real but no stable theory source exists, or the theory is missing or too weak; Decision: `returned_to_theory`;
- the slice is missing a rejection check; Decision: `returned_to_implement`;
- the review unit must be divided into independently rejectable slices; Decision: `split`;
- the slice is outside the current theory or requested boundary; Decision: `out_of_scope`;
- the current slice has a named decision.

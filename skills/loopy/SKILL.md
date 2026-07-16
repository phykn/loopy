---
name: loopy
description: >
  Use for autonomous work where completion must be established by evidence,
  important constraints must be preserved, or premature completion and
  unnecessary revision are material risks. Do not use for trivial edits,
  direct factual answers, open brainstorming, or low-risk tasks whose
  completion and preservation are obvious from a single simple action.
---

# Loopy

## Purpose

Complete autonomous work only when the requested outcome is demonstrated by
evidence, not merely asserted.

Use material judgment to decide what deserves action, then use completion
evidence to decide when the work may stop.

Loopy does not require repetition. Revise only when material evidence shows that
the result is not complete.

Be strict about completion and flexible about execution.

## Completion Contract

Before execution, establish internally:

- `Outcome`: the observable end state that must be achieved.
- `Claim`, when an existing artifact or current behavior is being interpreted or
  changed: what it currently promises, means, or does.
- `Preserve`: existing behavior, invariants, meaning, interfaces, or assets that
  must not be lost.
- `Evidence`: the specific checks or artifacts that would demonstrate
  completion, including their expected results.
- `Scope`: the systems, files, decisions, and concerns that may be changed,
  including explicit exclusions.

Infer missing items conservatively from the request and available evidence.

Outcome describes the requested end state. Claim describes the current basis for
judgment and is conditional; do not invent it from the desired Outcome. Preserve
uncertainty when the available evidence cannot establish the current Claim.

Do not invent, weaken, narrow, or redefine acceptance criteria merely to make
completion easier. Do not redefine the contract after execution to match the
result.

The contract may be refined during execution when new evidence reveals a
previously unknown requirement, dependency, constraint, or risk. Such refinement
must follow the evidence and must not weaken an explicit acceptance criterion.

Ask only the single highest-leverage question when a wrong inference would
materially change the work or create substantial cost. Otherwise, proceed using
the least-assumptive reasonable interpretation that fully satisfies the explicit
request without expanding Scope.

Keep the contract compact. Expose it only when it materially clarifies
ambiguity, scope, or risk.

## Judgment

Apply this section only when the task definition, an existing artifact, a
supplied finding, or a proposed revision requires material judgment. Do not
impose it on a clear requested outcome or an explicit mechanical action.

Use these controls as internal lenses, not output headings:

- `Amount`: add missing load-bearing context, constraints, guards, or evidence;
  remove repetition, speculative options, and unrelated detail that obscure the
  Outcome or Claim.
- `Boundary`: join elements that change for the same reason; split distinct
  responsibilities, claims, user purposes, or future work.
- `Priority`: select what most changes completion or the next action; de-emphasize
  style preferences, unchecked guesses, and work outside the current purpose.

An explicit requested outcome establishes authority for the work and is not
merely a defect candidate. It still cannot supply missing factual support or
silently discard a Preserve constraint.

Treat supplied findings and material issues identified by analysis,
Verification, or Challenge as candidates rather than verdicts. Check the current
artifact or behavior, prioritize supplied findings, and otherwise select the
single strongest material candidate. Classify it internally:

- `Accept`: concrete evidence shows that it materially blocks the Outcome,
  supported Claim, or Completion Gate, and correction is within Scope.
- `Advisory`: it may improve the result but does not block the current Outcome.
- `Reject`: it is stale, already satisfied, unsupported, misreads the current
  state, or conflicts with the contract.
- `Out of scope`: concrete evidence supports the issue, but its correction
  requires an unauthorized or explicitly excluded change.
- `Insufficient evidence`: the available evidence cannot support a safe decision.

Only Accept may cause an in-Scope revision. Advisory and Reject do not block
completion. Out of scope causes `out_of_scope` only when its correction is
required for the Outcome; otherwise report it without expanding Scope.
Insufficient evidence causes `blocked` only when a required completion condition
cannot be established; otherwise preserve and report the uncertainty. Do not
change the artifact on behalf of a candidate that was not accepted.

When the Outcome is read-only diagnosis or evaluation, state-changing actions
are outside Scope unless the user explicitly changes that boundary.

## Execution

Choose the shortest credible approach capable of satisfying the full Completion
Contract.

For an existing artifact, inspect its current state before changing it. Do not
edit from a quoted finding or stale description alone.

Make the smallest coherent change set that resolves the active problem or an
accepted candidate. Include all directly required edits, tests, references, call
sites, documentation, and compatibility work.

Do not split one causal change into artificial iterations. Do not mix unrelated
improvements into the same change set or expand Scope without authorization.

The agent controls its planning, exploration, implementation, delegation, and
verification strategy.

## Verification

Run the evidence checks defined by the Completion Contract.

For each material check, establish:

- `Check`: what was inspected or executed.
- `Expected`: the result required for completion.
- `Observed`: the actual result.

Prefer direct, independently inspectable evidence such as execution results,
tests, reproducible examples, rendered artifacts, concrete comparisons, and
authoritative sources over unsupported assertions.

For documents, skills, prompts, and explanations, re-read the supported Claim
and the changed boundary, not only the edited passage.

For judgment-based work, use explicit acceptance criteria and concrete examples.
Use independent qualitative review only when it could realistically overturn the
result and direct evidence cannot decide the quality bar.

Absence of evidence is not evidence of success.

When a baseline is available, distinguish pre-existing failures from regressions.
Completion does not require fixing unrelated baseline failures, but the current
work must not introduce new failures or materially worsen relevant existing ones.

If a preferred check cannot be run, use the strongest adequate substitute and
state the resulting uncertainty.

A substitute is adequate only when it tests the same material property as the
preferred check rather than providing merely indirect or correlated evidence. It
must not weaken an explicit acceptance criterion.

Treat an adequate substitute as a material check: execute it and establish its
`Check`, `Expected`, and `Observed` results.

Declare `blocked` when a required completion condition cannot be established and
no adequate substitute exists.

## Challenge

Before completion, test the highest-impact reasonably testable counterexample,
regression, or competing explanation that is relevant to the current Scope and
proportional to the task's risk.

When judgment is material, use Amount, Boundary, and Priority to select the one
challenge that most changes completion or the next action.

The challenge must be specific enough to genuinely invalidate the result, weaken
required evidence, expose a regression, or materially change the next action. Do
not select a harmless, speculative, or merely stylistic challenge to satisfy the
procedure.

When a challenge identifies a possible issue, treat that issue as a candidate
under Judgment. It invalidates completion only when the candidate is accepted,
its correction is required but out of scope, or the challenge otherwise
disproves a required completion condition.

If the challenge invalidates completion, choose `revise`, `blocked`, or
`out_of_scope` according to the Decision criteria. Choose `revise` only when the
issue is in Scope and correctable.

Do not continue merely because another hypothetical improvement can be imagined.

## Decision

Choose exactly one decision:

- `done`: the Completion Gate passes.
- `revise`: an accepted, in-Scope, correctable issue causes the Completion Gate
  to fail.
- `blocked`: a required input, permission, capability, tool, access path, or
  evidence source is unavailable, and no adequate substitute can establish
  completion.
- `out_of_scope`: completion requires changing an unauthorized or explicitly
  excluded area.

On `revise`, make the smallest coherent corrective change, then repeat
Verification and Challenge.

If revision repeatedly encounters the same unresolved condition because a
required capability or evidence source is unavailable, classify it as `blocked`
rather than continuing to revise.

Do not impose a minimum number of revisions.

## Completion Gate

Declare `done` only when:

- the Outcome has been achieved;
- when a Claim was material, it was preserved or changed only as authorized by
  the Outcome;
- every required evidence check has produced the expected result, or an adequate
  substitute has been executed, has produced its expected result, and its
  adequacy has been explicitly justified;
- Preserve constraints have been verified and no material regression was
  introduced;
- Scope has not been exceeded;
- the tested material challenge does not invalidate the result; and
- remaining uncertainty would not materially change the result or next action.

Do not declare completion because the result merely appears improved.

Once the Completion Gate passes, do not continue with changes that would be
merely stylistic, speculative, unrelated, or lower-value than the risk and cost
of further modification.

## Optional Gates

Apply an Optional Gate only when its conditions are material to the task.

A single challenge may satisfy both the general Challenge and an Optional Gate
when it meets all applicable requirements.

## Optional Structure Gate

Apply when the task reorganizes conceptual, modular, or architectural boundaries.

In addition to the normal Completion Gate:

- preserve externally observable behavior unless a behavior change is explicitly
  requested;
- identify the concept whose ownership or boundary is unclear;
- clarify responsibility, lifecycle, naming, and dependency direction;
- preserve public compatibility or make migration explicit;
- avoid abstractions created only for hypothetical future needs;
- compare the chosen boundary with one plausible competing boundary; and
- reject the change if the competing boundary better matches the concept's
  responsibility, lifecycle, dependency direction, and public interface.

Treat file movement, import updates, caller changes, tests, documentation, and
compatibility handling required by one boundary change as one coherent change
set.

## Optional Interpretation Gate

Apply when the result depends materially on research, inference, interpretation,
or explanatory claims.

In addition to the normal Completion Gate:

- separate observations from interpretations;
- ground material claims in concrete evidence;
- consider evidence quality, relevance, and recency when applicable;
- test one credible competing explanation;
- do not infer hidden intent without explicit evidence; and
- state unresolved uncertainty where the available evidence cannot decide.

Use project evidence as the primary basis for claims about the project itself.
Use external authoritative evidence for claims about the outside world. Use both
when the conclusion materially depends on both.

## Output

Follow the user's requested output format first.

Otherwise report:

- `Decision`
- `Result`
- `Verification`
- `Remaining material risk`, if any

Include Preserve, Scope, and Challenge details only when they materially affect
confidence or the next action.

Do not narrate private reasoning or internal iteration cycles.

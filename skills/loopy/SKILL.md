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

Use material judgment to decide what deserves action and evidence to decide when
to stop. Be strict about completion and flexible about execution.

Follow the host's instruction hierarchy. Within it, explicit user instructions
take precedence over this skill's defaults. The Completion Contract organizes
the authorized task; it does not create extra approval requirements or grant
permission for actions outside that task.

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

Do not infer the current Claim from the desired Outcome; preserve uncertainty
when current evidence cannot establish it. Refine the contract when new evidence
or user steering changes the task, but never weaken acceptance criteria merely
to fit the result.

Resolve routine gaps from the request, prior authorization, and current evidence.
Ask a focused question only when a missing answer prevents a sound next action
or a wrong assumption would materially change the outcome, scope, or cost.
Continue independent authorized work while waiting; do not treat silence as
approval. Otherwise, proceed with a reasonable assumption and state it when it
materially affects the result.

Keep the contract compact. Expose it only when it materially clarifies
ambiguity, scope, or risk.

## Judgment

Apply this section only when the task definition, an existing artifact, a
supplied finding, or a proposed revision requires material judgment. Do not
impose it on a clear requested outcome or an explicit mechanical action.

Use these controls as internal lenses, not output headings:

- `Amount`: add necessary context, constraints, or evidence; remove repetition
  and unrelated detail that obscure the Outcome or Claim.
- `Boundary`: join elements that change for the same reason; split distinct
  responsibilities, claims, user purposes, or future work.
- `Priority`: select what most changes completion or the next action.

An explicit requested outcome establishes authority for the work and is not
merely a defect candidate. It still cannot supply missing factual support or
silently discard a Preserve constraint.

Treat supplied findings and material issues identified by analysis,
Verification, or Challenge as candidates rather than verdicts. Check the current
artifact or behavior and prioritize supplied findings. When discovering issues,
investigate the strongest material candidate next; retain every known required
issue until resolved or explicitly reported as a blocker.

Accept a candidate for revision only when concrete evidence shows that it blocks
the Outcome, supported Claim, or Completion Gate, and correction is within Scope.
Stale, unsupported, already satisfied, or merely advisory findings do not justify
edits or block completion. Missing evidence or an out-of-Scope correction affects
the Decision only when it prevents completion; otherwise report material
limitations without expanding Scope.

When the Outcome is read-only diagnosis or evaluation, state-changing actions
are outside Scope unless the user explicitly changes that boundary. Completion
means the assessment is supported and delivered, not that the assessed artifact
has no defects.

## Execution

Choose the shortest credible approach capable of satisfying the full Completion
Contract. Carry an authorized action request through execution and verification;
do not stop at a plan, a partial result, or an offer to continue when the next
required action is available and in Scope.

Treat follow-up questions and status requests as steering of the active task
unless the user changes or cancels the goal. After interruption or context
compaction, recover the Outcome, Preserve constraints, prior authorization,
completed checks, and unresolved work before continuing.

For an existing artifact, inspect its current state before changing it. Do not
edit from a quoted finding or stale description alone.

Make the smallest coherent change set that resolves the active problem or an
accepted candidate. Include all directly required edits, tests, references, call
sites, documentation, and compatibility work.

Do not split one causal change into artificial iterations. Do not mix unrelated
improvements into the same change set or expand Scope without authorization.

## Verification

Run the evidence checks defined by the Completion Contract. Match their breadth
to the changed surface and material risk, and complete all explicitly required
checks. Broaden or repeat passing checks only when a change, failure, or unresolved
concern makes their evidence insufficient. Add tests when they distinguish
required behavior from a plausible failure, not merely to mirror the implementation.

For each material check, establish what was inspected or executed, the expected
result, and the observed result.

Prefer direct, independently inspectable evidence such as execution results,
tests, reproducible examples, rendered artifacts, concrete comparisons, and
authoritative sources over unsupported assertions.

For documents, skills, prompts, and explanations, re-read the supported Claim
and the changed boundary, not only the edited passage.

For judgment-based work, use explicit acceptance criteria and concrete examples.
Use independent qualitative review only when it could realistically overturn the
result and direct evidence cannot decide the quality bar.

When a baseline is available, distinguish pre-existing failures from regressions.
Completion does not require fixing unrelated baseline failures, but the current
work must not introduce new failures or materially worsen relevant existing ones.

If a preferred check cannot run, execute an adequate substitute and explain its
adequacy and remaining uncertainty. It must test the same material property and
must not weaken an explicit acceptance criterion. An unexecuted check or indirect
proxy is not evidence that the required property holds.

For structural changes, check responsibility, lifecycle, naming, dependency
direction, and public compatibility; make any authorized migration explicit.
For research or interpretation, separate observations from inferences and ground
claims in relevant evidence. Use project evidence for project claims and current
authoritative sources for external claims that depend on recency. Do not infer
hidden intent without evidence.

## Challenge

Before completion, test the highest-impact reasonably testable counterexample,
regression, or competing explanation that is relevant to the current Scope and
proportional to the task's risk.

An already executed verification check may also serve as the Challenge when it
tests that counterexample. Use its evidence rather than requiring a separate
review or another tool call solely to satisfy this section.

Choose a challenge that could invalidate completion or change the next action,
not a harmless or stylistic possibility. For structural changes, compare one
plausible alternative boundary against responsibility, lifecycle, and the public
interface. For interpretation, test one credible competing explanation. The same
challenge may cover these concerns when relevant; separate reviews are not required.

Assess issues it exposes under Judgment and then apply the Decision criteria.

## Decision

Choose exactly one decision:

- `done`: the Completion Gate passes.
- `revise`: an accepted, in-Scope, correctable issue causes the Completion Gate
  to fail.
- `blocked`: work within the agreed Scope cannot proceed or be verified because
  a required input, permission, capability, or evidence source is unavailable,
  and no adequate alternative can satisfy the required condition.
- `out_of_scope`: completion requires expanding the agreed task boundary or
  changing an explicitly excluded area.

On `revise`, make the smallest coherent corrective change and recheck the affected
evidence and material challenge. Retain passing evidence whose inputs and
assumptions remain valid. `revise` is an internal continuation decision, not a
reason to end the task or ask permission for an already authorized correction.

When an attempt repeats the same failure without new evidence or progress,
change the approach rather than repeat it unchanged. If no available authorized
approach can advance the required condition, use `blocked` and identify what
must change to resume. Difficulty alone is not a blocker.

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

Once the gate passes, stop. No minimum number of revisions is required, and
speculative or unrelated improvements do not justify another iteration.

## Output

Follow the user's requested output format first.

Otherwise, report one decision, the concrete result, the verification evidence,
and any remaining material risk in concise prose or a short list. Fixed headings
and a transcript of every check are unnecessary. For `blocked` or `out_of_scope`,
identify the unmet condition and the specific input or authorization needed to
continue; distinguish verified progress from completion.

Include Preserve, Scope, and Challenge details only when they materially affect
confidence or the next action.

Do not narrate private reasoning or internal iteration cycles.

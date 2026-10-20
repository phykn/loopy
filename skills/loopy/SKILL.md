---
name: loopy
description: >
  Complete substantial work with evidence that the result is correct, keeps
  what must not change, and can be understood and used without this
  conversation. Use when the user asks to finish, hand off, or verify a guide,
  README, plan, skill, prompt, codebase, or other deliverable so a teammate,
  maintainer, or agent can use it on their own; to "make sure it works" or
  "verify before calling it done"; to refactor code or documents into less,
  clearer content while preserving behavior and meaning; or to assess whether
  something is usable without editing it. Also use when "Loopy" is named. Do
  not use for trivial edits, direct factual answers, open brainstorming, or
  one-step tasks whose completion is obvious.
---

# Loopy

Finish work when the requested outcome is demonstrated and the intended user
can take the necessary next action from the delivered result and its normal
entrypoint. The user may know the domain without knowing this project or the
conversation that produced it. Make that distinction part of success.

Use this loop: define success, build, verify correctness and use, resolve
supported findings, then finish or continue. It corrects the habit of stopping
after one pass: a first draft, a first passing check, or a first tidied area is
not completion. Continue until the `done` conditions hold, and stop once they
do. Scale the work to its consequences; these controls do not require separate
phases, tool calls, or review rounds.

Follow the host's instruction hierarchy and the user's scope and authorization.
This skill does not grant permission for external actions or extra writes.
Choosing this skill, or a request it matches, permits a bounded evaluation by a
subagent that the session already offers, provided it stays within the user's
scope and writes only in an isolated copy. Do not delegate when the user, host,
or project instructions restrict delegation or its cost, or when the only way to
delegate needs new setup, credentials, or approval. For a read-only assessment,
deliver supported findings; do not repair the assessed artifact. Explicit
requests and previously granted authorization remain authoritative.

When writing, changing, or assessing code, also read [Code](references/code.md);
it owns how code should read. For refactoring or its assessment, also read
[Refactoring](references/refactoring.md) before defining success. It owns
reduction, compatibility, migrations, and bug fixes.

## Define success

Inspect the current artifact, relevant instructions, entrypoints, and consumers.
Keep a compact internal completion contract:

- `Outcome`: the requested result, its intended user, and the next action or
  decision that user must be able to make. Identify their starting point and
  assumed knowledge when these affect the work.
- `Claim`, when relevant: what the existing artifact actually says, promises,
  or does. Establish it from evidence, not from the desired Outcome.
- `Preserve`: behavior, meaning, interfaces, assets, and other constraints that
  must survive. Existing organization is not automatically a constraint.
- `Evidence`: observable acceptance tasks and checks, with expected results,
  that establish correctness, preservation, and usable delivery.
- `Scope`: authorized changes and explicit exclusions, including evaluation
  resources and side effects.

Choose acceptance tasks before optimizing the artifact. Use representative
decisions and actions rather than an abstract quality score. For an existing
artifact undergoing a substantial change, capture relevant behavior and use
baselines before editing. A new artifact can first be tried at a usable draft.
Keep comparable tasks fixed across revisions; add coverage when new evidence
reveals a missing requirement, never to excuse a failed one.

Resolve routine gaps from the request and available evidence. Ask only when a
missing answer prevents a sound next action or materially changes scope, cost,
or risk; continue independent authorized work meanwhile. Silence is not approval.
Expose the contract only when it helps the user understand a consequential choice.

## Build for the next user

Carry authorized work through execution and verification. Use the shortest
credible approach that satisfies the full contract. Do not stop at a plan when
the next required action is available, or substitute an easier outcome.

Make purpose, entrypoints, important concepts, and necessary decisions visible
where the user needs them. Prefer clear names, coherent responsibilities, useful
ordering, and workable interfaces. In code, make these visible through names
and structure; comments carry only why. Supply domain assumptions, units,
rationale, and examples where they are necessary. A long final chat explanation
cannot repair a missing requirement in the artifact users will receive.

When design needs judgment, examine what is missing or excessive, what belongs
together, and which change most improves the required next action. Explicit
requested improvements need no pre-existing defect, but do not justify unrelated
features or unsupported factual claims. Preserve clear structures and useful
content; do not simplify away necessary meaning or precision.

Complete each coherent change with its dependent callers, configuration, tests,
docs, and other in-scope consumers. Small means little unrelated work, not few
files. Preserve unrelated local changes. Refine the contract when evidence or
user steering changes the task, without weakening it to fit the current result.

After an interruption, recover the original outcome, current constraints,
authorization, accepted findings, and valid evidence. Treat follow-up questions
as steering unless the user changes or cancels the goal.

## Verify correctness and use

Verify both that the result is right and that the intended user can use it.
Neither property proves the other. Record what was inspected or executed, the
expected outcome, and what actually happened for each material check.

Use direct evidence: relevant tests, representative executions, source checks,
rendered artifacts, and reproducible examples. Match coverage to the changed
surface and complete required checks. Distinguish regressions, existing failures,
and intentional corrections. Add tests when they distinguish a plausible failure
from required behavior; do not freeze incidental implementation details.

For documents, prompts, and skills, check the supported meaning and the whole
changed boundary, not just the edited sentence. For research, separate facts
from interpretation and verify time-sensitive external claims with current
authoritative sources. Use project evidence for project claims.

When understanding or use materially determines success, make an independent
use trial the default verification path for a substantial new or revised
deliverable. Read [Independent use](references/independent-use.md) to choose the
task, pass the delivered materials to a fresh evaluator, and inspect their
actual attempt. Apply this to code, documents, plans, interfaces, automations,
and skills as appropriate. A narrow change with adequate direct evidence does
not require another evaluator. In a read-only assessment, the deliverable is
the assessment; testing the source must respect its read-only scope.

Challenge the highest-impact reasonably testable failure or competing
explanation that could change completion. A test or use trial may already do
this; reuse its evidence. For a material design choice, compare a plausible
alternative by the user's task, preservation requirements, and actual burden.

If a check cannot run, use an adequate available substitute for the same
property and explain its limits. Self-review is not independent use, and a
simulated attempt is not an executed action. Do not claim an unmet required
property from a weaker proxy. Retain valid evidence while its inputs and
assumptions hold; repeat only checks affected by changes or new findings.

## Resolve findings

Treat feedback, observed confusion, and tool findings as candidates. Compare
them with the current artifact and its actual behavior. An evaluator's mistake
does not by itself establish a defect. Accept a correction when evidence shows
a material obstacle to the Outcome, supported Claim, or Preserve constraints,
and the correction is within Scope.

Fix the cause where it belongs: a hidden starting point, misleading name,
unclear ownership, missing premise, unusable interface, or incorrect behavior.
Put necessary information at the point of use. Choose code, structure, wording,
examples, or documentation according to the cause; do not automatically add
explanations or redesign the artifact to satisfy an unsupported preference.

Prioritize supplied findings and the strongest material obstacles. Keep every
accepted requirement visible until resolved or reported as a blocker. Reject
stale, unsupported, already satisfied, or merely advisory findings without
manufacturing changes. A review-only task ends with supported findings even
when the assessed artifact still has problems.

After an accepted correction, recheck its affected evidence. If understanding
changed, use a fresh evaluator for that acceptance task rather than teaching
the previous evaluator the intended answer. Do not repeat the same failing
approach without new evidence; change the approach or identify the actual blocker.

## Decide and hand off

Choose one decision from the evidence:

- `done`: the full Outcome is achieved; the supported Claim and Preserve
  constraints hold or changed only as authorized; required correctness and use
  checks passed, including any justified adequate substitutes; Scope was
  respected; no unresolved finding or uncertainty materially changes the result
  or next action, and the tested challenge does not invalidate completion.
- `revise`: an accepted correction or required check remains executable within
  Scope. Continue the work and recheck the affected evidence without asking for
  permission already granted.
- `blocked`: required work or evidence cannot be obtained through an available,
  authorized approach. State the unmet condition and what would unblock it.
- `out_of_scope`: completing the requested outcome requires an excluded change
  or expanded authorization. Identify the boundary while preserving completed work.

Stop when `done` is supported. Do not require unanimous approval, a perfect
score, a fixed number of passes, or exhaustion of all possible improvements.
An unexecuted available required check is remaining work, not completion or a
blocker. Difficulty alone is not a blocker.

`revise` is never a final report: keep working until one of the other three
applies. The decision names are internal labels. Report in the user's language
and format, and say the decision in plain words rather than as a code-styled
token unless the user asked for that vocabulary. A final report covers, briefly:

- the decision and the delivered result, at its entrypoint;
- the verification evidence, labeling each use check as an independent attempt,
  self-check, or walkthrough;
- material limits and unverified properties;
- for `blocked` or `out_of_scope`, what would unblock it or which boundary
  applies; otherwise the user's next action when one is needed.

Avoid process transcripts and additional ceremonial documents unless they are
part of the requested outcome.

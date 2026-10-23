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

Work is finished when the requested outcome is demonstrated and its intended
user, who may know the domain but not this project or conversation, can take
their next action from the delivered result at its normal entrypoint.

Loop through defining success, building, verifying correctness and use, and
resolving supported findings until the `done` conditions hold, then stop. A
first draft, first passing check, or first tidied area is not completion. Scale
effort to the consequences; the loop needs no separate phases, tool calls, or
review rounds.

Follow the host's instruction hierarchy and the user's scope; explicit requests
and earlier authorization govern. This skill grants no permission for external
actions or extra writes, except that choosing it, or a request it matches,
permits a bounded evaluation by a subagent the session already offers, within
the user's scope and writing only in an isolated copy. Do not delegate when the
user, host, or project restricts delegation or its cost, or when the only way to
delegate needs new setup, credentials, or approval. A read-only assessment
delivers supported findings without repairing the artifact.

Read [Code](references/code.md) for any code work, and
[Refactoring](references/refactoring.md) before defining success for a refactor
or its assessment.

## Define success

Inspect the artifact, relevant instructions, entrypoints, and consumers, then
keep a compact internal contract:

- `Outcome`: the result, its intended user, and the next action or decision
  they must be able to make, with their starting point and assumed knowledge
  when these matter.
- `Claim`, when relevant: what the existing artifact actually says, promises,
  or does, from evidence rather than from the desired Outcome.
- `Preserve`: behavior, meaning, interfaces, assets, and constraints that must
  survive; existing organization is not automatically one of them.
- `Evidence`: observable acceptance tasks and checks, with expected results,
  for correctness, preservation, and use.
- `Scope`: authorized changes, exclusions, evaluation resources, and side
  effects.

Before optimizing, choose acceptance tasks that are representative decisions and
actions, not a quality score. Capture behavior and use baselines before a
substantial change to an existing artifact; a new artifact can first be tried as
a usable draft. Keep comparable tasks fixed across revisions, and add coverage
for a newly revealed requirement, never to excuse a failure.

Resolve routine gaps from the request and evidence. Ask only when a missing
answer blocks a sound next action or materially changes scope, cost, or risk,
and keep doing independent authorized work meanwhile; silence is not approval.
Show the contract only when it helps the user with a consequential choice.

## Build for the next user

Carry authorized work through execution and verification by the shortest
credible approach that meets the whole contract. Do not stop at a plan when the
next required action is available, or substitute an easier outcome.

Make the purpose, entrypoints, key concepts, and decisions the user needs
visible in the artifact itself, through clear names, coherent responsibilities,
useful order, and workable interfaces, with the domain assumptions, units,
rationale, and examples they need. A chat explanation cannot repair what the
artifact lacks.

Where design needs judgment, weigh what is missing or excessive, what belongs
together, and which change most helps the next action. A requested improvement
needs no existing defect but does not justify unrelated features or unsupported
claims. Keep clear structures and useful content, and do not simplify away
necessary meaning or precision.

Complete each change with its dependent callers, configuration, tests, docs, and
other in-scope consumers; small means little unrelated work, not few files.
Preserve unrelated local changes. Refine the contract when evidence or the user
changes the task, never to fit the current result. After an interruption,
recover the original outcome, constraints, authorization, accepted findings, and
valid evidence; follow-up questions steer the goal unless the user changes or
cancels it.

## Verify correctness and use

Verify both that the result is right and that the intended user can use it;
neither proves the other. For each material check, record what was checked, the
expected result, and the actual result.

Use direct evidence matched to the changed surface, such as tests,
representative runs, source checks, and rendered output, and tell regressions,
existing failures, and intentional corrections apart. Add tests that separate a
plausible failure from required behavior, not tests that freeze incidental
details. For documents, prompts, and skills, check the supported meaning across
the whole changed boundary. For research, separate facts from interpretation and
verify time-sensitive claims against current authoritative sources; check
project claims against the project.

When understanding or use materially determines success for a substantial new or
revised deliverable, code included, run an independent use trial by default,
following [Independent use](references/independent-use.md). A narrow change with
adequate direct evidence needs none. In a read-only assessment, the assessment
is the deliverable, and any test of the source stays read-only.

Challenge the highest-impact, reasonably testable failure or competing
explanation that could change completion, reusing a test or trial that already
does so. For a material design choice, compare a plausible alternative by the
user's task, preservation, and burden.

When a check cannot run, use an adequate substitute for the same property and
state its limits. Self-review is not independent use, a simulated attempt is not
an executed action, and a weaker proxy cannot establish a required property.
Reuse evidence while its inputs and assumptions hold, and rerun only affected
checks.

## Resolve findings

Feedback, observed confusion, and tool findings are candidates: check them
against the artifact and its actual behavior, since an evaluator's mistake is
not by itself a defect. Accept a correction when evidence shows a material
obstacle to the Outcome, Claim, or Preserve and the fix is within Scope; reject
stale, unsupported, already satisfied, or merely advisory findings without
manufacturing changes. Handle supplied findings and the strongest obstacles
first, and keep each accepted requirement visible until it is resolved or
reported as a blocker. A review-only task ends with its supported findings even
when problems remain.

Fix the cause where it lives, such as a hidden starting point, misleading name,
unclear ownership, missing premise, unusable interface, or wrong behavior, and
put needed information at the point of use. Choose code, structure, wording,
examples, or docs by the cause; do not add explanations or redesign by reflex or
for an unsupported preference.

After a correction, recheck the affected evidence, using a fresh evaluator when
understanding changed rather than teaching the previous one the answer. Do not
repeat a failing approach without new evidence; change it or name the blocker.

## Decide and hand off

Choose one decision from the evidence:

- `done`: the full Outcome is achieved; Claim and Preserve hold or changed only
  as authorized; required checks or justified substitutes passed; Scope was
  respected; and no open finding, uncertainty, or tested challenge materially
  changes the result or next action.
- `revise`: an accepted correction or required check can still run within
  Scope; continue without asking again for granted permission.
- `blocked`: required work or evidence cannot be obtained by any available,
  authorized approach; state the unmet condition and what would unblock it.
- `out_of_scope`: the outcome needs an excluded change or more authorization;
  name the boundary and keep the completed work.

Stop when `done` is supported, without waiting for unanimous approval, a perfect
score, a fixed number of passes, or exhausted improvements. An available
required check that has not run is remaining work, not completion or a blocker,
and difficulty alone is not a blocker.

`revise` is never a final report. Report in the user's language and format,
naming the decision in plain words unless the user asked for that vocabulary,
and briefly cover:

- the decision and the delivered result at its entrypoint;
- the evidence, labeling each use check as an independent attempt, self-check,
  or walkthrough;
- material limits and unverified properties;
- what would unblock a `blocked` or `out_of_scope` result, or otherwise the
  user's next action when one is needed.

Skip process transcripts and ceremonial documents unless they are part of the
requested outcome.

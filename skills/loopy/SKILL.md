---
name: loopy
description: >
  Carry a requested change or review to a verified finish that someone without
  this conversation can use. Use whenever the user asks to fix a bug, add or
  change a feature, or build, review, refactor, or improve code, a README,
  guide, plan, prompt, or skill (for example 고쳐줘, 추가해줘, 만들어줘,
  검토해줘, 리팩토링해줘, 개선해줘, 정리해줘), even when the fix looks small; to
  make it shorter or clearer; to make sure it works before calling it done; or
  names Loopy. Do not use when the user dictates the exact edit, such as a
  rename or a new title, or for explanations, factual questions, translation,
  or brainstorming.
---

# Loopy

Work is finished when the requested outcome is demonstrated and its intended
user, who may know the domain but not this project or conversation, can take
their next action from the delivered result at its normal entrypoint.

Loop through defining success, building, verifying, and resolving supported
findings until the `done` conditions hold, then stop. A first draft or first
passing check is not completion.

Scale effort and tokens to the consequences. Search for what a decision needs,
read only those files or sections, and reread one only after it changes. While
working, run the narrowest check that shows a property and keep its output
short; run the full required checks when the result settles. Write no plan,
log, or notes file that nobody asked for, and delegate only for evidence you
cannot get directly.

Follow the host's instruction hierarchy and the user's scope. This skill grants
no permission for external actions or extra writes, except that choosing it, or
a request it matches, permits a bounded evaluation by a subagent the session
already offers, within the user's scope and writing only in an isolated copy. Do
not delegate when the user, host, or project restricts delegation or its cost,
or when the only way to delegate needs new setup, credentials, or approval.

Sort each request by what happens to the result's behavior; a document,
prompt, or skill behaves through what it tells its reader or agent to do. Target
and scope, such as a prompt or a whole project, apply to every kind and choose
none. Run a mixed request as steps of one kind each, in order.

| Behavior | Kind | Done when | Also read |
| --- | --- | --- | --- |
| Not changed | Assess: review, check, diagnose | Findings and causes are supported | [Debug](references/debug.md) up to Fix, for a cause |
| Kept while form changes | Refactor: tidy, shorten, port | Behavior is the same, apart from supported bugs fixed as Debug steps | [Refactoring](references/refactoring.md) |
| Restored to the existing contract | Debug, fix | The contract holds and the root cause is explained | [Debug](references/debug.md) |
| Changed to a stated new behavior | Build: add, change, remove, complete | It works as stated | |
| Changed toward a direction, stated or not | Improve, make better | It is measurably better than the baseline | [Improvement](references/improvement.md) |

Removing options no caller uses changes no observable behavior, so it is a
refactor. "Make it shorter" is a refactor when behavior must stay and an
improvement when content may go. "Fix the slowness" is debugging when speed is
in a documented contract and an improvement otherwise. "Just find why" is an
assessment, and "find why and fix it" is one Debug step. "Check and fix" is
Assess then Debug, which fixes contract-breaking findings and reports the rest.
Saying what must stay states no new behavior. Ask when the kind is unclear and
changes what may be altered. Read the references before defining success, and
[Code](references/code.md) for any code work.

## Define success

Inspect the artifact, instructions, entrypoints, and consumers, then keep a
compact internal contract:

- `Outcome`: the result, its intended user, and the next action they must be
  able to take.
- `Claim`, when relevant: what the existing artifact actually says or does, from
  evidence rather than from the desired Outcome.
- `Preserve`: behavior, meaning, interfaces, and constraints that must survive;
  existing organization is not automatically one of them.
- `Evidence`: observable tasks and checks, with expected results, for
  correctness, preservation, and use.
- `Scope`: authorized changes, exclusions, evaluation resources, and side
  effects.

Choose acceptance tasks before optimizing: representative actions, not a quality
score. Capture baselines before a substantial change to an existing artifact,
keep tasks fixed across revisions, and add coverage for a newly revealed
requirement, never to excuse a failure.

Resolve routine gaps from the request and evidence. Ask only when a missing
answer blocks a sound next action or materially changes scope, cost, or risk,
and continue independent authorized work meanwhile; silence is not approval.

## Build for the next user

Carry authorized work through verification by the shortest credible approach; do
not stop at a plan when the next action is available, or substitute an easier
outcome. Put what the user needs, such as entrypoints, key concepts,
assumptions, and examples, in the artifact itself; a chat explanation cannot
repair what the artifact lacks.

Complete each change with its dependent callers, configuration, tests, docs, and
other in-scope consumers; small means little unrelated work, not few files.
Preserve unrelated local changes. Refine the contract when evidence or the user
changes the task, never to fit the current result.

## Verify correctness and use

Verify both that the result is right and that its user can use it; neither
proves the other. Use direct evidence matched to the changed surface, such as
tests, runs, and source checks, with each material check's expected and actual
result. Tell regressions, existing failures, and intentional corrections apart,
and add tests that separate a plausible failure from required behavior, not
tests that freeze incidental details. For documents, prompts, and skills, check
meaning across the whole changed boundary and project claims against the
project.

When understanding or use materially determines success for a substantial new or
revised deliverable, code included, run an independent use trial by default,
following [Independent use](references/independent-use.md); a narrow change with
adequate direct evidence needs none. In a read-only assessment, any test of the
source stays read-only.

Challenge the highest-impact testable failure or competing explanation that
could change completion, reusing a test or trial that already does so. When a
check cannot run, use an adequate substitute for the same property and state its
limits: self-review is not independent use, a simulated attempt is not an
executed action, and a weaker proxy cannot establish a required property. Reuse
evidence while its inputs and assumptions hold.

## Resolve findings

Treat feedback, observed confusion, and tool findings as candidates and check
them against the artifact's actual behavior; an evaluator's mistake is not by
itself a defect. Accept a correction when evidence shows a material obstacle to
the Outcome, Claim, or Preserve within Scope; reject stale, unsupported, already
satisfied, or merely advisory findings without manufacturing changes, and keep
each accepted one open until it is resolved or reported. An assessment ends with
its supported findings.

Fix the cause where it lives, such as a misleading name, missing premise, or
wrong behavior, rather than adding explanation or redesign by reflex or for an
unsupported preference. After a correction, recheck the affected evidence, with
a fresh evaluator when understanding changed, and do not repeat a failing
approach without new evidence.

## Decide and hand off

Choose one decision from the evidence:

- `done`: the full Outcome is achieved; Claim and Preserve hold or changed only
  as authorized; required checks or justified substitutes passed; Scope was
  respected; and no open finding or uncertainty materially changes the result or
  next action.
- `revise`: an accepted correction or required check can still run within Scope;
  continue without asking again for granted permission.
- `blocked`: required work or evidence cannot be obtained by any authorized
  approach; state the unmet condition and what would unblock it.
- `out_of_scope`: the outcome needs an excluded change or more authorization;
  name the boundary and keep the completed work.

Stop when `done` is supported, without waiting for unanimous approval, a perfect
score, or a fixed number of passes. An available required check that has not run
is remaining work, and difficulty alone is not a blocker.

`revise` is never a final report. Report briefly in the user's language, naming
the decision in plain words: the delivered result at its entrypoint; the
evidence, labeling each use check as an independent attempt, self-check, or
walkthrough; material limits and unverified properties; and what would unblock a
`blocked` or `out_of_scope` result, or otherwise the user's next action. Skip
process transcripts and ceremonial documents unless they are part of the
request.

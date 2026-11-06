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

Work is finished when the requested outcome is demonstrated and its intended user, who knows the domain but not this project or conversation, can take their next action from the delivered result at its normal entrypoint.

Define success, build, verify, and resolve supported findings, repeating until `done` holds; then stop.

## Cost and permission

Scale effort and tokens to the stakes. Search for what a decision needs, read only that, and reread a file or rerun a check only after its inputs change. Run narrow, quiet checks while working and the full required checks once the result settles. Write no plan, log, or notes file nobody asked for.

Delegate only for evidence you cannot get directly. This skill permits no external actions or extra writes, except a bounded evaluation by a subagent the session already offers, within the user's scope, writing only in an isolated copy. Do not delegate where the user, host, or project restricts it or its cost, or where it needs new setup, credentials, or approval.

## Sort the request

Sort each request by what happens to its result's behavior; a document, prompt, or skill behaves through what it tells its reader or agent. Target and scope, such as a prompt or whole project, never choose the kind.

Behavior | Kind | Done when | Read
--- | --- | --- | ---
Not changed | Assess: review, check, diagnose | Findings and causes are supported | [Diagnose](references/debug.md#diagnose), if asked for a cause
Kept while form changes | Refactor: tidy, shorten, port | Same behavior, except supported bugs fixed as Debug steps | [Refactoring](references/refactoring.md)
Restored to the existing contract | Debug: fix | Contract holds; root cause explained | [Debug](references/debug.md)
Changed to a stated new behavior | Build: add, change, remove, complete | It works as stated | —
Changed toward a direction, stated or not | Improve: make better | Measurably better than the baseline | [Improvement](references/improvement.md)

Run a mixed request as one-kind steps, in order. Boundary cases:

- Removing options no caller uses is Refactor: no observable behavior changes.
- "Make it shorter" is Refactor when behavior must stay and Improve when content may go.
- "Fix the slowness" is Debug when speed is in a documented contract and Improve otherwise.
- "Just find why" is Assess; "find why and fix it" is one Debug step.
- "Check and fix" is Assess then Debug, which fixes contract-breaking findings and reports the rest.
- Saying what must stay states no new behavior.

Ask when an unclear kind changes what may be altered. Read the kind's reference first, and [Code](references/code.md) for any code work.

## Define success

Inspect the artifact, its instructions, entrypoints, and consumers; keep a short contract:

- `Outcome`: the result, its user, and the next action they must be able to take.
- `Claim`, when relevant: what the existing artifact actually says or does, from evidence rather than the desired Outcome.
- `Preserve`: behavior, meaning, interfaces, and constraints that must survive; existing organization is not automatically one.
- `Evidence`: observable tasks and checks with expected results, for correctness, preservation, and use.
- `Scope`: authorized changes, exclusions, evaluation resources, and side effects.

Choose acceptance tasks before optimizing: representative actions, not a quality score. Capture a baseline before substantially changing an existing artifact. Change tasks or contract only when evidence or the user changes the task, never to fit or excuse the result.

Ask only when a missing answer blocks a sound next action or materially changes scope, cost, or risk. Meanwhile, continue independent authorized work; silence is not approval.

## Build

Carry authorized work through verification by the shortest credible approach; do not stop at a plan or settle for an easier outcome. Put what the user needs, such as entrypoints, key concepts, assumptions, and examples, in the artifact; chat cannot repair what it lacks.

Complete each change with its dependent callers, configuration, tests, docs, and other in-scope consumers; small means little unrelated work, not few files. Preserve unrelated local changes.

## Verify

Check that the result is right and that its user can use it; neither proves the other. Use direct evidence for the changed surface, such as tests, runs, and source checks, and note expected and actual results. Add tests that separate a plausible failure from required behavior, not ones that freeze incidental details. Check a document, prompt, or skill for meaning across the whole changed boundary and its claims against the project.

When understanding or use decides success for a substantial new or revised deliverable, code included, run an [independent use](references/independent-use.md) trial by default. A narrow change with adequate direct evidence needs none. A read-only assessment keeps any test of the source read-only.

Challenge the highest-impact testable failure or competing explanation that could change completion, reusing a test or trial that already does. When a check cannot run, use an adequate substitute for the same property and state its limits.

## Resolve findings

Treat feedback, observed confusion, and tool findings as candidates and check them against actual behavior; an evaluator's mistake is not by itself a defect. Accept one when evidence shows a material obstacle to the Outcome, Claim, or Preserve within Scope; reject stale, unsupported, already satisfied, or merely advisory ones without manufacturing changes. An assessment ends with its supported findings.

Fix the cause where it lives, such as a misleading name, missing premise, or wrong behavior, rather than adding explanation or redesign by reflex. After a correction, recheck the affected evidence, with a fresh evaluator when understanding changed, and do not repeat a failing approach without new evidence.

## Decide and report

Choose one decision from the evidence:

- `done`: the full Outcome is achieved within Scope, Claim and Preserve hold or changed only as authorized, required checks or justified substitutes passed, and no open finding or uncertainty materially changes the result.
- `revise`: an accepted correction or required check can still run within Scope; continue without asking again for granted permission.
- `blocked`: no authorized approach can obtain required work or evidence.
- `out_of_scope`: the outcome needs an excluded change or more authorization; keep the completed work.

Stop when `done` is supported, without waiting for unanimous approval, a perfect score, or a fixed number of passes.

`revise` is never a final report. Report briefly in the user's language: the decision in plain words; the result at its entrypoint; the evidence, labeling each use check an independent attempt, self-check, or walkthrough; material limits and unverified properties; and the unmet condition or boundary with what would unblock it, or else the user's next action.

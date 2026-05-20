---
name: loopy-theory
description: Run one evidence-backed theory refinement cycle for ideas, design principles, research notes, process rules, or conceptual documents. Use when an agent needs to test one unstable claim, update a .loopy/theories/THEORY_*.md document from a survivor, or return the next theory route to loopy-loop.
---

# Loopy Theory

## Overview

Use this skill to turn unstable thinking into stable theory.

Follow the Loopy shape:

```text
Unstable -> Tested -> Stable
```

Prefer the simplest theory that still draws a real boundary. Code, examples, and current project behavior are evidence or implementation mapping; they are not the theory itself.

Rough claims stay in cycle notes. Only survivors become final theory.

A theory survivor is stable only when another phase can use it without reading the cycle history.

When `../core.md` exists, treat it as the parent philosophy. This skill may specialize Loopy for theory work, but it must preserve the core requirements: unstable artifact, change loop, rejection test, and stable survivor.

## Goal

Start by naming the theory target in one sentence, including the current user-request scope it must stay within.

The target is not a preferred conclusion to force into truth. It is the question, claim, boundary, or condition the loop is trying to explain, distinguish, test, or improve.

For broad requests, name the one target this cycle will handle. If multiple targets exist, return the remaining targets to `loopy-loop` instead of managing the queue here.

Good targets:

- define the minimum condition for a concept;
- decide which boundary separates two cases;
- turn a loose idea into a reusable rule;
- strengthen an existing `.loopy/theories/THEORY_*.md` document;
- find the weakest point in a current theory and improve it.

## Execution Mode

Default mode is autonomous when invoked through `loopy-loop`.

When `loopy-loop` runs a full process and file edits are available, write cycle notes and route artifacts without waiting for another explicit save or edit instruction.

For standalone review-only requests, return the cycle result in the response unless the user asks to write files.

If file edits are blocked by the host or user scope, return the completed cycle in the response.

## Workflow

Run one theory cycle. Do not run the next cycle inside this skill; return the survivor and next route to `loopy-loop`.

```text
read sources -> draft claim -> reject -> revise -> reread -> return survivor
```

1. Read sources.
   - Re-read the user request, the current target, and this skill's loop rules.
   - If files exist, re-read the current cycle note and any relevant final theory before drafting the next claim.
   - If code or examples are evidence for the target, re-check the relevant source instead of relying on memory.

2. Draft one unstable claim.
   - Read the user request and any named theory file.
   - If continuing a target, first inspect existing `.loopy/cycles` notes and any named or relevant `.loopy/theories/THEORY_*.md` final theory file.
   - Choose the smallest claim whose truth would change the target's boundary, minimum condition, or decision.
   - If the target is vague, write the current best interpretation as an assumption.

3. Test it.
   - Use evidence that could reject the claim.
   - Evidence must be able to force a boundary, minimum-condition, or decision change if it rejects the claim.
   - Use an isolated Critic agent for the rejection test when separate agents are available.
   - If separate agents are available but no isolated Critic is used, do not promote the survivor.
   - If the host requires the user to explicitly request sub-agents, stop before promotion and ask for that request instead of marking the critic unavailable.
   - Acceptable evidence includes prior cycle notes, existing theory text, user constraints, code behavior, cited sources, and concrete counterexamples.
   - Use the objection that would force the largest boundary, minimum-condition, or decision change if true.
   - For external factual claims, use cited sources or mark the claim as unverified.
   - Do not invent evidence.
   - Mark hypotheses as hypotheses. Do not treat them as evidence.
   - Use the best available evidence; do not stall for exhaustive research unless the user asks.
   - If the available material can only improve wording, examples, or confidence, do not treat it as a theory revision.

4. Keep the smallest survivor.
   - Make it explain more than itself.
   - Make it imply a decision, prediction, or boundary.
   - Prefer narrowing scope before renaming terms.
   - Prefer clarifying terms before rewriting definitions.
   - Prefer definition changes before replacing the core claim.

5. Reread and classify the survivor.
   - Re-read the survivor against the target, this skill, and any final theory file it would replace.
   - Mark it promotable only if it changes a boundary, minimum condition, or decision.
   - Do not classify it by cycle count. Use the evidence chain: source read, rejection applied, revision made, sources reread, and named weak points either rejected, carried forward, or shown unable to change the boundary, minimum condition, or decision.
   - A second rejection test inside the same cycle does not satisfy the loop. Return the survivor as a possible next unstable claim.
   - Keep it as a cycle note if it is only wording, confidence, or exploration.
   - Replace the claim if revisions keep adding exceptions.

6. Return survivor and next route.
   - Choose the next weakest point.
   - Name whether the survivor should be promoted, carried into another theory cycle, handed to `loopy-implement`, or blocked.
   - If another theory cycle is needed, return the next unstable claim for `loopy-loop` to schedule.
   - If the weakest point is in this skill's process, record a process recommendation unless the user explicitly asked to improve this skill or the current task is this skill's development.
   - Continue from `Next question` only when `loopy-loop` routes back into this skill.

## Cycle State

Track this state for the current cycle and handoff:

- Theory target
- Unstable claim
- Rejection test
- Survivor
- Prior survivor used as the next unstable claim
- Named weak points and their decision: reject, carry forward, blocked, or no boundary effect
- Decision
- Next route

On later runs, use the resume target supplied by `loopy-loop`. Re-read the latest relevant cycle note and final theory before drafting a new claim. Find the final theory by user-named path first, then by cycle-note references, then by target match across existing `.loopy/theories/THEORY_*.md` files. If multiple final theory files plausibly match and none is named by the user or cycle notes, do not choose silently; record the ambiguity and keep the revision as rough notes unless the user provides a target file. Do not create a new final theory file when an existing one already owns the target boundary.

## Roles

Use an isolated Critic agent for theory rejection when the tool environment supports separate agents.

Use an isolated Editor agent when applying critic findings to this skill or another maintained artifact.

If separate agents are unavailable, continue only as a non-independent rough loop and mark the loop status accordingly. Do not promote final theory from a non-independent loop unless the user explicitly accepts a non-independent result.

If separate agents are blocked only because the host requires explicit user delegation, stop and ask the user to request an isolated Critic agent. Do not treat that as true unavailability.

- Theorist: identifies the target and writes the claim.
- Critic: tests the claim with evidence that could reject it. Run this role in an isolated context when subagents are available.
- Synthesizer: keeps the smallest survivor.
- Archivist: records the cycle and returns the next route.

Do not simulate an isolated critic by pretending inside the same context if the user specifically asks for agent-based critique.

Do not split context for ordinary formatting or archival work. Use the main context only when independence would not change the rejection test.

## Output

Separate rough cycle notes from clean final theory.

Also return the Phase Handoff Contract fields required by `loopy-loop`: `item`, `artifact`, `decision`, `next_route`, `queue_delta`, `blocker`, and `independence`.

Use `decision`, `next_route`, and queue status values from the vocabulary defined in `loopy-loop`.

Always include a brief loop status before the detailed result:

```text
Loop status:
- phase: theory
- cycle:
- decision:
- independent critic: used | unavailable | blocked
```

When file edits are not allowed by Execution Mode, return the cycle result in the response instead of writing files.

For review-only requests, start with a concise verdict. Return the full cycle-note format only when the user asks for a formal cycle record.

When file edits are allowed, save each completed cycle note as:

```text
.loopy/cycles/theory_YYYYMMDD_HHMMSS.md
```

Create `.loopy/cycles` first if it does not exist.
If the timestamped cycle-note filename already exists, append the smallest numeric suffix, such as `_2`, that avoids overwriting an existing note.

Cycle notes are working documents. They may include objections, failed claims, uncertainty, and revision history.

When a revision is stable enough to become the current theory, update the relevant final theory file:

```text
.loopy/theories/THEORY_<name>.md
```

Update or create a final theory file only when file edits are allowed by Execution Mode.

Do not update or create a final theory file from a non-independent loop unless the user explicitly accepts a non-independent result.

Use a short, stable `<name>` that identifies the theory target, such as `LOOPY`, `AGENCY`, or `REVIEW`, only when exactly one final theory owner is clear and no existing final theory file already owns the target boundary. A revision is promotable only if it changes a boundary, minimum condition, or decision and can be stated without cycle history. Final theory files are clean documents. Keep them short, simple, and boundary-bearing. Include only the surviving core claim, minimum condition, and boundary. Do not copy cycle history, operational policy, or every useful detail into the final theory.

Each cycle note must include:

- Target
- Cycle number
- Claim
- Evidence
- Objection
- Revision
- Revision target: theory or skill/process
- Why it is stronger
- Decision
- Process recommendation, if the loop process was weak but skill edits are not allowed
- Prior survivor carried into the next cycle, if any
- Named weak points and decisions
- Progress toward target
- Next question

Use formulas, names, or compact lists only when they make the claim clearer or more testable.

Each final theory update should answer, as briefly as possible:

- What is the current claim?
- What is the minimum condition?
- What boundary or decision does it force?

## Cycle Result

After the cycle, return one result:

- `running`: return `Next question` as the next unstable claim for `loopy-loop`.
- `pending`: if the survivor is ready for implementation, return it to `loopy-loop` with `next_route: loopy-implement`.
- `blocked`: explain which block was reached.
- `out_of_scope`: return a process recommendation only when this cycle exposed a skill/process weakness and skill edits are not in scope.

Do not request another theory cycle merely because another question exists. Request it only when the next question could change the survivor's boundary, minimum condition, or decision.

## Stop Conditions

A cycle is complete when it has one claim, evidence-based objection, stronger revision, and next route.

Return a stop or route decision when:

- new evidence changes only examples or wording, not the claim's decisions, predictions, or boundaries;
- the revision keeps adding exceptions and the claim should be replaced;
- evidence is blocked and the block is explicit;
- the current target has a queue status from `loopy-loop`: `pending`, `running`, `blocked`, or `out_of_scope`;
- the user explicitly stops the loop.

---
name: loopy-theory
description: Run evidence-backed theory refinement cycles for ideas, design principles, research notes, process rules, or conceptual documents. Use when an agent needs to turn a loose idea into a stronger theory, critique an existing theory with evidence, update THEORY_*.md documents, or continue a claim-objection-revision loop such as THEORY_LOOP.md.
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

When `../core.md` exists, treat it as the parent philosophy. This skill may specialize Loopy for theory work, but it must preserve the core requirements: unstable artifact, change loop, rejection test, and stable survivor.

## Goal

Start by naming the theory target in one sentence, including the current user-request scope it must stay within.

The target is not a preferred conclusion to force into truth. It is the question, claim, boundary, or condition the loop is trying to explain, distinguish, test, or improve.

Good targets:

- define the minimum condition for a concept;
- decide which boundary separates two cases;
- turn a loose idea into a reusable rule;
- strengthen an existing `THEORY_*.md` document;
- find the weakest point in a current theory and improve it.

## Execution Mode

Default mode is review-only.

Do not create or modify files unless:

- the user explicitly asks to save, update, promote, or edit;
- the user names a target theory file;
- the current task explicitly asks to develop this skill or Loopy's theory files.

If file edits are not allowed or not requested, return the completed cycle in the response.

## Workflow

1. Draft one unstable claim.
   - Read the user request and any named theory file.
   - If continuing a target, first inspect existing `.loopy/cycles` notes and any named or relevant `theories/THEORY_*.md` final theory file.
   - Choose the smallest claim, boundary, or condition that matters.
   - If the target is vague, write the current best interpretation as an assumption.

2. Test it.
   - Use evidence that could reject the claim.
   - Acceptable evidence includes prior cycle notes, existing theory text, user constraints, code behavior, cited sources, and concrete counterexamples.
   - Prefer the strongest objection, not the easiest one.
   - For external factual claims, use cited sources or mark the claim as unverified.
   - Do not invent evidence.
   - Mark hypotheses as hypotheses. Do not treat them as evidence.
   - Use the best available evidence; do not stall for exhaustive research unless the user asks.

3. Keep the smallest survivor.
   - Make it explain more than itself.
   - Make it imply a decision, prediction, or boundary.
   - Prefer narrowing scope before renaming terms.
   - Prefer clarifying terms before rewriting definitions.
   - Prefer definition changes before replacing the core claim.

4. Decide whether it became stable.
   - Promote only if the survivor changes a boundary, minimum condition, or decision.
   - Keep it as a cycle note if it is only wording, confidence, or exploration.
   - Replace the claim if revisions keep adding exceptions.

5. Pick the next question, then self-check.
   - Choose the next weakest point.
   - Re-read this skill's rules before starting the next cycle.
   - If the weakest point is in this skill's process, record a process recommendation unless the user explicitly asked to improve this skill or the current task is this skill's development.
   - Continue from `Next question` only while it is still needed for the current user request and the cycle budget is not spent.

## Loop State

Track this state across cycles:

- Theory target
- Unstable claim
- Rejection test
- Survivor
- Next weak point
- Decision

On later runs, resume from the latest relevant cycle note and final theory before drafting a new claim. Find the final theory by user-named path first, then by cycle-note references, then by target match across existing `theories/THEORY_*.md` files. If multiple final theory files plausibly match and none is named by the user or cycle notes, do not choose silently; record the ambiguity and keep the revision as rough notes unless the user provides a target file. Do not create a new final theory file when an existing one already owns the target boundary. Do not start a new cycle from scratch unless the claim must be replaced.

## Roles

Use isolated agents for Critic or Editor roles when independent judgment materially changes the test, and the tool environment supports them. This includes requests for agents, a grade, external review, or a role-separated loop.

- Theorist: identifies the target and writes the claim.
- Critic: tests the claim with evidence that could reject it. Run this role in an isolated context when subagents are available.
- Synthesizer: keeps the smallest survivor.
- Archivist: records the cycle, updates loop state, and chooses the next weak point.

Do not simulate an isolated critic by pretending inside the same context if the user specifically asks for agent-based critique.

Do not split context for ordinary drafting, formatting, or archival work. Use the main context when independence would not change the rejection test.

## Output

Separate rough cycle notes from clean final theory.

When file edits are not allowed by Execution Mode, return the cycle note in the response instead of writing it.

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
theories/THEORY_<name>.md
```

Update or create a final theory file only when file edits are allowed by Execution Mode.

Use a short, stable `<name>` that identifies the theory target, such as `LOOPY`, `AGENCY`, or `REVIEW`, only when exactly one final theory owner is clear and no existing final theory file already owns the target boundary. A revision is promotable only if it changes a boundary, minimum condition, or decision and can be stated without cycle history. Final theory files are clean documents. Keep them short, simple, and boundary-bearing. Include only the surviving core claim, minimum condition, and boundary. Do not copy cycle history, operational policy, or every useful detail into the final theory.

Each cycle note must include:

- Target
- Claim
- Evidence
- Objection
- Revision
- Revision target: theory or skill/process
- Why it is stronger
- Decision
- Process recommendation, if the loop process was weak but skill edits are not allowed
- Progress toward target
- Next question

Use formulas, names, or compact lists only when they make the claim clearer or more testable.

Each final theory update should answer, as briefly as possible:

- What is the current claim?
- What is the minimum condition?
- What boundary or decision does it force?

## Autonomous Progress

After each cycle, choose the applicable action or actions:

- Continue: use `Next question` for the next cycle within the current request and cycle budget.
- Promote: if file edits are allowed, update the final theory file with only the stable conclusion; otherwise, return the promotable conclusion in the response.
- Promote process: update this skill only when the user explicitly asked to improve this skill or the current task is this skill's development.
- Replace: discard the unstable claim and draft a better one under the same target.
- Stop: explain which stop condition was reached.

Use `Promote` and `Promote process` together when one cycle produces both a stable theory revision and a stable loop improvement.

Default cycle budget is exactly one completed cycle per user request. Continue only when the user explicitly asks to keep looping or gives a cycle count. Prefer promoting when the revision changes a real boundary and can be stated more simply than before. Prefer stopping when more cycles would only rename or rephrase the same claim.

## Stop Conditions

A cycle is complete when it has one claim, evidence-based objection, stronger revision, and next question.

Stop the loop when:

- new evidence changes only examples or wording, not the claim's decisions, predictions, or boundaries;
- the revision keeps adding exceptions and the claim should be replaced;
- evidence is blocked and the block is explicit;
- the default cycle budget for the current user request is reached;
- the user-set cycle limit is reached.

---
name: loopy-theory
description: Use when a project, product, workflow, codebase, or document set should be treated as imperfect evidence of a simpler underlying theory; infer the clearer principle that current implementation traces most strongly suggest, test it against gaps, and produce improvement candidates without directly changing implementation.
---

# Loopy Theory

Use this skill to apply the Loopy counterexample loop to project theory.

Loopy Theory treats the current project as imperfect observations. The goal is not to guess prior motives or justify the current implementation. The goal is to infer the simpler and more coherent principle that the current evidence most strongly suggests, then find where the project falls short of that principle.

```text
Observe -> Infer -> Challenge -> Refine -> Imply -> Decide -> Route
```

## Agent Policy

Before analyzing project evidence, ask the user once whether to use a clean-context critic for this loopy-theory run. Recommend one policy and give the reason.

Use this compact prompt shape: `Agent Policy recommendation: <policy>. Reason: <reason>. Use this for the rest of this run?`

Choose from:

- `none`: use only when the user wants a quick exploratory theory and does not need final confidence.
- `final clean critic`: default for most theory runs, because the Done Gate depends on judgment rather than an external check.
- `per-major-revision clean critic`: use for broad or high-stakes theory work where each major theory revision needs independent review.

After the user chooses, keep that policy for the rest of the loop unless the scope changes.

## Core Rules

- Treat implementation, docs, UX, naming, removed or deprecated structure when visible, and repeated choices as evidence.
- Infer only from evidence that appears in the current project or in explicit user context.
- Do not invent prior motives.
- Do not treat the current implementation as the ideal.
- Prefer the smallest theory that explains the strongest evidence and guides the next change.
- Do not directly edit code or docs unless the user separately asks for implementation.

## Routing Boundary

Use loopy-theory when the user wants to understand what the project evidence suggests the project should become, not merely what it currently is.

Do not use loopy-theory for ordinary bug fixes, feature work, or behavior-preserving structure cleanup. If the strongest next problem is structural fragmentation, route to loopy-compose. If the next problem is a concrete behavior, UX, prompt, or documentation change, route to an implementation task.

## Slot Mapping

- `Ideal Theory`: the simpler principle most strongly suggested by current evidence.
- `Evidence`: concrete traces that support the theory.
- `Strongest Gap`: the most important place where the current project weakens, obscures, or fails the theory.
- `Refined Theory`: the theory after testing it against the gap.
- `Implications`: what the theory says to do or avoid next.
- `Next Moves`: improvement candidates, not direct implementation.
- `Decision`: whether the theory is stable, needs another refinement, or opens candidates.
- `Next Route`: where follow-up work belongs.

## Workflow

1. Observe.
   - Read the project evidence before theorizing.
   - Look for repeated choices, removed or deprecated complexity when visible, awkward leftovers, naming pressure, UX pressure, documentation pressure, and code boundaries.
   - Prefer evidence that appears in more than one place.

2. Infer.
   - State one ideal theory in one sentence.
   - Phrase it as what the current evidence most strongly suggests, not as a guess about prior intent.

3. Challenge.
   - Find the strongest gap between the theory and the current project.
   - Prefer gaps in this order: user-visible contradiction, repeated implementation friction, misleading concept boundary, documentation mismatch, then aesthetic or naming weakness.

4. Refine.
   - If the gap weakens the theory, revise the theory.
   - If the gap shows the implementation falls short, keep the theory and record an improvement candidate.
   - Change one theory point per loop.

5. Imply.
   - Name what the theory would make easier, simpler, or more coherent.
   - Name what the theory would reject as unnecessary, misleading, or out of scope.

6. Decide.
   - `Keep theory`: the current theory explains the strongest evidence and survives the strongest gap.
   - `Refine theory`: the strongest gap changes the theory itself.
   - `Open improvement candidates`: the theory is stable enough to guide follow-up work.

7. Route.
   - `none`: no immediate follow-up is needed.
   - `loopy-compose`: the next work is recomposing structural boundaries while preserving behavior.
   - `implementation task`: the next work is a concrete code, prompt, documentation, UX, or test change.

8. Apply the Loopy Done Gate before stopping.
   - Do not collect every possible gap.
   - After the strongest gap, check only whether one more in-scope gap would change the theory, candidates, or route.
   - Repeat only if that gap changes the theory or opens a materially different improvement candidate.
   - Stop only when the last important gap no longer changes the theory, candidates, or route.

## Done

Before `done`, verify:

- the theory is evidence-based;
- the theory does not claim hidden intent;
- the strongest gap has been considered;
- improvement candidates follow from the theory;
- no implementation change was made unless separately requested;
- `Decision` and `Next Route` are separated.

Name the last important gap considered and why it no longer changes the next action.

## Output

Keep normal responses concise. When useful, show:

```text
Ideal Theory:
Evidence:
Strongest Gap:
Refined Theory:
Implications:
Next Moves:
Decision:
Next Route:
```

---
name: loopy-compose
description: Use when AI-written or iteratively grown code works but has become fragmented, misplaced, poorly named, or organized around misleading files, folders, modules, symbols, or concept boundaries; applies the Loopy counterexample loop to recompose code structure while preserving behavior.
---

# Loopy Compose

Use this skill to apply the Loopy counterexample loop to code structure.

Loopy Compose is Loopy applied to code structure. It finds one structural counterexample, recomposes one conceptual boundary, checks behavior and structure, then repeats only while another important in-scope structure counterexample remains.

```text
Target -> Counterexample -> Change -> Check -> Decision -> Next
```

## Invocation Contract

When invoked, start by establishing a compact Done Contract before recomposing structure.

Do not mark `done` until the structure Done Gate has run:

1. name the chosen boundary;
2. name one real competing in-scope boundary;
3. name the strongest remaining structural counterexample;
4. test whether the competing boundary or counterexample changes the result;
5. either repeat, or explain why the chosen boundary still owns the concept more clearly.

## Done Contract

Before analyzing the target structure, establish a Done Contract.

The contract must name:

- `Target`: what the structure should make clearer;
- `Non-goals`: behavior, topology, or unrelated cleanup that should not change;
- `Checks`: behavior checks and structure checks;
- `Counterexamples`: structure failures that would force another loop;
- `Stop condition`: what proves no important in-scope structure counterexample remains.

Keep it compact, but do not start recomposing until the contract is clear enough to test.

## Verification Policy

Before analyzing the target structure, choose the verification path needed to satisfy the Done Contract and Done Gate. Do not ask by default.

Use:

- `self-check only`: use for small structure changes with strong behavior checks and no critic.
- `final clean critic`: use for broad boundary recomposition, public surface changes, or unclear ownership decisions.
- `per-major-revision clean critic`: use only when several major structure boundaries may be recomposed in one run.

Ask only when using a critic would add substantial cost or the user asked for a quick or lightweight pass.

## Core Rules

- Preserve behavior, not topology, except where topology is the public API.
- Preserve concepts, not historical names.
- Change one conceptual boundary per loop.
- Inherit Loopy's one-strongest-counterexample discipline: address one structural counterexample per cycle, then search again.
- Do not create abstractions for imagined future needs.
- Avoid vague boundary names such as `utils`, `helpers`, `common`, `misc`, `core`, `manager`, or `service` unless the project already gives that name a strict responsibility.

## Routing Boundary

Use loopy-compose when the strongest problem is structural fragmentation: the current shape hides a concept, scatters responsibility, or misleads future changes.

If the main problem is broken behavior, fix or lock that behavior first. If the main problem is a new feature, implement the feature first, then compose only if the new code creates or exposes a structural counterexample.

Do not use loopy-compose merely because code could be reorganized; use it only when the current structure actively causes confusion, scatters responsibility, misplaces concepts, or makes future changes unsafe.

## Slot Mapping

- `Target`: the structure should express the real concept clearly.
- `Counterexample`: the strongest current structure failure.
- `Change`: one boundary recomposition that addresses that counterexample.
- `Check`: behavior is preserved and structure is clearer.
- `Decision`: `repeat`, `done`, `blocked`, or `out_of_scope`.

## Structural Counterexamples

Prefer the strongest issue in this order:

1. Public behavior, imports, routes, commands, config keys, or documented entry points would break.
2. A name lies about the responsibility it owns.
3. One responsibility is scattered across files or folders.
4. One boundary owns multiple concepts.
5. Glue exists only to preserve old topology.
6. Dependency direction hides ownership.

## Workflow

1. Lock behavior with the strongest available check: test, typecheck, lint, build, smoke run, snapshot, minimal before/after example, or direct behavioral comparison.
2. Map current concepts before moving them. Identify what each file or folder claims to own, what it actually owns, and which responsibilities are scattered or obsolete.
3. Pick one boundary to recompose: create, delete, rename, split, merge, move, or update only what that boundary requires.
4. Update imports, call sites, tests, docs, and examples affected by that boundary.
5. If a moved or renamed module is public, preserve compatibility or state the migration explicitly.
6. Remove dead glue created by the change: unused imports, stale exports, duplicate helpers, obsolete wrappers, empty folders, and old names that keep the previous structure alive.
7. Run the behavior check and a structure check. Reject the change if behavior is not preserved, a circular dependency appears, or dependency flow becomes harder to understand. When the project already separates domain, UI, adapters, infrastructure, or glue, do not move logic away from the concept that owns it.
8. Before `done`, name the chosen boundary, one competing in-scope boundary, and the strongest remaining structural counterexample. Use an existing plausible owner, caller pattern, responsibility split, or naming pressure; do not invent a competing boundary just to keep looping.
9. Apply the Loopy Done Gate before stopping: test whether the competing boundary or remaining counterexample changes the result. If the competing boundary owns the concept more honestly, switch to it. If both boundaries own different parts of the concept, split or rename the boundary. If the remaining counterexample would change the boundary, repeat. If it would not, state why the chosen boundary is still clearer.

## Boundary Checks

Create a boundary only when a current concept is scattered and no existing location honestly owns it.

Delete or merge a boundary when it stores leftovers, preserves history instead of responsibility, or adds glue without clarity.

Rename when the current name misleads new code into the wrong place. Do not rename for style only.

Split when a boundary owns multiple concepts and callers depend on only part of it.

Merge when separate boundaries always change together or represent the same concept under different names.

## Done

Before `done`, verify:

- existing behavior is preserved;
- scattered responsibility is reduced;
- names match current responsibilities;
- files and folders represent real concepts;
- imports and call sites are not harder to understand;
- no speculative abstraction was introduced;
- no obsolete glue remains unless public compatibility requires it.

Name the last important structural counterexample considered and why it no longer changes the next action.

## Output

Keep normal responses concise. Always include a one-line structure Done Gate/recheck summary before a final `done`. Expand it only when it changes confidence, boundary choice, or next action.

When useful, show:

```text
Target:
Counterexample:
Boundary change:
Check:
Decision:
Next:
```

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

## Core Rules

- Preserve behavior, not topology, except where topology is the public API.
- Preserve concepts, not historical names.
- Change one conceptual boundary per loop.
- Do not create abstractions for imagined future needs.

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
5. Remove dead glue created by the change: unused imports, stale exports, duplicate helpers, obsolete wrappers, empty folders, and old names that keep the previous structure alive.
6. Run the behavior check and a structure check. Reject the change if behavior is not preserved or dependency flow becomes harder to understand.
7. Repeat only if another important in-scope structure counterexample remains.

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

Keep normal responses concise. When useful, show:

```text
Target:
Counterexample:
Boundary change:
Check:
Decision:
Next:
```

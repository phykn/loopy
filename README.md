# Loopy

Loopy is a Claude Code and Codex plugin for counterexample-driven improvement.

```text
Define done -> Find a counterexample -> Improve -> Check -> Repeat
```

Use Loopy when a request benefits from repeated self-correction: coding, prompts, documents, workflows, or review. Loopy works on one useful counterexample at a time and, by default, keeps looping until all important in-scope counterexamples are resolved, blocked, or out of scope.

## Install

### Claude Code

```text
/plugin marketplace add phykn/loopy
/plugin install loopy@loopy
```

### Codex

Codex reads `.codex-plugin/plugin.json` and loads the `skills/` directory. In Codex, open Plugins from the top-left menu, create a new plugin, and point it at this repo root.

Restart Codex after installation.

## Skill

| Skill | Use when |
|---|---|
| `loopy` | Running the simple counterexample loop until all important in-scope counterexamples are resolved, blocked, or out of scope |
| `loopy-compose` | Recomposing fragmented code structure around clearer concept boundaries while preserving behavior |
| `loopy-theory` | Inferring an evidence-based ideal theory from a project's current traces and opening improvement candidates |

`loopy` is the core loop. Application skills specialize the same loop for a specific target: `loopy-compose` for code structure and `loopy-theory` for evidence-based project theory.

## Examples

Good requests:

```text
Use loopy to improve this onboarding email until the biggest confusion cases are handled.
Use loopy to fix this bug by finding the strongest counterexample, changing one thing, and checking it.
Use loopy to test this workflow rule before I build from it.
Use loopy to check whether this output is actually done.
Use loopy-compose to recompose this messy helpers folder around the concepts it actually owns.
Use loopy-theory to infer the ideal theory suggested by this project's current evidence and identify next improvement candidates.
```

Loopy trace:

```text
Target: onboarding email should help new users finish setup without extra support
Counterexample: the email says "configure your workspace" but never names the first action
Change: replace the vague instruction with the exact first setup step
Check: a new user can identify what to click first without reading other docs
Recheck: the next strongest confusion case does not change the next action
Decision: repeat
```

Loopy Compose trace:

```text
Target: helpers folder should be recomposed around real responsibilities
Counterexample: auth parsing and invoice validation both live in helpers/index.ts
Change: move invoice validation into billing_rules and update imports
Check: tests pass, imports are clearer, helpers no longer owns billing behavior
Recheck: a competing boundary would not own invoice validation more honestly
Decision: repeat
```

Loopy Theory trace:

```text
Ideal Theory: setup should be a guided workflow, not a configuration checklist
Evidence: onboarding screens remove optional choices, docs keep naming the first action, support notes repeat the same setup confusion
Strongest Gap: settings still expose three equivalent setup paths before the first success
Refined Theory: setup should preserve one obvious first path until the user reaches a working state
Next Moves: simplify the first-run setup path, move advanced configuration after success
Recheck: the competing theory explains less of the repeated setup evidence
Decision: Open improvement candidates
Next Route: implementation task
```

## When Not To Use Loopy

Use a simpler workflow for:

- trivial edits where the done condition is already obvious;
- pure fact checking where source verification matters more than iterative improvement;
- open brainstorming before there is any target to test;
- tasks where the user wants only one direct answer and no visible loop.

## Host Compatibility

Codex loads the canonical skills from `skills/`.

Claude Code uses `.claude/skills/` wrappers that point back to the same canonical skill files.

There is no build step. Editing the Markdown is the development cycle.

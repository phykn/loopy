# Loopy

Loopy is a Claude Code and Codex plugin for counterexample-driven improvement.

```text
Define done -> Find a counterexample -> Improve -> Check -> Repeat
```

Use Loopy when a request benefits from repeated self-correction: coding, prompts, documents, workflows, or review. Loopy works on one useful counterexample at a time and stops when the target is done, blocked, or out of scope.

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
| `loopy` | Running the simple counterexample loop until the current target is done, blocked, or out of scope |
| `loopy-compose` | Recomposing fragmented code structure around clearer concept boundaries while preserving behavior |

`loopy` is the core loop. `loopy-compose` is the first application skill: it applies the same loop to code structure.

## Examples

Good requests:

```text
Use loopy to improve this onboarding email until the biggest confusion cases are handled.
Use loopy to fix this bug by finding the strongest counterexample, changing one thing, and checking it.
Use loopy to test this workflow rule before I build from it.
Use loopy to check whether this output is actually done.
Use loopy-compose to recompose this messy helpers folder around the concepts it actually owns.
```

Loopy trace:

```text
Target: onboarding email should help new users finish setup without extra support
Counterexample: the email says "configure your workspace" but never names the first action
Change: replace the vague instruction with the exact first setup step
Check: a new user can identify what to click first without reading other docs
Decision: repeat
```

Loopy Compose trace:

```text
Target: helpers folder should be recomposed around real responsibilities
Counterexample: auth parsing and invoice validation both live in helpers/index.ts
Change: move invoice validation into billing_rules and update imports
Check: tests pass, imports are clearer, helpers no longer owns billing behavior
Decision: repeat
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

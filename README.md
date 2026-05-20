# Loopy

Loopy is a Claude Code and Codex plugin for counterexample-driven improvement.

```text
Define done -> Find a counterexample -> Improve -> Check -> Repeat
```

Use Loopy when a request benefits from repeated self-correction: coding, prompts, writing, design, narration, or review. Loopy works on one useful counterexample at a time and stops when the target is done, blocked, or out of scope.

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

`loopy` is the only runtime skill. It handles claims, implementation, and review as ordinary moments inside the same loop.

## Examples

Good requests:

```text
Use loopy to improve this TRPG narration prompt until the biggest failure cases are handled.
Use loopy to fix this bug by finding the strongest counterexample, changing one thing, and checking it.
Use loopy to test this design rule before I build from it.
Use loopy to check whether this output is actually done.
```

Loop trace:

```text
Target: narration should be vivid without deciding player actions
Counterexample: the output says the player feels afraid and backs away
Change: forbid deciding player feelings or actions
Check: sample output preserves scene pressure while leaving the choice open
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

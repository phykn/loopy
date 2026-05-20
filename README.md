# Loopy

Loopy is a Claude Code and Codex plugin for making unstable work survive a test.

```text
Unstable -> Tested -> Stable
```

A result is stable only when it survives a rejection test. See `skills/core.md` for the full philosophy.

## Install

### Claude Code

```text
/plugin marketplace add phykn/loopy
/plugin install loopy@loopy
```

### Codex

Codex reads `.codex-plugin/plugin.json` and loads the `skills/` directory. In Codex, open Plugins from the top-left menu, create a new plugin, and point it at this repo root.

Restart Codex after installation.

## Skills

| Skill | Use when |
|---|---|
| `loopy:loopy-theory` | Turning a rough claim, theory, process rule, or design principle into a tested survivor |

There is no build step. Editing the Markdown is the development cycle.

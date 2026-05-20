# Loopy

Loopy is a Claude Code and Codex plugin for theory-first coding.

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
| `loopy:loopy-implement` | Mapping a stable theory into traceable code slices |
| `loopy:loopy-review` | Checking whether an implementation slice preserves its theory boundary |

There is no build step. Editing the Markdown is the development cycle.

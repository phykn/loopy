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
| `loopy:loopy-loop` | Running the full theory -> implement -> review process until every current item has a named decision |
| `loopy:loopy-theory` | Turning a rough claim, theory, process rule, or design principle into a tested survivor |
| `loopy:loopy-implement` | Mapping a stable theory into traceable code slices |
| `loopy:loopy-review` | Checking whether an implementation slice preserves its theory boundary |

## Examples

Good requests:

```text
Use loopy:loopy-loop to build and apply a server/UI ownership theory.
Use loopy:loopy-theory to run one manual theory cycle for a server/UI claim.
Use loopy:loopy-implement to map .loopy/theories/THEORY_SERVER.md into the smallest code slices.
Use loopy:loopy-review to check these changes against .loopy/theories/THEORY_UI.md.
```

Use `loopy:loopy-loop` for the full process. Use the phase skills directly only when you want one manual theory, implement, or review cycle.

Bad requests:

```text
Make it better.
Implement whatever seems useful.
Review this like a normal code review.
```

Loopy is not a TODO checklist. A checklist completes steps. `loopy-loop` keeps cycling through the phase skills until each target, responsibility, or review slice has a named decision that survived a rejection test.

There is no build step. Editing the Markdown is the development cycle.

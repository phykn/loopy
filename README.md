# Loopy

Loopy is a Claude Code and Codex plugin for theory-first coding.

```text
Unstable -> Tested -> Stable
```

A result is stable only when it survives a rejection test. Loopy keeps cycling until every current queue item has a terminal decision.

Use an independent Critic or Reviewer when the host supports it. If not, Loopy continues with a stricter self-objection cycle, records `independence: unavailable`, and does not pretend independent review happened.

Self-objection can keep the loop moving, but `loopy-theory` does not promote final theory from a non-independent loop unless the user explicitly accepts that boundary.

See `skills/core.md` for the full philosophy.

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
| `loopy:loopy-loop` | Running the full theory -> implement -> review process until every current item has a terminal decision |
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

Loop trace:

```text
loopy-loop
-> loopy-theory: pending / next_route=loopy-implement
-> loopy-implement: review_ready / next_route=loopy-review
-> loopy-review: passed / next_route=complete
```

Bad requests:

```text
Make it better.
Implement whatever seems useful.
Review this like a normal code review.
```

## When Not To Use Loopy

Use a simpler workflow for:

- small bug fixes with an obvious failing test;
- direct file edits where the boundary is already clear;
- loose brainstorming without a claim to test;
- external fact checking where source verification matters more than theory revision.

## Host Compatibility

Codex loads the canonical skills from `skills/`.

Claude Code uses `.claude/skills/` wrappers that point back to the same canonical skill files.

When isolated agents are available, Loopy may use them for independent criticism or review. When they are unavailable, Loopy continues with self-objection and records `independence: unavailable`.

Loopy is not a TODO checklist. A checklist completes steps. `loopy-loop` keeps cycling through the phase skills until each target, responsibility, or review slice has a terminal decision recorded by the completion gate.

There is no build step. Editing the Markdown is the development cycle.

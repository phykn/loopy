# Loopy

Loopy is an instruction-only skill for Codex and Claude Code. Use it for
autonomous work where completion must be established by evidence, important
constraints must survive the work, or stopping too early would create material
risk.

Loopy establishes a compact Completion Contract, chooses the shortest credible
execution path, verifies the result, tests one material challenge, and returns
exactly one decision: `done`, `revise`, `blocked`, or `out_of_scope`.

When the task definition, an existing artifact, or a proposed revision requires
material judgment, Loopy also recovers the current Claim when one exists and uses
Amount, Boundary, and Priority to select only evidence-backed changes. This
judgment is internal: clear requested outcomes remain authoritative, and advisory
or unsupported possibilities do not trigger revision.

## Install

### Codex and the ChatGPT desktop app

Add the repository marketplace and install Loopy:

```text
codex plugin marketplace add phykn/loopy
codex plugin add loopy@loopy
```

Restart the ChatGPT desktop app if the plugin does not appear immediately.

### Claude Code

```text
/plugin marketplace add phykn/loopy
/plugin install loopy@loopy
```

Run `/reload-plugins` after updating an existing installation.

## Use

Invoke the skill explicitly when the work needs evidence-backed completion:

```text
Use loopy to complete this migration without losing existing behavior.
Use loopy to finish this document and verify every acceptance criterion.
Use loopy to resolve this bug, preserve the current interface, and prove the fix.
```

The skill may also be selected automatically when a request matches its
description.

Do not use Loopy for trivial edits, direct factual answers, open brainstorming,
or low-risk work whose completion is obvious from one simple action.

## Runtime structure

Both hosts load the same canonical file:

```text
skills/loopy/SKILL.md
```

Codex distribution metadata lives in `.codex-plugin/` and `.agents/plugins/`.
Claude Code distribution metadata lives in `.claude-plugin/`. There is no build
step and no duplicated host-specific skill body.

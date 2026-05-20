# Loopy

Loopy is a small skill system for autonomous agents.

## Background

Agents often finish steps without testing whether the result should survive.

Loopy starts from a different rule:

```text
Loopy = Loop(Unstable -> Tested -> Stable)
```

Work is stable only when it survives a test that could reject it.

## Purpose

Loopy provides reusable skills that turn rough work into stable output through a loop.

Current structure:

- `loopy/CORE.md`: shared Loopy philosophy.
- `loopy/loopy-theory/SKILL.md`: Codex skill for refining claims into theory.
- `.claude/skills/loopy-theory/SKILL.md`: Claude Code project skill wrapper.

## Install

Clone the repository:

```powershell
git clone https://github.com/phykn/loopy.git
cd loopy
```

For Codex, use the skill from:

```text
loopy/loopy-theory/SKILL.md
```

For Claude Code, open the repository as a project. Claude Code will load:

```text
.claude/skills/loopy-theory/SKILL.md
```

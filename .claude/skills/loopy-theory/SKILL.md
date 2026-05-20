---
name: loopy-theory
description: Use when refining ideas, design principles, research notes, process rules, or conceptual documents into evidence-backed theory; use when testing a claim, updating THEORY_*.md, or continuing a claim-objection-revision loop.
---

# Loopy Theory

This is a Claude Code compatibility wrapper. Use the canonical one-cycle runtime skill instructions in `../../../skills/loopy-theory/SKILL.md`.

Before running the cycle, also read the parent philosophy in `../../../skills/core.md` when it exists.

For Claude Code project use:

- treat `theories/THEORY_<name>.md` as stable theory output;
- treat `.loopy/cycles/theory_YYYYMMDD_HHMMSS.md` as rough cycle output;
- do not write to `docs/` unless the user explicitly names a file there.

# Repository Instructions

Loopy is a small Markdown-first plugin. Keep the public surface simple and avoid adding process that is not needed for the current task.

## Working Rules

- Read before editing. Check the current skill, manifest, wrapper, or doc before changing it.
- State assumptions for non-trivial work, especially when a request could mean behavior, wording, metadata, or repo structure.
- Make the smallest change that satisfies the request. Do not add new modes, generated files, registries, or compatibility layers unless they are directly required.
- Keep edits surgical. Do not refactor adjacent text or structure just because it could be cleaner.
- Preserve the intended shape: canonical skill behavior lives under `skills/`; `.claude/skills/` contains thin Claude Code wrappers; host metadata should describe the skills, not redefine them.

## Project Knowledge

- If `docs/wiki/index.md` exists, read it before design-sensitive changes, then only the linked pages that are relevant to the task.
- Treat `docs/wiki/` as a local maintained project knowledge base when it exists.
- Use `docs/wiki/sources.md` for source-grounding notes when the local wiki exists. Repository files may be cited directly when the repo is the subject.

## Wiki Sync Policy

Before finishing a change, check whether the diff changes durable project knowledge. If the local wiki exists, update it when durable knowledge changes.

Update `docs/wiki/` when changes affect:

- public skill behavior in `skills/**/SKILL.md`;
- plugin metadata in `.codex-plugin/` or `.claude-plugin/`;
- host wrappers in `.claude/skills/`;
- README claims, install instructions, examples, or compatibility notes;
- repository-level workflow rules in `AGENTS.md`.

Do not update the wiki for typo-only edits, formatting-only edits, transient experiments, or changes that do not alter durable project understanding.

When updating the local wiki, follow `docs/AGENTS.md`: update source-grounding in `docs/wiki/sources.md`, fold durable conclusions into topic pages, update `docs/wiki/index.md` if page purposes change, and record meaningful maintenance in `docs/wiki/log.md`.

## Verification

- For Markdown-only changes, inspect the diff and run `git diff --check`.
- For plugin metadata changes, also parse any changed JSON manifest.
- For skill behavior changes, verify that README claims, skill descriptions, host wrappers, and agent metadata still agree.
- Before finishing, report what was checked and any remaining unverified risk.

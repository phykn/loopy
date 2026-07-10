# Single-skill distribution design

## Goal

Turn Loopy from a three-skill plugin into one instruction-only `loopy` skill whose
runtime behavior lives in one `SKILL.md`, while packaging that same file for both
Codex and Claude Code through each host's current distribution structure.

The supplied completion-contract text is the new canonical behavior. The
existing `loopy-compose` and `loopy-theory` public skills are removed rather than
retained as modes or compatibility aliases.

## Chosen approach

Use one shared runtime source with native packaging metadata for each host.

```text
loopy/
├── .agents/plugins/marketplace.json
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── .claude-plugin/marketplace.json
├── skills/loopy/SKILL.md
├── README.md
├── LICENSE
└── AGENTS.md
```

Codex loads `skills/loopy/SKILL.md` through `.codex-plugin/plugin.json`. Claude
Code discovers the same plugin-root skill through its own plugin manifest. The
current `.claude/skills/` wrappers are therefore redundant and will be removed.
Per-skill `agents/openai.yaml` metadata will also be removed so the runtime skill
directory contains only `SKILL.md`; install-surface wording remains in the plugin
manifest.

This follows the current official layouts:

- Codex: <https://learn.chatgpt.com/docs/build-plugins>
- Claude Code: <https://code.claude.com/docs/en/plugins>
- Claude Code marketplaces: <https://code.claude.com/docs/en/plugin-marketplaces>

## Alternatives considered

1. Package only for Codex now. This is smaller but leaves the requested Claude
   Code compatibility unfinished even though both hosts can share the same
   skill directory.
2. Keep only `.claude-plugin/marketplace.json` and rely on Codex's legacy
   compatibility path. This saves one catalog file but does not follow Codex's
   current `.agents/plugins/marketplace.json` guidance.
3. Duplicate the skill under host-specific directories. This makes each host
   self-contained but creates two behavioral sources that can drift.

The shared-source, dual-native-metadata approach satisfies both hosts without
duplicating behavior or relying on a legacy path.

## Metadata and release behavior

The plugin name and skill name remain `loopy`. Descriptions, starter prompts,
README claims, and marketplace copy will describe evidence-based autonomous
completion rather than the removed counterexample, compose, and theory surfaces.

The version becomes `0.2.0` in both host manifests because the public skill set
changes from three skills to one. Existing author, repository, homepage, license,
and branding information remains unless a current schema requires a mechanical
shape change.

Codex receives a current repo marketplace entry at
`.agents/plugins/marketplace.json`. Claude Code retains its native
`.claude-plugin/marketplace.json`. Each catalog exposes the repository-root
plugin using the host's documented Git-backed source form.

## Documentation and user flow

The README will first explain what the single Loopy skill does, then provide
separate Codex and Claude Code installation instructions, invocation examples,
and a concise description of the completion decision states. All references to
`loopy-compose`, `loopy-theory`, three-skill composition, old Done Contract
terminology, and `.claude/skills/` wrappers will be removed.

The expected flow is:

1. A user adds or installs the Loopy plugin through the host's marketplace path.
2. The host loads the plugin-root `skills/loopy/SKILL.md`.
3. The user invokes `loopy`, or the host selects it from its description.
4. The skill establishes its Completion Contract, executes, verifies, challenges,
   and returns exactly one decision.

## Failure handling

Packaging failures should be caught before release:

- malformed manifests fail JSON parsing;
- malformed skill frontmatter fails skill or plugin validation;
- stale public claims fail a repository-wide search for removed skill names and
  terminology;
- accidental duplicate runtime skills fail the single-`SKILL.md` structure check;
- host incompatibility remains visible if an installed CLI validator is not
  available and must be reported rather than assumed away.

## Verification

Implementation is complete only when:

- exactly one file matches `skills/**/SKILL.md`;
- that file matches the supplied completion-contract content and has valid
  `name` and `description` frontmatter;
- all changed JSON manifests and catalogs parse;
- Codex metadata, Claude Code metadata, README wording, and the skill description
  agree on the single public skill;
- repository-wide searches find no live references to removed skills or wrappers;
- `claude plugin validate .` passes when the installed Claude CLI supports it;
- the strongest available Codex package validation passes without modifying the
  user's global plugin configuration;
- `git diff --check` passes and the final diff contains no unrelated changes.

No new scripts, hooks, connectors, compatibility aliases, generated files, or
runtime state are introduced.

# Loopy

Loopy is an instruction-only skill for Codex and Claude Code. It keeps an agent
working until a substantial result is correct, preserves what must not change,
and can be used without the conversation that produced it, instead of stopping
after a first draft or a first passing check.

Use it when someone else must act on the result: a maintainer finding where to
make a change, a teammate following a guide, a reader making a decision, or an
agent carrying out a skill. That user may know the domain but not the project.

## How it works

1. Define the outcome, its intended user and their next action, what must be
   preserved, the evidence of success, and the authorized scope.
2. Build the result with clear entrypoints, names, responsibilities, and the
   context its user needs.
3. Verify correctness and preservation. When use matters, a fresh subagent
   without the production conversation attempts a real task from the normal
   entrypoint, using only what a user would receive.
4. Fix the supported causes of observed obstacles and repeat the affected
   checks. Stop once the evidence shows the outcome, with no perfect score or
   fixed number of rounds.

The evaluator is a subagent the session already offers, such as a non-forked
Claude Code Agent or a fresh Codex subagent; it stays within the user's scope
and writes only in an isolated copy. Loopy checks what it actually did, and a
mistaken answer or stylistic preference alone does not justify a revision.
When delegation is restricted, or a small change already has direct evidence,
Loopy reports the strongest check it ran and its limits instead. Read-only
reviews stay read-only, and existing behavior and external contracts stay
protected.

## Use

```text
Use loopy to finish this guide so a new teammate can follow it without this chat.
Use loopy to make this plan executable by its intended owners.
Use loopy to complete this migration, preserve its interface, and verify the result.
Use loopy to assess this proposal and its evidence without editing it.
Use loopy to refactor this project into less, clearer code: fix supported
in-scope bugs, preserve external contracts, and verify a new maintainer can use it.
Use loopy to refactor these docs: group them by meaning and cut repetition
without losing claims.
```

For example, a setup guide is done when its commands work and a new teammate
can start from the README, produce the expected output, and recognize success.
If they get stuck, Loopy repairs the cause: the command, interface, order,
terminology, or a missing premise.

The skill is also selected automatically when a request matches its
description. It is not meant for trivial edits, direct factual answers, open
brainstorming, or tasks finished in one obvious step.

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

## Source and evaluation

Both hosts load [skills/loopy/SKILL.md](skills/loopy/SKILL.md), which reads
these references only when relevant:

- [Independent use](skills/loopy/references/independent-use.md): choosing the
  trial task, fresh context, evidence, and limits.
- [Code](skills/loopy/references/code.md): how written or changed code should
  read, with the least code, why-only comments, and no defensive or leftover
  code.
- [Refactoring](skills/loopy/references/refactoring.md): less, clearer code or
  documents with preserved behavior and contracts, coherent migrations, and
  fixes for supported bugs, across the whole project when asked.

To change the skill, follow [the evaluation procedure](evals/README.md); its
fixtures, acceptance criteria, and records stay outside the runtime skill.
Codex metadata lives in `.codex-plugin/` and `.agents/plugins/`, and Claude
Code metadata in `.claude-plugin/`; there is no build step or host-specific
copy of the skill.

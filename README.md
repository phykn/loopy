# Loopy

Loopy is an instruction-only skill for Codex and Claude Code. It carries
substantial work through to a result that is correct, preserves what matters,
and can be understood and used without the conversation that produced it.
It targets a common agent habit: stopping after one pass. A first draft or a
first passing check is not done until the result is verified.

Use it when you need a working handoff: a maintainer finding the right change
location, a teammate following a guide, a reader making a supported decision,
or an agent carrying out a skill. The intended user can know the domain while
being new to the project.

## How it works

1. Define the requested outcome, intended user, next action, preservation
   requirements, evidence, and authorized scope.
2. Build a coherent result with clear entrypoints, names, responsibilities,
   necessary context, and usable interfaces.
3. Verify correctness and preservation. For substantial deliverables whose
   understanding or use matters, also have a fresh evaluator attempt a real
   task from the normal entrypoint, using only the materials a user receives.
4. Check observed obstacles against the artifact, fix supported causes, and
   repeat the affected checks. Finish when the required outcome and use are
   demonstrated.

The fresh evaluator is a subagent the session already offers, such as a
non-forked Claude Code Agent or a fresh Codex subagent. It gets no production
conversation, intended answer, or earlier conclusions, stays within the user's
scope, and writes only in an isolated copy. Loopy inspects what it actually did;
a mistaken answer or stylistic preference does not by itself justify a revision.
Loopy skips the trial when the user, host, or project restricts delegation, or
when a small change already has adequate direct evidence, and then reports the
strongest permitted check and its limits, never as independent use. Passing
checks are reused while their inputs and assumptions hold.

The loop selects `done`, `revise`, `blocked`, or `out_of_scope`. It continues
executable authorized work, keeps read-only reviews read-only, and stops once
the evidence is sufficient, with no perfect score or fixed number of rounds.
Existing behavior and external contracts stay protected; a usability gain does
not excuse a regression.

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

For a concrete example, a setup guide is ready when its commands work and a new
teammate can start from the README, produce the expected output, and recognize
success. If they get stuck, Loopy checks the cause and repairs the right place:
the command, interface, order, terminology, or missing premise.

The skill can also be selected automatically when a request matches its
description. It is not intended for trivial edits, direct factual answers,
open brainstorming, or tasks whose completion is obvious from one simple action.

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

Both hosts load [skills/loopy/SKILL.md](skills/loopy/SKILL.md).
It routes to shared guidance only when relevant:

- [Independent use](skills/loopy/references/independent-use.md) defines task
  selection, fresh context, evidence, corrections, and limits.
- [Code](skills/loopy/references/code.md) defines how written or changed code
  should read: least code, why-only comments, and no defensive or leftover code.
- [Refactoring](skills/loopy/references/refactoring.md) turns code or documents
  into less, clearer content: structure, behavior baselines, compatibility,
  coherent migrations, supported bug fixes, and reader tasks. A project-wide
  request covers all major areas; a narrow request retains its boundary.

When changing the skill, follow [the evaluation procedure](evals/README.md);
its task fixtures, acceptance criteria, and records stay outside the runtime
skill.

Codex metadata lives in `.codex-plugin/` and `.agents/plugins/`; Claude Code
metadata lives in `.claude-plugin/`. There is no build step or duplicated
host-specific skill body.

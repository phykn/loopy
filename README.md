# Loopy

Loopy is an instruction-only skill for Claude Code and Codex. It keeps an agent
working until the requested outcome is demonstrated and the person who must use
the result can take their next action without the conversation that produced
it.

Agents often stop at a first draft or a first passing check: the tests pass,
but the README command fails, the fixed bug's cause is unexplained, or a new
teammate cannot follow the guide. Loopy closes that gap and scales its effort
and token use to what is at stake.

Use it when someone else must act on the result: a maintainer finding where to
make a change, a teammate following a guide, a reviewer making a decision, or
an agent carrying out a skill or prompt. That user may know the domain but not
the project.

## How it works

1. Define success: the outcome, its user and their next action, what must be
   preserved, the evidence that will show success, and the authorized scope.
2. Build the result, with what its user needs, such as entrypoints, key
   concepts, and examples, in the result itself.
3. Verify that the result is right and that its user can use it. When use
   decides success for a substantial deliverable, a fresh subagent without the
   conversation attempts a real task from the normal entrypoint.
4. Check each finding against actual behavior, fix the supported causes where
   they live, and recheck what the fixes affect. Stop once the evidence supports
   `done`, without waiting for a perfect score or a fixed number of rounds.

The evaluator is a subagent the session already offers, such as a non-fork
Claude Code Agent or a Codex subagent that does not fork the conversation. It
stays within the user's scope, writes only in an isolated copy, and takes no
external action. When delegation is restricted, or a narrow change already has
direct evidence, Loopy runs the strongest check it can and reports its limits.
Assessments stay read-only.

## Use

Loopy sorts each request by what happens to the result's behavior, whether the
result is code, a document, a prompt, or a skill:

| Behavior | Kind | Done when |
| --- | --- | --- |
| Not changed | Assess (검토해줘, 원인만 찾아줘) | Findings and causes are supported |
| Kept while form changes | Refactor (리팩토링해줘, 정리해줘) | Same behavior, except supported bugs fixed as Debug steps |
| Restored to the existing contract | Debug (고쳐줘) | The contract holds and the root cause is explained |
| Changed to a stated new behavior | Build (만들어줘, 추가해줘, 바꿔줘) | It works as stated |
| Changed toward a direction, stated or not | Improve (개선해줘) | It is measurably better than the baseline |

A mixed request runs as steps of one kind each, such as Assess then Debug for
"check and fix". "Make it shorter" is Refactor when everything must still work
as before and Improve when content may go.

```text
Use loopy to finish this guide so a new teammate can follow it without this chat.
Use loopy to assess this proposal and its evidence without editing it.
Use loopy to refactor this project into less, clearer code and preserve its
external contracts.
Use loopy to improve this prompt: it is too long, but keep the rules it must follow.
```

The hosts also select the skill automatically when a request matches its
description, in English or Korean, including bug fixes and feature additions
that look small. It is not meant for an edit the user dictates exactly, such as
a rename, or for explanations, factual questions, translation, or
brainstorming.

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

- [Code](skills/loopy/references/code.md): how written or changed code should
  read, with the least code, why-only comments, and no defensive or leftover
  code.
- [Debug](skills/loopy/references/debug.md): confirming a bug's root cause
  with a testable claim before any change, which an assessment of a cause also
  follows, then fixing it there with a regression test that fails first.
- [Refactoring](skills/loopy/references/refactoring.md): less, clearer code or
  documents with the same behavior and contracts, coherent migrations, and
  fixes for supported bugs, across the whole project when asked.
- [Improvement](skills/loopy/references/improvement.md): moving an artifact
  toward a goal, asking for one when neither the request nor the evidence
  settles it, with behavior changes and what they lose reported apart from
  reductions.
- [Independent use](skills/loopy/references/independent-use.md): choosing the
  trial task, giving the evaluator only what a user would have, and judging its
  attempt.

To change the skill, follow [the evaluation procedure](evals/README.md); its
fixtures, acceptance criteria, and records stay outside the runtime skill.
Codex metadata lives in `.codex-plugin/` and `.agents/plugins/`, and Claude
Code metadata in `.claude-plugin/`; there is no build step or host-specific
copy of the skill.

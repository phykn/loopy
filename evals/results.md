# Evaluation records

Records through 0.10.0 are in this file at commit d1d8e0b.

## Baselines

| Run | Skill | Result | Key outcome | Tokens | Control | Entry |
| --- | --- | --- | --- | --- | --- | --- |
| Activation | 0.9.0 description (unchanged in 1.0.0) | Passed | Three repetitions: `tune` 36/36 should-trigger and 0/24 near misses; `holdout` 24/24 and 0/27, counting the three dictated fixes | — | — | d1d8e0b `evals/results.md`, 0.9.0 entry |
| Routing | 1.0.0 | Passed | 21/21 requests sorted as expected, in order | 60,603 | — | [routing](#2026-11-06-routing-100) |

## 2026-11-06 routing (1.0.0)

- Date: 2026-11-06. macOS 27.0.1 (26A434), Python 3.13.16; `/usr/bin/python3` is
  3.9.6.
- `shasum -a 256 ~/.claude/CLAUDE.md`:
  `bdeb943b66445a9e4c5532dd0f362847f18560adfa763ee8420123a9af2a6df3`.
- `git -C ~/.claude/user-wiki rev-parse --short HEAD`: `f262154`.
- First run commit for 1.0.0: `46c736b`.

### Run 1

- Slot `Routing`, run commit `46c736b`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 60,603, the host's report, equal to the transcript's last usage.
- Isolation audit: exit 0 over 4 tool calls (two reads in the workspace, the
  write of `answers.md`, and the hand-back); no nested transcript.
  `git status --short` was empty after the run.
- Result: all 21 requests matched their `kinds` in order, with no reason given.
- The evaluator remarked that `r21` was an exact edit the user dictates, which
  the skill's description excludes. `r21` became an undictated Build request,
  and the check ran again as Run 2.

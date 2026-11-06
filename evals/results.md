# Evaluation records

Records through 0.10.0 are in this file at commit d1d8e0b.

## Baselines

| Run | Skill | Result | Key outcome | Tokens | Control | Entry |
| --- | --- | --- | --- | --- | --- | --- |
| Activation | 0.9.0 description (unchanged in 1.0.0) | Passed | Three repetitions: `tune` 36/36 should-trigger and 0/24 near misses; `holdout` 24/24 and 0/27, counting the three dictated fixes | — | — | d1d8e0b `evals/results.md`, 0.9.0 entry |
| Routing | 1.0.0 | Passed | 21/21 requests sorted as expected, in order, in both runs | 60,132 | — | [routing](#2026-11-06-routing-100) |
| guide | 1.0.0 | Passed | The README gives the folder, Python 3.9+, the exact command, its output, and the expected JSON; a fresh trial user packed and checked the samples on the first try | 89,531 | pending | [cases](#2026-11-06-cases-100) |

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

### Run 2

- Slot `Routing`, run commit `416aba2`, attempt 1 on the revised set. Claude
  Code 2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 60,132, the host's report, equal to the transcript's last usage.
- Isolation audit: exit 0 over 4 tool calls; no nested transcript.
  `git status --short` was empty after the run.
- Result: all 21 requests matched their `kinds` in order, with no reason given.
  The evaluator called `r14` the closest call and chose Refactor because the
  request names only what must stay.
- `416aba2` changed no file under `skills/loopy/`, `evals/prepare.py`, or
  `evals/README.md`, so [Final text](README.md#final-text) requires no rerun.

## 2026-11-06 cases (1.0.0)

- Date: 2026-11-06. macOS 27.0.1 (26A434), Python 3.13.16; `/usr/bin/python3` is
  3.9.6.
- `shasum -a 256 ~/.claude/CLAUDE.md`:
  `bdeb943b66445a9e4c5532dd0f362847f18560adfa763ee8420123a9af2a6df3`.
- `git -C ~/.claude/user-wiki rev-parse --short HEAD`: `f262154`.
- Each run used a new `--skill skills/loopy` workspace, its `prompt.md` as the
  whole prompt, and a fresh `general-purpose` subagent with `model: "opus"` and
  `effort: "xhigh"`, one run at a time.

### guide

- Slot `guide`, run commit `672855d`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 89,531, the host's report, equal to the transcript's last usage.
- Isolation audit: exit 0 over 25 tool calls in the evaluator's transcript and
  the nested transcript of its one Agent call. `git status --short` was empty
  after the run.
- The evaluator changed only `README.md`; `parcel.py` and both notes equal the
  fixture byte for byte.
- `guide#1` passed: the README says to run "From this folder, the one that
  contains `parcel.py`", names Python 3.9 or later, gives
  `python3 parcel.py notes --output packed.json`, and shows the printed line and
  the exact `packed.json` to compare with.
- `guide#2` passed: in a clean copy, that command printed
  `Packed 2 notes into packed.json` and wrote a `packed.json` that equals the
  README's JSON block byte for byte and holds both notes.
- `guide#3` passed: the README says "Without it, Parcel refuses to overwrite, so
  running the sample command a second time needs `--replace` or a new output
  path"; a second run in the clean copy exited 2 with the quoted reason, and the
  sample command carries no `--replace`.
- `guide#4` passed. Use: in the coordinator trial below, a fresh user packed and
  checked the samples on the first try. Record: `run.md` reports an independent
  attempt by one fresh subagent in `scratch/trial/guide`, and the transcript
  holds that Agent call and its nested transcript.
- The README's other claims held in the clean copy: missing output folders are
  created, and a non-UTF-8 note stops the run with `UnicodeDecodeError` before
  anything is written.
- Coordinator trial: 61,258 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 7 tool calls, no nested
  transcript. The trial user read `README.md` and `parcel.py`, ran the sample
  command, and compared `packed.json` with the README's block by `diff` and a
  parsed-JSON assert. It guessed how to compare the file, how to check the
  Python version, and the exit codes; none of these stopped it.

### Limits

- An evaluator's shell starts in the coordinator's checkout, so a relative read
  with no forbidden string or recursive search would not show in the audit.
- Evaluators and trial users are agents, so a trial shows use by a fresh agent,
  not by a person.

# Evaluation records

Records through 0.10.0 are in this file at commit d1d8e0b.

## Baselines

| Run | Skill | Result | Key outcome | Tokens | Control | Entry |
| --- | --- | --- | --- | --- | --- | --- |
| Activation | 0.9.0 description (unchanged in 1.0.0) | Passed | Three repetitions: `tune` 36/36 should-trigger and 0/24 near misses; `holdout` 24/24 and 0/27, counting the three dictated fixes | — | — | d1d8e0b `evals/results.md`, 0.9.0 entry |
| Routing | 1.0.0 | Passed | 21/21 requests sorted as expected, in order, in both runs | 60,132 | — | [routing](#2026-11-06-routing-100) |
| guide | 1.0.0 | Passed | The README gives the folder, Python 3.9+, the exact command, its output, and the expected JSON; a fresh trial user packed and checked the samples on the first try | 89,531 | pending | [cases](#2026-11-06-cases-100) |
| review | 1.0.0 | Passed | Found the unowned publishing step and the command check placed after publication, left owners as blanks to fill, and changed no file | 76,798 | pending | [cases](#2026-11-06-cases-100) |
| ready | 1.0.0 | Passed | Checked the empty-folder result (`0`, exit 0) against the CLI, rejected the retry suggestion, and changed no file | 83,796 | pending | [cases](#2026-11-06-cases-100) |
| refactor | 1.0.0 | Passed | Source 125 → 83 lines; sample outputs, refusals, and `--help` unchanged; the skipped invalid amount fixed with a test that fails on the original | 117,548 | pending | [cases](#2026-11-06-cases-100) |
| fix | 1.0.0 | Passed | Reproduced `total 9:00` and the −1380-minute entry before editing; `total 33:00`; only the duration line and one test changed | 78,578 | pending | [cases](#2026-11-06-cases-100) |

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

### review

- Attempt 1, invalid: slot `review`, run commit `54e2cca`. Claude Code 2.1.317,
  effort `xhigh`, model `claude-opus-5-5`. Tokens: 78,256, recorded apart from
  the total. Isolation audit: exit 1 at line 30,
  `cd ~/.claude/user-wiki && ls; cat graph/workflow.md 2>/dev/null || find . -name 'workflow*'`,
  run while reading the global instructions' wiki. The `find .` searched the
  wiki, but the audit flags every recursive search that does not name the
  workspace, so the run was not judged and was rerun with a new workspace and
  evaluator. `git status --short` was empty, and `plan.md` was unchanged.
- Attempt 2: slot `review`, run commit `4a82d9e`. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 76,798, the host's report, equal to the transcript's last usage.
- Isolation audit: exit 0 over 15 tool calls in the evaluator's transcript and
  the nested transcript of its one Agent call, a fresh agent that read only
  `plan.md`. `git status --short` was empty after the run.
- `review#1` passed: the reply names the unowned step, "6행 "Publish the guide on
  Friday."에 담당자가 없습니다", and the late check, "검증이 게시 뒤에 있고, 완료
  기준이 "페이지 온라인"뿐입니다 (7행, 9행)", with the missing failure path,
  location, handoffs, and test environment.
- `review#2` passed: each finding quotes the plan's current lines, each proposal
  is marked "제안:", and the example revision leaves `<게시 담당자>` and
  `<결정자>` for the team to fill; nothing claims the user's authorization.
- `review#3` passed: `plan.md` equals the fixture byte for byte, and the only
  file the evaluator wrote was `run.md`.

### ready

- Slot `ready`, run commit `2648b82`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 83,796, the host's report, equal to the transcript's last usage.
- Isolation audit: exit 0 over 14 tool calls; no Agent call. `git status --short`
  was empty after the run.
- `ready#1` passed: the evaluator ran an existing empty folder and got `0` with
  exit 0, and a missing folder with exit 2; in a clean copy, an empty folder
  printed `0` and exited 0.
- `ready#2` passed: `README.md`, `count.py`, and the note equal the fixture byte
  for byte, and the reply says "이전 리뷰의 "0이면 실패이니 재시도 안내" 의견은
  반영하지 않았습니다" because `0` is the documented empty result.
- `ready#3` passed: the evaluator made no edit and started no reviewer, and
  stopped with `done` after its checks: "고칠 근거가 있는 오류는 없어 파일을 바꾸지
  않았습니다". It also ran the checks on Python 3.9.6, 3.12, 3.13, and 3.14.

### refactor

- Slot `refactor`, run commit `8adf6b7`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 117,548, the host's report, equal to the transcript's last usage.
- Isolation audit: the first audit exited 1 at line 31,
  `cd ~/.claude/user-wiki && ls -R graph | head -50; ...`, a recursive listing
  inside the wiki the global instructions send agents to. With
  `--allow .claude/user-wiki` from `d5fef94` (below), it exits 0 over 42 tool
  calls in the evaluator's transcript and the nested transcript of its one Agent
  call. `git status --short` was empty after the run.
- `refactor#1` passed: in fresh copies of the fixture and the result, the
  sample's text, the JSON run and file bytes, the existing-output refusal, the
  wrong-header rejection, `--help`, a missing source, and a CSV without a BOM
  gave the same output and exit status.
- `refactor#2` passed: `records.py` keeps "Bank exports start with a byte order
  mark; utf-8-sig drops it so the header matches."; `cli.py` still checks the
  source and the existing output, and `read_records` still checks the header.
- `refactor#3` passed: no file-top docstring is left, and the `--help` text is
  the `description` argument. The restating comments, commented-out code,
  `format_amount_old`, the `os` and `sys` imports, `DEBUG`, `load`, the `sort`
  option, the `None` guard, the second category normalization, and the second
  total calculation are gone; one `summarize` makes the totals for both outputs.
- `refactor#4` passed: a row with amount `abc` or an empty amount now exits 2
  with `line 3: amount is not a number` and writes no JSON, where the original
  exited 0 and skipped it. The new `test_rejects_invalid_input` fails 5
  subtests on the original code and passes on the new, and `run.md` and the
  reply report the fix under its own heading, apart from the structural changes.
- `refactor#5` passed: the four tests cover the text totals, the JSON file in a
  new folder, the existing-output refusal, and the header and amount
  rejections; `test_prints_total_line` is gone.
- `refactor#6` passed: source lines 125 → 83 with plain names such as
  `summarize`, `format_text`, and `parse_amount`; `run.md` gives "소스 125 →
  83줄(버그 수정으로 늘어난 줄 포함). 테스트 61 → 68줄(회귀 경우 추가). README
  0줄 변경."
- `refactor#7` passed: all three modules and the test file changed for findings
  `run.md` names, and the README and sample were checked and kept.
- The evaluator also rejects `NaN` and infinite amounts, which the original
  printed or crashed on, and writes the JSON with mode `x`; it reports both as
  fixes.

### fix

- Slot `fix`, run commit `1e4ce81`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 78,578, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 22 tool
  calls; no Agent call. `git status --short` was empty after the run. The
  evaluator wrote one input file to the session scratchpad, deleted it, and
  recorded it; the scratchpad is exempt under Judging.
- `fix#1` passed: by `audit.py --calls`, line 55 printed `deploy -21:00`,
  `total 9:00`, and the parsed `('deploy', -1380)` for `23:30-00:30`; the new
  test failed at line 74, and the first edit to `entries.py` came at line 83.
- `fix#2` passed: the change is `(end - start) % MINUTES_PER_DAY` where
  `read_entries` stores the duration; the sample prints `build 22:30`,
  `review 7:30`, `deploy 3:00`, and `total 33:00`; `test_counts_entry_past_midnight`
  fails on the fixture's code and passes on the new.
- `fix#3` passed: only `entries.py` (the duration line, its constant, and a
  why-comment) and the added test differ from the fixture; `to_minutes`, its
  `None` check, `worklog.py`, `report.py`, the README, and the log are byte for
  byte unchanged, and the three existing tests are untouched.
- `fix#4` passed: the three existing tests pass on the new code, covering task
  order, `H:MM`, ignored blank and comment lines, and exit 2 with the line
  number for malformed and out-of-range times.
- `fix#5` passed: the reply gives the cause with the −1380 minutes, the fix, and
  the new test failing as `deploy -22:45` before the fix and passing after; it
  reports the missing `python` command apart from the fix, as the 0.10.0 run
  did, and changes nothing else.

### Changes during this work

- `d5fef94` changed `evals/audit.py`, its test, and `evals/README.md`: each
  `--allow` names a folder that a search may name besides the workspace. The
  audit had flagged `review` attempt 1 and `refactor` for recursive reads of the
  global instructions' wiki. Selection-table row: evaluation tool code that
  keeps every sentence sent to evaluators, and the README. It requires the
  package checks and unit tests, which passed on both Pythons, and one prepared
  workspace's `requests.md` and `prompt.md`, read for `fix`. No slot needs a
  rerun.

### Limits

- An evaluator's shell starts in the coordinator's checkout, so a relative read
  with no forbidden string or recursive search would not show in the audit.
- Evaluators and trial users are agents, so a trial shows use by a fresh agent,
  not by a person.
- `~/.claude/CLAUDE.md` changed on 2026-11-06, after the 0.10.0 baselines, and
  sends every evaluator to the user wiki; the runs read two to four of its
  pages, about 1,350 words for four, so token comparisons with those baselines
  include this change.

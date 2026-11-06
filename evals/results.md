# Evaluation records

Records through 0.10.0 are in this file at commit d1d8e0b.

## Baselines

| Run | Skill | Result | Key outcome | Tokens | Control | Entry |
| --- | --- | --- | --- | --- | --- | --- |
| Activation | 0.9.0 description (unchanged in 1.0.0) | Passed | Three repetitions: `tune` 36/36 should-trigger and 0/24 near misses; `holdout` 24/24 and 0/27, counting the three dictated fixes | — | — | d1d8e0b `evals/results.md`, 0.9.0 entry |
| Routing | 1.0.0 | Passed | 21/21 requests sorted as expected, in order, in both runs | 60,132 | — | [routing](#2026-11-06-routing-100) |
| guide | 1.0.0 | Passed | The README gives the folder, Python 3.9+, the exact command, its output, and the expected JSON; a fresh trial user packed and checked the samples on the first try; regression only | 89,531 | 4/4 | [cases](#2026-11-06-cases-100) |
| review | 1.0.0 | Passed | Found the unowned publishing step and the command check placed after publication, left owners as blanks to fill, and changed no file; regression only | 76,798 | 3/3 | [cases](#2026-11-06-cases-100) |
| ready | 1.0.0 | Passed | Checked the empty-folder result (`0`, exit 0) against the CLI, rejected the retry suggestion, and changed no file; regression only | 83,796 | 3/3 | [cases](#2026-11-06-cases-100) |
| refactor | 1.0.0 | Passed | Source 125 → 83 lines; sample outputs, refusals, and `--help` unchanged; the skipped invalid amount fixed with a test that fails on the original | 117,548 | 6/7 | [cases](#2026-11-06-cases-100) |
| fix | 1.0.0 | Passed | Reproduced `total 9:00` and the −1380-minute entry before editing; `total 33:00`; only the duration line and one test changed | 78,578 | 4/5 | [cases](#2026-11-06-cases-100) |
| cause | 1.0.0 | Passed | Return sign fixed after the parsed moves showed `('gadget', -2)`; no clamp; the new test fails on the original and on a clamped copy; regression only | 74,896 | 5/5 | [cases](#2026-11-06-cases-100) |
| diagnose | 1.0.0 | Passed | Cause confirmed from the normalized keys and the README's two-row example (`members 2`); expected 5; task files unchanged; regression only | 75,522 | 5/5 | [cases](#2026-11-06-cases-100) |
| feature | 1.0.0 | Passed | January totals 512.50; output without `--month` unchanged; the month checked at the CLI and rows' dates checked only with `--month`; regression only | 106,516 | 5/5 | [cases](#2026-11-06-cases-100) |
| docs | 1.0.0 | Passed | Documentation 94 → 75 lines in two files; the FAQ's overwrite claim corrected and the broken link removed; code unchanged | 98,859 | 5/7 | [cases](#2026-11-06-cases-100) |
| improve | 1.0.0 | Passed | Attempt 6, after a fourth wording fix the person chose: the criteria and a walkthrough of the sample under the original prompt were written before the first edit; every hard rule kept at 405 → 232 words (42.7%), and the trial bot posted the expected blocker | 96,438 | 3/6 | [cases](#2026-11-06-cases-100) |
| review (Codex) | 1.0.0 | Passed | Named the unowned publishing step and the command check after publication, named no owner for the gaps, and changed no file | 142,502 | — | [Codex](#2026-11-06-codex-100) |
| refactor (Codex) | 1.0.0 | Failed | Behavior, `--help`, and the boundary checks kept and the invalid amount fixed with a regression test, but both output functions still compute the grand total (`refactor#3`), a host difference | 628,176 | — | [Codex](#2026-11-06-codex-100) |
| fix (Codex) | 1.0.0 | Passed | Reproduced `total 9:00` and the −1380-minute entry before editing; `total 33:00`; only the duration lines and the added tests changed | 226,534 | — | [Codex](#2026-11-06-codex-100) |
| feature (Codex) | 1.0.0 | Passed | January totals 512.50; output without `--month` unchanged; the month checked at the CLI, with every invalid value exiting 2 and writing nothing | 257,686 | — | [Codex](#2026-11-06-codex-100) |
| improve (Codex) | 1.0.0 | Failed | 405 → 184 words (54.6%) with every hard rule kept, and the trial bot posted the expected blocker; but the events cannot show the baseline `run.md` says it wrote before the first edit (`improve#1`), a host difference | 494,087 | — | [Codex](#2026-11-06-codex-100) |

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

### cause

- Slot `cause`, run commit `ebc9369`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 74,896, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 18 tool
  calls; no Agent call. `git status --short` was empty after the run.
- `cause#1` passed: by `audit.py --calls`, line 52 printed `gadget -4`,
  `total 11`, and the parsed moves with `('gadget', -2)` for the return; the
  new test failed at line 71, and line 75 says "Fails for the predicted reason
  (return subtracted: 3-3-2 = -2)" before the only code edit, at line 76.
- `cause#2` passed: `moves.py` now negates only `out`
  (`if kind == "out":`); the sample prints `widget 9`, `gadget 0`, `bolt 6`,
  and `total 15`. The run made three edits, two to the test file and that
  line, and none adds or removes a clamp.
- `cause#3` passed: `test_returns_go_back_into_stock` (`in 3`, `out 3`,
  `return 2` giving `gadget 2`) fails on the fixture's code and passes on the
  new. On a copy of the fixture that clamps stock at zero, the sample prints
  the right totals but this test fails.
- `cause#4` passed: only that line of `moves.py` and the added test differ from
  the fixture; `stock.py`, `report.py`, the README, and the log are byte for
  byte unchanged, and the three existing tests are untouched and pass.
- `cause#5` passed: the reply says the October 8 gadget return was subtracted
  instead of added, which gave `-4` and `11`; that only `out` is negated now; and
  that the new test failed as `gadget -2` before the fix and passes after. It
  leaves negative stock from over-shipping as a question instead of clamping.

### diagnose

- Slot `diagnose`, run commit `cfd869f`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 75,522, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 12 tool
  calls; no Agent call. `git status --short` was empty after the run.
- `diagnose#1` passed: line 51 printed `members 7`, and the reply says the
  real count is 5 because rows 4 and 6 repeat `ann@example.com` and
  `bo.kim@mail.test` in other letter case.
- `diagnose#2` passed: the claim is that `normalize` lowercases only the
  domain; line 51 printed the keys, such as `'Ann@Example.com' -> 'Ann@example.com'`,
  and line 56 ran the README's two-row example and printed `members 2`, all
  outside `tasks/`.
- `diagnose#3` passed: the reply says "앞뒤 공백은 제대로 처리됩니다", names the
  domain lowercasing as working, and offers no other cause.
- `diagnose#4` passed: `diff -r` finds the task directory identical to the
  fixture, with no new file; the fix is only a suggestion for whoever fixes it.
- `diagnose#5` passed: the reply gives `members.py`, `normalize()`, lines 34–36,
  the keys and the two-row run as evidence, and "실제 5명".

### feature

- Slot `feature`, run commit `74ef376`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 106,516, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 14 tool
  calls; no Agent call. `git status --short` was empty after the run.
- `feature#1` passed: in a fresh copy, `--month 2026-01` prints `food 12.50`,
  `rent 500.00`, and `total 512.50`, and writes the same totals with `--json`.
  Without it, the sample's text and JSON are unchanged, and error runs differ
  only in the usage line, which now lists `[--month YYYY-MM]`. The fixture's
  tests pass on the new code, and `test_sums_only_given_month` covers the
  filter.
- `feature#2` passed: `parse_month` in `cli.py` is the option's `type`, and
  `2026-1`, `2026-13`, `2026-00`, `26-01`, `abc`, an empty value,
  `2026-01-05`, and ` 2026-01` each exit 2 with no output or JSON.
- `feature#3` passed: no docstring, no broad handler, no fallback, and no
  wrapper was added. `parse_month` and `is_iso_date` hold the checks, and the
  one added comment gives a reason: "Python 3.11+ also parses forms such as
  20260105; the round trip keeps only YYYY-MM-DD."
- `feature#4` passed: the diff is the option, the month filter in
  `read_records` with its date check, three tests, and three README lines; no
  existing line was rewritten except the `read_records` call and signature.
- `feature#5` passed: the README adds the `--month 2026-01` command, "With
  `--month YYYY-MM`, it sums only the rows dated in that month", and the
  rejection of an invalid date with `--month`, which the tests confirm.

### docs

- Slot `docs`, run commit `defef52`, attempt 1. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 98,859, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 31 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh user of an isolated copy. `git status --short` was empty
  after the run.
- `docs#1` passed: the README gives Python 3.9 or newer with nothing to install
  and the sample command, and its one link reaches `docs/usage.md`. That page
  gives the `--json` command, alphabetical order and two decimals, the JSON
  shape, the refusal to replace, the exact header, the category comparison,
  decimal amounts, the byte order mark, and exit status 2 with the line.
- `docs#2` passed: the evaluator ran a second `--json` to the same path (exit
  2, file unchanged), `docs/usage.md` now says "Ledger never replaces an
  existing file", and the reply reports the FAQ's overwrite claim under its own
  heading.
- `docs#3` passed: the `docs/output.md` link is gone, and the one local link
  left, `README.md` to `docs/usage.md`, resolves.
- `docs#4` passed: the FAQ's five entries were merged and the file deleted;
  output, JSON, input, and error rules live only in `docs/usage.md`, and filler
  such as "Ledger is a tool" and "It is important to note" is gone.
- `docs#5` passed: `cli.py`, `records.py`, `report.py`, and the sample equal the
  fixture byte for byte, and `docs/usage.md` is still at the path the epilog
  names.
- `docs#6` passed: documentation lines 94 → 75 (28 and 47) with every premise
  above kept, and the reply gives "94줄에서 75줄로" and names the factual fixes.
- `docs#7` passed: in a fresh copy, the README command prints exactly its text
  block, and the `--json` command exits 0 and writes the described JSON.
  `python cli.py CSV_FILE [--json JSON_PATH]` in `docs/usage.md` is a synopsis
  with placeholders, not a runnable command.

### improve

- Attempt 1, stopped: slot `improve`, run commit `07a5d86`. The coordinator
  stopped the evaluator before it finished, when the session reached its usage
  limit. The run was not judged, and its workspace was deleted. Tokens: 79,655
  at the stop, from the transcript's last usage, recorded apart from the total.
- Attempt 2: slot `improve`, run commit `07a5d86`. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 98,434, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 21 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh agent given only the revised prompt and the sample.
  `git status --short` was empty after the run.
- The evaluator changed only `review-bot.md`; both notes and the sample equal
  the fixture byte for byte.
- `improve#1` failed. Before the first write to `review-bot.md`, the calls are
  reads and `wc -l -w -c` (405 words), and the transcript holds no text that
  states criteria. No review of `samples/pr-42.diff` under the original prompt
  appears anywhere in the run: `run.md`, written after the edits, checks only
  the revised prompt.
- `improve#2` passed: the eight numbered rules keep never approve or merge,
  changed lines only, the exact format with `blocker`, `major`, and `minor`,
  skipping `gen/` and lockfiles, the author's language with English when
  unsure, at most 10 comments with blockers first, and `request_changes` on a
  blocker. The added clause "keep the severity words in English" keeps the
  format exact and drops no rule.
- `improve#3` passed: the history, the exhortations, and "Good code is
  readable, maintainable, and correct" are gone, and a phrase search for them
  finds nothing.
- `improve#4` passed: the `ircbot` step is gone because the tool "was removed
  in March 2026" (`notes/tools.md`); the style rule went and "Do not comment on
  formatting" stayed; the forced praise went because the feedback calls it
  "noise".
- `improve#5` passed: `run.md` lists five behavior changes, each with what is
  lost, apart from four wording and structure cuts, and the reply keeps that
  split; both give 405 → 233 words, 42.5% fewer by `len(text.split())`.
- `improve#6` passed. Use: in the coordinator trial below, the bot posted one
  Korean comment in the required form on the off-by-one,
  `[blocker] app/history.py:5 - items[-n - 1:]은 최근 n건이 아니라 n+1건을 반환합니다 ...`,
  called `request_changes`, and skipped the quote change and `gen/schema.py`,
  with no `ircbot` call and no approval. The notes and the sample equal the
  fixture in the workspace and in the trial copy.
- Coordinator trial: 59,397 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 4 tool calls, no nested
  transcript. The trial bot read only `review-bot.md` and the diff, and left
  out a doubt about sorting payments without `paid_at` because the diff does
  not show that data.
- Cause of `improve#1`: skill wording. `references/improvement.md` said
  "Record the baseline on those tasks and measures", and the evaluator
  recorded only the measure. The change below makes the baseline run the tasks
  on the current version before the first edit, and the slot reruns.

- Attempt 3: slot `improve`, run commit `e4db507`. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 90,488, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 20 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh agent given only the revised prompt, the sample, and the
  two tool signatures. `git status --short` was empty after the run.
- The evaluator changed only `review-bot.md`; both notes and the sample equal
  the fixture byte for byte.
- `improve#1` failed. Before the first write to `review-bot.md`, the one
  baseline call measured the original (63 lines, 405 words, 17 exhortation
  words) and listed its conflicting and obsolete lines, and the transcript
  holds no text. The review of `samples/pr-42.diff` under the original prompt
  appears only in the "Baseline" section of `run.md`, written after the edits,
  as a "walkthrough plus the observed behavior in `feedback.md`".
- `improve#2` passed: the three sections keep never approve or merge, changed
  lines only, the exact format with `blocker`, `major`, and `minor`, skipping
  `gen/` and lockfiles, "the language of the pull request description; if
  unsure, use English" for comments and the summary, at most 10 comments with
  blockers first, and `request_changes` on a blocker.
- `improve#3` passed: the history, the exhortations, and the generic advice are
  gone, and a phrase search for them finds nothing.
- `improve#4` passed: the `ircbot` step is gone because the tool "was removed
  in March 2026"; the style rule went and the formatting rule stayed; the
  forced praise went because the feedback calls it noise.
- `improve#5` passed: `run.md` lists three behavior changes, each with "Lost:",
  apart from the wording and structure changes, and gives 217 words (was 405),
  46.4% fewer by `len(text.split())`. The reply repeats 405 to 217 words; the
  message to the user gives lines, 63 to 31.
- `improve#6` passed. Use: in the coordinator trial, the bot posted one Korean
  `[blocker] app/history.py:5` comment in the required form on the off-by-one,
  called `request_changes`, and skipped the quote change and `gen/schema.py`,
  with no `ircbot` call and no approval. The notes and the sample equal the
  fixture in the workspace and in the trial copy.
- Coordinator trial: 59,236 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 4 tool calls, no nested
  transcript.
- Cause of `improve#1`: skill wording. After `57697eb` the sentence still began
  "Before editing" and put the baseline run in a "then" clause; the evaluator
  ran the measures before the edit and wrote the walkthrough down at the end.
  The second change below ties the record to the first edit.

- Attempt 4: slot `improve`, run commit `86affd0`. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 94,811, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 24 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh agent given a copy of the revised prompt, the sample, and
  a list of the two tools. `git status --short` was empty after the run.
- The evaluator changed only `review-bot.md`; both notes and the sample equal
  the fixture byte for byte.
- `improve#1` failed. Before the first write to `review-bot.md`, the calls
  record the criteria and measures: a static check of the original reports 63
  lines, 405 words, 16 exhortation words, 13 kept rules, and four open
  problems. No call reviews `samples/pr-42.diff` under the original prompt,
  and the transcript holds no text. `run.md`, written after the edits, takes
  the sample's before behavior from "my own walkthrough of the original
  prompt, backed by the production observations in `notes/feedback.md`".
- `improve#2` passed: the six numbered rules and three steps keep never approve
  or merge, changed lines only, the exact format with `blocker`, `major`, and
  `minor`, skipping `gen/` and lockfiles, the author's language with English
  when unsure, at most 10 comments with blockers first, and `request_changes`
  on a blocker.
- `improve#3` failed: the role keeps the generic advice as "leave comments that
  help the author make the code correct, readable, and maintainable", and
  `run.md` says the role "keeps ... the goal of correct, readable, maintainable
  code". The history and the exhortations are gone.
- `improve#4` passed: the `ircbot` step is gone because the tool was removed in
  March 2026 (`notes/tools.md`); the style rule went and the formatting rule
  stayed; the forced praise went because the feedback calls it noise.
- `improve#5` passed: `run.md` lists three behavior changes, each with "Lost:",
  apart from the wording and structure changes, and both it and the reply give
  405 → 226 words, 44.2% fewer by `len(text.split())`.
- `improve#6` passed. Use: in the coordinator trial, the bot posted one Korean
  `[blocker] app/history.py:5` comment in the required form on the off-by-one,
  called `request_changes`, and skipped the quote change and `gen/schema.py`,
  with no `ircbot` call and no approval. The notes and the sample equal the
  fixture in the workspace and in the trial copy.
- Coordinator trial: 59,310 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 3 tool calls, no nested
  transcript.
- Cause of `improve#1`: skill wording. The second change moved the record
  before the first edit, and the criteria and measures moved with it, but the
  evaluator kept its one fresh agent for the result. It took the sample's
  before behavior from its reading and the feedback, and wrote that down only
  at the end, so the baseline never ran the review task. Cause of
  `improve#3`: skill wording. The removal examples name "generic exhortation"
  but not generic advice, and the evaluator kept the quality goals as a goal.
  The third change below covers both.

- Attempt 5: slot `improve`, run commit `c1c5d11`. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 94,737, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 21 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh agent given a copy of the revised prompt, the tool
  signatures, and the sample. `git status --short` was empty after the run.
- The evaluator changed only `review-bot.md`; both notes and the sample equal
  the fixture byte for byte.
- `improve#1` failed. Before the first write to `review-bot.md`, the one
  baseline call printed the original's size (63 lines, 405 words, 2,383 bytes),
  its six headings, and its rule lines, and the transcript holds no text. The
  review of `samples/pr-42.diff` under the original prompt is in `run.md`,
  "Self-walkthrough on pr-42 (self-check, not independent)", and it names the
  quote comment, the praise, and the failing `ircbot` call next to the correct
  blocker; `run.md` was written after the edits.
- `improve#2` passed: "Rules" and "Required steps" keep never approve or merge,
  changed lines only, the exact format with `blocker`, `major`, and `minor`,
  skipping `gen/` and lockfiles, the author's language with English when
  unsure, at most 10 comments with blockers first, and `request_changes` on a
  blocker.
- `improve#3` passed: the history, the exhortations, and "Good code is
  readable, maintainable, and correct" are gone, and a phrase search for them
  finds nothing.
- `improve#4` passed: the `ircbot` step is gone because the tool was removed in
  March 2026; the style rule went and the formatting rule stayed; the forced
  praise went because the feedback calls it noise.
- `improve#5` passed: `run.md` lists four behavior changes, each with "Lost:",
  apart from the wording and structure changes; it and the message to the user
  give 405 → 227 words, 44.0% fewer by `len(text.split())`.
- `improve#6` passed. Use: in the coordinator trial, the bot posted a Korean
  `[blocker] app/history.py:5` comment in the required form on the off-by-one
  and a `[minor]` comment on sorting without `paid_at`, called
  `request_changes`, and skipped the quote change and `gen/schema.py`, with no
  `ircbot` call and no approval. The notes and the sample equal the fixture in
  the workspace and in the trial copy.
- Coordinator trial: 60,509 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 4 tool calls, no nested
  transcript.
- Cause of `improve#1`: skill wording. The baseline walkthrough was complete
  this time, but it was written down only in the final `run.md`. The judge
  counts only what the transcript shows before the first edit.
- The three skill fixes Failure triage allows in one task are used, so the
  slot is not rerun. T10 stays unchecked, and this failure goes to the person.
- The person chose one more fix beyond the cap ("나로 해봐", 2026-11-06). The
  fourth change below follows, and the slot reruns as attempt 6.

- Attempt 6: slot `improve`, run commit `f33ecb3`. Claude Code 2.1.317, effort
  `xhigh`, model `claude-opus-5-5`.
- Tokens: 96,438, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 23 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh agent given only the revised prompt, two sample pull
  requests, and the two tool signatures. `git status --short` was empty after
  the run.
- The evaluator changed only `review-bot.md`; both notes and the sample equal
  the fixture byte for byte. Outside the task it wrote
  `eval/baseline/review-bot.md`, a copy of the original, and `eval/pr-43.diff`,
  a second sample of its own.
- `improve#1` passed. Before the first write to `review-bot.md`, the evaluator
  wrote `run.md` with "Contract (written before the first edit)": the bot's
  reviews of `pr-42` and of the second sample and a maintainer's reading as
  tasks with expected results, and the measures. Its "Baseline (original file
  ..., before editing)" gives 63 lines, 405 words, one contradiction, and one
  call to a removed tool, and a self-check walkthrough of `pr-42` under the
  original prompt: the blocker likely found, but a quote comment, the forced
  praise, and the `ircbot` call.
- `improve#2` passed: the three sections keep never approve or merge, changed
  lines only, the exact format with `blocker`, `major`, and `minor`, skipping
  `gen/` and lockfiles, "Write everything you post in the language of the pull
  request description. If you are not sure, use English.", at most 10 comments
  with blockers first, and `request_changes` on a blocker.
- `improve#3` passed: the history, the exhortations, and the generic advice are
  gone, and a phrase search for them finds nothing.
- `improve#4` passed: the `ircbot` step is gone because the tool was removed in
  March 2026 (`notes/tools.md`); the style rule went and the formatting rule
  stayed, now naming spacing, quotes, and line length; the forced praise went
  because the feedback calls it noise.
- `improve#5` passed: `run.md` lists three behavior changes, each with "Lost:",
  apart from the wording and structure changes; it and the message to the user
  give 405 → 232 words, 42.7% fewer by `len(text.split())`.
- `improve#6` passed. Use: in the coordinator trial, the bot posted a Korean
  `[blocker] app/history.py:5` comment in the required form on the off-by-one
  and a `[minor]` comment on sorting without `paid_at`, called
  `request_changes`, and skipped the quote change and `gen/schema.py`, with no
  `ircbot` call and no approval. The notes and the sample equal the fixture in
  the workspace and in the trial copy.
- Coordinator trial: 60,690 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 4 tool calls, no nested
  transcript.
- The baseline walkthrough put the blocker on line 12, its line in the diff
  file; after its trial the evaluator recounted the new file and recorded the
  correction to line 5. It also restored the language rule's scope, which its
  first draft had narrowed and its trial flagged, and rechecked that line by
  reading only.

### Token total

| Case | 0.10.0 | 1.0.0 | Change |
| --- | --- | --- | --- |
| guide | 80,778 | 89,531 | +8,753 |
| review | 77,285 | 76,798 | −487 |
| ready | 73,360 | 83,796 | +10,436 |
| refactor | 113,141 | 117,548 | +4,407 |
| fix | 75,361 | 78,578 | +3,217 |
| cause | 73,549 | 74,896 | +1,347 |
| diagnose | 75,817 | 75,522 | −295 |
| feature | 85,129 | 106,516 | +21,387 |
| docs | 96,215 | 98,859 | +2,644 |
| improve | 89,918 | 96,438 | +6,520 |
| Total | 840,553 | 898,482 | +57,929 (+6.9%) |

- The 1.0.0 column is each slot's last judged run; failed, invalid, and stopped
  runs are recorded apart. The total is over R11's cap of 840,553.
- About 15,000 of the rise is the first turn's context, before any skill read:
  48,415–48,636 tokens in the 0.10.0 transcripts (Claude Code 2.1.308) and
  49,896–50,100 now (2.1.317), about 1,500 per run, from the host and the
  global instructions (see Limits).
- `feature` adds 21,387: its evaluator also checked each row's date when
  `--month` is given and fixed one bug of its own during the run. `code.md`
  keeps the 0.10.0 rule on validating input at trust boundaries.
- The other 21,542 is spread over the remaining cases, led by `ready`
  (+10,436) and `guide` (+8,753). Old runs of one case already differed by up
  to 5,084 tokens (`fix` 73,159–78,243; `guide` 81,599–86,314); `guide` is
  3,217 above its highest 0.10.0 run.
- The skill text is smaller than 0.10.0 (`SKILL.md` body 1,336 → 1,097 words;
  references 2,623 → 2,100), so the coordinator judged the rise not
  skill-caused. Failure triage sends such a rise to the person. On 2026-11-06,
  asked whether to accept it as environment-caused, the person answered "계속"
  ("continue"), which is recorded as acceptance. That answer was given at
  896,781; `improve` attempt 6, the rerun the person chose afterward, replaced
  attempt 5 and added 1,701.

### Changes during this work

- `d5fef94` changed `evals/audit.py`, its test, and `evals/README.md`: each
  `--allow` names a folder that a search may name besides the workspace. The
  audit had flagged `review` attempt 1 and `refactor` for recursive reads of the
  global instructions' wiki. Selection-table row: evaluation tool code that
  keeps every sentence sent to evaluators, and the README. It requires the
  package checks and unit tests, which passed on both Pythons, and one prepared
  workspace's `requests.md` and `prompt.md`, read for `fix`. No slot needs a
  rerun.
- `57697eb` changed `references/improvement.md`: before the first edit, the
  baseline now runs the criteria's tasks and measures on the current version
  and records the results, after `improve` attempt 2 recorded only the word
  count. Selection-table row: one reference, `improvement.md` → `improve`. It
  requires `improve`, rerun as attempt 3, and `improve (Codex)`, which T12 runs
  after this commit. The package checks and unit tests passed on both Pythons; the
  references total 2,098 words.
- `d035cf8` changed `references/improvement.md` again: the criteria sentence no
  longer carries the timing, and a sentence of its own says "Before the first
  edit, run those tasks and measures on the current version and record the
  results as the baseline", after `improve` attempt 3 wrote its baseline
  walkthrough only at the end. Selection-table row: one reference,
  `improvement.md` → `improve`. It requires `improve`, rerun as attempt 4, and
  `improve (Codex)`, which T12 runs after this commit. The package checks and
  unit tests passed on both Pythons; the references total 2,099 words. This is
  the second of the three skill fixes Failure triage allows in this task.
- `76d8e27` changed `references/improvement.md` a third time. "Before the first
  edit, record the baseline: run those tasks and measures on the current
  version, doing a task yourself if no fresh evaluator is left." The removal
  examples now say "generic exhortation or advice", and the comparison says
  "Rerun the baseline on the result and compare", which keeps the meaning in
  fewer words. This followed `improve` attempt 4. Selection-table row: one
  reference, `improvement.md` → `improve`. It requires `improve`, rerun as
  attempt 5, and `improve (Codex)`, which T12 runs after this commit. The
  package checks and unit tests passed on both Pythons, and the references
  total 2,100 words, the cap. This is the last of the three skill fixes Failure
  triage allows in this task.
- `9230073` changed `references/improvement.md` a fourth time, beyond the cap,
  because the person chose one more fix ("나로 해봐", 2026-11-06). "Before the
  first edit, write down the criteria and baseline: run each task and measure
  on the current version, yourself if no fresh evaluator is left; written
  later, they are hindsight." This followed `improve` attempt 5, whose
  transcript shows neither the criteria nor a review of the sample before the
  first edit. To stay within the 2,100-word cap, "easier to follow" became
  "clearer", and "when it is a judgment call that materially affects users"
  became "when a judgment call materially affects users". Selection-table row:
  one reference, `improvement.md` → `improve`. It requires `improve`, rerun as
  attempt 6, and `improve (Codex)`, which T12 runs after this commit. The
  package checks and unit tests passed on both Pythons, and the references
  total 2,100 words.

### Limits

- An evaluator's shell starts in the coordinator's checkout, so a relative read
  with no forbidden string or recursive search would not show in the audit.
- Evaluators and trial users are agents, so a trial shows use by a fresh agent,
  not by a person.
- `~/.claude/CLAUDE.md` changed on 2026-11-06, after the 0.10.0 baselines, and
  sends every evaluator to the user wiki; the runs read two to four of its
  pages, about 1,350 words for four, so token comparisons with those baselines
  include this change.
- Evaluators write no text between tool calls, and their thinking is
  redacted, so a criterion judged by order counts only what a call shows.
  `improve` attempts 2 to 5 may have walked through the sample before their
  edits without writing it down.

## 2026-11-06 control (1.0.0)

- Date: 2026-11-06. macOS 27.0.1 (26A434), Python 3.13.16; `/usr/bin/python3` is
  3.9.6.
- `shasum -a 256 ~/.claude/CLAUDE.md`:
  `bdeb943b66445a9e4c5532dd0f362847f18560adfa763ee8420123a9af2a6df3`.
- `git -C ~/.claude/user-wiki rev-parse --short HEAD`: `f262154`.
- Each run used a new `--control` workspace, which holds no skill and whose
  `requests.md` begins "Do not use any Loopy skill.", with its `prompt.md` as
  the whole prompt and a fresh `general-purpose` subagent with
  `model: "opus"` and `effort: "xhigh"`, one run at a time. Criteria were
  judged as in the cases entry, and the trials used the same prompts.

### guide (control)

- Slot `guide (control)`, run commit `2f10c46`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 81,995, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 25 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh reader of a copy of the task. `git status --short` was
  empty after the run. The nested agent wrote and deleted a temporary file in
  the session scratchpad, which Judging excludes.
- The evaluator changed only `README.md`; `parcel.py` and both notes equal the
  fixture byte for byte.
- `guide#1` passed: the README says "Open a terminal in this folder, the one
  that contains `parcel.py`", names Python 3.9 or later with nothing to
  install, gives `python3 parcel.py notes --output notes.json`, and shows the
  printed line and the exact `notes.json` to compare with.
- `guide#2` passed: in a clean copy, that command printed
  `Packed 2 notes into notes.json` and wrote a `notes.json` that equals the
  README's JSON block byte for byte and holds both notes.
- `guide#3` passed: the README says "Parcel does not overwrite an existing
  file" and shows the refusal; a second run in the clean copy exited 2 with
  those two lines and left the file unchanged, and `--replace` is named as the
  way to overwrite.
- `guide#4` passed. Use: in the coordinator trial below, a fresh user packed
  and checked the samples on the first try. Record: `run.md` reports a
  fresh-context check by one subagent, and the transcript holds that Agent call
  and its nested transcript.
- The README's other claims held in the clean copy: both wrong-folder errors,
  `Packed 0 notes` for a folder without `.txt` files, created output folders,
  and a `UnicodeDecodeError` with nothing written.
- Coordinator trial: 60,470 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 7 tool calls, no nested
  transcript. The trial user guessed whether "exactly" includes the final line
  break, how to check the Python version, and how to open the file; none of
  these stopped it.
- Loopy-only criteria: none.

### review (control)

- Slot `review (control)`, run commit `d53d1f7`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 68,711, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 9 tool calls;
  no Agent call. `git status --short` was empty after the run.
- `review#1` passed: the reply names "게시 담당자와 방법이 없습니다 (6행)" and
  "명령 확인이 게시 뒤에 있습니다 (7행)", with the completion rule that ignores
  the check, the missing handoff, and Jae's missing environment.
- `review#2` passed: the proposals are marked "파일에는 반영하지 않은 제안",
  and the example plan keeps Mina and Jae in the roles the plan gives them and
  leaves `<owner>` and `<decider>` blank; nothing claims the user's
  authorization.
- `review#3` passed: `plan.md` equals the fixture byte for byte, and the only
  file the evaluator wrote was `run.md`.
- Loopy-only criteria: none.

### ready (control)

- Slot `ready (control)`, run commit `cee1fa8`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 71,974, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 11 tool calls;
  no Agent call. `git status --short` was empty after the run.
- `ready#1` passed: the evaluator's check script ran an existing empty folder
  and got `0` with exit 0, and a missing folder with exit 2, on Python 3.9.6,
  3.12.15, 3.13.16, and 3.14.9; in a clean copy, an empty folder printed `0`
  and exited 0.
- `ready#2` passed: `README.md`, `count.py`, and the note equal the fixture
  byte for byte, and the reply says "이전 리뷰의 "0이면 실패이니 재시도 안내"
  의견은 반영하지 않았습니다" because `0` ends with exit 0 and nothing on
  stderr.
- `ready#3` passed: the evaluator made no edit and started no reviewer, and
  stopped after its checks; besides `run.md` it wrote only `scratch/check.sh`,
  in the workspace outside the task.
- Loopy-only criteria: none.

### refactor (control)

- Slot `refactor (control)`, run commit `814c3df`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 120,260, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 35 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a read-only reviewer of the task. `git status --short` was empty
  after the run.
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
  total calculation are gone; one `build_report` makes the totals for both
  outputs.
- `refactor#4` passed: a row with amount `abc` now exits 2 with
  `line 3: amount is not a number: 'abc'` and writes no JSON, and an empty
  amount likewise, where the original exited 0 and skipped the row.
  `test_rejects_bad_row` fails on the original code (7 failures with
  `test_rejects_malformed_csv`) and passes on the new, and `run.md` and the
  reply report the fixes under their own heading.
- `refactor#5` passed: the six tests cover the text totals, the JSON file in a
  new folder, the existing-output refusal, and the header, row, and CSV
  rejections; `test_prints_total_line` is gone.
- `refactor#6` failed: source lines went 125 → 95 with plain names such as
  `build_report` and `parse_row`, and the bug-fix table names the additions,
  but neither `run.md` nor the reply gives the change in lines for source,
  tests (61 → 88), or docs.
- `refactor#7` passed: all three modules and the test file changed for findings
  `run.md` names, and the README changed for the field-count rule.
- The evaluator also rejects rows without exactly three fields, `NaN`,
  infinite, and `sNaN` amounts, and malformed CSV, which the original skipped,
  miscounted, printed, or crashed on, and added the field-count rule to the
  README's rejection sentence; it reports these as fixes.
- Loopy-only criteria: `refactor#6`.

### fix (control)

- Slot `fix (control)`, run commit `5ec091c`, attempt 1. Claude Code 2.1.317,
  effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 70,695, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 16 tool calls;
  no Agent call. `git status --short` was empty after the run.
- `fix#1` failed: by `audit.py --calls`, line 42 printed `deploy -21:00` and
  `total 9:00` before the first edit to `entries.py` at line 61, but no call
  before that edit isolates the `23:30-00:30` entry or its duration, and the
  run's only text comes after the fix. The trace to that entry appears only in
  the report.
- `fix#2` passed: the change is `(end - start) % (24 * 60)` where
  `read_entries` stores the duration; the sample prints `build 22:30`,
  `review 7:30`, `deploy 3:00`, and `total 33:00`;
  `test_counts_entry_past_midnight` fails on the fixture's code and passes on
  the new.
- `fix#3` passed: only the duration line in `entries.py` and the added test
  differ from the fixture; `to_minutes`, its `None` check, `worklog.py`,
  `report.py`, the README, and the log are byte for byte unchanged, and the
  three existing tests are untouched.
- `fix#4` passed: the three existing tests pass on the new code, and in a clean
  copy a malformed and an out-of-range time each exit 2 with `line 1`.
- `fix#5` passed: the reply gives the cause as −23 hours (33 − 24 = 9), the
  fix, and the new test failing on a copy of the old code; it reports the
  missing `python` command apart from the fix and changes nothing else.
- Loopy-only criteria: `fix#1`.

### cause (control)

- Slot `cause (control)`, run commit `b34ec92`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 69,211, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 16 tool calls;
  no Agent call. `git status --short` was empty after the run.
- `cause#1` passed: by `audit.py --calls`, line 42 printed `gadget -4` and
  `total 11`; the text at line 45 names `moves.py` line 22, "which subtracts
  `return` like `out`, while the README says returns go back into stock"; the
  new test failed at line 69 with `gadget -2`, as that claim predicts, before
  the only code edit, at line 71. An earlier edit of `moves.py`, at line 46,
  was refused because the file had not been read, and changed nothing.
- `cause#2` passed: `moves.py` now negates only `out` (`if kind == "out":`);
  the sample prints `widget 9`, `gadget 0`, `bolt 6`, and `total 15`. The
  run's edits are the added test and that line, and none adds or removes a
  clamp.
- `cause#3` passed: `test_returns_go_back_into_stock` (`in 3`, `out 3`,
  `return 2` giving `gadget 2`) fails on the fixture's code and passes on the
  new. On a copy of the fixture that clamps stock at zero, the sample prints
  the right totals but this test fails.
- `cause#4` passed: only that line of `moves.py` and the added test differ from
  the fixture; `stock.py`, `report.py`, the README, and the log are byte for
  byte unchanged, and the three existing tests are untouched and pass.
- `cause#5` passed: the reply says returns were subtracted like shipments, so
  gadget came to 3-3-2-2=-4 instead of 0 and the total was 4 too low; that only
  `out` is subtracted now; and that the new test failed before the fix and all
  four pass after. It leaves negative stock from over-shipping as a question
  instead of clamping.
- Loopy-only criteria: none.

### diagnose (control)

- Slot `diagnose (control)`, run commit `59ba71a`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 67,044, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 8 tool calls;
  no Agent call. `git status --short` was empty after the run.
- `diagnose#1` passed: line 44 printed `members 7`, and the reply says 5
  people signed up, with Ann Lee and Bo Kim each counted twice for addresses
  that differ in letter case.
- `diagnose#2` passed: the claim is that `normalize` lowercases only the
  domain; line 44 printed the keys, such as
  `'Ann@Example.com' -> 'Ann@example.com'`, seven distinct, and five when the
  whole address is lowercased, without writing in `tasks/`.
- `diagnose#3` passed: the reply says `strip()` already handles the spaces
  around Cy Park's address and that the CSV itself is fine, and offers no other
  cause.
- `diagnose#4` passed: `diff -r` finds the task directory identical to the
  fixture, with no new file; the reply applies no fix.
- `diagnose#5` passed: the reply gives `members.py`, `normalize`, lines 34–36,
  the keys as evidence, and 5 + 2 = 7.
- Loopy-only criteria: none.

### feature (control)

- Slot `feature (control)`, run commit `4783c5c`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 91,960, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 18 tool
  calls; no Agent call. `git status --short` was empty after the run.
- `feature#1` passed: in a fresh copy, `--month 2026-01` prints `food 12.50`,
  `rent 500.00`, and `total 512.50`, and writes the same totals with `--json`.
  Without it, the sample's text and JSON are unchanged, and error runs differ
  only in the usage line, which now lists `[--month YYYY-MM]`. The fixture's
  tests pass on the new code, and the four new tests, which fail on the
  original code, cover the filter.
- `feature#2` passed: `parse_month` in `cli.py` is the option's `type`, and
  `2026-13`, `2026-00`, `26-01`, `abc`, an empty value, `2026-01-05`, and
  ` 2026-01` each exit 2 with no output or JSON. `2026-1` is accepted as
  January, which `run.md` records as a decision and the README does not rule
  out.
- `feature#3` passed: no docstring, comment, broad handler, fallback, unused
  option, or wrapper was added; `parse_month` turns `strptime`'s `ValueError`
  into the option's error.
- `feature#4` passed: the diff is the option, the month filter in
  `read_records` with its date check, four tests, and the README's command and
  two paragraphs; no existing line was rewritten except the `read_records` call
  and signature and the README's rejection sentence.
- `feature#5` passed: the README adds the `--month 2026-01` command, "With
  `--month YYYY-MM`, it sums only the rows dated in that month", the
  `total 0.00` of an empty month, and the rejections, which a clean copy
  confirms: `2026-02-30` under `--month` exits 2 with `line 3` and no JSON.
- Loopy-only criteria: none.

### docs (control)

- Slot `docs (control)`, run commit `7978c95`, attempt 1. Claude Code 2.1.317,
  effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 90,300, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 25 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a read-only reviewer of the result. `git status --short` was
  empty after the run.
- `docs#1` passed: the README gives Python 3.9 or newer with nothing to install
  and the sample command, and links to `docs/usage.md`, which gives the
  `--json` command, alphabetical order and two decimals, the JSON shape, the
  refusal to replace, the exact header, the category comparison, decimal
  amounts, the byte order mark, and exit status 2 with the line.
- `docs#2` passed: `run.md` sets `cli.py:15-16` against the FAQ's overwrite
  claim, the evaluator's check script ran `--json` to an existing path (exit
  2, file unchanged), the FAQ now says "Ledger stops with an error and leaves
  the file unchanged", and the reply reports it as "사실 오류 수정", apart from
  the structure.
- `docs#3` passed: the `docs/output.md` link is gone, and all six local links
  resolve.
- `docs#4` failed: the FAQ keeps three entries that restate rules
  `docs/usage.md` owns, each with a link: the category comparison nearly word
  for word, the refusal to replace, and the amount error. `run.md` keeps the
  page because "파일 삭제는 되돌릴 수 없고". The sample command also appears in
  both the README and `docs/usage.md`.
- `docs#5` passed: `cli.py`, `records.py`, `report.py`, and the sample equal the
  fixture byte for byte, and `docs/usage.md` is still at the path the epilog
  names.
- `docs#6` failed: documentation lines went 94 → 104 (README 34 → 32, FAQ
  23 → 16, usage 37 → 56), and neither `run.md` nor the reply gives a line
  change; both name the factual fix.
- `docs#7` passed: in a fresh copy, the README command prints exactly its text
  block, and the `--json` command exits 0 and writes a file equal to the JSON
  block in `docs/usage.md`.
- Loopy-only criteria: `docs#4`, `docs#6`.

### improve (control)

- Slot `improve (control)`, run commit `93ab4dc`, attempt 1. Claude Code
  2.1.317, effort `xhigh`, model `claude-opus-5-5`.
- Tokens: 77,133, the host's report, equal to the transcript's last usage.
- Isolation audit (with `--allow .claude/user-wiki`): exit 0 over 16 tool
  calls in the evaluator's transcript and the nested transcript of its one
  Agent call, a fresh agent given only the revised prompt, the sample, and the
  two tool signatures. `git status --short` was empty after the run.
- The evaluator changed only `review-bot.md`; both notes and the sample equal
  the fixture byte for byte.
- `improve#1` failed: before the first write to `review-bot.md`, at line 43,
  the calls are reads and a copy of the original with `wc -w -l`; no call
  states criteria, and no review of `samples/pr-42.diff` under the original
  prompt appears anywhere in the run.
- `improve#2` passed: "Rules" and "Steps" keep never approve or merge, changed
  lines only, the exact format with `blocker`, `major`, and `minor`, skipping
  `gen/` and lockfiles, the author's language with English when unsure, at
  most 10 comments with blockers first, and `request_changes` on a blocker.
- `improve#3` failed: the history and the repeated exhortations are gone, but
  "Good code is readable, maintainable" survives as a review target, "code
  that is hard to read or maintain", which `run.md` lists as kept, and the
  role now asks for "clear, respectful comments".
- `improve#4` passed: the `ircbot` step is gone because the tool was removed in
  March 2026 (`notes/tools.md`); the style rule went and the formatting rule
  stayed, now naming spacing, quotes, and line length; the forced praise went
  because the feedback calls it noise.
- `improve#5` failed: the prompt shrank 405 → 230 words, 43.2% by
  `len(text.split())`, and `run.md` and the reply give the counts, but one
  "Removed" list mixes the history and filler with the style rule, the praise,
  and the `ircbot` step, and names nothing lost.
- `improve#6` passed. Use: in the coordinator trial, the bot posted one Korean
  `[blocker] app/history.py:5` comment in the required form on the off-by-one,
  called `request_changes`, and skipped the quote change and `gen/schema.py`,
  with no `ircbot` call and no approval. The notes and the sample equal the
  fixture in the workspace and in the trial copy.
- Coordinator trial: 59,593 tokens, Claude Code 2.1.317, effort `xhigh`, model
  `claude-opus-5-5`; isolation audit exit 0 over 4 tool calls, no nested
  transcript.
- Loopy-only criteria: `improve#1`, `improve#3`, `improve#5`.

### Comparison

| Case | 1.0.0 tokens | 1.0.0 attempts | Control tokens | Control attempts | Criteria passed (1.0.0, control) | Loopy-only criteria |
| --- | --- | --- | --- | --- | --- | --- |
| guide | 89,531 | 1 | 81,995 | 1 | 4/4, 4/4 | none |
| review | 76,798 | 2 (1 invalid) | 68,711 | 1 | 3/3, 3/3 | none |
| ready | 83,796 | 1 | 71,974 | 1 | 3/3, 3/3 | none |
| refactor | 117,548 | 1 | 120,260 | 1 | 7/7, 6/7 | `refactor#6` |
| fix | 78,578 | 1 | 70,695 | 1 | 5/5, 4/5 | `fix#1` |
| cause | 74,896 | 1 | 69,211 | 1 | 5/5, 5/5 | none |
| diagnose | 75,522 | 1 | 67,044 | 1 | 5/5, 5/5 | none |
| feature | 106,516 | 1 | 91,960 | 1 | 5/5, 5/5 | none |
| docs | 98,859 | 1 | 90,300 | 1 | 7/7, 5/7 | `docs#4`, `docs#6` |
| improve | 96,438 | 6 (1 stopped, 4 failed) | 77,133 | 1 | 6/6, 3/6 | `improve#1`, `improve#3`, `improve#5` |
| Total | 898,482 | 16 | 809,283 | 10 | 50/50, 43/50 | 7 in 4 cases |

- Tokens are each slot's last judged run, the host's report. The coordinator
  trials are apart: `guide` 61,258 with the skill and 60,470 without,
  `improve` 60,690 and 59,593.
- With the skill, the last judged runs used 89,199 more tokens, 11.0% above
  the control; only `refactor` used fewer, by 2,712.
- The seven Loopy-only criteria fall in three groups: what the report gives,
  the line change or each behavior change with its loss (`refactor#6`,
  `docs#6`, `improve#5`; in `docs` the lines also rose); evidence written
  before the first edit (`fix#1`, `improve#1`); and removing repetition or
  generic advice (`docs#4`, `improve#3`). `guide`, `review`, `ready`, `cause`,
  `diagnose`, and `feature` have none, and their Baselines rows say
  "regression only".

### Control limits

- Control evaluators ran in this Claude Code session, whose skill list still
  names the installed Loopy plugin. `requests.md` told them not to use any
  Loopy skill, and no subagent transcript in this session holds a Skill call.
- The comparison uses the ten cases the skill was tuned on, so it may
  overstate the skill's effect on new tasks.
- Each slot ran once. A criterion judged by what a call shows before the
  first edit, such as `fix#1` or `improve#1`, can turn on whether an agent
  writes its reasoning down.
- The coordinator judged both runs of each case and knew which was the
  control.
- The cases entry's limits on relative reads, agent trial users, and the
  global instructions apply here too.

## 2026-11-06 Codex (1.0.0)

- Date: 2026-11-06. macOS 27.0.1 (26A434), Python 3.13.16; `/usr/bin/python3` is
  3.9.6.
- `shasum -a 256 ~/.claude/CLAUDE.md`:
  `bdeb943b66445a9e4c5532dd0f362847f18560adfa763ee8420123a9af2a6df3`. Codex
  reads `~/.codex/AGENTS.md` instead, which points to the same wiki;
  `shasum -a 256 ~/.codex/AGENTS.md`:
  `8cb3374520aa3cb85effc214d7cdb8c407846234563508fb0d0b15aa6ca3a3c9`.
- `git -C ~/.claude/user-wiki rev-parse --short HEAD`: `f262154`.
- `codex --version`: `codex-cli 0.166.0`. The JSONL reports no model, so the
  model is the `model` and `model_reasoning_effort` in `~/.codex/config.toml`
  at run time: `gpt-6.1-sol`, `medium`.
- The person agreed on 2026-11-06 ("승인 (Recommended)") to a temporary
  marketplace and plugin in `~/.codex/config.toml` and to six or more Codex
  runs on their ChatGPT usage. Before the install, `~/.codex/config.toml` was
  copied to a git-ignored folder under `docs/`.
- Every `codex exec` ran with standard input from `/dev/null`, so only the
  prompt reached it.

### Selection smoke

- Attempt 1 did not run: Codex replied "You've hit your usage limit" and "try
  again at 7:41 PM" before any model turn, with no usage object. The temporary
  install was removed during the wait, `diff` against the saved config printed
  nothing, and the install was made again after 19:41.
- Attempt 2, run commit `ba4d753`: `codex plugin list` showed
  `loopy@loopy-dev  installed, enabled  1.0.0`, installed at
  `~/.codex/plugins/cache/loopy-dev/loopy/1.0.0`. The `fix-amount` request, run
  with `-s read-only` on a copy of `fixtures/refactor` outside the repository,
  produced this command event, the run's second command:
  `/bin/zsh -lc 'cat /Users/kn/.codex/plugins/cache/loopy-dev/loopy/1.0.0/skills/loopy/SKILL.md'`.
  It then read `references/debug.md` and `references/code.md` from the same
  folder. Tokens: 144,422 (input 142,062 and output 2,360; the usage object
  also reports 129,536 cached input and 230 reasoning output tokens).
- Right after, `codex plugin remove loopy@loopy-dev` and
  `codex plugin marketplace remove loopy-dev` ran, the temporary folders and
  the empty `~/.codex/plugins/cache/loopy-dev` were deleted, and `diff` between
  the saved copy and `~/.codex/config.toml` printed nothing.

### review (Codex)

- Slot `review (Codex)`, run commit `126e708`, attempt 1. Codex CLI 0.166.0,
  model `gpt-6.1-sol` with `medium` effort from `~/.codex/config.toml`; the
  JSONL reports no model.
- Tokens: 142,502 (input 140,090 and output 2,412; the usage object also
  reports 123,008 cached input and 140 reasoning output tokens).
- Isolation: `grep -c -F -f <tmp>/forbidden.txt <ws>.jsonl` printed 0 over 5
  commands and one file change. The run read the wiki's `index.md`,
  `workflow.md`, and `docs.md`, then `requests.md`, `skill/SKILL.md`, and the
  plan; it started no subagent. `git status --short` was empty after the run.
- `review#1` passed: "게시 담당자와 게시 대상·방법이 없음 (`plan.md:3–6`) …
  금요일 게시 주체는 없다" and "검증 전에 게시되고, 실패해도 완료로 처리될 수
  있음 (`plan.md:6–9`)", with the missing failure path and schedule.
- `review#2` passed: each finding states the plan's current lines, then what
  to add ("…명시해야 한다"); no owner is named for the gaps, and the report
  says "검토 완료가 배포 승인이나 계획의 실행 가능 판정을 뜻하지 않는다".
- `review#3` passed: `plan.md` equals the fixture byte for byte, and the only
  file the run wrote was `run.md`, besides the `final.md` that `-o` writes.

### refactor (Codex)

- Slot `refactor (Codex)`, run commit `3330f5a`, attempt 1. Codex CLI 0.166.0,
  model `gpt-6.1-sol` with `medium` effort from `~/.codex/config.toml`; the
  JSONL reports no model.
- Tokens: 628,176 (input 618,750 and output 9,426; the usage object also
  reports 587,264 cached input and 1,683 reasoning output tokens).
- Isolation: `grep -c -F -f <tmp>/forbidden.txt <ws>.jsonl` printed 0 over 17
  commands and one file change. The run read the wiki's `index.md`,
  `workflow.md`, `code.md`, and `docs.md`, the skill with four references, and
  the task. `git status --short` was empty after the run. `run.md` reports one
  fresh subagent that followed the README on a copy and left its results in
  `scratch/trial-use/`; the JSONL holds no event for it, so its reads were not
  audited. The fixture's tests made and removed temporary folders under
  `$TMPDIR`, as in the Claude Code runs, and `run.md` says so.
- `refactor#1` passed: in fresh copies of the fixture and the result, the
  sample's text, the JSON run and file bytes, the existing-output refusal, the
  wrong-header rejection, `--help`, a missing source, and a CSV without a BOM
  gave the same output and exit status.
- `refactor#2` passed: `records.py` keeps "Bank exports may start with a byte
  order mark." over `encoding="utf-8-sig"`; `cli.py` still checks the source
  and the existing output, and `read_records` still checks the header.
- `refactor#3` failed: no file-top docstring is left, the `--help` text is the
  `description` argument, and the restating comments, commented-out code,
  `format_amount_old`, the `os` and `sys` imports, `DEBUG`, `load`, the `sort`
  option, the `None` guard, and the second category normalization are gone, and
  one `sum_categories` makes the category totals for both outputs. But
  `format_text` and `write_json` each still compute
  `sum(totals.values(), Decimal('0'))`, the fixture's two lines unchanged;
  `run.md` names only the category sums as the removed duplicate. The Claude
  Code skill and control runs computed that total once.
- `refactor#4` passed: a row with amount `oops` or an empty amount now exits 2
  with `line 3: amount must be a number` and writes no JSON, where the original
  exited 0 and skipped it. The new tests fail 8 times on the original code and
  pass on the new, and `run.md` reports the fix under its own heading, apart
  from the structural changes.
- `refactor#5` passed: the six tests cover the text totals, the JSON file, the
  existing-output refusal, and the header and amount rejections;
  `test_prints_total_line` is gone.
- `refactor#6` passed: source lines 125 → 85 with plain names such as
  `sum_categories` and `format_text`; `run.md` gives "합계 125→85 (40줄 감소).
  테스트 61→84 (23줄 증가), README 23→23 (변경 없음)" and names the bug-fix
  additions.
- `refactor#7` passed: `run.md` assesses all three modules, the tests, the
  README, the sample, and the dependencies, and changed each module and the
  tests for the findings it names.
- The run also writes the JSON with mode `x`, so a file created after the first
  check is refused, and rejects `NaN` and infinite amounts; it reports both as
  fixes.
- Failure triage for `refactor#3`: a host difference, not skill wording.
  `references/refactoring.md` already says to remove "duplicated knowledge
  with the same reason to change", and this run applied it to the category
  sums and the normalization; with the same text, the Claude Code run removed
  the duplicated total, and so did the control run without the skill. The text
  is unchanged, so the slot was not rerun.

### fix (Codex)

- Slot `fix (Codex)`, run commit `fb79bc6`, attempt 1. Codex CLI 0.166.0,
  model `gpt-6.1-sol` with `medium` effort from `~/.codex/config.toml`; the
  JSONL reports no model.
- Tokens: 226,534 (input 223,308 and output 3,226; the usage object also
  reports 192,768 cached input and 207 reasoning output tokens).
- Isolation: `grep -c -F -f <tmp>/forbidden.txt <ws>.jsonl` printed 0 over 15
  commands and three file changes; no subagent. `git status --short` was empty
  after the run. The tests ran with `TMPDIR` set to a folder in the workspace.
- `fix#1` passed: by the JSONL event order, event 24 printed `deploy -21:00`
  and `total 9:00`, event 26 printed the parsed `[('deploy', -1380)]`, event 33
  named `23:30-00:30` as the cause after the new tests failed at event 32, and
  the first edit to `entries.py` came at event 35.
- `fix#2` passed: the change adds `if end < start: end += 24 * 60` before
  `end - start` where `read_entries` stores the duration; the sample prints
  `build 22:30`, `review 7:30`, `deploy 3:00`, and `total 33:00`;
  `test_counts_overnight_entries` and `test_week_total_exceeds_24_hours` fail on
  the fixture's code and pass on the new.
- `fix#3` passed: only those two lines in `entries.py` and three added tests
  differ from the fixture; the third, `test_equal_times_count_as_zero`, pins
  the boundary of the new comparison. `to_minutes`, its `None` check,
  `worklog.py`, `report.py`, the README, and the log are byte for byte
  unchanged, and the three existing tests are untouched.
- `fix#4` passed: the three existing tests pass on the new code, covering task
  order, `H:MM`, ignored blank and comment lines, and exit 2 with the line
  number for malformed and out-of-range times.
- `fix#5` passed: `run.md` gives the cause with the −1380 minutes, the fix, and
  the new tests failing 2 of 6 before the fix and passing after; the reply and
  `run.md` report the missing `python` command apart from the fix, and nothing
  else changed.

### feature (Codex)

- Slot `feature (Codex)`, run commit `d6693db`, attempt 1. Codex CLI 0.166.0,
  model `gpt-6.1-sol` with `medium` effort from `~/.codex/config.toml`; the
  JSONL reports no model.
- Tokens: 257,686 (input 253,119 and output 4,567; the usage object also
  reports 220,672 cached input and 781 reasoning output tokens).
- Isolation: `grep -c -F -f <tmp>/forbidden.txt <ws>.jsonl` printed 0 over 17
  commands and two file changes, among them `rg --files` over the wiki's
  `graph` folder; no subagent. `git status --short` was empty after the run.
- `feature#1` passed: in a fresh copy, `--month 2026-01` prints `food 12.50`,
  `rent 500.00`, and `total 512.50`, and writes the same totals with `--json`.
  Without it, the sample's text and JSON are unchanged, and error runs differ
  only in the usage line, which now lists `[--month YYYY-MM]`. The fixture's
  tests pass on the new code, and `test_filters_month_in_text_and_json` covers
  the filter; the new tests fail 8 times on the original code.
- `feature#2` passed: `parse_month` in `cli.py` is the option's `type`, and
  `2026-1`, `2026-13`, `2026-00`, `26-01`, `abc`, an empty value,
  `2026-01-05`, and ` 2026-01` each exit 2 with no output or JSON.
- `feature#3` passed: no docstring, comment, broad handler, fallback, or
  wrapper was added; `parse_month` holds the check and catches only
  `ValueError`.
- `feature#4` passed: the diff is the `date` import, `parse_month`, the option,
  the two-line filter in `main`, three tests, and the README lines; no existing
  line was rewritten.
- `feature#5` passed: the README adds the `--month 2026-01` command and says
  the option sums "only records from the specified year and month", with the
  January totals, the `--json` behavior, `total 0.00` when nothing matches,
  and "An invalid month (such as `2026-13` or `2026-1`) is rejected with
  status 2."; each claim matched a run in the fresh copy.

### improve (Codex)

- Slot `improve (Codex)`, run commit `91a4456`, attempt 1. Codex CLI 0.166.0,
  model `gpt-6.1-sol` with `medium` effort from `~/.codex/config.toml`; the
  JSONL reports no model.
- Tokens: 494,087 (input 484,375 and output 9,712; the usage object also
  reports 466,048 cached input and 1,649 reasoning output tokens).
- Isolation: `grep -c -F -f <tmp>/forbidden.txt <ws>.jsonl` printed 0 over 19
  commands and 7 file changes. `git status --short` was empty after the run.
  `run.md` reports one fresh subagent that reviewed three pull requests from
  copies in `scratch/trial/`; the JSONL holds no event for it, so its reads
  were not audited.
- The run changed only `review-bot.md`; both notes and the sample equal the
  fixture byte for byte. Outside the task it wrote `scratch/`: a copy of the
  original, the trial inputs and result, and `verify_trial.py`.
- `improve#1` failed, as not shown. Before the first edit of `review-bot.md`
  at event 35, the events show the word count (event 26, `63 405 2383`), a
  message naming the formatting conflict, the forced praise, and the `ircbot`
  call to remove and the rules to keep (event 29), a copy of the original
  (event 31), and the creation of `run.md` (event 33). Codex's file-change
  events carry a path but no content, so what `run.md` held at event 33 is not
  in the record. Its final text has "편집 전 계약과 기준" and "편집 전 관측"
  sections with tasks for `pr-42` and a walkthrough of the sample under the
  original prompt, but nothing dates them, and Judging takes the order from the
  events, not from `run.md`.
- `improve#2` passed: the three sections keep never approve or merge, changed
  lines only, the exact format with `blocker`, `major`, and `minor`, skipping
  `gen/` and lockfiles, "Write in the language of the author's PR description;
  use English if unsure.", at most 10 comments keeping the most severe with
  blockers first, and `request_changes` on a blocker.
- `improve#3` passed: the history, the exhortation paragraphs, the closing
  "Remember" line, and "Good code is readable, maintainable, and correct" are
  gone; one opening line keeps "useful, respectful feedback on correctness,
  security, readability, and maintainability".
- `improve#4` passed: the `ircbot` step is gone because `notes/tools.md` says
  the tool was removed; the always-comment-on-style sentence went and the
  formatting rule stayed, naming spacing, quotes, and line length, "the linter
  handles it"; the forced praise went because the feedback calls it noise.
- `improve#5` passed: `run.md` lists the wording cuts apart from three behavior
  changes, each with what is lost, such as "잃는 동작은 불필요한 서식 댓글이다";
  it and the reply give 405 → 184 words, 54.6% fewer by `len(text.split())`.
- `improve#6` passed. Use: in the coordinator trial, the bot posted one Korean
  `[blocker] app/history.py:5` comment in the required form on the slice that
  returns n+1 items and called `request_changes`, and skipped the quote change
  and `gen/schema.py`, with no `ircbot` call, no praise, and no approval. The
  notes and the sample equal the fixture in the workspace and in the trial
  copy.
- Coordinator trial, run as a Claude Code subagent as Codex runs require:
  59,551 tokens, the host's report, equal to the transcript's last usage;
  Claude Code 2.1.317, effort `xhigh`, model `claude-opus-5-5`; isolation
  audit exit 0 over 3 tool calls, no nested transcript.
- Failure triage for `improve#1`: a host difference in what the record shows,
  not skill wording. The run wrote `run.md` before its first edit, as
  `references/improvement.md` asks, but Codex's events do not record what a
  patch writes, where a Claude Code `Write` call does. The text is unchanged,
  so the slot was not rerun.

### Codex summary

- `review`, `fix`, and `feature` passed every criterion in Codex.
  `refactor (Codex)` failed `refactor#3` and `improve (Codex)` failed
  `improve#1`; Failure triage gives both a host difference, not skill wording,
  so the skill was not changed and neither slot was rerun. All five slots
  passing every criterion, the Codex check's completion condition, is not met,
  and the person decides how to proceed.
- Tokens over the five runs: 1,748,985, besides 144,422 for the selection
  smoke; they are not compared with the Claude Code total.

### Codex limits

- `codex exec --json` emits no event for a subagent. `refactor` and `improve`
  each report one in `run.md`, with results in `scratch/`, but its commands
  were not audited.
- File-change events carry a path and a kind but no content, so a criterion
  judged by what the record shows before the first edit can be shown in Claude
  Code, whose `Write` calls hold the text, and not in Codex (`improve#1`).
- The isolation check is a fixed-string search over the events, so a read
  that names none of the strings goes unseen, and `--ephemeral` keeps no
  session file to compare.
- Each slot ran once, with the model and effort in the person's Codex config
  (`gpt-6.1-sol`, `medium`), not the `xhigh` effort of the Claude Code runs.

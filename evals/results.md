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
| fix | 1.0.0 | Passed | Reproduced `total 9:00` and the −1380-minute entry before editing; `total 33:00`; only the duration line and one test changed | 78,578 | pending | [cases](#2026-11-06-cases-100) |
| cause | 1.0.0 | Passed | Return sign fixed after the parsed moves showed `('gadget', -2)`; no clamp; the new test fails on the original and on a clamped copy | 74,896 | pending | [cases](#2026-11-06-cases-100) |
| diagnose | 1.0.0 | Passed | Cause confirmed from the normalized keys and the README's two-row example (`members 2`); expected 5; task files unchanged | 75,522 | pending | [cases](#2026-11-06-cases-100) |
| feature | 1.0.0 | Passed | January totals 512.50; output without `--month` unchanged; the month checked at the CLI and rows' dates checked only with `--month` | 106,516 | pending | [cases](#2026-11-06-cases-100) |
| docs | 1.0.0 | Passed | Documentation 94 → 75 lines in two files; the FAQ's overwrite claim corrected and the broken link removed; code unchanged | 98,859 | pending | [cases](#2026-11-06-cases-100) |
| improve | 1.0.0 | Failed | Attempt 5 failed only `improve#1`: its review of the sample under the original prompt was written down after the edits; every hard rule kept at 405 → 227 words (44.0%), and the trial bot posted the expected blocker | 94,737 | pending | [cases](#2026-11-06-cases-100) |

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
| improve | 89,918 | 94,737 | +4,819 |
| Total | 840,553 | 896,781 | +56,228 (+6.7%) |

- The 1.0.0 column is each slot's last judged run; failed, invalid, and stopped
  runs are recorded apart. The total is over R11's cap of 840,553.
- About 15,000 of the rise is the first turn's context, before any skill read:
  48,415–48,636 tokens in the 0.10.0 transcripts (Claude Code 2.1.308) and
  49,896–50,100 now (2.1.317), about 1,500 per run, from the host and the
  global instructions (see Limits).
- `feature` adds 21,387: its evaluator also checked each row's date when
  `--month` is given and fixed one bug of its own during the run. `code.md`
  keeps the 0.10.0 rule on validating input at trust boundaries.
- The other 19,841 is spread over the remaining cases, led by `ready`
  (+10,436) and `guide` (+8,753). Old runs of one case already differed by up
  to 5,084 tokens (`fix` 73,159–78,243; `guide` 81,599–86,314); `guide` is
  3,217 above its highest 0.10.0 run.
- The skill text is smaller than 0.10.0 (`SKILL.md` body 1,336 → 1,097 words;
  references 2,623 → 2,100), so the coordinator judged the rise not
  skill-caused. Failure triage sends such a rise to the person. On 2026-11-06,
  asked whether to accept it as environment-caused, the person answered "계속"
  ("continue"), which is recorded as acceptance.

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

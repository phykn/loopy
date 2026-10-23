# Evaluation records

## 2026-10-23 fix case (0.9.0)

The catalogue gains `fix`, a plain bug report on the Fix route. Since 0.9.0
selects Loopy for bug fixes much more often, this case checks what it then
does. The fixture is a work-log CLI. Its README says an entry whose end is
earlier than its start ran past midnight, but `entries.py` subtracts the times,
so the sample's `23:30-00:30` entry counts as minus 23 hours. The request
reports only the symptom: a total of 9:00 for about 33 hours of work. The trap
sits next to the bug: `to_minutes` returns `None` for an out-of-range time and
its caller checks for it. That is awkward but correct, and it is already
covered by the tests. The skill was unchanged, and the case ran once and
passed.

### Conditions and inputs

- Skill: 0.9.0 at commit `5b9f3cf`, prepared with
  `prepare.py --skill skills/loopy --case fix`.
- Environment: macOS, Claude Code 2.1.302, Opus 5.5, Python 3.13.16. The
  coordinator also ran the delivered tests on Python 3.9.6.
- One fresh Claude Code `general-purpose` subagent ran in its own workspace. Its
  prompt matched the 0.9.0 cases: apply the supplied skill rather than the
  installed one, work only in the workspace, delegate at most one bounded
  fresh-context check, and record any question instead of asking. The user's
  global instructions were active, and the agent read the guidance wiki they
  point to.
- The case and fixture were written before the run, and the run did not change
  them.

| Input | SHA-256 |
| --- | --- |
| Case definitions | `64aac80704ae53ead01f617b735a0ad82fe7ff876af7abcba064686b80d795fe` |
| Fixture `fixtures/fix` (the sorted `shasum -a 256` listing of its files) | `59f99dc73f332c2ba3c7db717a795942da5e1e19097333d9e7c630a7e8d88514` |
| SKILL.md | `a8e413b0139485a5a3d7b1478aac5a2d21b0fd750343444ca3f6c6308ac38ec3` |
| code.md | `9baaad839d77c8a33c8520a5efec39eff97a3936ed76d74390661cc962d64b92` |

### Task outcome

The coordinator checked the agent's tool-call order in its transcript, compared
the result with the fixture byte for byte, and reran it from a clean copy.

| Criterion | Result |
| --- | --- |
| Reproduced first | Passed. The agent's first command, before any edit, printed `deploy -21:00` and `total 9:00`. Its contract traced these to `23:30-00:30` and the README's midnight rule. It then wrote the regression test and saw it fail before editing the code. |
| Cause fixed with a regression test | Passed. `entries.py` now computes `(end - start) % (24 * 60)`, with a one-line why-comment. The sample prints `build 22:30`, `review 7:30`, `deploy 3:00`, and `total 33:00`. The added `test_counts_entries_past_midnight` fails on the fixture's `entries.py` (`deploy -22:45`) and passes after the fix. |
| Unrelated code unchanged | Passed. Only `entries.py` (one line plus the comment) and the added test differ. `to_minutes`, the `None` check, `worklog.py`, `report.py`, the README, and the sample log are byte-for-byte unchanged, and the three existing tests are untouched. |
| README contract holds | Passed. All four tests pass on Python 3.13 and 3.9. A malformed line or an out-of-range time exits 2 and names line 2, a missing file exits 2, and comment and blank lines are still ignored. |
| Fix reported apart | Passed. The report gives the cause, the fix, the test, and the before and after output. Its only other note, that `python` is missing so `python3` was used, is set apart. |

The agent decided the narrow change did not need an independent use trial and
delegated nothing, as `SKILL.md` allows when direct evidence is adequate. Its
scratch file stayed in the workspace. The fixture's tests write temporary logs
to the system temp directory.

### Limits

- One run, so the result may be variance.
- The report did not mention the `None` return. The case therefore shows the
  trap left alone, but not how Loopy reports a smell it notices.
- The bug shows on the first run of the sample, and the README states the rule.
  The case checks the fix workflow, not hard diagnosis.
- The agent was told to apply Loopy, so this case does not measure selection;
  `activation.py` does.
- Codex, other models, and human use were not exercised.

## 2026-10-23 activation, goalless improve routing, and maintainer map (0.9.0)

0.9.0 changes four things:

- **Description.** It now names bug fixes and feature additions, says to use
  Loopy even when the fix looks small, and narrows the exclusion to edits the
  user dictates exactly. Under realistic settings it was selected for 60 of 60
  should-trigger runs, where 0.8.0 managed 34 of 60. Neither version was
  selected for any near miss.
- **Routing.** The Improve row now admits a request with or without a stated
  goal. Under 0.8.0's routing, a bare 개선해줘 matched no row.
- **Activation runner.** `evals/activation.py` keeps the realistic runner, and
  `evals/README.md` maps each changed file to its cases.
- **Shortening.** A pass on the runtime text kept only the cuts a fresh reviewer
  found lossless.

Runtime text excluding the frontmatter went from 3,450 to 3,401 words:
`SKILL.md` body 1,202, `code.md` 344, `improvement.md` 312,
`independent-use.md` 501, and `refactoring.md` 1,042. The description grew from
73 to 104 words. All seven cases ran on the final text. Six passed, and
`improve` missed only its size threshold.

### Conditions and inputs

- Baseline: 0.8.0 at commit `5b0d34f`, exported with `git archive`.
- Environment: macOS, Claude Code 2.1.302, Opus 5.5, Python 3.13.16. The helper
  tests and `check.py` also ran on Python 3.9.6.
- The user's global instructions and other plugins were active in every
  activation run and case. The global instructions point to a guidance wiki
  that agents read at the start of every task.
- Each case ran in its own `prepare.py --case` workspace with its own fresh
  Claude Code `general-purpose` subagent. Each subagent was told to apply the
  supplied skill rather than the installed one, to work only in its workspace,
  and to delegate at most one bounded fresh-context check. They were also told
  to record any question instead of asking, because no user was available.

| Input | SHA-256 |
| --- | --- |
| Case definitions | `547162a3fef86eacab71054fc5ed4d4cfc2e3a5e1e5977903c1bee95fc9feb36` |
| Activation queries | `bb147f5d532afe2650d3a4ea598752cec37127f262022ca916247b950f833fa7` |
| Final SKILL.md | `a8e413b0139485a5a3d7b1478aac5a2d21b0fd750343444ca3f6c6308ac38ec3` |
| Final code.md | `9baaad839d77c8a33c8520a5efec39eff97a3936ed76d74390661cc962d64b92` |
| Final improvement.md | `6b04c3d0aabf9d4664610c9546b2d7ee3942552ae223f2c7f0106c82ac4f24c8` |
| Final independent-use.md | `60b320eb7a9a4b34d2eed0834737e8f4b3979a620b005cb3a341cf43c9da493e` |
| Final refactoring.md | `dfea2aef3e5639849ceacde4d1d35542d0968bf8ecac57122240982d95455f1e` |

### Routing

Two fresh agents had only the routing section, one from 0.8.0 and one revised.
Each classified the same 14 requests. Under 0.8.0, four found no matching row
and would have asked:

- a bare 이 프로젝트 개선해줘;
- the improve half of 개선후 리팩토링 진행;
- 이 가이드 좀 더 낫게 만들어줘;
- 프롬프트 개선해줘. 규칙은 유지해, which has the same shape as the `improve`
  case.

Under the revised rules all four route to Improve, and the other ten classify
the same as before. Both agents noted that "remove unused options" could
arguably meet the Refactor test first, but both routed it to Build, so it was
left unchanged.

### Activation

The runner was a scratch copy of what is now `evals/activation.py`. Its project
copy also held a git repository. The two plugin copies differed only in the
description.

The query sets were fixed before the candidate was written: `tune` has 12
should-trigger queries and 8 near misses, and `holdout` has 8 and 6. After the
description was shaped, three near misses were added to `holdout`. These are
fixes the user dictates exactly, and they probe whether "even when the fix
looks small" over-triggers.

| Set | 0.8.0 should-trigger | 0.9.0 should-trigger | 0.8.0 near misses | 0.9.0 near misses |
| --- | --- | --- | --- | --- |
| `tune` | 26/36 | 36/36 | 0/24 | 0/24 |
| `holdout` | 8/24 | 24/24 | 0/18 | 0/18 |
| Dictated fixes | | | 0/9 | 0/9 |

0.8.0 missed most bug-fix and feature requests:

- `tune`: `fix-amount` 0/3, `add-month` 0/3, `json-average` 1/3, `en-fix` 2/3,
  `tidy` 2/3;
- `holdout`: `h-count`, `h-sort`, `h-en-since`, and `h-en-crash` 0/3 each,
  `h-fix-total` 1/3, `h-fix-blank` 2/3, `h-docs` 2/3.

In each missed run the agent read files and then edited without calling a
skill.

The first `add-month` runs passed the query as an argument, and `claude` parsed
its leading `--month` as an option. Those runs were discarded and rerun with the
query on stdin, which `activation.py` now does.

The 0.8.0 record's 30/30 came from a different runner and query set, with at
most six turns and 10 + 10 queries, so the two results are not comparable.

### Shortening

The first pass cut 3,450 words to 3,373. A fresh reviewer compared it with
0.8.0 and found one material loss: evaluation no longer explicitly barred
deployment, messages, and destructive operations. It also found six minor
narrowings:

- a fresh re-trial after a revision;
- the strongest authorized fallback check;
- when a helper or interface may be extracted;
- how supported interfaces are identified;
- existing organization as evidence;
- applying the question rules to ambiguous bugs.

All seven were restored. Five cuts it judged covered by `SKILL.md` remain. The
runtime text is close to its floor under the no-loss constraint, as in the 0.8.0
record.

### Task outcomes

The coordinator checked each result from a clean copy and compared protected
files byte for byte.

| Case | Result |
| --- | --- |
| `guide` | Passed. README 7 → 76 lines. The documented command printed the shown line and produced the shown JSON byte for byte. The refusal exits 2 and leaves the file unchanged, and `--replace` rebuilds. A fresh-user trial ran, and source and notes are unchanged. |
| `review` | Passed. Found that no one owns publication and that commands are checked only after the release counts as complete. The suggested revision uses placeholders instead of invented owners. The plan is unchanged. |
| `ready` | Passed without edits. The empty folder printed `0` with exit 0, and the retry suggestion was rejected. An unreadable folder also prints `0`; this was reported as an open question, not edited. |
| `refactor` | Passed. Text, JSON, refusal, wrong header, BOM input, and `--help` match the original. An invalid amount now exits 2 with its line number, writes no JSON, and has a regression test. The seeded excess was removed and the BOM why-comment kept. Source 125 → 78 lines, tests 61 → 66. |
| `feature` | Passed. January totals 512.50. Output without `--month` is unchanged. An invalid month exits 2 at the argparse boundary, and no comments were added. Source 81 → 91, tests 61 → 100. |
| `docs` | Passed. Documentation 94 → 60 lines. The FAQ and its wrong overwrite claim were removed and reported, and the broken link is gone. Every claim is reachable from the README, the commands produce the stated output, and the code is unchanged. |
| `improve` | Failed only the size criterion: 405 → 247 words is 39%, against 40%. Every other criterion was met. The hard rules kept their meaning, including the English fallback. `ircbot`, forced praise, and the formatting conflict were resolved from the notes, and each loss was reported. Under the revised prompt, a fresh agent produced one Korean `blocker` and `request_changes` on `pr-42.diff`, writing the tool calls out rather than running them. The baseline review under the original prompt was a walkthrough. |

`improvement.md` changed only "for a stated goal" to "toward a goal". The same
path passed at 229 and 240 words in 0.8.0 and failed at 36% once, so this miss
was recorded rather than rerun.

### Maintainer use

A fresh maintainer used a copy of the repository and followed it from the
README:

- found the cases and commands for a `code.md` change;
- described the activation measurement and what counts as a selection;
- ran `check.py`, the 17 tests, and `quick_validate.py`, all of which passed;
- confirmed that a `refactor` packet withholds every acceptance criterion.

Its friction was fixed in `evals/README.md`:

- where a `git archive` export puts the skill;
- that a change to the description alone runs activation instead of cases;
- naming `refactoring.md` in step 4;
- activation examples that skipped `--set` and wrote into the repository;
- no version-bump rule.

### Limits

- The cases ran once each on the final text, and activation ran three times per
  query, so small differences may be variance.
- Headless runs in a small project are not interactive sessions with long
  context.
- The catalogue has no case for a plain bug fix, so what Loopy does once
  selected for one is covered only inside `refactor`.
- Codex, other models, human use, and host installation were not exercised.

## 2026-10-23 improve mode, request routing, and activation (0.8.0)

0.8.0 adds an improve mode (`references/improvement.md`), routes requests by
five kinds told apart by what sets the target (review, refactor, fix, build,
improve), rewrites the activation description around those kinds with Korean
examples, and adds the `improve` case. Loopy's improve mode was then applied to
Loopy itself, with the goal from earlier feedback that the content is longer
than needed. Runtime text went from 4,216 words in 0.7.2, and 4,514 with the
new mode and routing, to 3,529: `SKILL.md` 1,276, `code.md` 352,
`improvement.md` 313, `independent-use.md` 529, and `refactoring.md` 1,059.
Every case passed on the texts it ran against; this is one run per case and
text.

### Conditions and inputs

- Baseline: 0.7.2 at commit `a6abafd`, exported with `git archive`.
- Environment as in the 0.7.2 record below: macOS, Python 3.13.16, one fresh
  Claude Code `general-purpose` subagent on Opus 5.5 per case and text, with
  the same prompt and permission to delegate fresh-context checks inside the
  workspace. Global instructions were present.
- The `improve` case and fixture were written before any skill edit in this
  change.
- Texts, in order:
  - 0.7.2 baseline.
  - Candidate: 0.7.2 plus improve mode, routing, and the new description
    (4,514 words).
  - Improved: the improve pass at 3,400 words, which met its own target of at
    most 3,400.
  - Restored: two fresh reviewers compared the improved text with the
    candidate. They found material losses, including:
    - the refactor finish no longer requiring the project's checks or Loopy's
      `done`;
    - project claims no longer checked against the project;
    - accepted findings no longer kept open;
    - trial-validity checks for knowledge the user lacks and when to state the
      purpose;
    - the evaluator no longer told not to modify the source;
    - safe reproduction and path casing.

    They also found that the new Build test misrouted "improve, but keep these
    rules" to Build. These were restored or fixed. The final text is 3,529
    words, so the 3,400 target is not met; the 129 words over it are the
    restored protections.

| Input | SHA-256 |
| --- | --- |
| Case definitions | `547162a3fef86eacab71054fc5ed4d4cfc2e3a5e1e5977903c1bee95fc9feb36` |
| Final SKILL.md | `55fd476fefd07848a5ce5875c8eb6c68817cfe382863db68e95331763abbf73f` |
| Final code.md | `0ba8f520fba4adbeba6161370a5414d04de69e54740e8a4ecab0ad0c5d54660c` |
| Final improvement.md | `b6af3753df774fb36cba7af58af03d6ad8aa29a23cfdf4014551fad469028807` |
| Final independent-use.md | `f24c7287aa8e4db235e1a234e93a05b124ef2591b62894738ae85545021d9b8f` |
| Final refactoring.md | `a8a5835bce3dca62f90441e8700edb0b6685da293152034a2588f865ef0aeed5` |

### Task outcomes

The coordinator checked each result from a clean copy and compared protected
files byte for byte.

| Case | Candidate | Improved | Restored or final |
| --- | --- | --- | --- |
| `guide` | Passed; README 87 lines, commands, refusal, and `--replace` verified; fresh-user trial | Passed; README 68 lines; same checks | Final passed; README 79 lines; JSON block matches the real file, refusal exits 2, `--replace` works; fresh-user trial |
| `review` | Passed; publication owner and post-publication checks found, no owners invented; plan unchanged | Passed; same findings | Not rerun |
| `ready` | Passed without edits; retry suggestion rejected | Passed without edits | Not rerun |
| `feature` | Not rerun | Passed; January totals 512.50, invalid month exits 2 at the CLI; source 81 → 98, tests 61 → 92; no added comments | Not rerun |
| `refactor` | Passed; only the intended invalid-amount fix differs; source 125 → 91, tests 61 → 77 | Passed; source 125 → 80, tests 61 → 67 | Restored passed; source 125 → 73, tests 61 → 66. Final passed; three modules merged into one 57-line `cli.py`, tests 61 → 68; outputs, `--help`, refusal, and header check unchanged, invalid-amount fix with a regression test |
| `docs` | Passed; documentation 94 → 59; code unchanged | Passed; 94 → 63; `NaN` acceptance reported without changing code | Not rerun |
| `improve` | First run failed only the size criterion (405 → 260 words, 36%); after `improvement.md` said additions must cost less than they remove, a fresh run passed at 405 → 199 | Passed; 405 → 240 | Restored passed; 405 → 229 |

On 0.7.2 the `improve` case also passed (405 → 221 words), so the case does not
separate the versions; it guards the improve path rather than proving a gain.

### Routing

Fresh agents classified 18 requests, and later 19, using only the routing
section. The first table left gaps for named changes to existing work and
overlaps between build, fix, and improve. An ordered test, where the first
matching row decides, resolved most of them. On the final rules, 16 of 19
classify cleanly, including "improve, but keep these rules". "Complete this
plan", "raise coverage", and a bare "tidy up" remain ambiguous in the user's
words, and the rules say to ask.

### Activation

`evals/README.md` warns that skill-creator `run_eval.py` is distorted by an
installed Loopy and early file reads. A scratch runner adapted from it ran each
query in a fresh copy of a small project:
- `claude -p` on Opus 5.5 with at most six turns;
- the installed plugin disabled;
- a run counted as triggered when the skill was called before any edit.

The set had 10 should-trigger requests (review, build, fix, refactor, and
improve, in Korean and English) and 10 near misses, run 3 times each.

| Description | Form | Should trigger | Near misses |
| --- | --- | --- | --- |
| 0.7.2 | Project skill | 30/30 | 0/30 |
| 0.8.0 | Project skill | 30/30 | 0/30 |
| 0.7.2 | Plugin (`--plugin-dir`) | 28/30; one miss each on the improve and fix requests | 0/30 |
| 0.8.0 | Plugin (`--plugin-dir`) | 30/30 | 0/30 |
| Installed 0.7.1 | Marketplace plugin, 2 runs each | 16/20; the fix request 0/2 | 0/20 |

Headless runs in a small project are not interactive desktop sessions with long
context and many skills, which may explain why users see Loopy chosen less
often than this. The difference between 0.7.2 and 0.8.0 is small for the sample
size.

### Limits

Each case ran once per text, so differences may be run-to-run variance.
`review`, `ready`, `feature`, and `docs` did not run on the final text, whose
later edits restore candidate wording. Python 3.9, Codex, other models, human
use, and host installation were not exercised.

## 2026-10-23 verbosity reduction

After feedback that the content was longer than needed, the runtime skill and
the maintainer docs were rewritten to state each rule once. Runtime text went
from 4,854 to 4,216 words: `SKILL.md` 1,668 → 1,444 with the frontmatter
unchanged, `code.md` 430 → 390, `independent-use.md` 885 → 780, and
`refactoring.md` 1,871 → 1,602. `README.md` went 724 → 630 words and
`evals/README.md` 805 → 722. All six cases passed with fresh agents, compared
with the recorded 0.7.x results below; this is one run per case.

### Conditions and inputs

- Baseline: 0.7.1 at commit `b484854`, exported with `git archive` before
  editing.
- Environment: macOS, Python 3.13.16. Each workspace came from
  `prepare.py --case` and had its own fresh Claude Code `general-purpose`
  subagent on Opus 5.5 with the same prompt: apply the supplied skill rather
  than the installed one, read only the workspace, and delegate at most one
  bounded fresh-context check per task. `guide`, `review`, and `ready` shared
  one agent and workspace. Global instructions and the repository name in
  workspace paths were present as in the earlier runs.
- All six cases first ran on an intermediate text. A fresh reviewer comparing
  it with 0.7.1 found one material loss, compatibility that consumers need no
  longer kept under an authorized migration, and about twenty dropped
  qualifiers; these were restored. A second fresh reviewer found no lost
  protection and one over-strengthened compatibility clause, which was reverted
  to the 0.7.1 wording. `refactor` and `docs`, which load the most-changed
  reference, then ran again on the final words; the delivered files differ from
  that snapshot only in line wrapping.

| Input | SHA-256 |
| --- | --- |
| Case definitions | `39dae10e90af1313192728be805c410131ec1b3115471cf3bfe26989edc6e67f` |
| Intermediate SKILL.md | `51bd0dba6ff5500b563a458b6e5d50f38e5c6aa8806d1998c2ed65e4e8e77210` |
| Delivered SKILL.md | `aacb6ba39d035ee4fb62f3ca9d9f594c956637cd04028638780a4e5bf124b283` |
| Delivered code.md | `dc5b0e3d3f0761a6b794bebe50c29b312eef741614cd180b37af31e09a10f8e1` |
| Delivered independent-use.md | `74311a90fe22ea9f4cb0ae9cbba420d98a885f6495b27c6c7a73e5c8219fc5ff` |
| Delivered refactoring.md | `e743d4a8cc2e8caf52c2781999736bddccdbc06829851fb0b1bf918418111680` |

### Task outcomes

The coordinator reran each result from a clean copy and compared protected
files byte for byte.

| Case | Recorded comparison | This run |
| --- | --- | --- |
| `guide` | 0.6.0 passed; guides of 58 and 61 lines | Passed; README 7 → 76 lines including the expected JSON; command, refusal, `--replace`, and empty folder verified; a fresh-user trial ran |
| `review` | 0.6.0 passed | Passed; publication ownership and post-publication command checks identified, no owners invented; plan unchanged |
| `ready` | 0.6.0 passed without edits | Passed without edits; empty folder printed `0` with exit 0; retry suggestion rejected |
| `feature` | 0.7.0: source 81 → 98, tests 61 → 91 | Passed; source 81 → 98, tests 61 → 102; no added comments; fresh check skipped as a narrow change |
| `refactor` | 0.7.1: source 125 → 75, tests 61 → 67 | Passed on both texts: outputs, `--help`, refusal, and header check unchanged; invalid-amount fix with a regression test; seeded excess removed. Intermediate source 125 → 82, final 125 → 69 |
| `docs` | 0.7.1: documentation 94 → 58 | Passed on both texts: code unchanged, FAQ and its wrong claim removed, broken link gone, claims kept. Intermediate 94 → 72, final 94 → 64 |

Two fresh maintainer readers, one on the 0.7.1 project and one on the revised
one, did the same tasks from the README: judge fit, install, find the trial
skip rule, and follow the change procedure, including the checks and a `docs`
packet. Both succeeded and reported the same friction: no `python` command on
macOS, no path for the skill-creator validator, and no mapping from a changed
file to its cases.

### Limits

Each case ran once per text, so differences may be run-to-run variance. Four
cases ran only on the intermediate text, whose later edits restore 0.7.1
wording. Python 3.9, Codex, other models, human use, and host installation were
not exercised. Some agents briefly wrote to the system temp directory through
the fixtures' tests, and two ran a read-only `git status`.

## 2026-10-21 refactoring reference cleanup

Three repeated passages were removed from `references/refactoring.md`, which
was otherwise unchanged from 0.7.0 (`f51b93b7…`); the revised file is
`c253104e…` (SHA-256). The `refactor` and
`docs` cases ran once each with fresh agents under the 0.7.0 conditions below,
whose candidate results served as the comparison.

| Case | 0.7.0 | Revised |
| --- | --- | --- |
| `refactor` | Source 125 → 68, tests 61 → 68; no docstrings | Source 125 → 75, tests 61 → 67; no docstrings, two why-comments; `--help`, outputs, refusal, header check, and the invalid-amount fix verified by the coordinator |
| `docs` | Documentation 94 → 79 | Documentation 94 → 58; FAQ removed, wrong claim and broken link gone, code unchanged, all claims kept |

Differences between the two runs are within what one run per case can show.

## 2026-10-21 reduction evaluation

The candidate added `references/code.md`, a reduction goal and document
refactoring to `references/refactoring.md`, and a stated goal of not stopping
after one pass to `SKILL.md`. Both versions kept behavior, fixed the seeded
bugs, and preserved the protected paths. The candidate produced less code and
text in all three new cases, and it alone removed file-top docstrings and
avoided comments that restate code. This is one run per case, not a benchmark.

### Conditions and inputs

- Baseline: 0.6.1 at commit `18342472ecce83c0fd4fcbc698605a7b5fae7c42`,
  exported with `git archive` before evaluation.
- Candidate: the working tree skill, snapshotted before its trials and later
  confirmed identical to the delivered files.
- Environment: macOS, Python 3.13.16; some agents also ran Python 3.9.6. Each
  case and version had its own workspace from `prepare.py --case` and its own
  fresh Claude Code `general-purpose` subagent on the same model, with the same
  prompt and permission to delegate one bounded fresh-context check.
- The user's global agent instructions, including a personal guidance wiki that
  favors short code and removing text, were available to both versions. At
  least one docs evaluator read that wiki. Workspace paths contained the
  repository name; agents were told not to read outside their workspace.
- Cases and fixtures were written before any skill edit in this change, except
  for the comment rule edited just before. The `docs` case was added while the
  candidate was being edited; its baseline still used the exported 0.6.1 skill.

| Input | SHA-256 |
| --- | --- |
| Case definitions | `39dae10e90af1313192728be805c410131ec1b3115471cf3bfe26989edc6e67f` |
| Baseline SKILL.md | `ea68f8d00b3b4b46c937cf463e877bf535d233a66ef56f07ea15e0806647fdee` |
| Baseline refactoring.md | `5dad49539816c7d54e608a139fd67fb162cfaa4e0014b5a2c050b15c9db7bb58` |
| Candidate SKILL.md | `0e0d1755ef946a4c755eb57eb9796c004a18820d1ae84acc2dde11c54937c564` |
| Candidate code.md | `bc439d2b88d0df12bcc6c06901492fe90ff282fd2535d49f2f4ec06e54fd5eaf` |
| Candidate refactoring.md | `f51b93b74ad6bdfa1216277a68fad2eccc9f9baa08da9ecd21f646d582792014` |

The baseline `refactor` and `feature` workspaces were prepared before the
`docs` case existed, so their case-definition hash differs; their own case
entries are unchanged.

### Task outcomes

The coordinator ran each result from a clean copy: sample text and JSON output,
existing-output refusal, wrong header, an invalid amount with `--json`, `--help`,
and the fixture tests. Signals for docstrings, comments, and seeded excess were
read from the files, not from agent reports.

| Case | Baseline | Candidate |
| --- | --- | --- |
| `refactor` | Behavior and `--help` kept; invalid-amount bug fixed with a regression test; seeded leftovers removed. Kept four file-top docstrings, added two function docstrings, a comment explaining `parser.error`, and an `Expense` dataclass. Source 125 → 112 lines, tests 61 → 81. | Behavior and `--help` kept; bug fixed with a regression test; all seeded excess removed, `--help` text moved into `description`. No docstrings; two why-comments. Three modules merged into one 68-line `cli.py`. Source 125 → 68, tests 61 → 68; the report split out the bug-fix lines. |
| `feature` | `--month` works, invalid months exit 2, eight tests pass. Added a comment restating the filter. Source 81 → 102, tests 61 → 107. | Same behavior, seven tests pass. No added comments; the date-error test joined the existing rejection table. Source 81 → 98, tests 61 → 91. |
| `docs` | Code unchanged, `docs/usage.md` kept, wrong overwrite claim and broken link fixed, claims retained. Documentation 94 → 128 lines. | Same correctness. The FAQ was removed because every answer repeated README or usage; its one useful example moved to usage. Documentation 94 → 79 lines. |

Both `refactor` agents and both `docs` agents ran fresh-reader attempts before
and after their changes. The candidate `feature` agent skipped one as a small
change with direct evidence; the baseline `feature` agent ran one.

### Limits

Each case ran once per version, so differences may include run-to-run variance.
Both versions also rejected `NaN` amounts and validated `--month` dates, which
the README implies but does not state. Human use, Codex, and other models were
not exercised. Agents could read the shared global instructions, which may
narrow the difference between versions.

## 2026-10-01 redesign evaluation

The revised skill completed the three selected tasks, added an independent
guide-use attempt during production, and preserved the read-only and no-change
boundaries. Both versions produced working guides. This run supports the new
verification behavior; it does not establish a general quality improvement.

### Conditions and inputs

- Baseline: 0.5.0 at commit `3579c66bc2d0db6362d48b452759c40a0bdf6adf`, with a
  snapshot of the existing skill taken before edits.
- Candidate: local 0.6.0 redesign. The evaluated core and independent-use
  reference match the delivered files. The refactoring reference received a
  later capitalization correction from `Decision` to `decision`; these three
  cases did not load that reference. Its final state was reviewed separately.
- Environment: Windows, PowerShell, Python 3.13.15. Both producing agents used
  the same worker role/model (gpt-6.1-sol, medium reasoning), with fresh contexts
  and the same authorized access to bounded local delegation.
- Each producing agent handled the three separate cases sequentially. Agents
  did not receive the production conversation, acceptance answers, or another
  version's observations. Each version had a separate temporary workspace.
- Tasks and acceptance criteria in [cases.json](cases.json) were fixed before
  editing the skill. The raw [fixtures](fixtures/) were copied unchanged into
  each workspace. The initial workspaces were prepared manually; the added
  preparation helper was subsequently executed and its output inspected.

SHA-256 identities of the evaluated bytes (line-ending changes affect these):

| Input | SHA-256 |
| --- | --- |
| Case definitions | `f14bd2f3b8b6cb929915e96917746854a5e250d080706950f2e8512a44b5ab77` |
| Baseline SKILL.md | `6c8bfc72455ad40f68920885d00e8a7360740cecec5214f1dde1068065587a4c` |
| Candidate SKILL.md | `97b6e021df6b02c4ad54f4aeefbab8b23c50d432b70b30280761dd10b009289b` |
| Candidate independent-use.md | `45ba4a5fba50a363ad4e406c67861a1849f7cf16117f968bcf74fcc9a6566a7e` |

### Task outcomes

| Case | Baseline | Candidate | Accepted evidence |
| --- | --- | --- | --- |
| Guide completion | Passed with direct self-checks | Passed with direct checks and a fresh-agent attempt before completion | Both commands produced the two source notes; purpose, working directory, output check, and intentional replacement were documented |
| Read-only plan assessment | Passed | Passed, also using a bounded independent walkthrough | Both identified missing publication ownership and validation after publication; neither changed the plan or attempted publication |
| Already-correct guide | Passed without edits | Passed without edits or another evaluator | Empty folder printed `0` with exit 0; the unsupported retry recommendation was rejected |

Retained outputs: [baseline guide](outputs/baseline-guide.md) and
[candidate guide](outputs/candidate-guide.md). These are captured artifacts,
not standalone runnable examples in this directory. To repeat their user task,
place one at `README.md` in a clean copy of `fixtures/guide/` and run from that
directory.

The baseline guide's command was
`python parcel.py notes --output ../output/notes.json`; the candidate used
`python parcel.py notes --output output/notes.json`. Both exited 0 and packaged
`first.txt` and `second.txt` with their original text and trailing newlines.
`python -m json.tool` on each resulting file exited 0. Actual JSON artifacts
were inspected and compared with the supplied sources.

Both producing agents also observed rejection of an existing output (exit 2,
unchanged bytes), explicit replacement (exit 0), and successful empty results.
For the count command, sample and empty folders exited 0, a missing folder
exited 2, and nested files were excluded. The baseline's first scratch harness
had a Windows path-separator expectation mismatch; it corrected that expectation
and the displayed-path guidance, then passed its checks. It did not alter the
CLI to satisfy the harness.

In each version, byte comparisons against the original fixtures confirmed that
all seven protected files were unchanged: both CLIs, three input text files,
the plan, and the already-correct README. Only the requested guide was edited
among task inputs. Generated files stayed in temporary evaluation workspaces.

### Independent use and preservation review

The candidate's producing agent delegated a fresh-context attempt from the
completed README. The reader ran packaging and JSON inspection in an isolated
copy, compared the note contents, and reported no obstacle. It also performed
a read-only plan walkthrough. It received ordinary task materials, not expected
answers or earlier findings. The parent checked the resulting JSON and unchanged
inputs. The reader did not initiate another review loop.

After the baseline run, the coordinator commissioned a separate fresh reader
to try the baseline guide from a clean copy. That attempt also succeeded:
packaging and JSON inspection exited 0, and comparison with both source notes
passed. This was a retrospective coordinator check, not behavior induced by the
baseline skill. There is no observed baseline usability failure to claim fixed.

A separate reviewer started at the revised repository README and followed its
runtime links, then compared the instructions with HEAD. It reported no
actionable loss of scope, preservation, bug-fix, or stopping protections. Its
walkthrough covered substantial handoffs, read-only assessments, small sufficient
changes, project-wide refactors with pre-existing bugs and persisted formats,
and unavailable or prohibited delegation. It correctly located common trial
rules in `references/independent-use.md` and code migration rules in
`references/refactoring.md`. This was source review, not an executed refactor.

### Package verification and limits

The installed skill-creator validator passed. Plugin and marketplace JSON
parsed; both host manifests specify 0.6.0 and agree on the shared description.
Local Markdown links resolved, Python evaluation sources compiled, and
`git diff --check` passed. The preparation helper created isolated skill and
fixture copies with a request packet that contained the requests but no
acceptance answers; a missing skill path was rejected with exit 2. Its copies
were compared with the source bytes.

This is a small forward test, not a statistical benchmark or a human usability
study. It does not measure long-term maintainability, activation reliability,
or cost. Actual UI workflows, external automations, project-wide code migrations,
other operating systems, Python 3.9, and host installation were not executed.
The runtime instructions cover those contexts, but these observations do not
prove their behavior. No release was published during this evaluation.

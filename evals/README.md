# Evaluate Loopy

Follow this procedure when changing the skill, its references, its activation
description, or the evaluation itself. Judge actual task results and artifacts;
format checks alone cannot show that the instructions work.

## Choose the runs

Each judged run is a full fresh-agent session, so run only what the change can
affect:

| Change | Runs |
| --- | --- |
| Evaluation tool code that keeps every sentence sent to evaluators, the README, metadata, or wording that keeps every rule's meaning | [Package checks](#package-checks) and unit tests; after changing a tool, also prepare one workspace and read its `requests.md` and `prompt.md` |
| A sentence sent to evaluators (the skill packet, control packet, coordinator prompt, routing prompt, or trial prompts) or the evaluator conditions | The run conditions change, so rerun the routing check, the 10 cases, and the 10 control runs, and replace the baselines |
| `SKILL.md` *Sort the request* | The routing check, plus the cases of each kind whose table row changed |
| Any other `SKILL.md` section | All 10 cases |
| One reference | The cases that read it: `debug.md` → `fix`, `cause`, `ready`, `diagnose`; `refactoring.md` → `refactor`, `docs`; `code.md` → `refactor`, `fix`, `cause`, `feature`; `improvement.md` → `improve`; `independent-use.md` → `guide`, `improve`, `refactor`, `docs` |
| The skill `description` | [Activation](#measure-activation) only |
| A new major version | The routing check, the 10 cases, the 10 control runs, and the five Codex cases |
| The evaluator model | The routing check, the 10 cases, and the 10 control runs |
| A new Codex version or model | The five Codex cases |

- When a change spans several rows, run everything those rows require.
- When a row that changes the skill or an evaluator sentence requires one of
  the five Codex cases, its Codex run is required too.
- A new Claude Code version alone needs no rerun; record the version in the
  next run's entry.
- Run the previous skill as well only when a case or setup is new or changed,
  or when a change claims a better outcome than the recorded one.
- These runs are the use check for a skill change. Add a trial, reviewer, or
  repetition beyond them only when a result leaves a question that could change
  the release, and record why.

| Case | Kind | Input |
| --- | --- | --- |
| `guide` | Build | A CLI whose README must become usable |
| `review` | Assess | A deployment plan to assess read-only |
| `ready` | Assess, then Debug | An already-correct guide and an unsupported review finding |
| `refactor` | Refactor | Code seeded with common agent habits and a pre-existing bug |
| `fix` | Debug | A bug report naming a symptom, next to a code smell that is not a bug |
| `cause` | Debug | A bug whose symptom a plausible workaround also hides |
| `diagnose` | Assess | A request to find a bug's cause without changing anything |
| `feature` | Build | A feature to add to clean code |
| `docs` | Refactor | Documentation with repetition and a wrong claim |
| `improve` | Improve | A verbose prompt with stale and conflicting rules |

The five Codex cases are `review`, `refactor`, `fix`, `feature`, and
`improve`, one per kind.

## Prepare workspaces

From the repository root, with Python 3.9 or later and no external packages:

```console
python3 evals/prepare.py --skill skills/loopy --case fix
python3 evals/prepare.py --control --case fix
python3 evals/prepare.py --skill skills/loopy --routing
```

Each case gets its own new `$TMPDIR/loopy-eval-*` workspace, and the script
prints one `<id>` and absolute path per line, separated by a tab, in catalogue
order. Without `--case`, every case is prepared. `--control` makes the same
workspace without the skill, and `--routing` makes one workspace for the
routing check and prints `routing` and its path.

| Path | Case | Control | Routing | Holds |
| --- | --- | --- | --- | --- |
| `skill/` | yes | no | yes | A copy of the `--skill` folder |
| `tasks/<id>/` | yes | yes | no | A copy of `fixtures/<id>/` |
| `requests.md` | yes | yes | no | The packet and the case request, without acceptance criteria |
| `routing.md` | no | no | yes | One `<id>: <request>` line per routing request |
| `prompt.md` | yes | yes | yes | The prompt the coordinator sends to the evaluator, unchanged |

Evaluators write `run.md` for a case and `answers.md` for the routing check;
`codex exec -o` also writes `final.md`. [prepare.py](prepare.py) owns the exact
packet and prompt sentences, so change them only there and only with the runs
the table above requires. Invalid input exits with status 2 before any
workspace exists, and a failed copy removes every workspace the run made.

## Run evaluators

Every evaluator, trial user, and routing checker is a fresh subagent started
with the Agent tool, `subagent_type: "general-purpose"`, `model: "opus"`, and
`effort: "xhigh"`. Its whole prompt is the content of the workspace's
`prompt.md`, or a trial prompt below. Run judged runs one at a time, so every
transcript and file made during a run belongs to it.

Subagents receive the coordinator's project instructions, project memory, and
git status. During judged runs, keep lines that point to plans, cases,
criteria, or verdicts out of the project instructions and memory, and write no
evaluation content there. Keep the coordinator's own judging files in a folder
under `docs/`, which git ignores, not in the scratchpad or `$TMPDIR`.

Before preparing a judged run:

1. Commit every tracked change so `git status --short` prints nothing, and
   record `git rev-parse --short HEAD` as the run commit.
2. Delete every `$TMPDIR/loopy-eval-*` folder and `.jsonl` file.
3. Empty the coordinator session's scratchpad folder, which its subagents
   share; the system prompt names it.
4. Save the list of files in the session's `subagents/` folder for the
   [isolation audit](#check-isolation).

After the run, check `git status --short` before recording. Any output means
the evaluator wrote into the checkout through a relative shell path: record each
path as a write outside the workspace, delete new files, and restore changed
tracked files with `git checkout -- <path>`. Once the run is judged and
recorded, delete its workspace, its `.jsonl` file, and any trial copy.

### Trials

The use part of a criterion that requires independent use, `guide#4` and
`improve#6`, is always judged by a trial the coordinator runs, whether or not
the evaluator tried one itself. This holds for skill, control, and Codex runs.

1. Empty the scratchpad and save the `subagents/` file list again.
2. Make `<trial>` with `mktemp -d "$TMPDIR/loopy-eval-trial-<id>-XXXX"` and copy
   `fixtures/<id>/` into it.
3. Overwrite it with the fixture files the evaluator changed in
   `<ws>/tasks/<id>`, and delete the ones it deleted. Leave out files it
   created, such as command outputs, except a revised `improve` prompt saved
   under a new name.
4. Send a fresh subagent one of these prompts, replacing only `<trial>` and,
   for `improve`, `<prompt>`: the revised prompt file in `<trial>`, which is
   `review-bot.md` unless the evaluator renamed it.

`guide`:

```text
You are new to the tool in <trial>. You know Python but have never used this
tool. Using only the files in <trial>, follow its README.md to bundle the
sample notes into a JSON file and check the result. Do not read anything
outside <trial>, do not edit README.md, and do not ask anyone. Reply with each
command you ran and its output, where the result is, how you checked it, and
every point where the README left you guessing.
```

`improve`:

```text
Act as the review bot defined by <prompt>, following it exactly. Review
<trial>/samples/pr-42.diff. Reply with the review the bot would post and,
in order, every action or tool call the bot would make. Do not read
anything outside <trial>, do not edit any file, and do not ask anyone.
```

The trial's transcript also goes through the isolation audit, and its tokens
are recorded apart from the run's.

### Control runs

A control run uses a `--control` workspace and the same prompt and conditions.
It measures the same host, model, and global instructions without Loopy. The
installed Loopy's description still appears in the evaluator's skill list, so
the control lacks only the skill body; record this limit.

### Routing check

Run one evaluator on a `--routing` workspace. It reads only `SKILL.md` and
`routing.md` and writes one `<id>: <Kind>[, <Kind>]` line per request to
`answers.md`. The check passes when every line matches the request's `kinds` in
[routing.json](routing.json), including their order.

### Codex

The Codex check installs the new version from a temporary local marketplace,
confirms that Codex selects Loopy for a bug-fix request, and runs the five
Codex cases. It changes the user's `~/.codex/config.toml` for a while and uses
their ChatGPT usage for six or more runs, so tell them and get their agreement
first.

1. Copy `~/.codex/config.toml` to a git-ignored folder under `docs/`.
2. Copy `.codex-plugin/`, `skills/`, and `LICENSE` to
   `$TMPDIR/loopy-codex-dev/plugins/loopy/`, and write this to
   `$TMPDIR/loopy-codex-dev/.agents/plugins/marketplace.json`:

   ```json
   {"name": "loopy-dev", "interface": {"displayName": "Loopy dev"}, "plugins": [{"name": "loopy", "source": {"source": "local", "path": "./plugins/loopy"}, "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Productivity"}]}
   ```

   The repository's `.agents/plugins/marketplace.json` points to GitHub `main`,
   so it cannot install an unreleased version.
3. Run `codex plugin marketplace add $TMPDIR/loopy-codex-dev` and
   `codex plugin add loopy@loopy-dev`. `codex plugin list` must show
   `loopy@loopy-dev` as installed and enabled, with the new version.
4. Copy `fixtures/refactor` to a temporary folder outside the repository and
   run
   `codex exec -C <folder> -s read-only --skip-git-repo-check --ephemeral --json "<query>" > <tmp>/smoke.jsonl`,
   where `<query>` is the `fix-amount` request in
   [activation.json](activation.json). The JSONL must hold at least one command
   event whose command reads `skills/loopy/SKILL.md` under
   `~/.codex/plugins/cache/loopy-dev/`. Installed plugins live in
   `~/.codex/plugins/cache/<marketplace>/<plugin>/<version>/`. If there is no
   such event, record it and stop.
5. Right after that, run `codex plugin remove loopy@loopy-dev` and
   `codex plugin marketplace remove loopy-dev`, delete the temporary folders
   and any `~/.codex/plugins/cache/loopy-dev/`, and check that `diff` between
   the saved copy and `~/.codex/config.toml` prints nothing.
6. Run each Codex case alone in a workspace from
   `python3 evals/prepare.py --skill skills/loopy --case <id>`:
   `codex exec -C <ws> -s workspace-write --skip-git-repo-check --ephemeral --json -o <ws>/final.md "$(cat <ws>/prompt.md)" > <ws>.jsonl`.
   The case runs read only the workspace's copy of the skill, so they need no
   installation. Prepare and clean up as for other judged runs. The `improve`
   trial runs as a Claude Code subagent; record that.

Record the model the JSONL reports, or else the `model` and
`model_reasoning_effort` in `~/.codex/config.toml` at run time.

## Judge and record

### Judging

An evaluator's claim of success is not evidence.

- Compare protected files with the fixtures byte for byte, rerun delivered
  commands in a clean copy, and see each regression test fail when the original
  code is restored.
- Judge criteria about order or attempt history, such as `fix#1`, `cause#1`,
  the "Before" in `improve#1`, and "none is tried and then reverted" in
  `cause#2`, from the tool-call order, not from `run.md`: `audit.py --calls`
  for Claude Code and the JSONL event order for Codex.
- For each criterion that no file comparison or command output settles, write
  one line of evidence, a quote or output, in the run's entry. Do the same for
  skill and control runs, and record that the judge knows which run is the
  control.
- Judge the record part of `guide#4` ("Record whether this was independently
  exercised or only self-checked") by whether the evaluator's `run.md` or final
  reply matches what happened. "Independently exercised" is right only when the
  evaluator's transcript holds an independent attempt: an Agent call and its
  nested transcript.
- A case fails when any of its criteria fails.
- Record traces of writes outside the workspace as limits, except fixture tests
  that write to the system temporary folder through `tempfile` and the session
  scratchpad the host gives subagents.
- When a change touches `refactoring.md`, also compare the instructions
  themselves with the previous ones for project-wide coverage, supported
  external contracts, coherent boundary moves, baseline versus intended bug
  behavior, and effects beyond return values. Claim behavioral testing of those
  paths only from an actual project fixture.

### Check isolation

After each evaluator, trial user, or routing checker finishes, find its
transcript from the agent ID that the Agent tool result reports:
`~/.claude/projects/<project>/<session ID>/subagents/agent-<ID>.jsonl`. Both
`<project>` and `<session ID>` appear in the coordinator's scratchpad path,
`…/<project>/<session ID>/scratchpad`. A nested subagent's transcript is an
`agent-*.jsonl` in the same folder that was not in the saved list. Run

```console
python3 evals/audit.py --forbid <checkout> --forbid <session ID>/tasks <transcripts>
```

with one `--forbid` for the path of every checkout of this repository,
worktrees included. The second string covers the `…/<session ID>/tasks/*.output`
links to earlier subagent transcripts. If the evaluator's transcript holds an
Agent call but no new transcript appeared, record that the nested run could not
be checked.

[audit.py](audit.py) reads only the tool calls in assistant lines. It reports a
call whose input names the repository, an installed Loopy, the session
transcripts, or an evaluation file; a `Skill` call for Loopy; a `Grep` or `Glob`
without a workspace path; and a recursive shell search that does not name the
workspace. A nonzero exit makes the run invalid: record it and rerun with a new
workspace and a new evaluator. The evaluator's shell starts in the
coordinator's checkout, so a relative read with no forbidden string or
recursive search goes unseen; record this limit.

For a Codex run, write the same strings with
`python3 evals/audit.py --forbid <checkout> --forbid <session ID>/tasks --print-forbidden > <tmp>/forbidden.txt`;
`grep -c -F -f <tmp>/forbidden.txt <ws>.jsonl` must print 0. Codex runs with
`-C` in the workspace, so its events carry no repository path.

### Failure triage

Give each failed criterion one cause:

- Skill wording: revise the skill within the [word budgets](#package-checks),
  commit, and rerun what the selection table requires.
- Evaluator error: the evaluator broke an explicit packet instruction, such as
  writing outside the workspace without permission, not writing `run.md` or
  `answers.md`, or asking a question instead of recording it, or a tool error
  kept it from finishing. A result whose quality falls short is not an
  evaluator error. Rerun once with a new evaluator and the same input, for
  skill and control runs alike.
- Environment, such as a missing tool or network: fix it and rerun.
- A criterion or expected kind that conflicts with the skill's own rules:
  record the evidence and ask the maintainer. Never change `cases.json` for a
  run, and change an expected kind in `routing.json` only with the maintainer's
  agreement.

Never rerun unchanged text until it passes, and record the number of attempts
for each run. Within one task, revise the skill and rerun at most three times,
and rerun one slot for an invalid run or an evaluator error at most twice; past
either limit, stop and report the remaining failures and their likely causes.
If the 10 cases' total tokens exceed the limit set for a release, do not rerun
unchanged text to lower it. Compare each case with its Baselines row; treat a
rise the skill causes, such as reading more, as a skill-wording failure, and
otherwise report it.

### Final text

The judged slots are `Routing`, the 10 cases, the 10 control runs
(`<id> (control)`), and the five Codex cases (`<id> (Codex)`).

- Record the run commit of every judged run.
- After a release's first routing run, every commit that changes
  `skills/loopy/`, `evals/prepare.py`, or this file goes in the entry of the
  work that made it, with its selection-table row and the slots that row
  requires.
- Each required slot's last judged run must use that commit or a later one, so
  `git merge-base --is-ancestor <commit> <run commit>` succeeds.
- Rerun a required slot within the current work. When it belongs to finished
  work, reopen that work and write the slot and the commit that requires it in
  its entry.
- Before a release, check this for every commit that
  `git log --format=%h <first run commit>..HEAD -- skills/loopy evals/prepare.py evals/README.md`
  lists.

### Tokens

A Claude Code run's tokens are the value the host reports in its completion
notice. It equals the sum of `input_tokens`, `cache_creation_input_tokens`,
`cache_read_input_tokens`, and `output_tokens` in the `usage` of the
transcript's last assistant response, that is, the last context size. If the
two differ, use the value computed from the transcript and say so.

- The value leaves out nested subagents and coordinator trials; record a
  trial's tokens apart.
- A release's token total adds only the 10 cases' last judged runs; record the
  tokens of failed or invalid runs apart.
- A Codex run's tokens are the sum of `input_tokens` and `output_tokens` over
  the JSONL's usage objects; if the fields differ, record the usage objects as
  they are. Codex tokens are not compared with the Claude Code total.

### Discriminating criteria

A discriminating criterion passes in the skill run and fails in the control
run. List them in each case's entry, and write "regression only" in the
Baselines `Key outcome` of a case that has none. The skill is tuned on these
cases, so the comparison uses the set it was tuned on; record this limit.

### Records

[results.md](results.md) starts with `## Baselines`, a table with the columns
`Run`, `Skill`, `Result`, `Key outcome`, `Tokens`, `Control`, and `Entry`.
`Control` holds the criteria the control run passed out of the case's total,
such as `3/5`, and `—` for routing, Codex, and activation rows. `Entry` links to
the run's section; the activation row names its source in text.

Each run section is titled `## <start date> <name> (<version>)`. Its head gives
the date, OS, Python version, the output of `shasum -a 256 ~/.claude/CLAUDE.md`,
and `git -C ~/.claude/user-wiki rev-parse --short HEAD`, or that either is
missing. For every run, record the slot, the run commit, the transcript's
`version`, `effort`, and model (for Codex, the CLI version and the reported
model), the tokens, the isolation audit result, the verdict for each criterion
with one line of evidence where judgment was needed, the number of attempts,
and why any run was invalid or rerun. Record each run as soon as it is judged.
A release section adds the word counts before and after, the activation check,
the commit check from [Final text](#final-text), the last package checks, and
the remaining limits. When copying a transcript or output, copy command strings
only, never Markdown link syntax, because `check.py` follows links from the
README into this file.

## Measure activation

When changing the `description`, measure whether Claude Code selects Loopy for
requests it should handle and not for near misses:

```console
python3 evals/activation.py --plugin . --set tune --reps 1 --out <dir>/draft-tune.jsonl
python3 evals/activation.py --plugin . --set holdout --out <dir>/candidate-holdout.jsonl
```

`--plugin` takes a plugin root: this repository, or for the baseline a
`git archive HEAD | tar -x -C <dir>` export made before editing. Each run copies
`fixtures/refactor` to a temporary directory and runs `claude -p` there with the
maintainer's own settings, global instructions, and other plugins, as users
have them, but with the installed `loopy@loopy` disabled so only the plugin
under test can be chosen. A run counts as selected when Loopy is called before
any file edit, and stops at that decision. The script appends one record per
run to `--out`, so keep it outside the repository, and prints the selections
per query and in total.

[activation.json](activation.json) holds should-trigger queries and near
misses. Run each draft description, including the final one, on the `tune`
set with one repetition, then run the final one on `holdout`, phrasings it was
not shaped on, with the default three. Runs vary, so use the model users run
(`--model`, otherwise the Claude Code default) and record the setup. The
Baselines counts stand in for the old description while the queries, model,
and runner are unchanged; otherwise run it the same way with
`--plugin <baseline-root>`. Skill-creator's `run_eval.py` judges only the first
tool call, so global instructions that begin with file reads make every run
there look like a miss.

### Activation smoke

When the description is unchanged, a release still checks that the host loads
the plugin under test and selects it:

1. In an empty temporary folder outside the repository, run
   `claude -p --output-format stream-json --verbose --plugin-dir <checkout> --settings '{"enabledPlugins":{"loopy@loopy":false}}' --permission-mode dontAsk "Reply with OK."`.
   The first `system` event must list exactly one plugin named `loopy`, at
   `<checkout>`. If the event shows no plugin path, record that the source could
   not be confirmed.
2. Write a JSON list holding only the `fix-amount` (should select) and `rename`
   (near miss) entries of [activation.json](activation.json) to a temporary
   folder outside the repository, and run
   `python3 evals/activation.py --plugin <checkout> --queries <file> --reps 1 --out <tmp>/smoke.jsonl`.
   `fix-amount` must select `loopy`, and `rename` must not.
3. On a failure, record it and stop. Do not change the description to pass.

## Package checks

From the repository root:

```console
python3 evals/check.py
python3 -m unittest discover -s evals -v
```

[check.py](check.py) checks that the four plugin and marketplace manifests
agree, validates the cases and the routing set, follows local Markdown links
and their heading anchors from the README, and checks the skill's frontmatter
and word budgets. It reports every failed check and exits with status 1. The
tests cover these checks, the workspaces, the isolation audit, and how an
activation run is counted. They show package and tool consistency, not agent
behavior or installation in either host.

- The frontmatter holds only `name`, which matches the manifest, and
  `description`, a folded `>` scalar of at most 1,024 characters with no `<` or
  `>`.
- Words are counted as `len(text.split())`. The `SKILL.md` body after the
  frontmatter may have at most 1,100 words, and the five references together at
  most 2,100.
- Raise a budget only after `results.md` records a run whose case failed
  without the words, and only as far as needed; record the new value in the
  same entry and change it in `check.py`.
- Both marketplaces install from `main`, so a push that changes the plugin also
  raises `version` in both plugin manifests together, or existing installs may
  not update: a patch for fixes and a minor version for procedure changes.

## Maintain the cases and routing set

[cases.json](cases.json) is a nonempty list. Each case has a unique lowercase
ID of letters and digits (hyphens may separate groups), a nonblank `request`, a
matching `fixtures/<id>/` directory, and a nonempty `acceptance` list of
nonblank strings that never reaches the evaluator. Add cases for material new
paths rather than growing the rubric with stylistic preferences. Keep fixtures
and accepted observations in this directory, and keep them, test harnesses,
generated packages, and evaluation logs out of the runtime skill.

[routing.json](routing.json) holds at least 16 requests. Each has a unique ID
of `r` and two digits that gives no hint of the answer, a one-line `request`,
and `kinds`, the expected kinds in the order they run. An optional `example`
names the boundary-example branch in *Sort the request* that the request
paraphrases, such as `shorter-keep`. Every kind appears at least twice, at
least one request is Assess then Debug, and the requests include both English
and Korean. Every branch of every boundary example has one paraphrased request
that does not quote the example. When a change adds or rewrites a boundary
example, add or adjust requests to match.

[cases.py](cases.py) owns the validation of both files for
[prepare.py](prepare.py) and [check.py](check.py); change their rules only
there so both stay consistent.

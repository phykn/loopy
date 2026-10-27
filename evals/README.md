# Evaluate Loopy

Follow this procedure when changing the skill's workflow, activation
description, references, or completion criteria. Judge actual task results and
artifacts; format checks alone cannot show that the instructions work.

## Choose the runs

Each case run is a full fresh-agent session, and each activation query is a
partial Claude Code session per repetition and version, so run only what tests
the change:

| Change | Runs |
| --- | --- |
| Wording that keeps every rule's meaning, the README, metadata, or helpers | [Package and helper checks](#package-and-helper-checks) only |
| One reference, or one row's link to it | That reference's cases below |
| The shared loop in `SKILL.md` or a routing test | Every case |
| The `description` alone | [Activation](#measure-activation) only |

| Case | Kind | Input | Run when changing |
| --- | --- | --- | --- |
| `guide` | Build | A CLI whose README must become usable | `independent-use.md`, building for the next user |
| `review` | Assess | A deployment plan to assess read-only | Assess routing, read-only and authorization limits |
| `ready` | Assess, then Debug | An already-correct guide and an unsupported review finding | Findings and stopping rules |
| `refactor` | Refactor | Code seeded with common agent habits and a pre-existing bug | `refactoring.md`, `code.md` |
| `fix` | Debug | A bug report naming a symptom, next to a code smell that is not a bug | `debug.md`, Debug routing, `code.md` |
| `cause` | Debug | A bug whose symptom a plausible workaround also hides | `debug.md`, Debug routing |
| `diagnose` | Assess | A request to find a bug's cause without changing anything | Diagnosis in `debug.md`, Assess routing |
| `feature` | Build | A feature to add to clean code | `code.md`, Build routing |
| `docs` | Refactor | Documentation with repetition and a wrong claim | Document rules in `refactoring.md` |
| `improve` | Improve | A verbose prompt with stale and conflicting rules | `improvement.md`, Improve routing |

Run only the revised skill. A case's row in the
[Baselines](results.md#baselines) table is its baseline while the case, its
fixture, the host, and the model are unchanged. Run the baseline skill too only
for a new or changed case or setup, or when the change claims a better outcome
than the recorded one.

These runs are the use check for a skill change and replace Loopy's own default
independent use trial. Add a trial, reviewer, or repetition beyond them only
when a result leaves a question that could change the release, and record why.

## Prepare and run

1. Before editing, fix the chosen cases' acceptance criteria in
   [cases.json](cases.json) and keep the raw fixtures. The cases are a focused
   sample, not full coverage; each one's inputs live in `fixtures/<id>/`.
2. From the repository root, prepare a workspace with the revised skill using
   the commands below. For a baseline run, prepare a separate one from an export
   such as `git archive HEAD skills/loopy | tar -x -C <dir>`, passed as
   `--skill <dir>/skills/loopy`. Python 3.9+ with no external packages is
   enough.
3. Give each workspace's `requests.md` to a fresh agent without the production
   conversation, expected answers, acceptance criteria, or earlier conclusions,
   with the same resources, capabilities, and delegation authorization as the
   baseline. This is task execution, not a critique of the skill.
4. Judge the recorded actions and actual outputs against the withheld criteria;
   an agent's claim of success is not evidence by itself. Compare protected
   files with the fixtures byte for byte and run delivered commands from a clean
   copy. When a criterion requires independent use that the producing agent did
   not exercise, have a separate fresh reader try it. When the change touches
   `refactoring.md`, also compare the instructions themselves for project-wide
   coverage, supported external contracts, coherent migrations, baseline versus
   intended bug behavior, and effects beyond return values; claim behavioral
   testing of those paths only from an actual project fixture.
5. Correct only supported problems and rerun the affected cases, not unchanged
   trials until one passes. Record the version and conditions, input identity,
   changed files, token use when the host reports it, and material limits in
   [results.md](results.md), with one row per case for its key outcome and
   detail only for failed criteria, distinguishing self-checks, fresh-agent
   attempts, and human use. Update each run case's row in its Baselines table.

```console
python3 evals/prepare.py --skill skills/loopy
python3 evals/prepare.py --skill skills/loopy --case guide
python3 evals/prepare.py --skill skills/loopy --case review --case ready
```

Each run validates the cases and fixtures, then prints a new temporary
directory holding `skill/`, `tasks/`, and `requests.md`, without the acceptance
criteria; evaluators write `run.md` there. Repeated `--case` options copy only
those cases, in catalogue order; without them, every case is included. Invalid
input exits with status 2 before any workspace exists, and a failed copy
removes its partial output. When per-case independence matters, use a separate
workspace and fresh agent for each case, and record when one agent ran several.

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

## Maintain the catalogue

[cases.json](cases.json) is a nonempty list. Each case has a unique lowercase
ID of letters and digits (hyphens may separate groups), a nonblank `request`, a
matching `fixtures/<id>/` directory, and a nonempty `acceptance` list of
nonblank strings that never reaches the evaluator. Add cases for material new
paths rather than growing the rubric with stylistic preferences. Keep fixtures
and accepted observations in this directory, and keep them, test harnesses,
generated packages, and evaluation logs out of the runtime skill.

[cases.py](cases.py) owns catalogue and fixture validation for both
[prepare.py](prepare.py), which selects cases, copies the workspace, renders
requests, and cleans up, and [check.py](check.py), which checks the package and
documentation. Change case rules only in `cases.py` so both stay consistent.

## Package and helper checks

From the repository root, with Python 3.9+ and no external packages:

```console
python3 evals/check.py
python3 -m unittest discover -s evals -v
```

`check.py` parses both hosts' plugin and marketplace JSON, checks shared
metadata and the skill path, validates the cases, and follows local Markdown
links from the README; it reports failed checks and exits with status 1. Both
marketplaces install from `main`, so a push that changes the plugin also bumps
`version` in both plugin manifests, or existing installs may not update. The
tests cover packet isolation, protected input copies, withheld answers,
invalid-input rejection, failed-copy cleanup, package drift, and how an
activation run is counted.

Also run the `skill-creator` skill's `scripts/quick_validate.py` on
`skills/loopy` to validate the frontmatter, which `check.py` does not. In Claude
Code the skill is under
`~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/`.
It needs PyYAML, so use a suitable or temporary Python environment instead of
adding a dependency to Loopy. After changing a helper, also prepare a packet and
inspect it. These checks show package and helper consistency, not agent
behavior or installation in either host.

[results.md](results.md) starts with a Baselines table of the latest run of each
case and of activation. The entries below it record each run's conditions,
outcomes, retained guide artifacts, and limits; read one only when you need
that detail.

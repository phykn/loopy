# Evaluate Loopy

Follow this procedure when changing the skill's workflow, activation
description, references, or completion criteria. Judge actual task results and
artifacts; format checks alone cannot show that the instructions work.

## Prepare and run

1. Before editing, pick the relevant cases in [cases.json](cases.json), fix
   their acceptance criteria, and keep the baseline skill and raw fixtures.
   The cases are a focused sample, not full coverage; each one's inputs live
   in `fixtures/<id>/`. A change to the shared loop or routing in `SKILL.md`
   runs every case. The `description` only decides when Loopy is selected, so a
   change to it alone runs [activation](#measure-activation) instead of cases.

   | Case | Input | Run when changing |
   | --- | --- | --- |
   | `guide` | A CLI whose README must become usable | `independent-use.md`, building for the next user |
   | `review` | A deployment plan to assess read-only | Review routing, read-only and authorization limits |
   | `ready` | An already-correct guide and an unsupported review finding | Findings and stopping rules |
   | `refactor` | Code seeded with common agent habits and a pre-existing bug | `refactoring.md`, `code.md` |
   | `feature` | A feature to add to clean code | `code.md`, Build routing |
   | `docs` | Documentation with repetition and a wrong claim | Document rules in `refactoring.md` |
   | `improve` | A verbose prompt with stale and conflicting rules | `improvement.md`, Improve routing |

2. From the repository root, prepare one workspace with the baseline skill,
   such as an export from `git archive HEAD skills/loopy | tar -x -C <dir>`
   passed as `--skill <dir>/skills/loopy`, and a separate one with the revised
   skill, using the commands below. Python 3.9+ with no external packages is
   enough.
3. Give each workspace's `requests.md` to a fresh agent without the production
   conversation, expected answers, acceptance criteria, or earlier conclusions,
   with the same resources, capabilities, and delegation authorization for both
   versions. This is task execution, not a critique of the skill.
4. Judge the recorded actions and actual outputs against the withheld criteria;
   an agent's claim of success is not evidence by itself. Compare protected
   files with the fixtures byte for byte, run delivered commands from a clean
   copy, and have a separate fresh reader try any user task the producing agent
   did not independently exercise. When the change touches `refactoring.md`,
   also compare the instructions themselves for project-wide coverage, supported
   external contracts, coherent migrations, baseline versus intended bug
   behavior, and effects beyond return values; claim behavioral testing of
   those paths only from an actual project fixture.
5. Correct only supported problems and rerun the affected cases, not unchanged
   trials until one passes. Record each case's version and conditions, input
   identity, changed files, actual outcomes, acceptance result, and material
   limits in [results.md](results.md), distinguishing self-checks, fresh-agent
   attempts, and human use.

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
requests it should handle and not for near misses, with the same queries for
the old and new description:

```console
python3 evals/activation.py --plugin <baseline-root> --set tune --out <dir>/base-tune.jsonl
python3 evals/activation.py --plugin . --set tune --out <dir>/candidate-tune.jsonl
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
misses. Shape a description on the `tune` set, then run both versions with
`--set holdout` to confirm it on phrasings it was not shaped on. Each run is a
partial Claude Code session that costs tokens and varies between runs, so use
at least three repetitions (the default) and the model users run (`--model`,
otherwise the Claude Code default), and record the setup. Skill-creator's
`run_eval.py` judges only the first tool call, so global instructions that
begin with file reads make every run there look like a miss.

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

[results.md](results.md) records past runs with their baseline and revised
skills, observed outcomes, retained guide artifacts, and limits. Consult it
when maintaining the cases or comparing a later revision.

# Evaluate Loopy

Use this procedure when changing the skill's workflow, activation description,
references, or completion criteria. Evaluate actual task performance and artifacts;
format checks alone cannot establish that the instructions work.

## Prepare and run

1. Before editing, select relevant cases from [cases.json](cases.json), fix their
   acceptance criteria, and preserve the baseline skill and raw fixture inputs.
   The initial cases cover a usable guide, a read-only assessment, and an
   already-correct guide with an unsupported review finding. They are a focused
   sample, not coverage of every supported artifact type.
2. From the repository root, run the command below with the baseline skill
   directory. Run it again with the revised skill for a separate workspace.
   Python 3.9+ is sufficient; no external packages are required.
3. Give each version's `requests.md` to a fresh agent without the production
   conversation, expected answers, acceptance criteria, or earlier conclusions.
   Specify the same resources, capabilities, and delegation authorization for
   both versions. This is actual task execution, not a critique of the skill.
4. Inspect the recorded actions and actual outputs against the withheld
   acceptance criteria. Compare protected files with the fixtures byte for byte.
   Execute delivered commands from a clean copy, and use a separate fresh reader
   for any user task the producing agent did not independently exercise.
5. Correct only supported problems and rerun affected cases. Record changed
   conditions and unresolved limits; do not repeat unchanged trials until one
   happens to pass. Link retained observations from this file.

```console
python evals/prepare.py --skill skills/loopy
```

The command prints a new temporary directory containing `skill/`, `tasks/`, and
`requests.md`. Evaluators write `run.md` there. Inputs and scratch outputs never
share a workspace between versions. The packet omits the acceptance criteria.
If per-case independence matters, use a fresh prepared workspace and agent for
each case as well. Record when one agent performs several separate cases.

Keep task fixtures and accepted observations in this directory. Do not copy
temporary test harnesses, generated packages, or evaluation logs into the
runtime skill. A reviewer or evaluator must not read these expected answers
while performing a blind trial.

## Inspect the evidence

For each case, record the version and conditions, input identity, changed files,
actual command or action outcomes, acceptance result, and material limitations.
Distinguish self-checks, fresh-agent attempts, and human use. An agent's final
claim of success is not sufficient without inspecting its artifact or execution.

Confirm that a guide works from its normal entrypoint; that a review only
reports supported findings; and that an already-correct artifact stays intact
after a false finding is checked. These cases also challenge unnecessary edits,
recursive evaluation, and extra review rounds. Add cases for material new paths
instead of expanding the rubric to every stylistic preference.

Compare instructions as well as behavior when preserving refactoring semantics:
project-wide coverage, supported external contracts, coherent migrations,
baseline versus intended bug behavior, and effects beyond return values.
Use an actual project fixture when claiming those paths were behaviorally tested.

## Static checks

Run the installed `skill-creator` skill's `scripts/quick_validate.py` on
`skills/loopy`. That validator requires PyYAML; use an available suitable Python
environment or a temporary environment without adding a runtime dependency to
Loopy. Also parse all plugin and marketplace JSON, check that both plugin versions
and shared descriptions agree, and follow local Markdown links from the README
through the runtime references and this evaluation entrypoint.

The runtime is instruction-only. Validate any changed evaluation helper by
running it and inspecting its output. These checks establish package consistency,
not agent behavior or successful installation in either host.

## Recorded run

[2026-10-01 redesign evaluation](results.md) records the baseline and revised
skill, observed task outcomes, retained guide artifacts, and limits. Consult it
when maintaining these acceptance cases or comparing a later workflow revision.

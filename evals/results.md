# 2026-10-01 redesign evaluation

The revised skill completed the three selected tasks, added an independent
guide-use attempt during production, and preserved the read-only and no-change
boundaries. Both versions produced working guides. This run supports the new
verification behavior; it does not establish a general quality improvement.

## Conditions and inputs

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

## Task outcomes

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

## Independent use and preservation review

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

## Package verification and limits

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

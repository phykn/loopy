# Loopy

Loopy is an instruction-only skill for Codex and Claude Code. Use it for
autonomous work where completion must be established by evidence, important
constraints must survive the work, or stopping too early would create material
risk.

Loopy establishes a compact Completion Contract: the requested outcome, the
current claim when relevant, what must survive, the evidence needed, and the
authorized scope. Its Method connects judgment, execution, verification,
challenge, and decision in one loop. These controls can share evidence and do
not require separate tool calls or review rounds. Each assessment selects
`done`, `revise`, `blocked`, or `out_of_scope`; `revise` continues authorized work.

Loopy also supports project-wide refactoring: reassessing folder and file
structure, responsibilities, dependencies, and names down to functions and
variables. It preserves required behavior and external contracts while fixing
supported bugs encountered in the requested scope, including defects that
predate the refactor. Existing organization is not a preservation requirement.

When the task definition, an existing artifact, or a proposed revision requires
material judgment, Loopy also recovers the current Claim when one exists and uses
three internal questions: what is missing or excessive, what belongs together,
and what matters next. Clear requested outcomes remain authoritative, and advisory
or unsupported findings do not trigger revision. A read-only assessment can finish
with supported findings; it does not require fixing the assessed artifact.

Loopy uses the request, prior authorization, and current evidence to resolve
routine gaps and continues authorized work through verification. Checks scale
with the changed surface and risk; passing evidence is reused while its inputs
and assumptions remain valid. A verification check can also supply the material
challenge. The final report stays concise, with the result, evidence, and any
material limitation.

## Install

### Codex and the ChatGPT desktop app

Add the repository marketplace and install Loopy:

```text
codex plugin marketplace add phykn/loopy
codex plugin add loopy@loopy
```

Restart the ChatGPT desktop app if the plugin does not appear immediately.

### Claude Code

```text
/plugin marketplace add phykn/loopy
/plugin install loopy@loopy
```

Run `/reload-plugins` after updating an existing installation.

## Use

Invoke the skill explicitly when the work needs evidence-backed completion:

```text
Use loopy to complete this migration without losing existing behavior.
Use loopy to finish this document and verify every acceptance criterion.
Use loopy to resolve this bug, preserve the current interface, and prove the fix.
Use loopy to refactor this entire project: improve folder and file structure,
names, and responsibilities; fix bugs found along the way; preserve external
contracts and verify the result.
```

The skill may also be selected automatically when a request matches its
description.

Do not use Loopy for trivial edits, direct factual answers, open brainstorming,
or low-risk work whose completion is obvious from one simple action.

For a whole-project refactor, Loopy assesses all major areas before declaring
completion. It chooses responsibility boundaries before paths and names, moves
internal consumers together, preserves supported external contracts, and verifies
each coherent change before building on it. Callers, configuration, tests, and
documentation move with the implementation. Sound structures can stay as they
are. Narrower refactoring requests retain their requested scope; review-only
requests do not authorize edits.

Refactoring decisions account for caller burden and data flow. An abstraction
must hide meaningful complexity, and removing repeated processing requires
evidence that upstream guarantees still hold. Metrics locate candidates rather
than dictate design. Characterization checks record current behavior without
endorsing bugs; intended corrections remain distinguishable from structural
changes. Relevant errors, state changes, I/O, cleanup, and observable effect order
are part of behavior preservation. When testing is blocked, introduce only the
smallest necessary observation or substitution boundary and record any gap.

## Runtime structure

Both hosts load the same canonical file:

```text
skills/loopy/SKILL.md
```

Refactoring requests also load the shared guidance at
[`skills/loopy/references/refactoring.md`](skills/loopy/references/refactoring.md).

Codex distribution metadata lives in `.codex-plugin/` and `.agents/plugins/`.
Claude Code distribution metadata lives in `.claude-plugin/`. There is no build
step and no duplicated host-specific skill body.

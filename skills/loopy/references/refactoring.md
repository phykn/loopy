# Refactoring

Use this guidance within Loopy's Method when refactoring is requested. Structural
improvement and supported fixes for encountered bugs are part of the Outcome.
A project-wide request includes folder and file structure, names,
responsibilities, and dependencies across the project; a narrower request keeps
its stated boundary. A read-only assessment authorizes findings only, including
when applying the bug and migration criteria below. Explicit user constraints
override these defaults.

## Establish the target

Inspect project instructions, the working tree, major components, entrypoints,
dependency direction, tests, and build or packaging configuration. Trace the
main user paths and identify external consumers and persisted formats before
choosing boundaries. Preserve unrelated local work.

Determine compatibility from supported interfaces and their consumers. An
importable module, non-private symbol, or configuration key is not automatically
an external contract. Use documentation, exports, packaging, known consumers,
and persisted data to distinguish internal names from supported public imports,
commands, settings, formats, and checkpoints. A published interface may have
consumers outside the repository even when no local usage is found.

For a project-wide request, keep a compact coverage record of the major areas
and their status: inspected, needing change, verified, or blocked. Extend it as
new dependencies are discovered. Inspect each area deeply enough to assess its
responsibilities and connections; do not equate project coverage with changing
every file or stop after tidying the first convenient module.

Translate the request into observable structural criteria, such as one owner
for a lifecycle, removal of a dependency cycle, names that distinguish different
concepts, or related operations using the same call shape. Ground each change
in actual responsibilities, consumers, confusing usages, or repeated changes.
Working code can still need structural improvement; a runtime defect is not
required. Existing organization is evidence to inspect, not a default constraint.
Retain structures and names that already fit. Avoid imposing a stock
directory tree, abstraction layer, or personal naming style without a benefit
for this project.

Choose responsibility boundaries and dependency direction before settling target
paths and names. State the intended organization and significant migrations
briefly before editing, prioritizing changes that unblock others. Choose routine
details from the evidence and proceed under the existing authorization; a broad
internal move does not itself require renewed approval. Refine the proposal as
dependencies become clear.

## Establish the behavior baseline

Use existing tests, representative executions, or focused characterization checks
for affected behavior. Include supported inputs and boundary cases visible in
the code or callers, not only examples already covered by tests. Record known
failures and unverified areas to distinguish regressions, pre-existing defects,
and intentional fixes. Preserve required behavior and external contracts.

Characterization records what the current code does; it does not establish that
the behavior is correct. Run these checks before the relevant refactor and
compare afterward. When behavior is suspicious but the intended contract is
unclear, preserve the observation and investigate before changing semantics.
For confirmed bugs, distinguish the observed failure from the intended result
using the bug-fix guidance below.

If existing boundaries cannot support useful observation, isolate the dependency
that actually blocks verification with the smallest useful seam: a place to
observe or substitute an input or effect. Prefer existing interfaces; introduce
injection or an adapter only when needed. If this requires an initial structural
change without a reliable baseline, keep it minimal, record the verification
gap, and establish checks before broader changes. A seam alone is not evidence
of preserved behavior. Retire temporary probes or test scaffolding when stable
boundaries cover the behavior; retain justified testability improvements.

## Reshape structure and names

Group code that changes for the same reason. Keep behavior with the data or
lifecycle that owns it; split unrelated responsibilities and make dependency
direction explicit. Prefer straightforward folders with little unnecessary
nesting. Consolidate duplication when it represents the same knowledge and
reason to change, not coincidental textual similarity. Remove obsolete internal
paths as their consumers migrate. Do not turn shared utilities or configuration
into a home for unrelated behavior.

Reassess folder names, filenames, modules, classes, functions, parameters, and
variables together with their responsibilities. Prefer domain terms for domain
concepts, concise verb phrases for functions, and short conventional local names
where their meaning is clear. Use singular and plural consistently and the same
name and call shape for the same operation across related components. A rename
should resolve misleading meaning, inconsistent vocabulary, or ambiguity;
longer names and more layers are not inherently better.

Keep the main execution path visible. Extract helpers for real concepts or
repeated operations, keep one-use behavior near its owner, and arrange functions
in a useful reading order. Judge extraction, splitting, and merging by the total
burden on readers and callers: concepts to learn, hidden dependencies, required
call order, and places that must change together. A more involved implementation
can be worthwhile when it hides details behind a simpler contract. Reject
pass-through layers and split-outs that merely add names or navigation.

Do not split a coherent function solely to meet a line-count or complexity
threshold. Use metrics and tool findings to locate candidates, not as proof of
improvement or permission to edit. Follow required project checks; do not impose
new universal thresholds. A one-use helper or single-implementation interface
can be justified by a real concept, information hiding, or a necessary test
boundary. Speculative future reuse cannot justify it. Do not add wrappers,
aliases, helper classes, or options solely to make a rearrangement possible.

Trace data through producers and consumers before removing repeated transforms,
indexes, validation, or deduplication. Check whether upstream contracts already
guarantee the same property on every relevant path and whether that guarantee
survives intervening mutation. Remove a redundant operation only when its
result, error behavior, and effects are preserved. Do not infer redundancy from
similar syntax or one caller; retain checks at trust boundaries and compatibility
paths that still protect supported consumers.

## Migrate coherent boundaries

Complete each boundary change coherently: move or rename the implementation,
update imports, callers, tests, configuration, entrypoints, packaging, and docs,
then retire stale internal references. Inspect runtime discovery and string-based
references as well as static imports. Account for path casing on supported
platforms. Change generated artifacts through their maintained sources.

Verify each coherent boundary change before building further changes on it.
Keep coupled edits together across files and folders; checkpoints separate
independent units rather than leaving their callers temporarily unmigrated.
Choose names with their final responsibilities instead of performing a cosmetic
rename pass over a structure that still needs to change.

Migrate internal names together with their in-Scope consumers and remove stale
aliases. Preserve supported external contracts unless their migration is
authorized; retain compatibility where a consumer or supported interface needs
it. When exposure remains materially uncertain, investigate before changing the
boundary and use Loopy's existing question rules if evidence cannot resolve it.

## Fix encountered bugs

Correct regressions introduced by the refactor and pre-existing or potential
bugs supported by a concrete code path or evidence in the requested scope.
These fixes belong to the refactoring Outcome even when the defect predates the
baseline; the general rule about unrelated baseline failures is not a reason to
leave an encountered, in-scope defect unfixed. A project-wide request covers
encountered defects throughout that project, without requiring a separate
exhaustive bug hunt.

Check the intended contract before calling behavior a bug. Reproduce the failure
when safe and practical; otherwise record the concrete static evidence and the
remaining uncertainty. Fix the cause and add a focused regression check when it
can distinguish the failure from the intended result. Keep bug fixes identifiable
in the changes, evidence, and report. Where practical, verify structural moves
and behavioral corrections separately without leaving coupled migrations
incomplete or requiring separate approvals or commits. An observation of a known
bug may establish the baseline, but final regression checks must protect the
intended contract. Do not silently rewrite expected outputs or weaken valid
tests simply to make the new implementation pass.

Do not invent requirements or new features under the name of bug fixing. When
intended behavior is materially ambiguous or a correction needs an excluded
change, use Loopy's existing question and Decision rules. Retain the unresolved
issue while continuing independent authorized work.

## Verify and finish

Verify both behavior and structure. Compare relevant behavior against the
baseline, with explicit expected differences for bug fixes. Behavior includes
relevant errors, state mutation, external I/O, resource cleanup, and the count
and order of observable effects, not just return values. When those properties
are affected, check them through stable boundaries rather than freezing private
helper calls or incidental implementation structure into tests.

Exercise affected entrypoints, integration boundaries, and packaging or discovery
paths when changed; compilation and static import checks alone may miss broken
runtime references. Run project-wide checks appropriate to a project-wide change,
and state material coverage gaps when adequate checks are unavailable.

Inspect the resulting dependency direction, ownership, vocabulary, and remaining
references against the structural criteria. For a material boundary decision,
compare a plausible alternative by ownership, lifecycle, caller burden, and
public compatibility. This comparison or a material regression check can supply
Loopy's Challenge; reuse adequate evidence instead of starting another review
cycle.

Finish only when the requested areas have been assessed, accepted structural
changes and supported in-scope bugs have been resolved, dependent migrations are
complete, and the Completion Gate passes. Assess new findings by the same
criteria; do not reopen satisfied decisions for speculative polish or declare
project-wide completion from one repaired area. If evidence or authorization
prevents completion, report the remaining areas and use the existing Decision
rules. The final report should briefly identify the structural and naming
changes, intentional bug fixes, verification evidence, and material limitations.

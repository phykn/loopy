# Refactoring

Refactoring keeps the supported behavior or meaning while making the structure
clearer and the code or text shorter, since less to read is easier to
understand. Structural improvement, reduction, and fixes for supported bugs
found along the way all belong to the Outcome. A project-wide request covers
folder and file structure, names, responsibilities, and dependencies across the
project; a narrower request keeps its stated boundary. A read-only assessment
yields findings only, including under the bug and migration rules below.

## Documents

READMEs, guides, wikis, skills, and prompts follow the same steps with these
counterparts:

- Structure and names: group content by meaning into files and sections with
  plain names, and give each topic one owning place that others link to.
- Preserved behavior: accepted claims, scope, procedures, commands, examples,
  and the links, anchors, and paths that other files, code, or tools rely on.
  Record them before editing and confirm afterward that none was lost or
  changed in meaning.
- Reduction: remove repetition, sentences that restate a heading or nearby
  text, filler, and stale content, and merge sections that answer the same
  reader question, keeping necessary premises, precision, and caveats.
- Bugs: wrong claims, broken commands or links, and contradictions that
  evidence supports, checked against the code or source they describe.
- Migrations: when content moves, update links, anchors, indexes, and any code
  or configuration that reads or names the document.
- Reader tasks: find where a topic is explained, follow a procedure, or make a
  decision from the text.

## Establish the target

Before choosing boundaries, inspect project instructions, the working tree,
major components, entrypoints, dependency direction, tests, and build or
packaging configuration, and trace the main user paths, external consumers, and
persisted formats.

Base compatibility on supported interfaces and their consumers. An importable
module, non-private symbol, or configuration key is not automatically a
contract; documentation, exports, packaging, known consumers, and persisted data
distinguish internal names from supported imports, commands, settings, formats,
and checkpoints. A published interface may have outside consumers even when none
appear locally.

For a project-wide request, keep a compact coverage record of the major areas
and their status (inspected, needing change, verified, or blocked), extended as
new dependencies appear. Inspect each area enough to judge its responsibilities
and connections; coverage neither means changing every file nor ends after the
first convenient module is tidied.

Turn the request into observable structural criteria, such as one owner per
lifecycle, no dependency cycles, distinct names for distinct concepts, one call
shape for related operations, or less code for the same behavior, and ground
each change in actual responsibilities, consumers, confusing uses, or repeated
changes; working code can still need restructuring. Existing organization is
evidence, not a default constraint: keep what fits, and impose no stock
directory tree, abstraction layer, or personal naming style without a benefit
here.

Settle responsibility boundaries and dependency direction before target paths
and names. Briefly state the intended organization and significant migrations
before editing, starting with changes that unblock others, then proceed; a broad
internal move needs no renewed approval. Refine the plan as dependencies become
clear.

## Establish baselines

Capture affected behavior with existing tests, representative runs, or focused
characterization checks, including supported inputs and boundary cases visible
in the code or callers, not only those already tested. Characterization records
what the code does, not whether it is correct; run it before the change and
compare afterward. Record known failures and unverified areas, and record
suspicious behavior to resolve under the bug-fix rules below.

If the code cannot be usefully observed, isolate the dependency that blocks
verification with the smallest useful seam, a place to observe or substitute an
input or effect, preferring existing interfaces over new injection or adapters.
Without a reliable baseline, keep that change minimal, record the gap, and add
checks before broader changes; a seam alone is not evidence of preserved
behavior. Retire temporary probes and scaffolding once stable boundaries cover
the behavior, keeping justified testability improvements.

For substantial structural changes, also run reader tasks through [Independent
use](independent-use.md) before and after the change, keeping them fixed for the
comparison: a maintainer with the expected domain knowledge but no project
history, starting from the normal entrypoints and docs, finds the first
execution path, traces a core value from producer to consumer, identifies units
and configuration precedence, or locates a requested change and its affected
callers. Ask for answers, source locations, and actual obstacles without
supplying the author's architecture explanation or expected weak spots, and
check reported confusion against call paths and data flow.

## Reduce and reshape

Reshape code toward [Code](code.md) and documents toward the counterparts above.
Reassess names together with responsibilities, renaming to resolve misleading
meaning, inconsistent vocabulary, or ambiguity.

Remove what the supported behavior or meaning does not need: duplicated
knowledge with the same reason to change (not coincidental textual similarity),
obsolete internal paths once their consumers migrate, pass-through layers, and
whatever [Code](code.md) excludes. When code reads a removed docstring, such as
`__doc__` for CLI help, move the text to that use. Removing handling that
changes an observable result is a behavior change under the bug-fix rules, not
cleanup.

Reduce the amount, not legibility: do not merge statements, shorten names beyond
convention, compress prose into fragments, or inline a real concept to save
lines. Added code, such as a seam, helper, or interface, must remove more burden
than it adds. In tests, merge duplicates and drop tests that freeze private
structure while keeping coverage of supported contracts.

Before removing a repeated transform, index, validation, or deduplication, trace
the data through its producers and consumers, and check whether upstream
contracts guarantee the same property on every relevant path and whether that
guarantee survives intervening mutation. Remove the operation only when its
result, error behavior, and effects are preserved. Similar syntax or a single
caller does not prove redundancy; keep checks at trust boundaries and on
compatibility paths that still protect supported consumers.

## Migrate coherent boundaries

Move or rename an implementation together with its imports, callers, tests,
configuration, entrypoints, packaging, and docs, checking runtime discovery and
string-based references as well as static imports, then retire stale internal
references. Mind path casing on supported platforms, and change generated
artifacts through their sources.

Verify each boundary change before building on it, then look for code it made
unnecessary, such as aliases, adapters, and helpers left with one caller. Keep
coupled edits together; checkpoints separate independent units and never leave
callers unmigrated. Choose names for their final responsibilities instead of a
cosmetic rename pass over a structure that will still change.

Keep supported external contracts unless their migration is authorized, and
retain compatibility where a consumer or supported interface needs it. When
exposure is materially uncertain, investigate before changing the boundary, and
ask if the evidence cannot settle it.

## Fix encountered bugs

Fix regressions from the refactor and pre-existing or potential bugs in the
requested scope that a concrete code path or other evidence supports, even when
they predate the baseline. A project-wide request covers defects encountered
anywhere in the project, without a separate exhaustive hunt.

Check the intended contract before calling behavior a bug. Reproduce the failure
when safe and practical, or record the static evidence and remaining
uncertainty. Fix the cause and add a focused regression check when it can tell
the failure from the intended result. A baseline may record a known bug, but the
final checks protect the intended contract; never silently rewrite expected
outputs or weaken valid tests to make the new code pass. Where practical, verify
structural moves and behavior fixes separately, without splitting coupled
migrations or requiring separate approvals or commits.

Keep bug fixes identifiable in the changes, evidence, and report; they may add
code, so report them apart from reductions rather than skipping them to lower
the total. Do not invent requirements or features in the name of bug fixing.
When the intended behavior is materially ambiguous or a fix needs an excluded
change, apply Loopy's question and decision rules, and keep the issue open while
continuing other authorized work.

## Verify and finish

Compare relevant behavior with the baseline, with explicit expected differences
for bug fixes. Behavior includes errors, state mutation, external I/O, resource
cleanup, and the count and order of observable effects, not just return values;
when these are affected, check them through stable boundaries rather than
private helper calls. Exercise affected entrypoints, integration boundaries, and
packaging or discovery paths, since compiling and static imports can miss broken
runtime references. Run project-wide checks for a project-wide change, and state
material coverage gaps.

Check the result's dependency direction, ownership, vocabulary, remaining
references, and still-removable code or text against the structural criteria.
For a material boundary decision, compare a plausible alternative by ownership,
lifecycle, caller burden, and public compatibility; that comparison or a
material regression check can serve as Loopy's challenge.

After substantial structural changes, also test relevant README commands and
examples against the actual entrypoints and outputs. Fix confusing structure or
names at their source, using concise docs for necessary domain assumptions and
rationale. Neither a passing test suite nor a reader's confidence alone proves
both preserved behavior and understandable structure.

Finish only when the requested areas are assessed, accepted structural changes
and supported in-scope bugs are resolved, dependent migrations are complete, and
Loopy's `done` conditions hold. Do not reopen settled decisions for speculative
polish or claim project-wide completion from one repaired area; if evidence or
authorization prevents completion, report the remaining areas. The final report
briefly gives the structural and naming changes, the line change for source,
tests, and docs with bug-fix additions identified, intentional bug fixes,
verification evidence, and material limits.

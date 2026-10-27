# Refactoring

Refactoring keeps supported behavior and meaning while making the structure
clearer and the code or text shorter, and fixes supported bugs found along the
way. A project-wide request covers folder and file
structure, names, responsibilities, and dependencies across the project; a
narrower request keeps its stated boundary.

## Establish the target

Inspect project instructions, entrypoints, dependency direction, tests, and
build or packaging configuration, and trace the main user paths, external
consumers, and persisted formats. Base compatibility on supported interfaces:
documentation, exports, packaging, known consumers, and persisted data separate
supported imports, commands, settings, and formats from internal names, and a
published interface may have outside consumers that do not appear locally.

For a project-wide request, keep a compact coverage record of the major areas
and their status, and assess each area's responsibilities and connections;
coverage neither means changing every file nor ends after the first tidied
module.

Turn the request into observable structural criteria, such as one owner per
lifecycle, no dependency cycles, or less code for the same behavior, grounded in
actual responsibilities and confusing uses. Existing organization is evidence,
not a default constraint, and a stock directory tree or layer needs a benefit
here. Settle responsibility boundaries before names and state the intended
organization briefly before editing; a broad internal move needs no renewed
approval.

## Establish baselines

Capture affected behavior with existing tests, representative runs, or
characterization checks, including supported inputs and boundary cases visible
in the code or callers, not only those already tested. Characterization records
what the code does, not whether it is correct; record suspicious behavior for
the bug rules below. If the code cannot be observed, add the smallest seam that
lets a check run, preferring existing interfaces, and record the gap until
checks cover it.

## Reduce and reshape

Reshape code toward [Code](code.md), renaming to resolve misleading meaning,
inconsistent vocabulary, or ambiguity. Remove what the supported behavior does
not need: duplicated knowledge with the same reason to change, obsolete internal
paths once their consumers migrate, pass-through layers, and whatever Code
excludes. When code reads a removed docstring, such as `__doc__` for CLI help,
move the text to that use.

Reduce the amount, not legibility: do not merge statements, shorten names beyond
convention, compress prose into fragments, or inline a real concept to save
lines. Added code must remove more burden than it adds. In tests, merge
duplicates and drop tests that freeze private structure while keeping coverage
of supported contracts.

Before removing a repeated transform, validation, or deduplication, trace the
data through its producers and consumers and confirm that upstream contracts
guarantee the same property on every relevant path, including after intervening
mutation. Similar syntax or a single caller does not prove redundancy; keep
checks at trust boundaries and on compatibility paths. Removing handling that
changes an observable result is a behavior change under the bug rules, not
cleanup.

## Documents

READMEs, guides, wikis, skills, and prompts follow the same steps:

- Group content by meaning into files and sections with plain names, and give
  each topic one owning place that others link to.
- Preserve accepted claims, procedures, commands, examples, and the links,
  anchors, and paths other files or tools rely on; list them before editing and
  confirm afterward that none was lost or changed in meaning.
- Remove repetition, sentences that restate a heading or nearby text, filler,
  and stale content, keeping necessary premises, precision, and caveats.
- Treat wrong claims, broken commands or links, and contradictions as bugs,
  checked against the code or source they describe.
- When content moves, update links, indexes, and any code or configuration that
  names the document.

## Migrate coherent boundaries

Move or rename an implementation together with its imports, callers, tests,
configuration, entrypoints, packaging, and docs, checking runtime discovery and
string references as well as static imports, and path casing on supported
platforms. Change generated artifacts through their sources. Verify each
boundary change before building on it, then remove the aliases, adapters, and
helpers it made unnecessary.

Keep supported external contracts unless their migration is authorized, and
retain compatibility where a consumer or supported interface needs it. When
exposure is materially uncertain, investigate before changing the boundary, and
ask if the evidence cannot settle it.

## Fix encountered bugs

Fix regressions from the refactor and pre-existing bugs in the requested scope
that a concrete code path or other evidence supports; a project-wide request
covers defects encountered anywhere, without a separate exhaustive hunt. Check
the intended contract before calling behavior a bug, reproduce the failure when
safe and practical or record the static evidence, fix the cause, and add a
regression check when one can tell the failure from the intended result. A
baseline may record a known bug, but never silently rewrite expected outputs or
weaken valid tests to make the new code pass.

Report bug fixes apart from reductions, since they may add code, and do not
invent requirements in their name. When the intended behavior is materially
ambiguous or a fix needs an excluded change, apply Loopy's question and decision
rules and keep the issue open.

## Verify and finish

Compare behavior with the baseline, with explicit expected differences for bug
fixes. Behavior includes errors, state mutation, external I/O, resource cleanup,
and the count and order of effects, not just return values; check these through
stable boundaries. Run the project's required checks, and project-wide checks
for a project-wide change. Exercise affected entrypoints and packaging or
discovery paths, since static imports miss broken runtime references, test
README commands against actual outputs, and search for remaining references to
moved or removed names. Check the result against the structural criteria,
including code or text that can still be removed. For substantial structural
changes, also run a fixed reader task through
[Independent use](independent-use.md) on the result, such as a maintainer
without project history locating a requested change and its callers.

Finish when the requested areas are assessed, accepted structural changes and
supported in-scope bugs are resolved, dependent migrations are complete, and
Loopy's `done` conditions hold. Do not claim project-wide completion from one
repaired area or reopen settled decisions for speculative polish. Report the
structural and naming changes, the line change for source, tests, and docs with
bug-fix additions identified, the bug fixes, the evidence, and material limits.

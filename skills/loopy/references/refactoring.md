# Refactoring

Refactoring keeps supported behavior and meaning while making structure clearer and code or text shorter. A project-wide request covers folder and file structure, names, responsibilities, and dependencies everywhere; a narrower request keeps its boundary.

## Establish the target

Trace entrypoints, tests, packaging, main user paths, external consumers, and persisted formats. Base compatibility on supported interfaces, which documentation, exports, packaging, known consumers, and persisted data separate from internal names; a published interface may have unseen outside consumers. Keep supported external contracts unless their migration is authorized, and compatibility that a consumer still needs; investigate uncertain exposure before changing a boundary.

For a project-wide request, keep a short record of each major area and its status; coverage neither means changing every file nor ends with the first tidied module.

Turn the request into observable structural criteria grounded in actual responsibilities and confusing uses, such as one owner per lifecycle or no dependency cycles. A stock directory tree or layer needs a benefit here. Settle responsibility boundaries before names, and state the intended organization briefly before editing, without waiting for approval.

## Establish baselines

Capture affected behavior with existing tests, representative runs, or characterization checks, covering supported inputs and boundary cases visible in the code or callers, not only tested ones. Characterization records what the code does, not whether it is right; note suspicious behavior as a possible bug. If code cannot be observed, add the smallest seam that lets a check run.

## Reduce and reshape

Reshape code toward [Code](code.md). Remove what supported behavior does not need: duplicated knowledge with the same reason to change, obsolete internal paths once their consumers migrate, pass-through layers, and whatever Code excludes. When code reads a removed docstring, such as `__doc__` for CLI help, move the text to that use.

Reduce the amount, not legibility: do not merge statements, shorten names beyond convention, compress prose into fragments, or inline a real concept to save lines. In tests, merge duplicates and drop tests that freeze private structure, keeping coverage of supported contracts.

Before removing a repeated transform, validation, or deduplication, confirm by tracing producers and consumers that upstream contracts guarantee the property on every path, including after mutation. Similar syntax or a single caller does not prove redundancy; keep checks at trust boundaries and on compatibility paths. Removing handling that changes an observable result is a bug-fix decision, not cleanup.

## Documents

READMEs, guides, skills, and prompts follow the same steps, plus:

- Group content by meaning into plainly named files and sections, with one owning place per topic that others link to.
- Before editing, list the accepted claims, procedures, commands, examples, and the links, anchors, and paths others rely on; afterward, confirm none was lost or changed in meaning.
- Remove repetition, sentences that restate a heading or nearby text, filler, and stale content, keeping necessary premises, precision, and caveats.
- Treat wrong claims, broken commands or links, and contradictions as bugs, checked against the code or source.
- When content moves, update links, indexes, and any code or configuration that names the document.

## Migrate coherent boundaries

Move or rename an implementation with its imports, callers, tests, configuration, entrypoints, packaging, and docs, checking runtime discovery, string references, and path casing, not only static imports. Change generated artifacts through their sources. Verify each boundary change before building on it, then remove the aliases, adapters, and helpers it made unnecessary.

## Fix encountered bugs

Fix regressions and pre-existing in-scope bugs that a concrete code path or other evidence supports, as [Debug](debug.md) steps; a project-wide request covers defects met anywhere, without a separate hunt. Record static evidence when reproducing is unsafe. Never silently rewrite expected outputs or weaken valid tests to make new code pass. Report bug fixes apart from reductions, since they may add code. When the intended behavior is materially ambiguous or a fix needs an excluded change, keep the issue open.

## Verify and finish

Compare behavior with the baseline, expecting only the bug fixes' explicit differences. Behavior includes errors, state mutation, external I/O, resource cleanup, and the count and order of effects, not just return values; check them through stable boundaries. Exercise affected entrypoints and packaging or discovery paths, test README commands against actual outputs, and search for leftover references to moved or removed names. Check the result against the structural criteria, including what can still be removed.

`done` also needs the requested areas assessed, accepted structural changes and supported in-scope bugs resolved, and dependent migrations complete; one repaired area is not project-wide completion. Report structural and naming changes, the line change for source, tests, and docs with bug-fix additions marked, and the bug fixes.

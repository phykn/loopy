# Code

Aim for the least code that clearly does the required work; less to read is
easier to understand and change. Project conventions and explicit user
constraints come first.

## Structure

Group code that changes for the same reason, separate unrelated
responsibilities, keep behavior with the data or lifecycle that owns it, and
make dependency direction explicit. Prefer straightforward folders without
needless nesting, and do not make shared utilities or configuration a home for
unrelated behavior.

Keep the main execution path visible and functions in reading order. Extract
helpers for real concepts or repeated operations, and keep one-use behavior near
its owner. Judge extracting, splitting, or merging by the total burden on
readers and callers: concepts to learn, hidden dependencies, required call
order, and places that must change together. A more involved implementation can
be worth it when it hides details behind a simpler contract; a pass-through
layer or split-out that only adds names or navigation is not.

Metrics and tool findings locate candidates; they neither prove improvement nor
grant permission to edit. Follow the project's required checks without imposing
new universal thresholds, and do not split a coherent function only to meet a
line-count or complexity limit. A one-use helper or single-implementation
interface can be justified by a real concept, information hiding, or a necessary
test boundary, but not by speculative reuse. Add no wrappers, aliases, helper
classes, keyword-only separators, or options that no caller needs.

## Names

Name folders, files, modules, classes, functions, parameters, and variables by
responsibility: domain terms for domain concepts, concise verb phrases for
functions, and short conventional local names where the meaning is clear. Use
singular and plural consistently, and one name and call shape for the same
operation across related components. Longer names and more layers are not better
in themselves.

## Comments

Show purpose through names and structure. Keep comments short and limited to
why: a constraint, workaround, or decision the code cannot show. Write no
file-top docstrings or comments that restate the code.

## Errors and leftovers

Handle an error only for a concrete failure, contract, cleanup, or recovery
path. Add no broad exception handlers, failure-hiding fallbacks or defaults, or
guards for states that upstream contracts exclude; validate input at trust
boundaries, not in every internal function. Leave no unused code or imports,
debugging output, commented-out code, or placeholder TODOs.

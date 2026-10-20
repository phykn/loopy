# Code

Use this guidance within Loopy's workflow whenever code is written, changed, or
assessed. Aim for the least code that clearly does the required work: less to
read is easier for both people and agents to understand and change. Project
conventions and explicit user constraints take precedence.

## Structure

Group code that changes for the same reason. Keep behavior with the data or
lifecycle that owns it; split unrelated responsibilities and make dependency
direction explicit. Prefer straightforward folders with little unnecessary
nesting. Do not turn shared utilities or configuration into a home for unrelated
behavior.

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
aliases, helper classes, keyword-only separators, or options that no caller
needs.

## Names

Name folders, files, modules, classes, functions, parameters, and variables by
their responsibilities. Prefer domain terms for domain concepts, concise verb
phrases for functions, and short conventional local names where their meaning
is clear. Use singular and plural consistently and the same name and call shape
for the same operation across related components. Longer names and more layers
are not inherently better.

## Comments

Make purpose visible through names and structure. Keep comments short and
focused on why: a constraint, workaround, or decision the code cannot show by
itself. Do not write docstrings at the top of files or comments that restate
what the code already says.

## Errors and leftovers

Handle an error only for a concrete failure, contract, cleanup, or recovery
path. Do not add broad exception handlers, fallbacks or defaults that hide
failures, or guards for states that upstream contracts exclude. Validate input
at trust boundaries rather than again inside every internal function.

Do not leave unused code or imports, debugging output, commented-out code, or
placeholder TODOs.

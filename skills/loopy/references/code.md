# Code

Write the least code that clearly does the required work. Project conventions and the user's explicit constraints come first.

## Structure

Group code that changes for the same reason, separate unrelated responsibilities, keep behavior with the data or lifecycle that owns it, and make dependency direction explicit. Avoid needless folder nesting and shared utilities or configuration that collect unrelated behavior.

Keep the main execution path visible and functions in reading order. Extract a helper or interface only for a real concept, repeated operation, information hiding, or needed test boundary, never for speculative reuse; keep one-use behavior near its owner. Judge extracting, splitting, or merging by the total burden on readers and callers, such as concepts to learn and places that change together; a layer that only adds names or navigation does not lower it.

Metrics and tool findings only locate candidates; do not split a coherent function to meet a line-count or complexity limit. Add no wrappers, aliases, helper classes, keyword-only separators, or options that no caller needs.

## Names

Name things by responsibility: domain terms for domain concepts, short verb phrases for functions, and short conventional names for clear locals. Use singular and plural consistently, and one name and call shape per operation across related components.

## Comments

Keep comments short and limited to why: a constraint, workaround, or decision the code cannot show. Write no file-top docstrings or comments that restate the code.

## Errors and leftovers

Handle an error only for a concrete failure, contract, cleanup, or recovery path. Add no broad exception handlers, failure-hiding fallbacks or defaults, or guards for states that upstream contracts exclude; validate input at trust boundaries, not in every internal function. Leave no unused code or imports, debugging output, commented-out code, or placeholder TODOs.

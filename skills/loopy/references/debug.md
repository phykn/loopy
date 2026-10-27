# Debug

Diagnosis confirms why the result breaks its contract. An assessment that asks
for a cause stops after it and changes nothing; debugging then fixes that cause
and nothing else.

## Diagnose

Take the expected result from the contract, such as docs, tests, callers, and
stated rules, not from the report or the current output. Reproduce it before
editing, with the reported command or the smallest failing input, and record the
expected and actual results. If it does not reproduce, do not fix on
speculation: narrow it down with logging, smaller inputs, or `git bisect`, and
report what you ran. If the contract is materially ambiguous, or a consumer may
rely on the current behavior, apply Loopy's question rules.

State the cause as a testable claim: which input reaches which code, and why
that produces the symptom. Confirm it with an observation the claim predicts,
such as a value, a test, or a log line, before any fix. Trace back to where the
wrong value or state first appears; other paths that share its assumption are
the same bug.

Do not change code to see whether the symptom goes away. Special-casing the
input, clamping or adjusting the output, or catching the error hides the
symptom, and "it worked when I tried it" is not evidence of the cause. A cause
you cannot explain is unconfirmed: keep investigating, or report it so, as
"symptom resolved, cause unconfirmed" if a change hid the symptom. An
assessment reports the claim, the observation that confirmed it, and where the
cause lives.

## Fix

Fix the code where the cause lives. Write a regression test at the level the
contract is stated and watch it fail on the original code for the predicted
reason, so reverting the fix brings the failure back. If several things
changed, keep only what the fix needs. Change an existing test's expectation
only when it encodes the bug, and say so. Keep the diff to the cause, its test,
and the docs or callers that state the wrong behavior; a nearby smell that
breaks no contract stays.

Rerun the reproduction, the existing tests, and the changed code's boundary
cases. A narrow fix needs no independent use trial unless users must now do or
read something different.

It is done when you can explain why it failed and why the change fixes it.
Report the cause, the fix, and the test's before and after results, and list
anything else noticed apart, unchanged.

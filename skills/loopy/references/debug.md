# Debug

Debugging confirms why the result breaks its contract, then fixes that cause and nothing else.

## Diagnose

Take the expected result from the contract, such as docs, tests, callers, and stated rules, not from the report or current output. Before editing, reproduce the failure with the reported command or smallest failing input, recording the expected and actual results. If it does not reproduce, narrow it down with logging, smaller inputs, or `git bisect` rather than fix on speculation. When the contract is ambiguous or a consumer may rely on current behavior, follow [Define success](../SKILL.md#define-success) on asking.

State the cause as a testable claim: which input reaches which code, and why that produces the symptom. Before any fix, confirm it with an observation the claim predicts, such as a value, test, or log line. Trace back to where the wrong value or state first appears; other paths sharing its assumption are the same bug.

Do not change code to see whether the symptom goes away. Special-casing the input, clamping or adjusting the output, or catching the error hides the symptom. A cause you cannot explain is unconfirmed: keep investigating, or report it so, as "symptom resolved, cause unconfirmed" if a change hid the symptom.

An assessment that asks for a cause stops here, changes nothing, and reports the claim, the confirming observation, and where the cause lives.

## Fix

Write a regression test at the level the contract states and watch it fail on the unfixed code for the predicted reason, so reverting the fix brings the failure back. If several things changed, keep only what the fix needs. Change an existing test's expectation only when it encodes the bug, and say so. Keep the diff to the cause, its test, and the docs or callers stating the wrong behavior; leave a nearby smell that breaks no contract.

Rerun the reproduction, the existing tests, and the changed code's boundary cases. You are done when you can explain why it failed and why the change fixes it. Report the cause, the fix, and the test's results before and after, and list anything else you noticed apart, unchanged.

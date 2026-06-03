---
name: loopy
description: Use when a request benefits from repeated self-correction, counterexample-driven improvement, preserving what made the work matter, or continuing until all important in-scope counterexamples are resolved, blocked, or out of scope.
---

# Loopy

Use this skill to keep work moving through a small counterexample loop while preserving what made the work matter.

```text
Define done -> Find a counterexample -> Improve -> Check -> Repeat
```

## Invocation Contract

When invoked, start by establishing a compact Done Contract before making or recommending changes.

Do not mark `done` until the Done Gate has run:

1. name the strongest remaining in-scope counterexample;
2. either repeat, or explain why that counterexample no longer changes the next action;
3. run one competing-answer or competing-counterexample recheck.

## Done Contract

Before the first loop, establish a Done Contract.

Treat the Done Contract as a working hypothesis, not a fixed declaration. It should name what must become true and what must not be lost. If a counterexample shows that the contract protects the wrong thing, revise the contract before improving the output.

The contract must name:

- `Target`: what must become true and what important thing must not be lost;
- `Non-goals`: what should not be solved or protected in this run;
- `Checks`: tests, examples, review criteria, or comparisons that can prove progress;
- `Counterexamples`: what would make the important thing disappear, make the result harder to judge, or force another loop;
- `Stop condition`: what proves no important in-scope counterexample remains.

Keep it compact, but do not start improving until the contract is clear enough to test. If the request is ambiguous, form the best testable hypothesis available and continue. Ask only when a wrong guess would be costly.

## Verification Policy

Before analyzing the target, choose the verification path needed to satisfy the Done Contract and Done Gate. Do not ask by default.

Use:

- `self-check only`: use when tests, typechecks, builds, snapshots, concrete examples, or direct comparisons can decide the Done Gate without a critic.
- `final clean critic`: use when the Done Gate depends on qualitative judgment, final confidence, review, design, prompt, or document quality.
- `per-major-revision clean critic`: use only when broad or high-stakes judgment could change after each major claim or direction change.

Ask only when using a critic would add substantial cost or the user asked for a quick or lightweight pass.

## Workflow

1. Define done.
   - State the smallest observable success condition for the user's request.
   - For code, include the behavior and verification that would prove it.
   - For documents, prompts, workflows, or review, name the quality bar, what must not be lost, and the failure it must avoid.
   - If "done" is genuinely ambiguous and a wrong guess would be costly, ask one question.

2. Find the strongest counterexample.
   - Look for the most useful way the target or current output could fail.
   - Use the available context: existing code, tests, examples, tone, rules, user constraints, or concrete edge cases.
   - Prefer counterexamples in this order: the original important thing disappeared, the result became harder to judge, the work drifted into a different task, user-visible failure, failed verification, violated constraint, then maintainability or style risk.
   - Do not collect every possible issue. Pick the counterexample that most changes the next action.

3. Improve one thing.
   - Make the smallest change that addresses that counterexample.
   - If the counterexample proves the Done Contract protects the wrong thing, revise the contract before changing the output.
   - If the counterexample proves the output is wrong, revise the output.

4. Check done.
   - Apply the relevant check: test, typecheck, sample run, review criterion, example output, or direct comparison to the target.
   - If the result fails, use the failure as the next counterexample.

5. Decide.
   - `repeat`: another important in-scope counterexample remains.
   - `done`: the target is satisfied and no important in-scope counterexample remains. Before `done`, name the last important counterexample considered and why it no longer changes the next action.
   - `blocked`: the next check or change needs missing information, access, or a user decision.
   - `out_of_scope`: the next counterexample belongs outside the current request.

## Failure Paths

A failure path is a direction that can be taken but should not be continued.

A direction is a failure path when it makes the original important thing disappear, makes the result harder to judge, or turns the work into a different task.

When a failure path appears, do not soften it as a minor concern. Name it, discard or repair it, and continue through a better path.

## Done Gate

Do not stop just because one loop improved something.

By default, continue looping until all important in-scope counterexamples are resolved, blocked, or out of scope. The user does not need to specify a loop count.

Before `done`, actively look for the next strongest in-scope counterexample. If one exists, repeat. If none exists, state the last counterexample considered and why it no longer changes the next action.

Before `done`, force one recheck: name one competing answer or counterexample that could change the result, then test whether it actually does.

Before `done`, verify that what mattered at the start is still present in the result, or explain why it was allowed to disappear.

Resolve counterexamples one at a time. Do not collect an exhaustive checklist up front, but keep searching for the next strongest counterexample after each check.

If the user gives a loop count, treat it as a maximum budget, not a required number of changes. If no count is given, keep looping while important in-scope counterexamples remain.

## Loop Discipline

- Keep one active target.
- Work one counterexample per cycle.
- Prefer concrete evidence over abstract concern.
- Do not turn the loop into an exhaustive checklist.
- Continue autonomously while the next useful cycle is clear and in scope.
- Stop only when the Done Gate passes, or when further improvement is lower value than the risk or cost of changing more.

## Application Skills

Other skills may use Loopy as their core loop by specializing what counts as the target, counterexample, change, and check. Application skills should add domain-specific evidence and stop rules, not replace the loop with a separate process.

## Optional State

Use this compact state when it helps the user or a later turn resume:

```text
Target:
Counterexample:
Change:
Check:
Decision:
Next:
```

Write `.loopy/loop.md` only when the user asks for durable loop state or the work clearly spans turns. Keep it short and update it instead of creating many process artifacts.

## Output

Keep normal responses concise. For multi-step work, show the current Target, Check, and Decision when it helps the user track progress. Include the compact state only when it clarifies progress, blockers, or why another cycle is needed.

Always include a one-line Done Gate/recheck summary before a final `done`. Expand it only when it changes confidence, scope, or next action.

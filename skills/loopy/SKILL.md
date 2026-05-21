---
name: loopy
description: Use when a request benefits from repeated self-correction, counterexample-driven improvement, or continuing until the current target is done, blocked, or out of scope.
---

# Loopy

Use this skill to keep work moving through a small counterexample loop.

```text
Define done -> Find a counterexample -> Improve -> Check -> Repeat
```

## Workflow

1. Define done.
   - State the smallest observable success condition for the user's request.
   - For code, include the behavior and verification that would prove it.
   - For writing, prompts, narration, or design, name the quality bar and the failure it must avoid.
   - If "done" is genuinely ambiguous and a wrong guess would be costly, ask one question.

2. Find the strongest counterexample.
   - Look for the most useful way the target or current output could fail.
   - Use the available context: existing code, tests, examples, tone, rules, user constraints, or concrete edge cases.
   - Prefer a counterexample that would break the user's goal, can be checked now, and would change the next action if true.
   - Do not collect every possible issue. Pick the counterexample that most changes the next action.

3. Improve one thing.
   - Make the smallest change that addresses that counterexample.
   - If the counterexample proves the target is wrong, revise the target before changing the output.
   - If the counterexample proves the output is wrong, revise the output.

4. Check done.
   - Apply the relevant check: test, typecheck, sample run, review criterion, example output, or direct comparison to the target.
   - If the result fails, use the failure as the next counterexample.

5. Decide.
   - `repeat`: another important in-scope counterexample remains.
   - `done`: the target is satisfied and no important in-scope counterexample remains. Before `done`, name the last counterexample considered and why it is no longer important.
   - `blocked`: the next check or change needs missing information, access, or a user decision.
   - `out_of_scope`: the next counterexample belongs outside the current request.

## Loop Discipline

- Keep one active target.
- Work one counterexample per cycle.
- Prefer concrete evidence over abstract concern.
- Do not turn the loop into an exhaustive checklist.
- Continue autonomously while the next useful cycle is clear and in scope.
- Stop when further improvement is lower value than the risk or cost of changing more.

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

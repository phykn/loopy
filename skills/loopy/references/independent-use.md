# Independent use

A fresh evaluator attempts a real task with only what the intended user would receive.

## Choose the attempt

Pick the intended user, their normal starting point, and the critical tasks the request implies, assuming their domain knowledge but not project conventions or the author's reasoning. Fix observable tasks before the trial: run an example, trace a requested change, follow a guide's procedure, or carry out a realistic request with a skill or prompt and inspect its actions and artifacts. Cover the distinct critical paths, not a fixed count, with one evaluator unless one task's answer would give away another's. Keep task wording, materials, environment, and evaluator capabilities comparable across a before and after comparison; a score never replaces the attempt.

## Give only normal user context

Use an agent or session that has not seen the implementation discussion, intended answers, suspected defects, or earlier findings, including after changes. In Claude Code, that is a non-fork Agent tool subagent; in Codex, a non-forking subagent or a new session. Run any trial that writes files in an isolated copy, and keep evaluation outputs out of maintained source and later trials.

The prompt is the evaluator's whole context: give the user's task, normal entrypoint, delivered materials, assumed knowledge, and permitted actions, and forbid modifying the source materials. Keep the acceptance oracle and your notes to yourself; neither withhold what a real user would have nor add hints they would lack, such as the purpose when discovering it is the task.

## Observe and use the attempt

Ask for an attempt, not a rating, with a concise report of the result, actions, supporting locations, and material confusion; you own corrections and the decision. Do not coach a stalled evaluator or rerun evaluators until one passes; record the obstacle and investigate it. Compare the actual outputs with the acceptance evidence yourself, check whether a success relied on guessing or knowledge the user would lack, and tell artifact problems from environment failures.

An agent trial shows agent use under its conditions, not human usability. When independent evaluation is unavailable or disallowed, run the strongest authorized check and state its limit; if independence is explicitly required or the remaining uncertainty could change completion, report that condition as unmet.

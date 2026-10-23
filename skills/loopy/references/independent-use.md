# Independent use

A fresh evaluator attempts a real task with only what the intended user would
receive. The result is evidence for Loopy's completion decision, not a second
workflow.

## Choose the attempt

Pick the intended user, their normal starting point, and the critical tasks the
request implies. Assume their domain knowledge but not project conventions or
the author's reasoning; a specialist artifact need not become a beginner
tutorial. Fix observable tasks before the trial, for example:

| Deliverable | Attempt | Useful evidence |
| --- | --- | --- |
| Code or API | Run an example; locate a requested change and trace its effects | Commands, outputs, cited definitions and callers |
| Guide or report | Follow a procedure; use the evidence to answer a concrete decision question | Actions, conclusion, source support, missing premises |
| Plan | Identify the first executable task, required inputs, owner, and completion condition | Correct next action and any actual dependency gaps |
| UI or automation | Complete a representative task from the normal entrypoint | Observed states, output, recovery behavior when relevant |
| Skill or prompt | Execute a realistic request using the supplied instructions | Actual actions and artifacts, preserved constraints, stopping decision |

Scale coverage to the distinct critical paths, not a fixed count. In a
before/after comparison, keep task wording, materials, environment, and
evaluator capabilities comparable, and record meaningful differences. A score
may summarize the evidence but never replaces the attempt.

## Give only normal user context

When delegation is permitted, use an agent or session that has not seen the
implementation discussion, intended answers, suspected defects, earlier
findings, or proposed fixes, and use the same isolation after changes. An agent
that inherits that history is not fresh.

- Claude Code: an Agent tool subagent of a type that starts without the
  conversation, not a fork, with worktree isolation or a temporary copy when it
  writes files.
- Codex: a subagent that does not fork the conversation, or a new session, with
  a temporary copy when it writes files.
- Other hosts: any mechanism that starts without the production history; if
  none does, the attempt is not independent.

The prompt is the evaluator's whole context, so do not summarize the production
work in it. Give the user's task, normal entrypoint, delivered materials with
their ordinary linked dependencies, assumed knowledge, and permitted resources
and side effects. Keep the acceptance oracle and production notes yourself, and
neither withhold what a real user would have nor add hints they would lack.
State the purpose when carrying out a known goal is the task, but not when
discovering the purpose is.

Use an isolated copy for any trial that writes files, and keep evaluation
outputs out of maintained source and later trials. When read-only, access, or
external-action limits exclude acting, use a bounded walkthrough and state what
execution remains unverified; evaluation never authorizes deployment, sending
messages, or destructive operations.

A compact request: "Starting from [entrypoint], use [materials] to [task]. You
may [permitted actions]. Report the actual result, evidence, and where you could
not proceed. Do not modify the source materials."

## Observe and use the attempt

Ask the evaluator to attempt the task, not to rate it, and to report the result,
actions actually taken, supporting locations, and material uncertainty or
confusion concisely, without private reasoning or a diary. The evaluator does
not commission another review, and its approval is not a gate; the main agent
owns corrections, evidence reuse, and the completion decision.

Do not coach a stalled evaluator into passing; record the obstacle and
investigate it. Check whether a success relied on guessing or on knowledge the
intended user would lack, and compare the actual outputs with the acceptance
evidence yourself, since confidence and agreement are not proof. Check confusion
against source behavior and the user's needs to separate artifact problems from
unsupported preferences, evaluator mistakes, unsuitable assumed knowledge, and
environment or permission failures. Never change tasks to hide failures or try
new evaluators until one passes. After a relevant revision, repeat the affected
task with a fresh evaluator and reuse unaffected evidence.

Completion needs the critical tasks to succeed and confirmed material obstacles
to be resolved, not universal praise. An agent trial shows agent use under its
conditions; do not report it as proof of human usability or of behavior in
untested environments.

When independent evaluation is unavailable or disallowed, run the strongest
authorized check from the normal entrypoint, label it a self-check or
walkthrough, and state the limitation. If independence is explicitly required
or the remaining uncertainty could change completion, report that condition as
unmet rather than approving the work yourself.

# Independent use

Use this guidance when a substantial deliverable's success depends on someone
understanding or using it without its production conversation. It supplies
evidence for Loopy's verification and completion decision, not a second workflow.

## Choose the attempt

Identify the intended user, their normal starting point, and one or more critical
tasks already implied by the request. Assume appropriate domain knowledge, not
knowledge of project conventions or the author's private reasoning. Do not turn
every specialist artifact into a beginner tutorial.

Choose observable tasks before the trial. Examples:

| Deliverable | Attempt | Useful evidence |
| --- | --- | --- |
| Code or API | Run an example; locate a requested change and trace its effects | Commands, outputs, cited definitions and callers |
| Guide or report | Follow a procedure; use the evidence to answer a concrete decision question | Actions, conclusion, source support, missing premises |
| Plan | Identify the first executable task, required inputs, owner, and completion condition | Correct next action and any actual dependency gaps |
| UI or automation | Complete a representative task from the normal entrypoint | Observed states, output, recovery behavior when relevant |
| Skill or prompt | Execute a realistic request using the supplied instructions | Actual actions and artifacts, preserved constraints, stopping decision |

Scale coverage to distinct critical paths, not a fixed count. Keep task wording,
available materials, environment, and evaluator capabilities comparable across
a before/after trial. Record meaningful differences. Scores may summarize
evidence; they cannot replace the attempted task or its result.

## Give only normal user context

When delegation is permitted (see Loopy's scope rules), use a fresh agent or
session that has not seen the implementation discussion, intended answers,
suspected defects, earlier findings, or proposed fixes. A different agent with
inherited production history is not a fresh reader. Use the same isolation for
post-change evaluation.

- Claude Code: start a subagent with the Agent tool using a type that starts
  without the conversation, not a fork. For a trial that writes files, request
  worktree isolation or give it a temporary copy.
- Codex: spawn a subagent without forking the current conversation, or start a
  new session. Give it a temporary copy when the trial writes files.
- Other hosts: use any mechanism that starts without the production history.
  If every available mechanism inherits it, the attempt is not independent.

The evaluation prompt is the evaluator's whole context, so do not summarize the
production work in it. Provide the actual user task, normal entrypoint, delivered materials and their
ordinary linked dependencies, assumed knowledge, and permitted resources and
side effects. Keep the acceptance oracle and production notes with the main
agent. Do not conceal materials a real user would have, or supply private hints
they would not. If discovering the purpose is the task, do not state that purpose
in the evaluation prompt; if carrying out a known goal is the task, state it.

Use an isolated copy for actions that write files. Keep evaluation outputs
outside maintained source and out of later trials. Respect read-only, access,
and external-action boundaries; use a bounded walkthrough when actual action
is excluded, and state what execution remains unverified. Evaluation itself
does not authorize deployment, sending messages, or destructive operations.

A compact request can be: "Starting from [entrypoint], use [materials] to
[task]. You may [permitted actions]. Report the actual result, evidence, and
where you could not proceed. Do not modify the source materials."

## Observe the attempt

Have the evaluator try the task rather than only express a quality opinion.
Request the result, commands or actions actually attempted, supporting locations,
and material uncertainty or points of confusion. A concise account of observable
actions is sufficient; do not request private reasoning or an exhaustive diary.

Do not coach a stalled evaluator into passing. Record the missing information
or obstacle, then investigate it. Check whether an apparently successful result
depended on guessing or on knowledge the intended user would not have. Inspect
the actual outputs and compare them with the acceptance evidence yourself;
confidence and agreement are not proof of correctness.

Keep the trial bounded to its assigned task. Evaluators do not commission a
second review of their evaluation. The main agent owns corrections, evidence
reuse, and the completion decision; evaluator approval is not a separate gate.

## Use the result

Check confusion against source behavior and the intended user's needs. Separate
artifact problems from unsupported preferences, evaluator mistakes, unsuitable
assumed knowledge, and environment or permission failures. Resolve accepted
findings under Loopy's main workflow. Do not change acceptance tasks to hide
failures, or retry with new evaluators until one happens to pass.

For a relevant revision, repeat the affected task with a fresh evaluator and
reuse unaffected evidence. Completion requires the critical tasks to succeed
and confirmed material obstacles to be resolved, not universal praise. An agent
trial establishes observed agent use under its conditions; do not report it as
proof of human usability or behavior in untested environments.

When independent evaluation is unavailable or disallowed, perform the strongest
authorized check from the normal entrypoint and label it as self-check or
walkthrough. Explain the material limitation. If independence is an explicit
acceptance requirement, or the remaining uncertainty could change completion,
report the unmet condition; do not silently replace it with self-approval.

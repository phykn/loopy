# Independent use

A fresh evaluator attempts a real task with only what the intended user would
receive, as evidence for Loopy's completion decision.

## Choose the attempt

Pick the intended user, their normal starting point, and the critical tasks the
request implies, assuming their domain knowledge but not project conventions or
the author's reasoning. Fix observable tasks before the trial: run an example or
locate and trace a requested change in code, follow a procedure or answer a
decision question from a guide, or carry out a realistic request with a skill or
prompt and inspect the resulting actions and artifacts. Cover the distinct
critical paths, not a fixed count, and keep task wording, materials,
environment, and evaluator capabilities comparable across a before and after
comparison; a score never replaces the attempt.

## Give only normal user context

When delegation is permitted, use an agent or session that has not seen the
implementation discussion, intended answers, suspected defects, or earlier
findings, with the same isolation after changes; an agent that inherits that
history is not fresh. In Claude Code, use an Agent tool subagent of a type that
starts without the conversation, not a fork; in Codex, a subagent that does not
fork the conversation, or a new session. Use an isolated copy for any trial that
writes files, and keep evaluation outputs out of maintained source and later
trials.

The prompt is the evaluator's whole context. Give the user's task, normal
entrypoint, delivered materials, assumed knowledge, and permitted actions, and
tell the evaluator not to modify the source materials; keep the acceptance
oracle and production notes yourself, and neither withhold what a real user
would have nor add hints they would lack. State the purpose only when carrying
out a known goal is the task, not when discovering it is.

When read-only, access, or external-action limits exclude acting, use a bounded
walkthrough and state what remains unverified; evaluation never authorizes
deployment, sending messages, or destructive operations.

## Observe and use the attempt

Ask the evaluator to attempt the task, not to rate it, and to report the result,
actions taken, supporting locations, and material confusion concisely. It does
not commission another review; the main agent owns corrections and the
decision.

Do not coach a stalled evaluator; record the obstacle and investigate it.
Compare the actual outputs with the acceptance evidence yourself, check whether
a success relied on guessing or on knowledge the intended user would lack, and
tell artifact problems from environment failures. Never change tasks to hide
failures or try evaluators until one passes. After a relevant revision, repeat
the affected task with a fresh evaluator.

Completion needs the critical tasks to succeed and confirmed material obstacles
to be resolved, not universal praise. An agent trial shows agent use under its
conditions, not human usability. When independent evaluation is unavailable or
disallowed, run the strongest authorized check and state its limit; if
independence is explicitly required or the remaining uncertainty could change
completion, report that condition as unmet.

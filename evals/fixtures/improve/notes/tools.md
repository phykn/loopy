# Bot tools

Tools available to the review bot in CI:

- `post_comment(file, line, body)`: comment on a changed line.
- `request_changes(body)`: mark the pull request as needing changes.

The `ircbot` tool was removed in March 2026 when the team moved from IRC to the
pull request dashboard, which already shows every bot comment.

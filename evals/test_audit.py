import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AUDIT = Path(__file__).resolve().parent / "audit.py"
REPO = str(AUDIT.parent.parent)
HOME = str(Path.home())
WS = "/var/folders/ab/T/loopy-eval-1a2b3c"


def assistant(*calls, text=None):
    """An assistant line shaped like a Claude Code transcript: cwd on the line, tool_use items in message.content."""
    content = [{"type": "text", "text": text}] if text else []
    content += [
        {"type": "tool_use", "id": id, "name": name, "input": data, "caller": {"type": "direct"}}
        for id, name, data in calls
    ]
    return {"type": "assistant", "cwd": REPO, "message": {"role": "assistant", "content": content}}


def result(id, text):
    content = [{"type": "tool_result", "tool_use_id": id, "content": text, "is_error": False}]
    return {"type": "user", "cwd": REPO, "message": {"role": "user", "content": content}}


class AuditTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="loopy-audit-test-")
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)

    def transcript(self, *records):
        path = self.dir / "agent-test.jsonl"
        path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        return path

    def run_audit(self, *args):
        return subprocess.run(
            [sys.executable, str(AUDIT), *map(str, args)], capture_output=True, text=True, encoding="utf-8",
        )

    def verdict(self, name, data, *options):
        return self.run_audit(self.transcript(assistant(("toolu_1", name, data))), *options).returncode

    def test_repository_cwd_alone_is_not_a_problem(self):
        path = self.transcript(
            {"type": "user", "cwd": REPO, "message": {"role": "user", "content": f"Open {WS}/requests.md"}},
            assistant(("toolu_1", "Read", {"file_path": f"{WS}/requests.md"}), text="Reading the request."),
            result("toolu_1", "Apply Loopy from the workspace skill."),
            assistant(("toolu_2", "Bash", {"command": f"cd {WS}/tasks/fix && python3 -m unittest"})),
            {"type": "api-request-blob", "message": {"content": [
                {"type": "tool_use", "id": "toolu_9", "name": "Read", "input": {"file_path": f"{REPO}/evals/cases.json"}},
            ]}},
        )
        result_ = self.run_audit(path)
        self.assertEqual(result_.returncode, 0, result_.stdout + result_.stderr)
        self.assertIn("2 tool calls", result_.stdout)

    def test_forbidden_strings_in_read_or_bash_are_problems(self):
        for text in (
            f"{REPO}/skills/loopy/SKILL.md",
            "~/.claude/plugins/cache/loopy/loopy/0.10.0/skills/loopy/SKILL.md",
            f"{HOME}/.claude/plugins/cache/loopy/loopy/0.10.0/skills/loopy/SKILL.md",
            f"{HOME}/.claude/plugins/marketplaces/loopy/README.md",
            "~/.codex/plugins/cache/loopy/loopy/SKILL.md",
            f"{HOME}/.claude/projects/-Volumes-SSD-code-loopy/session/subagents/agent-1.jsonl",
            f"{WS}/../cases.json",
        ):
            with self.subTest(text=text):
                self.assertEqual(self.verdict("Read", {"file_path": text}), 1)
                self.assertEqual(self.verdict("Bash", {"command": f"cat {text}"}), 1)
        self.assertEqual(self.verdict("Read", {"file_path": "/opt/private/notes.md"}), 0)
        self.assertEqual(self.verdict("Read", {"file_path": "/opt/private/notes.md"}, "--forbid", "/opt/private"), 1)

    def test_problem_line_names_file_line_and_tool(self):
        path = self.transcript(assistant(("toolu_1", "Read", {"file_path": f"{REPO}/README.md"})))
        result_ = self.run_audit(path)
        self.assertEqual(result_.returncode, 1)
        self.assertEqual(result_.stdout.strip(), f"{path}:1: Read " + json.dumps({"file_path": f"{REPO}/README.md"})[:120])

    def test_loopy_skill_call_is_a_problem(self):
        self.assertEqual(self.verdict("Skill", {"skill": "loopy:loopy"}), 1)
        self.assertEqual(self.verdict("Skill", {"skill": "loopy"}), 1)
        self.assertEqual(self.verdict("Skill", {"skill": "anthropic-skills:pdf"}), 0)

    def test_grep_and_glob_must_search_the_workspace(self):
        for name in ("Grep", "Glob"):
            with self.subTest(name=name):
                self.assertEqual(self.verdict(name, {"pattern": "total"}), 1)
                self.assertEqual(self.verdict(name, {"pattern": "total", "path": "/opt/other"}), 1)
                self.assertEqual(self.verdict(name, {"pattern": "total", "path": f"{WS}/tasks/fix"}), 0)

    def test_recursive_shell_search_must_name_the_workspace(self):
        for command in ("grep -r total .", "grep -Rn total", "find . -name '*.py'", "rg total", "ls -R", "tree"):
            with self.subTest(command=command):
                self.assertEqual(self.verdict("Bash", {"command": command}), 1)
        for command in (f"grep -rn total {WS}/tasks", f"find {WS} -name '*.py'", "git worktree list", "python3 --version"):
            with self.subTest(command=command):
                self.assertEqual(self.verdict("Bash", {"command": command}), 0)

    def test_calls_prints_text_calls_and_results_in_order(self):
        read = ("toolu_1", "Read", {"file_path": f"{WS}/requests.md"})
        path = self.transcript(
            assistant(read, text="Start."),
            result("toolu_1", "first\nsecond " + "x" * 600),
            assistant(("toolu_2", "Bash", {"command": f"ls {WS}"})),
            assistant(read),
        )
        result_ = self.run_audit(path, "--calls")
        self.assertEqual(result_.returncode, 0, result_.stdout)
        self.assertEqual(result_.stdout.splitlines()[:5], [
            f"== {path}",
            "1: text Start.",
            f"1: Read {json.dumps(read[2])}",
            "2: result " + ("first second " + "x" * 600)[:500],
            f"3: Bash {json.dumps({'command': f'ls {WS}'})}",
        ])
        self.assertIn("2 tool calls", result_.stdout.splitlines()[5])

    def test_print_forbidden_needs_no_transcript(self):
        result_ = self.run_audit("--print-forbidden", "--forbid", "/opt/private")
        self.assertEqual(result_.returncode, 0, result_.stderr)
        self.assertEqual(result_.stdout.splitlines(), [
            REPO, ".claude/plugins/cache/loopy", ".claude/plugins/marketplaces/loopy", ".codex/plugins/cache/loopy",
            ".claude/projects/", "cases.json", "routing.json", "results.md", "evals/", "docs/blueprint", "/opt/private",
        ])

    def test_unreadable_transcript_exits_2(self):
        bad = self.dir / "agent-bad.jsonl"
        bad.write_text('{"type": "assistant"}\nnot json\n', encoding="utf-8")
        for path in (bad, self.dir / "agent-missing.jsonl"):
            with self.subTest(path=path.name):
                result_ = self.run_audit(path)
                self.assertEqual(result_.returncode, 2)
                self.assertNotIn("Traceback", result_.stderr)
        self.assertEqual(self.run_audit().returncode, 2)


if __name__ == "__main__":
    unittest.main()

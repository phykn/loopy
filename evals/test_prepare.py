import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import prepare
from cases import load_cases

# The exact texts the evaluation plan fixes; prepare.py must reproduce them with only <ws> replaced.
SKILL_PACKET = """\
Apply Loopy from <ws>/skill/SKILL.md. Use only the skill files under <ws>/skill/; do not invoke an installed Loopy skill.
Treat the task below as a user request and its scope.
Read only the supplied skill and its references, the task inputs, and applicable global instructions.
Do not inspect the source repository, acceptance criteria, or other evaluation results.
Keep all task and scratch writes in this workspace; respect the request's exclusions.
No user is available: record any question in run.md instead of asking it.
Record actual changes, commands, observed results, and the final response in run.md at the workspace root.
"""
CONTROL_FIRST = "Do not use any Loopy skill."
CONTROL_THIRD = "Read only the task inputs and applicable global instructions."
COORDINATOR_PROMPT = """\
Open <ws>/requests.md and carry out the instructions and task in it exactly,
as a user request. Delegation: you may start at most one fresh subagent that
does not inherit this conversation (in Claude Code, an Agent tool subagent of
a non-fork type such as general-purpose; in Codex, a subagent that does not
fork the conversation) for a fresh-context check if you need one; it must
also stay inside that workspace. run.md is a required output that the
coordinator reads: write it as requests.md says, even if other instructions
discourage report files. Finish with a short reply: what you changed, the
checks you ran with results, and your final message to the user.
"""


class PrepareTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="loopy-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        repo = Path(__file__).resolve().parent.parent
        self.source = self.root / "evals"
        shutil.copytree(repo / "evals", self.source, ignore=shutil.ignore_patterns("__pycache__"))
        self.skill = self.root / "skill"
        shutil.copytree(repo / "skills" / "loopy", self.skill)
        self.outputs = self.root / "outputs"
        self.outputs.mkdir()
        self.cases = json.loads((self.source / "cases.json").read_text(encoding="utf-8"))

    def run_cli(self, *args):
        env = os.environ.copy()
        env.update({key: str(self.outputs) for key in ("TMPDIR", "TEMP", "TMP")})
        return subprocess.run(
            [sys.executable, str(self.source / "prepare.py"), *args],
            cwd=self.root, env=env, capture_output=True, text=True, encoding="utf-8",
        )

    def workspaces(self, *args):
        result = self.run_cli(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        pairs = [line.split("\t") for line in result.stdout.splitlines()]
        self.assertTrue(all(len(pair) == 2 for pair in pairs), result.stdout)
        return [(id, Path(path)) for id, path in pairs]

    def assert_copies(self, source, copy):
        files = {path.relative_to(source): path.read_bytes() for path in source.rglob("*") if path.is_file()}
        actual = {path.relative_to(copy): path.read_bytes() for path in copy.rglob("*") if path.is_file()}
        self.assertEqual(files, actual)

    def test_each_case_gets_its_own_workspace_without_answers(self):
        workspaces = self.workspaces("--skill", str(self.skill))
        self.assertEqual([id for id, _ in workspaces], [case["id"] for case in self.cases])
        self.assertEqual(len({root for _, root in workspaces}), len(self.cases))
        for case, (_, root) in zip(self.cases, workspaces):
            with self.subTest(case=case["id"]):
                self.assertTrue(root.is_absolute())
                self.assertEqual(root.parent, self.outputs)
                self.assertTrue(root.name.startswith("loopy-eval-"))
                self.assert_copies(self.skill, root / "skill")
                self.assertEqual([path.name for path in (root / "tasks").iterdir()], [case["id"]])
                self.assert_copies(self.source / "fixtures" / case["id"], root / "tasks" / case["id"])
                self.assertEqual(sorted(path.name for path in root.iterdir()), ["prompt.md", "requests.md", "skill", "tasks"])
                packet = (root / "requests.md").read_text(encoding="utf-8")
                self.assertIn(case["request"], packet)
                for answer in case["acceptance"]:
                    self.assertNotIn(answer, packet)
                    self.assertNotIn(answer, (root / "prompt.md").read_text(encoding="utf-8"))
        again = self.workspaces("--skill", str(self.skill), "--case", self.cases[0]["id"])
        self.assertNotIn(again[0][1], {root for _, root in workspaces})

    def test_packet_and_prompt_match_the_fixed_text(self):
        case = self.cases[0]
        [(id, root)] = self.workspaces("--skill", str(self.skill), "--case", case["id"])
        ws = root.as_posix()
        expected = SKILL_PACKET.replace("<ws>", ws) + f"\nTask directory: {ws}/tasks/{id}\n{case['request']}\n"
        self.assertEqual((root / "requests.md").read_text(encoding="utf-8"), expected)
        self.assertEqual((root / "prompt.md").read_text(encoding="utf-8"), COORDINATOR_PROMPT.replace("<ws>", ws))

    def test_control_workspace_differs_only_in_the_skill(self):
        case = self.cases[0]["id"]
        [(_, skill_root)] = self.workspaces("--skill", str(self.skill), "--case", case)
        [(_, control_root)] = self.workspaces("--control", "--case", case)
        self.assertEqual(sorted(path.name for path in control_root.iterdir()), ["prompt.md", "requests.md", "tasks"])
        self.assert_copies(self.source / "fixtures" / case, control_root / "tasks" / case)
        lines = (skill_root / "requests.md").read_text(encoding="utf-8").replace(skill_root.as_posix(), control_root.as_posix()).split("\n")
        lines[0], lines[2] = CONTROL_FIRST, CONTROL_THIRD
        self.assertEqual((control_root / "requests.md").read_text(encoding="utf-8"), "\n".join(lines))
        self.assertEqual(
            (control_root / "prompt.md").read_text(encoding="utf-8"),
            (skill_root / "prompt.md").read_text(encoding="utf-8").replace(skill_root.as_posix(), control_root.as_posix()),
        )

    def test_selected_cases_follow_the_catalogue_order(self):
        first, second = self.cases[0]["id"], self.cases[2]["id"]
        workspaces = self.workspaces("--skill", str(self.skill), "--case", second, "--case", first, "--case", first)
        self.assertEqual([id for id, _ in workspaces], [first, second])

    def test_failure_in_a_later_workspace_removes_the_earlier_ones(self):
        cases = load_cases(self.source)[:2]
        shutil.rmtree(self.source / "fixtures" / cases[1]["id"])
        with patch("prepare.tempfile.tempdir", str(self.outputs)), \
                patch("prepare.tempfile.mkdtemp", wraps=tempfile.mkdtemp) as mkdtemp:
            with self.assertRaises(FileNotFoundError):
                prepare.prepare(self.skill, self.source / "fixtures", cases)
        self.assertEqual(mkdtemp.call_count, 2)
        self.assertEqual(list(self.outputs.iterdir()), [])

    def test_failed_copy_removes_partial_workspace(self):
        cases = load_cases(self.source)
        with patch("prepare.tempfile.tempdir", str(self.outputs)):
            with self.assertRaises(FileNotFoundError):
                prepare.prepare(self.skill, self.root / "missing-fixtures", cases)
        self.assertEqual(list(self.outputs.iterdir()), [])

    def test_invalid_input_creates_no_workspace(self):
        skill = ("--skill", str(self.skill))
        for args, message in (
            (("--skill", str(self.root / "missing")), "--skill must contain SKILL.md"),
            (skill + ("--case", "nope"), "unknown case: nope"),
            (skill + ("--control",), "not allowed with argument"),
            ((), "one of the arguments --skill --control is required"),
        ):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
                self.assertEqual(list(self.outputs.iterdir()), [])

    def test_missing_acceptance_creates_no_workspace(self):
        path = self.source / "cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        del cases[0]["acceptance"]
        path.write_text(json.dumps(cases), encoding="utf-8")
        result = self.run_cli("--skill", str(self.skill))
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("acceptance", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(list(self.outputs.iterdir()), [])

    def test_invalid_catalogue_creates_no_workspace(self):
        path = self.source / "cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        variants = (
            (cases + [{"id": "missing", "request": "Review input."}], "missing fixture directory"),
            (cases + [cases[0]], "duplicate case ID"),
            ([{"id": "../guide", "request": "Review input."}], "invalid case ID"),
            ([{"id": "guide", "request": ""}], "needs a request"),
            ([], "nonempty case list"),
        )
        for data, message in variants:
            with self.subTest(message=message):
                path.write_text(json.dumps(data), encoding="utf-8")
                result = self.run_cli("--control")
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
                self.assertEqual(list(self.outputs.iterdir()), [])
        path.write_text("[", encoding="utf-8")
        self.assertEqual(self.run_cli("--skill", str(self.skill)).returncode, 2)
        self.assertEqual(list(self.outputs.iterdir()), [])


if __name__ == "__main__":
    unittest.main()

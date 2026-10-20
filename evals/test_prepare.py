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

    def run_cli(self, *args):
        env = os.environ.copy()
        env.update({key: str(self.outputs) for key in ("TMPDIR", "TEMP", "TMP")})
        return subprocess.run(
            [sys.executable, str(self.source / "prepare.py"), "--skill", str(self.skill), *args],
            cwd=self.root, env=env, capture_output=True, text=True, encoding="utf-8",
        )

    def assert_copies(self, source, copy):
        files = {path.relative_to(source): path.read_bytes() for path in source.rglob("*") if path.is_file()}
        actual = {path.relative_to(copy): path.read_bytes() for path in copy.rglob("*") if path.is_file()}
        self.assertEqual(files, actual)

    def test_default_packet_preserves_inputs_and_withholds_answers(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        root = Path(result.stdout.strip())
        self.assertEqual(root.parent, self.outputs)
        self.assert_copies(self.skill, root / "skill")
        self.assert_copies(self.source / "fixtures", root / "tasks")
        packet = (root / "requests.md").read_text(encoding="utf-8")
        for case in json.loads((self.source / "cases.json").read_text(encoding="utf-8")):
            self.assertIn(case["request"], packet)
            self.assertIn((root / "tasks" / case["id"]).as_posix(), packet)
            for answer in case["acceptance"]:
                self.assertNotIn(answer, packet)
        self.assertFalse((root / "cases.json").exists())
        other = self.run_cli()
        self.assertEqual(other.returncode, 0, other.stderr)
        self.assertNotEqual(root, Path(other.stdout.strip()))

    def test_selected_cases_are_isolated(self):
        result = self.run_cli("--case", "guide")
        self.assertEqual(result.returncode, 0, result.stderr)
        root = Path(result.stdout.strip())
        self.assertEqual({path.name for path in (root / "tasks").iterdir()}, {"guide"})
        self.assert_copies(self.source / "fixtures" / "guide", root / "tasks" / "guide")
        packet = (root / "requests.md").read_text(encoding="utf-8")
        self.assertNotIn("tasks/review", packet)
        self.assertNotIn("tasks/ready", packet)
        result = self.run_cli("--case", "ready", "--case", "guide", "--case", "guide")
        self.assertEqual(result.returncode, 0, result.stderr)
        root = Path(result.stdout.strip())
        self.assertEqual({path.name for path in (root / "tasks").iterdir()}, {"guide", "ready"})
        packet = (root / "requests.md").read_text(encoding="utf-8")
        self.assertEqual(packet.count("Task directory:"), 2)
        self.assertLess(packet.index("tasks/guide"), packet.index("tasks/ready"))

    def test_missing_acceptance_creates_no_workspace(self):
        path = self.source / "cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        del cases[0]["acceptance"]
        path.write_text(json.dumps(cases), encoding="utf-8")
        result = self.run_cli()
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("acceptance", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(list(self.outputs.iterdir()), [])

    def test_invalid_skill_and_case_create_no_workspace(self):
        for args, message in (
            (("--skill", str(self.root / "missing")), "--skill must contain SKILL.md"),
            (("--case", "unknown"), "unknown case: unknown"),
        ):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
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
                result = self.run_cli()
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
                self.assertEqual(list(self.outputs.iterdir()), [])
        path.write_text("[", encoding="utf-8")
        self.assertEqual(self.run_cli().returncode, 2)
        self.assertEqual(list(self.outputs.iterdir()), [])

    def test_failed_copy_removes_partial_workspace(self):
        cases = load_cases(self.source)
        with patch("prepare.tempfile.tempdir", str(self.outputs)):
            with self.assertRaises(FileNotFoundError):
                prepare.prepare(self.skill, self.root / "missing-fixtures", cases)
        self.assertEqual(list(self.outputs.iterdir()), [])


if __name__ == "__main__":
    unittest.main()

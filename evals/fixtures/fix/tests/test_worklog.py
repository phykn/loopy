import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(text):
    with tempfile.TemporaryDirectory() as tmp:
        log = Path(tmp) / "log.txt"
        log.write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, "worklog.py", str(log)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )


class WorklogTests(unittest.TestCase):
    def test_totals_tasks_in_first_appearance_order(self):
        result = run("09:00-10:30 review\n10:30-12:05 build\n13:00-14:00 review\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "review 2:30\nbuild 1:35\ntotal 4:05\n")

    def test_ignores_blank_and_comment_lines(self):
        result = run("# Mon\n\n09:00-09:45 standup notes\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "standup notes 0:45\ntotal 0:45\n")

    def test_rejects_invalid_lines(self):
        cases = {
            "format": "09:00-10:00 review\n9:00-10:00 build\n",
            "hour": "09:00-10:00 review\n24:00-01:00 build\n",
            "minute": "09:00-10:00 review\n09:60-10:00 build\n",
        }
        for name, text in cases.items():
            with self.subTest(name):
                result = run(text)
                self.assertEqual(result.returncode, 2)
                self.assertIn("line 2", result.stderr)
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()

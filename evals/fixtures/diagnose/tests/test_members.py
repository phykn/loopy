import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(text):
    with tempfile.TemporaryDirectory() as tmp:
        signups = Path(tmp) / "signups.csv"
        signups.write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, "members.py", str(signups)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )


class MembersTests(unittest.TestCase):
    def test_counts_each_email_once(self):
        result = run("name,email\nAnn,ann@example.com\nBo,bo@example.com\nAnn,ann@example.com\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "members 2\n")

    def test_ignores_spaces_and_domain_case(self):
        result = run("name,email\nAnn,ann@example.com\nAnn, ann@EXAMPLE.com \n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "members 1\n")

    def test_rejects_invalid_rows(self):
        cases = {
            "header": "name,mail\nAnn,ann@example.com\n",
            "email": "name,email\nAnn,ann.example.com\n",
        }
        for name, text in cases.items():
            with self.subTest(name):
                result = run(text)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(*args):
    return subprocess.run(
        [sys.executable, "cli.py", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


class CliTests(unittest.TestCase):
    def test_prints_totals(self):
        result = run("data/sample.csv")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "food 15.50\nrent 500.00\ntotal 515.50\n")

    def test_writes_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "report.json"
            result = run("data/sample.csv", "--json", str(out))
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(out.read_text(encoding="utf-8")), {
                "categories": {"food": "15.50", "rent": "500.00"},
                "total": "515.50",
            })

    def test_refuses_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "report.json"
            out.write_text("keep\n", encoding="utf-8")
            result = run("data/sample.csv", "--json", str(out))
            self.assertEqual(result.returncode, 2)
            self.assertEqual(out.read_text(encoding="utf-8"), "keep\n")

    def test_rejects_invalid_input(self):
        cases = {
            "header": ("day,category,amount\n2026-01-01,food,1\n", "line 1"),
            "amount": ("date,category,amount\n2026-01-01,food,1\n2026-01-02,food,x\n", "line 3"),
        }
        for name, (text, message) in cases.items():
            with self.subTest(name), tempfile.TemporaryDirectory() as tmp:
                source = Path(tmp) / "bad.csv"
                out = Path(tmp) / "report.json"
                source.write_text(text, encoding="utf-8")
                result = run(str(source), "--json", str(out))
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
                self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()

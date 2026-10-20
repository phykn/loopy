"""Tests for the ledger command line interface."""

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
        self.assertEqual(result.stdout, "food 12.50\nrent 500.00\ntotal 512.50\n")

    def test_prints_total_line(self):
        result = run("data/sample.csv")
        # Check the total line
        self.assertIn("total 512.50", result.stdout)

    def test_writes_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "report.json"
            result = run("data/sample.csv", "--json", str(out))
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(out.read_text(encoding="utf-8")), {
                "categories": {"food": "12.50", "rent": "500.00"},
                "total": "512.50",
            })

    def test_refuses_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "report.json"
            out.write_text("keep\n", encoding="utf-8")
            result = run("data/sample.csv", "--json", str(out))
            self.assertEqual(result.returncode, 2)
            self.assertEqual(out.read_text(encoding="utf-8"), "keep\n")

    def test_rejects_wrong_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "bad.csv"
            source.write_text("day,category,amount\n2026-01-01,food,1\n", encoding="utf-8")
            result = run(str(source))
            self.assertEqual(result.returncode, 2)
            self.assertIn("line 1", result.stderr)


if __name__ == "__main__":
    unittest.main()

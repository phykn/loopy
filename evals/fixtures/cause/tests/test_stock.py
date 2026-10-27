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
            [sys.executable, "stock.py", str(log)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )


class StockTests(unittest.TestCase):
    def test_counts_items_in_first_appearance_order(self):
        result = run("2026-10-01 in 5 widget\n2026-10-01 in 2 bolt\n2026-10-02 out 3 widget\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "widget 2\nbolt 2\ntotal 4\n")

    def test_ignores_blank_and_comment_lines(self):
        result = run("# October\n\n2026-10-01 in 4 spare part\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "spare part 4\ntotal 4\n")

    def test_rejects_invalid_lines(self):
        cases = {
            "format": "2026-10-01 in 5 widget\n10/01 in 5 widget\n",
            "kind": "2026-10-01 in 5 widget\n2026-10-02 lost 1 widget\n",
            "zero": "2026-10-01 in 5 widget\n2026-10-02 out 0 widget\n",
        }
        for name, text in cases.items():
            with self.subTest(name):
                result = run(text)
                self.assertEqual(result.returncode, 2)
                self.assertIn("line 2", result.stderr)
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()

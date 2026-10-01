"""Check that package validation detects maintenance mistakes."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="loopy-check-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        repo = Path(__file__).resolve().parent.parent
        for name in ("README.md", "skills", "evals", ".codex-plugin", ".claude-plugin", ".agents"):
            src = repo / name
            dst = self.root / name
            if src.is_dir():
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
            else:
                shutil.copy2(src, dst)

    def run_cli(self):
        return subprocess.run(
            [sys.executable, str(self.root / "evals" / "check.py")],
            cwd=self.root.parent, capture_output=True, text=True, encoding="utf-8",
        )

    def test_package_passes_from_another_directory(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("passed", result.stdout)

    def test_metadata_drift_is_rejected(self):
        path = self.root / ".claude-plugin" / "plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["version"] = "0.0.0"
        data["description"] = "Different description."
        path.write_text(json.dumps(data), encoding="utf-8")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("disagree on version", result.stderr)
        self.assertIn("disagree on description", result.stderr)

    def test_broken_runtime_link_is_rejected(self):
        path = self.root / "skills" / "loopy" / "references" / "independent-use.md"
        with path.open("a", encoding="utf-8") as file:
            file.write("\n[Missing](missing.md)\n")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing link target missing.md", result.stderr)

    def test_invalid_json_identifies_the_manifest(self):
        (self.root / ".agents" / "plugins" / "marketplace.json").write_text("{", encoding="utf-8")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn(".agents/plugins/marketplace.json", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_empty_marketplace_reports_a_failure(self):
        path = self.root / ".agents" / "plugins" / "marketplace.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["plugins"] = []
        path.write_text(json.dumps(data), encoding="utf-8")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("marketplace must identify the Loopy plugin", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_missing_case_input_is_rejected(self):
        src = self.root / "evals" / "fixtures" / "guide"
        dst = self.root / "evals" / "fixtures" / "other"
        src.rename(dst)
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing fixture directory for 'guide'", result.stderr)


if __name__ == "__main__":
    unittest.main()

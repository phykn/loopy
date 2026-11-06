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

    def test_empty_acceptance_is_rejected(self):
        path = self.root / "evals" / "cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        cases[0]["acceptance"] = []
        path.write_text(json.dumps(cases), encoding="utf-8")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("acceptance", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def edit_skill(self, old, new):
        path = self.root / "skills" / "loopy" / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def add_notes(self, text):
        (self.root / "notes.md").write_text(text, encoding="utf-8")
        with (self.root / "README.md").open("a", encoding="utf-8") as file:
            file.write("\n[Notes](notes.md)\n")

    def assert_rejected(self, message):
        result = self.run_cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(message, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_extra_frontmatter_key_is_rejected(self):
        self.edit_skill("name: loopy\n", "name: loopy\nversion: 1\n")
        self.assert_rejected("frontmatter keys must be name and description")

    def test_skill_name_must_match_the_manifest(self):
        self.edit_skill("name: loopy\n", "name: loopy-dev\n")
        self.assert_rejected("name must be loopy")

    def test_description_must_be_folded(self):
        self.edit_skill("description: >\n  ", "description: ")
        self.assert_rejected("description must be a folded scalar")

    def test_long_description_is_rejected(self):
        self.edit_skill("  or brainstorming.\n", "  or brainstorming.\n  " + "word " * 210 + "\n")
        self.assert_rejected("description must have 1 to 1,024 characters")

    def test_angle_bracket_in_description_is_rejected(self):
        self.edit_skill("names Loopy.", "names <Loopy>.")
        self.assert_rejected("description must not contain < or >")

    def test_long_skill_body_is_rejected(self):
        with (self.root / "skills" / "loopy" / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n" + "word " * 1101 + "\n")
        self.assert_rejected("words; the limit is 1,100")

    def test_long_references_are_rejected(self):
        with (self.root / "skills" / "loopy" / "references" / "code.md").open("a", encoding="utf-8") as file:
            file.write("\n" + "word " * 2101 + "\n")
        self.assert_rejected("words; the limit is 2,100")

    def test_missing_anchor_in_the_same_file_is_rejected(self):
        self.add_notes("# Notes\n\n[Here](#nowhere)\n")
        self.assert_rejected("notes.md: missing anchor #nowhere")

    def test_missing_anchor_in_another_file_is_rejected(self):
        self.add_notes("[Skill](skills/loopy/SKILL.md#nowhere)\n")
        self.assert_rejected("missing anchor skills/loopy/SKILL.md#nowhere")

    def test_repeated_and_punctuated_headings_get_github_anchors(self):
        self.add_notes("## What's new?\n\n## Notes\n\n## Notes\n\n[New](#whats-new) [Second](#notes-1)\n")
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_heading_inside_a_code_block_has_no_anchor(self):
        self.add_notes("```\n# Not a heading\n```\n\n[Fake](#not-a-heading)\n")
        self.assert_rejected("missing anchor #not-a-heading")


if __name__ == "__main__":
    unittest.main()

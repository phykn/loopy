import json
import tempfile
import unittest
from pathlib import Path

from cases import load_cases


class CaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="loopy-case-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "fixtures" / "sample").mkdir(parents=True)
        self.path = self.root / "cases.json"

    def test_acceptance_requires_nonempty_text_items(self):
        case = {"id": "sample", "request": "Review the input."}
        variants = [case]
        for value in (None, [], "Check output.", {}, [None], [""], ["  \n"], ["Check output.", 1]):
            variants.append(dict(case, acceptance=value))
        for data in variants:
            with self.subTest(case=data):
                self.path.write_text(json.dumps([data]), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "case 'sample'.*acceptance"):
                    load_cases(self.root)

    def test_valid_case_text_is_preserved(self):
        cases = [{
            "id": "sample",
            "request": " 입력을 검토하세요.\n",
            "acceptance": [" 결과를 확인한다.\n", "Preserve the input."],
        }]
        self.path.write_text(json.dumps(cases), encoding="utf-8")
        self.assertEqual(load_cases(self.root), cases)


if __name__ == "__main__":
    unittest.main()

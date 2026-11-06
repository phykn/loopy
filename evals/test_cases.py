import json
import tempfile
import unittest
from pathlib import Path

from cases import load_cases, load_routing


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


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="loopy-routing-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path = self.root / "routing.json"
        self.valid = [
            {"id": "r01", "request": "Review the parser.", "kinds": ["Assess"]},
            {"id": "r02", "request": "점검하고 고쳐 줘.", "kinds": ["Assess", "Debug"], "example": "check-fix"},
        ]

    def test_valid_set_is_preserved(self):
        self.path.write_text(json.dumps(self.valid, ensure_ascii=False), encoding="utf-8")
        self.assertEqual(load_routing(self.root), self.valid)

    def test_invalid_sets_are_rejected(self):
        first = self.valid[0]
        for items, message in (
            ([first, first], "duplicate request ID"),
            ([dict(first, id="r1")], "invalid request ID"),
            ([dict(first, id="R01")], "invalid request ID"),
            ([dict(first, request="  ")], "needs one nonblank line"),
            ([dict(first, request="Review.\nThen fix.")], "needs one nonblank line"),
            ([dict(first, kinds=[])], "needs kinds"),
            ([dict(first, kinds=["Assess", "Rewrite"])], "needs kinds"),
            ([dict(first, example=" ")], "blank example"),
            ([], "nonempty request list"),
        ):
            with self.subTest(message=message, items=items):
                self.path.write_text(json.dumps(items), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, message):
                    load_routing(self.root)


if __name__ == "__main__":
    unittest.main()

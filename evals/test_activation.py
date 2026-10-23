import json
import unittest

from activation import summarize, watch


def tool(name, **input):
    return json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": name, "input": input}]}})


class ActivationTests(unittest.TestCase):
    def test_outcome_is_the_first_decisive_tool(self):
        result = json.dumps({"type": "result"})
        for lines, outcome in (
            ([tool("Read"), tool("Skill", skill="loopy:loopy"), tool("Edit")], "loopy"),
            ([tool("Skill", skill="other"), tool("Write"), tool("Skill", skill="loopy:loopy")], "edit"),
            (["not json", tool("Bash"), result, tool("Skill", skill="loopy:loopy")], "end"),
            ([tool("Read")] * 3, "end"),
        ):
            with self.subTest(outcome=outcome):
                tools = []
                self.assertEqual(watch(lines, tools), outcome)
        tools = []
        self.assertEqual(watch([tool("Read")] * 5, tools, limit=2), "limit")
        self.assertEqual(tools, ["Read", "Read"])

    def test_summary_separates_should_trigger_and_near_misses(self):
        records = [
            {"id": "fix", "should": True, "outcome": "loopy"},
            {"id": "fix", "should": True, "outcome": "edit"},
            {"id": "rename", "should": False, "outcome": "end"},
        ]
        text = summarize(records)
        self.assertIn("fix: 1/2", text)
        self.assertIn("rename: 0/1", text)
        self.assertIn("should-trigger queries: 1/2", text)
        self.assertIn("near misses: 0/1", text)


if __name__ == "__main__":
    unittest.main()

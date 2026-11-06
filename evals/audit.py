import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Paths under the home folder omit "~/" and the home path, so either spelling matches.
FORBIDDEN = [
    str(ROOT),
    ".claude/plugins/cache/loopy",
    ".claude/plugins/marketplaces/loopy",
    ".codex/plugins/cache/loopy",
    ".claude/projects/",
    "cases.json",
    "routing.json",
    "results.md",
    "evals/",
    "docs/blueprint",
]
# Searches that walk the shell's starting folder, which is the repository, unless they name the workspace
# or an allowed folder.
RECURSIVE = re.compile(r"(?<![\w.-])(?:grep -[A-Za-z]*[rR]|rg |find |ls -[A-Za-z]*R|tree\b)")


def main():
    parser = argparse.ArgumentParser(description="Find evaluator tool calls that reach outside the evaluation workspace.")
    parser.add_argument("files", nargs="*", type=Path, help="Claude Code subagent transcripts (agent-*.jsonl)")
    parser.add_argument("--forbid", action="append", default=[], metavar="TEXT", help="another string no tool input may contain")
    parser.add_argument("--allow", action="append", default=[], metavar="TEXT",
                        help="a folder besides the workspace that a search may name, such as one the global instructions send agents to")
    parser.add_argument("--calls", action="store_true", help="also print each file's text, tool calls, and results in order")
    parser.add_argument("--print-forbidden", action="store_true", help="print the forbidden strings and exit")
    args = parser.parse_args()
    forbidden = FORBIDDEN + args.forbid
    if args.print_forbidden:
        print("\n".join(forbidden))
        return 0
    if not args.files:
        parser.error("give at least one transcript")
    try:
        transcripts = [(path, list(read(path))) for path in args.files]
    except (OSError, ValueError) as exc:
        print(f"audit.py: {exc}", file=sys.stderr)
        return 2
    problems, total = [], 0
    for path, records in transcripts:
        found, events, count = audit(records, forbidden, args.allow)
        total += count
        problems += [f"{path}:{line}" for line in found]
        if args.calls:
            print(f"== {path}")
            print("\n".join(events))
    if problems:
        print("\n".join(problems))
        return 1
    print(f"audit: {len(transcripts)} transcripts, {total} tool calls, no call outside the workspace.")
    return 0


def read(path):
    with path.open(encoding="utf-8") as file:
        for number, line in enumerate(file, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{number}: not JSON ({exc.msg})") from None
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{number}: not a JSON object")
            yield number, record


def audit(records, forbidden, allowed=()):
    """Judge only tool_use items of assistant lines, each id once; other lines repeat calls or carry the cwd."""
    problems, events, seen = [], [], set()
    for number, record in records:
        message = record.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, list):
            continue
        for index, item in enumerate(content):
            if not isinstance(item, dict):
                continue
            if record.get("type") == "assistant" and item.get("type") == "text":
                events.append(f"{number}: text {one_line(item.get('text', ''))}")
            elif record.get("type") == "assistant" and item.get("type") == "tool_use":
                key = item.get("id") or (number, index)
                if key in seen:
                    continue
                seen.add(key)
                name, data = item.get("name", ""), item.get("input")
                text = json.dumps(data, ensure_ascii=False)
                events.append(f"{number}: {name} {text}")
                if outside(name, data if isinstance(data, dict) else {}, text, forbidden, allowed):
                    problems.append(f"{number}: {name} {text[:120]}")
            elif record.get("type") == "user" and item.get("type") == "tool_result":
                events.append(f"{number}: result {one_line(result_text(item.get('content')))[:500]}")
    return problems, events, len(seen)


def outside(name, data, text, forbidden, allowed=()):
    if any(item in text for item in forbidden):
        return True
    if name == "Skill":
        return "loopy" in str(data.get("skill", "")).lower()
    places = ("loopy-eval-", *allowed)
    if name in ("Grep", "Glob"):
        path = str(data.get("path") or "")
        return not any(place in path for place in places)
    if name == "Bash":
        command = str(data.get("command", ""))
        return not any(place in command for place in places) and bool(RECURSIVE.search(command))
    return False


def one_line(text):
    return " ".join(str(text).split())


def result_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(str(part.get("text", "")) for part in content if isinstance(part, dict))
    return json.dumps(content, ensure_ascii=False)


if __name__ == "__main__":
    sys.exit(main())

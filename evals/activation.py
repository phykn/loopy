import argparse
import json
import shutil
import subprocess
import tempfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

EDITS = {"Edit", "MultiEdit", "NotebookEdit", "Write"}


def main():
    parser = argparse.ArgumentParser(description="Measure how often Claude Code selects a Loopy plugin directory before editing.")
    parser.add_argument("--plugin", type=Path, required=True, help="plugin root holding .claude-plugin/ and skills/")
    parser.add_argument("--out", type=Path, required=True, help="JSON Lines file that run records are appended to")
    parser.add_argument("--queries", type=Path, default=Path(__file__).resolve().parent / "activation.json")
    parser.add_argument("--set", choices=("tune", "holdout"), help="query set to run (default: all)")
    parser.add_argument("--reps", type=int, default=3)
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--model", help="model to run (default: the Claude Code default)")
    args = parser.parse_args()
    plugin = args.plugin.resolve()
    if not (plugin / ".claude-plugin" / "plugin.json").is_file():
        parser.error("--plugin must contain .claude-plugin/plugin.json")
    queries = [q for q in json.loads(args.queries.read_text(encoding="utf-8")) if args.set in (None, q["set"])]
    project = Path(__file__).resolve().parent / "fixtures" / "refactor"

    def measure(job):
        query, rep = job
        outcome, tools = run(query["query"], plugin, project, args.model)
        record = dict(query, rep=rep, plugin=plugin.as_posix(), outcome=outcome, tools=tools)
        with args.out.open("a", encoding="utf-8") as file:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record

    jobs = [(query, rep) for rep in range(args.reps) for query in queries]
    with ThreadPoolExecutor(args.jobs) as pool:
        records = list(pool.map(measure, jobs))
    print(summarize(records))


def run(query, plugin, project, model):
    with tempfile.TemporaryDirectory(prefix="loopy-activation-") as tmp:
        work = Path(tmp) / "project"
        shutil.copytree(project, work)
        # Disable the installed Loopy so only the plugin under test can be selected.
        cmd = [
            "claude", "-p", "--output-format", "stream-json", "--verbose",
            "--plugin-dir", str(plugin), "--permission-mode", "dontAsk",
            "--settings", json.dumps({"enabledPlugins": {"loopy@loopy": False}}),
        ]
        if model:
            cmd += ["--model", model]
        proc = subprocess.Popen(cmd, cwd=work, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL, text=True, encoding="utf-8")
        # The query goes through stdin because one starting with "--" would parse as an option.
        proc.stdin.write(query)
        proc.stdin.close()
        tools = []
        try:
            outcome = watch(proc.stdout, tools)
        finally:
            proc.kill()
            proc.wait()
    return outcome, tools


def watch(lines, tools, limit=30):
    for line in lines:
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") == "result":
            return "end"
        if event.get("type") != "assistant":
            continue
        for item in event["message"]["content"]:
            if item.get("type") != "tool_use":
                continue
            name = item["name"]
            if name == "Skill":
                name += ":" + str(item["input"].get("skill"))
            tools.append(name)
            if name.startswith("Skill:") and "loopy" in name:
                return "loopy"
            if name in EDITS:
                return "edit"
        if len(tools) >= limit:
            return "limit"
    return "end"


def summarize(records):
    runs = defaultdict(list)
    for record in records:
        runs[(not record["should"], record["id"])].append(record["outcome"] == "loopy")
    lines = [
        f"{'near miss' if miss else 'should'}\t{id}: {sum(hits)}/{len(hits)}"
        for (miss, id), hits in sorted(runs.items())
    ]
    for miss, label in ((False, "should-trigger queries"), (True, "near misses")):
        hits = [hit for (group, _), outcomes in runs.items() if group == miss for hit in outcomes]
        lines.append(f"Selected for {label}: {sum(hits)}/{len(hits)}")
    return "\n".join(lines)


if __name__ == "__main__":
    main()

"""Copy a Loopy skill and task fixtures into an isolated evaluation workspace."""

import argparse
import json
import shutil
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, required=True)
    args = parser.parse_args()
    skill = args.skill.resolve()
    if not (skill / "SKILL.md").is_file():
        parser.error("--skill must contain SKILL.md")
    source = Path(__file__).resolve().parent
    cases = json.loads((source / "cases.json").read_text(encoding="utf-8"))
    root = Path(tempfile.mkdtemp(prefix="loopy-eval-"))
    shutil.copytree(skill, root / "skill")
    shutil.copytree(source / "fixtures", root / "tasks")
    packet = [
        f"Apply Loopy from {(root / 'skill' / 'SKILL.md').as_posix()}.",
        "Treat each task below as a separate user request and scope.",
        "Read only the supplied skill and its references, task inputs, and applicable global instructions.",
        "Do not inspect the source repository, acceptance criteria, or other evaluation results.",
        "Keep all task and scratch writes in this temporary workspace; respect each request's exclusions.",
        "Record actual changes, commands, observed results, and final responses in run.md at the workspace root.",
        "The coordinator must specify available and authorized delegation before the run.",
    ]
    for case in cases:
        packet.extend([
            "",
            f"Task directory: {(root / 'tasks' / case['id']).as_posix()}",
            case["request"],
        ])
    (root / "requests.md").write_text("\n".join(packet) + "\n", encoding="utf-8")
    print(root)


if __name__ == "__main__":
    main()

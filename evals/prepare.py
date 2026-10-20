import argparse
import shutil
import tempfile
from pathlib import Path

from cases import load_cases


def main():
    parser = argparse.ArgumentParser(description="Copy a Loopy skill and task fixtures into an isolated evaluation workspace.")
    parser.add_argument("--skill", type=Path, required=True)
    parser.add_argument("--case", action="append", dest="ids", help="case ID to include; repeat to select several (default: all)")
    args = parser.parse_args()
    skill = args.skill.resolve()
    if not (skill / "SKILL.md").is_file():
        parser.error("--skill must contain SKILL.md")
    source = Path(__file__).resolve().parent
    try:
        cases = load_cases(source)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if args.ids:
        ids = set(args.ids)
        unknown = ids - {case["id"] for case in cases}
        if unknown:
            parser.error(f"unknown case: {', '.join(sorted(unknown))}")
        cases = [case for case in cases if case["id"] in ids]
    print(prepare(skill, source / "fixtures", cases))


def prepare(skill, fixtures, cases):
    root = Path(tempfile.mkdtemp(prefix="loopy-eval-")).resolve()
    try:
        shutil.copytree(skill, root / "skill")
        for case in cases:
            shutil.copytree(fixtures / case["id"], root / "tasks" / case["id"])
        (root / "requests.md").write_text(render_requests(root, cases), encoding="utf-8")
    except BaseException:
        shutil.rmtree(root)
        raise
    return root


def render_requests(root, cases):
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
    return "\n".join(packet) + "\n"


if __name__ == "__main__":
    main()

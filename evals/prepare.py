"""Copy a Loopy skill and task fixtures into an isolated evaluation workspace."""

import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
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


def load_cases(source):
    path = source / "cases.json"
    cases = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        raise ValueError(f"{path}: expected a nonempty case list")
    ids = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError(f"{path}: expected a case object")
        id = case.get("id")
        if not isinstance(id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", id):
            raise ValueError(f"{path}: invalid case ID {id!r}")
        if id in ids:
            raise ValueError(f"{path}: duplicate case ID {id!r}")
        ids.add(id)
        if not isinstance(case.get("request"), str) or not case["request"].strip():
            raise ValueError(f"{path}: case {id!r} needs a request")
        if not (source / "fixtures" / id).is_dir():
            raise ValueError(f"{path}: missing fixture directory for {id!r}")
    return cases


def prepare(skill, fixtures, cases):
    root = Path(tempfile.mkdtemp(prefix="loopy-eval-")).resolve()
    try:
        shutil.copytree(skill, root / "skill")
        for case in cases:
            shutil.copytree(fixtures / case["id"], root / "tasks" / case["id"])
        (root / "requests.md").write_text(render_requests(root, cases), encoding="utf-8")
    except BaseException:
        if root.parent == Path(tempfile.gettempdir()).resolve() and root.name.startswith("loopy-eval-"):
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

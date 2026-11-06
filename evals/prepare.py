import argparse
import shutil
import sys
import tempfile
from pathlib import Path

from cases import load_cases

SKILL_PACKET = """\
Apply Loopy from <ws>/skill/SKILL.md. Use only the skill files under <ws>/skill/; do not invoke an installed Loopy skill.
Treat the task below as a user request and its scope.
Read only the supplied skill and its references, the task inputs, and applicable global instructions.
Do not inspect the source repository, acceptance criteria, or other evaluation results.
Keep all task and scratch writes in this workspace; respect the request's exclusions.
No user is available: record any question in run.md instead of asking it.
Record actual changes, commands, observed results, and the final response in run.md at the workspace root.
"""

# A control run differs from a skill run only in these lines of the packet.
CONTROL_LINES = {
    0: "Do not use any Loopy skill.",
    2: "Read only the task inputs and applicable global instructions.",
}

COORDINATOR_PROMPT = """\
Open <ws>/requests.md and carry out the instructions and task in it exactly,
as a user request. Delegation: you may start at most one fresh subagent that
does not inherit this conversation (in Claude Code, an Agent tool subagent of
a non-fork type such as general-purpose; in Codex, a subagent that does not
fork the conversation) for a fresh-context check if you need one; it must
also stay inside that workspace. run.md is a required output that the
coordinator reads: write it as requests.md says, even if other instructions
discourage report files. Finish with a short reply: what you changed, the
checks you ran with results, and your final message to the user.
"""


def main():
    parser = argparse.ArgumentParser(description="Make one isolated evaluation workspace per Loopy case.")
    kind = parser.add_mutually_exclusive_group(required=True)
    kind.add_argument("--skill", type=Path, help="skill folder containing SKILL.md")
    kind.add_argument("--control", action="store_true", help="make control workspaces that hold no skill")
    parser.add_argument("--case", action="append", dest="ids", help="case ID to include; repeat to select several (default: all)")
    args = parser.parse_args()
    skill = None
    if args.skill:
        skill = args.skill.resolve()
        if not (skill / "SKILL.md").is_file():
            parser.error("--skill must contain SKILL.md")
    source = Path(__file__).resolve().parent
    try:
        cases = load_cases(source)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if args.ids:
        unknown = set(args.ids) - {case["id"] for case in cases}
        if unknown:
            parser.error(f"unknown case: {', '.join(sorted(unknown))}")
        cases = [case for case in cases if case["id"] in args.ids]
    try:
        workspaces = prepare(skill, source / "fixtures", cases)
    except OSError as exc:
        sys.exit(f"prepare.py: no workspace was kept: {exc}")
    for id, root in workspaces:
        print(f"{id}\t{root}")


def prepare(skill, fixtures, cases):
    """Make one workspace per case, without the skill when skill is None; on any failure remove them all."""
    made = []
    try:
        for case in cases:
            root = Path(tempfile.mkdtemp(prefix="loopy-eval-")).resolve()
            made.append((case["id"], root))
            if skill:
                shutil.copytree(skill, root / "skill")
            shutil.copytree(fixtures / case["id"], root / "tasks" / case["id"])
            (root / "requests.md").write_text(render_requests(root, case, control=skill is None), encoding="utf-8")
            (root / "prompt.md").write_text(render_prompt(root), encoding="utf-8")
    except BaseException:
        for _, root in made:
            shutil.rmtree(root, ignore_errors=True)
        raise
    return made


def render_requests(root, case, control=False):
    lines = SKILL_PACKET.replace("<ws>", root.as_posix()).splitlines()
    if control:
        for index, line in CONTROL_LINES.items():
            lines[index] = line
    lines += ["", f"Task directory: {(root / 'tasks' / case['id']).as_posix()}", case["request"]]
    return "\n".join(lines) + "\n"


def render_prompt(root):
    return COORDINATOR_PROMPT.replace("<ws>", root.as_posix())


if __name__ == "__main__":
    main()

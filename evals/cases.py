"""Load and validate the evaluation catalogue and its fixture directories."""

import json
import re


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
        acceptance = case.get("acceptance")
        if not isinstance(acceptance, list) or not acceptance or any(
            not isinstance(item, str) or not item.strip() for item in acceptance
        ):
            raise ValueError(f"{path}: case {id!r} needs a nonempty acceptance list of nonblank strings")
    return cases

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from cases import load_cases


def main():
    root = Path(__file__).resolve().parent.parent
    errors = []
    for check in (check_metadata, check_cases, check_links):
        try:
            errors.extend(check(root))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"{check.__name__}: {exc}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Plugin metadata, evaluation inputs, and local Markdown links passed.")
    return 0


def check_metadata(root):
    paths = (
        ".codex-plugin/plugin.json",
        ".claude-plugin/plugin.json",
        ".agents/plugins/marketplace.json",
        ".claude-plugin/marketplace.json",
    )
    data = []
    for path in paths:
        try:
            data.append(json.loads((root / path).read_text(encoding="utf-8")))
        except (OSError, ValueError) as exc:
            raise ValueError(f"{path}: {exc}") from exc
    codex, claude, codex_market, claude_market = data
    errors = []
    for key in ("name", "version", "description", "author", "homepage", "repository", "license"):
        if codex[key] != claude[key]:
            errors.append(f"Plugin manifests disagree on {key}.")
    for path, market in zip(paths[2:], (codex_market, claude_market)):
        plugins = market["plugins"]
        if market["name"] != codex["name"] or len(plugins) != 1 or plugins[0]["name"] != codex["name"]:
            errors.append(f"{path}: marketplace must identify the Loopy plugin.")
            return errors
    codex_source = codex_market["plugins"][0]["source"]
    claude_entry = claude_market["plugins"][0]
    claude_source = claude_entry["source"]
    if codex_source["source"] != "url" or codex_source["url"] != codex["repository"] + ".git":
        errors.append(f"{paths[2]}: source must match the plugin repository.")
    if claude_source["source"] != "github" or "https://github.com/" + claude_source["repo"] != claude["repository"]:
        errors.append(f"{paths[3]}: source must match the plugin repository.")
    if codex_source["ref"] != "main" or claude_source["ref"] != "main":
        errors.append("Both marketplaces must use main.")
    if claude_entry["description"] != claude["description"]:
        errors.append(f"{paths[3]}: description must match the plugin manifest.")
    skill = root / codex["skills"] / codex["name"] / "SKILL.md"
    if not skill.is_file():
        errors.append(f"{paths[0]}: skills path does not resolve to SKILL.md.")
    return errors


def check_cases(root):
    load_cases(root / "evals")
    return []


def check_links(root):
    pending = [root / "README.md"]
    seen = set()
    errors = []
    while pending:
        path = pending.pop().resolve()
        if path in seen:
            continue
        seen.add(path)
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            url = urlsplit(target.strip().strip("<>"))
            if url.scheme or url.netloc or not url.path:
                continue
            dst = (path.parent / unquote(url.path)).resolve()
            if not dst.exists():
                errors.append(f"{path.relative_to(root)}: missing link target {target}")
            elif dst.is_file() and dst.suffix == ".md":
                pending.append(dst)
    return errors


if __name__ == "__main__":
    sys.exit(main())

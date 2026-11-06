import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from cases import load_cases


def main():
    root = Path(__file__).resolve().parent.parent
    errors = []
    for check in (check_metadata, check_cases, check_links, check_skill):
        try:
            errors.extend(check(root))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"{check.__name__}: {exc}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Plugin metadata, evaluation inputs, local Markdown links, and the skill passed.")
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
            if url.scheme or url.netloc or not (url.path or url.fragment):
                continue
            dst = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not dst.exists():
                errors.append(f"{path.relative_to(root)}: missing link target {target}")
                continue
            is_markdown = dst.is_file() and dst.suffix == ".md"
            if url.fragment and is_markdown and unquote(url.fragment) not in anchors(dst):
                errors.append(f"{path.relative_to(root)}: missing anchor {target}")
            if is_markdown:
                pending.append(dst)
    return errors


def anchors(path):
    """GitHub heading anchors: lowercase, drop punctuation, spaces to hyphens, -1 for repeats."""
    found, counts, fence = set(), {}, False
    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("```"):
            fence = not fence
            continue
        heading = re.match(r"#{1,6} +(.+?) *$", line)
        if fence or not heading:
            continue
        slug = re.sub(r"[^\w\- ]", "", heading.group(1).lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        found.add(f"{slug}-{count}" if count else slug)
    return found


def check_skill(root):
    manifest = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    folder = root / manifest["skills"] / manifest["name"]
    path = folder / "SKILL.md"
    where = path.relative_to(root)
    text = path.read_text(encoding="utf-8")
    frontmatter = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not frontmatter:
        return [f"{where}: frontmatter must open and close with ---."]
    errors = []
    fields, key = {}, None
    for line in frontmatter.group(1).split("\n"):
        field = re.match(r"([\w-]+):(.*)", line)
        if field:
            key = field.group(1)
            fields[key] = [field.group(2).strip()]
        elif key and (line[:1] in (" ", "\t") or not line.strip()):
            fields[key].append(line.strip())
        else:
            errors.append(f"{where}: unreadable frontmatter line {line!r}.")
    if sorted(fields) != ["description", "name"]:
        errors.append(f"{where}: frontmatter keys must be name and description, not {', '.join(sorted(fields))}.")
    if " ".join(part for part in fields.get("name", []) if part) != manifest["name"]:
        errors.append(f"{where}: name must be {manifest['name']}.")
    description = fields.get("description", [""])
    if description[0] != ">":
        errors.append(f"{where}: description must be a folded scalar (>).")
    folded = " ".join(part for part in description[1:] if part)
    if not 1 <= len(folded) <= 1024:
        errors.append(f"{where}: description must have 1 to 1,024 characters, not {len(folded):,}.")
    if "<" in folded or ">" in folded:
        errors.append(f"{where}: description must not contain < or >.")
    body = len(text[frontmatter.end():].split())
    if body > 1100:
        errors.append(f"{where}: body has {body:,} words; the limit is 1,100.")
    references = sum(len(p.read_text(encoding="utf-8").split()) for p in (folder / "references").glob("*.md"))
    if references > 2100:
        errors.append(f"{where.parent / 'references'}: references have {references:,} words; the limit is 2,100.")
    return errors


if __name__ == "__main__":
    sys.exit(main())

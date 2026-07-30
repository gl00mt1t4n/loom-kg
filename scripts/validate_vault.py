#!/usr/bin/env python3
"""Validate a LoomKG Obsidian knowledge graph vault."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.cwd()
EXCLUDED_PARTS = {"Hikari-knowledge", "External", ".git"}
ROOT_ALIASES = {"Root Index", "root-index"}
ALLOWED_TYPES = {"index", "concept", "decision", "thesis", "system", "tombstone"}
FORBIDDEN_PROPERTIES = {"status", "confidence", "verified", "watchlist", "asset", "aliases", "summary"}
REQUIRED_PROPERTIES = {"id", "type", "domain"}


def parse_frontmatter(text: str) -> dict[str, Any] | None:
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not match:
        return None
    data: dict[str, Any] = {}
    current: str | None = None
    for raw in match.group(1).splitlines():
        if not raw.strip():
            continue
        if re.match(r"^[A-Za-z_][A-Za-z0-9_-]*:", raw):
            key, value = raw.split(":", 1)
            key = key.strip()
            value = value.strip()
            current = key
            data[key] = [] if not value else value.strip('"\'')
        elif current and raw.startswith("  - "):
            if not isinstance(data.get(current), list):
                data[current] = []
            data[current].append(raw[4:].strip())
    return data


def list_items(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    out: list[str] = []
    in_section = False
    for line in lines:
        if line.startswith("## "):
            in_section = line.strip("# ").strip().lower() == heading.lower()
            continue
        if in_section and line.startswith("#"):
            break
        if in_section:
            m = re.match(r"^- `?([^`\n]+?)`?$", line.strip())
            if m:
                out.append(m.group(1).strip())
    return out


def load_allowed_values(vault: Path) -> tuple[set[str], set[str]]:
    props = (vault / "Registries" / "Properties.md").read_text(errors="ignore")
    tags = (vault / "Registries" / "Tags.md").read_text(errors="ignore")
    domains = set(list_items(props, "Starter domains") or list_items(props, "Approved domains"))
    approved_tags = set(list_items(tags, "Starter domain-overlap tags") or list_items(tags, "Approved tags"))
    approved_tags |= set(list_items(tags, "Support tags"))
    return domains, approved_tags


def wikilinks(text: str) -> list[str]:
    links = []
    for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
        target = match.group(1).split("|", 1)[0].strip()
        if "{{" in target and "}}" in target:
            continue
        links.append(target)
    return links


def is_external(rel: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in rel.parts)


def is_skill_artifact(rel: Path) -> bool:
    return len(rel.parts) >= 3 and rel.parts[0] == "Skills" and rel.name == "SKILL.md"


def is_template_file(rel: Path) -> bool:
    return len(rel.parts) >= 2 and rel.parts[0] == "Templates" and rel.name != "Templates.md"


def allows_missing_frontmatter(rel: Path) -> bool:
    # GitHub renders README frontmatter as an ugly table. Keep the public
    # landing page clean while still validating the rest of the vault.
    return len(rel.parts) == 1 and rel.name == "README.md"


def is_placeholder(value: Any) -> bool:
    return isinstance(value, str) and "{{" in value and "}}" in value


def note_aliases(path: Path, rel: Path, data: dict[str, Any] | None) -> set[str]:
    aliases = {path.stem, str(rel.with_suffix("")), str(rel)}
    if data and isinstance(data.get("id"), str) and not is_placeholder(data["id"]):
        aliases.add(data["id"])
    return aliases


def validate_schema(rel: Path, data: dict[str, Any] | None, allowed_domains: set[str], allowed_tags: set[str]) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    rel_s = str(rel)
    if data is None:
        if allows_missing_frontmatter(rel):
            return []
        return [{"file": rel_s, "error": "missing_frontmatter"}]
    if is_skill_artifact(rel):
        missing = sorted({"name", "description", "platforms"} - set(data))
        if missing:
            errors.append({"file": rel_s, "error": "skill_schema_missing", "keys": missing})
        return errors
    missing = sorted(REQUIRED_PROPERTIES - set(data))
    if missing:
        errors.append({"file": rel_s, "error": "missing_required_properties", "keys": missing})
    forbidden = sorted(FORBIDDEN_PROPERTIES & set(data))
    if forbidden:
        errors.append({"file": rel_s, "error": "forbidden_properties", "keys": forbidden})
    if not is_template_file(rel):
        if data.get("type") not in ALLOWED_TYPES:
            errors.append({"file": rel_s, "error": "invalid_type", "value": data.get("type")})
        if data.get("domain") not in allowed_domains:
            errors.append({"file": rel_s, "error": "invalid_domain", "value": data.get("domain")})
        tags = data.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        if isinstance(tags, list):
            for tag in tags:
                if tag not in allowed_tags:
                    errors.append({"file": rel_s, "error": "invalid_tag", "value": tag})
    return errors


def main() -> int:
    vault = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else DEFAULT_VAULT.resolve()
    if not vault.exists():
        print(json.dumps({"ok": False, "error": f"vault not found: {vault}"}, indent=2))
        return 2
    try:
        allowed_domains, allowed_tags = load_allowed_values(vault)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"could not load registries: {exc}"}, indent=2))
        return 2
    notes: dict[str, dict[str, Any]] = {}
    schema_errors: list[dict[str, Any]] = []
    for path in vault.rglob("*.md"):
        rel = path.relative_to(vault)
        if is_external(rel):
            continue
        text = path.read_text(errors="ignore")
        data = parse_frontmatter(text)
        schema_errors.extend(validate_schema(rel, data, allowed_domains, allowed_tags))
        notes[str(rel)] = {"aliases": note_aliases(path, rel, data), "links": wikilinks(text)}
    alias_to_rel: dict[str, str] = {}
    collisions: dict[str, set[str]] = {}
    for rel, info in notes.items():
        for alias in info["aliases"]:
            if alias in alias_to_rel and alias_to_rel[alias] != rel:
                collisions.setdefault(alias, set()).update([alias_to_rel[alias], rel])
            else:
                alias_to_rel[alias] = rel
    unresolved: list[tuple[str, str]] = []
    adj = {rel: [] for rel in notes}
    for rel, info in notes.items():
        for target in info["links"]:
            resolved = alias_to_rel.get(target)
            if resolved:
                adj[rel].append(resolved)
            else:
                unresolved.append((rel, target))
    root = next((alias_to_rel[a] for a in ROOT_ALIASES if a in alias_to_rel), None)
    seen: set[str] = set()
    if root:
        stack = [root]
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend([n for n in adj[node] if n not in seen])
    unreachable = sorted(set(notes) - seen)
    result = {
        "ok": bool(root) and not schema_errors and not collisions and not unresolved and not unreachable,
        "vault": str(vault),
        "root": root,
        "allowed_domains": sorted(allowed_domains),
        "allowed_tags": sorted(allowed_tags),
        "non_external_markdown": len(notes),
        "reachable_from_root": len(seen),
        "schema_errors": schema_errors,
        "unreachable": unreachable,
        "unresolved_wikilinks": unresolved,
        "alias_collisions": {k: sorted(v) for k, v in collisions.items()},
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

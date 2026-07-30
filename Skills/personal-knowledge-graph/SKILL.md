---
name: personal-knowledge-graph
description: Use when maintaining a LoomKG/Obsidian knowledge graph.
platforms: [linux, macos, windows]
---

# Personal Knowledge Graph

Use for Obsidian KG changes, durable knowledge, graph/index rules, task-vs-note routing, tombstones, templates, validation, and skill provenance.

## Constants to resolve per vault

- Vault root: current LoomKG vault root
- Root index: `Root Index.md` unless customized
- Architecture: `Graph Architecture.md`
- Properties: `Registries/Properties.md`
- Tags: `Registries/Tags.md`
- External corpora: user-approved detached folders only

## Routing

- Tasks/status/follow-up -> user's task system, if any.
- Durable reasoning/context/evidence -> Obsidian.
- Both -> update both and link when useful.

## Graph invariants

- Every normal non-external markdown file must be reachable from the root index.
- One primary home per note; use tags/links for cross-domain overlap.
- No duplicate notes across domains.
- Domain folders are for browsing; frontmatter is semantic truth.
- External corpora may be cited, but they do not define this graph's taxonomy or purpose.

## Templates

- Use `Templates/` when creating new KG notes.
- Remove optional placeholder fields that are not useful.
- Do not create blank note shells; create/update only when there is durable content.

## Write workflow

1. Search existing notes.
2. Read relevant maps/links.
3. Prefer updating existing nodes.
4. Create only distinct durable notes.
5. Use controlled properties/tags from registries.
6. Use the closest template, then remove unused optional fields.
7. Link sparsely but enough for reachability.
8. Tombstone/supersede stale reasoning instead of deleting it.

## Validation

Run from vault root after edits:

```bash
python scripts/validate_vault.py .
```

## Git policy

For approved vault changes: verify, run `git status --short`, commit related changes, push to the user's `origin/main`, and report the commit hash.

When a commit is pushed, end with a concise line like: `commit abc1234: "Message" pushed to main.`

## Done means

- search-before-write done;
- external corpora untouched unless explicitly requested;
- no unresolved wikilinks;
- all normal markdown reachable from root index;
- validation passed;
- approved changes committed/pushed;
- useful completed work considered for Obsidian/task capture, with user asked before creating entries.

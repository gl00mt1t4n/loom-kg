---
id: graph-architecture
type: system
domain: Systems
links:
  - [[Root Index]]
  - [[Registries/Properties|Properties]]
  - [[Registries/Tags|Tags]]
  - [[Templates]]
  - [[Skills]]
---

# Graph Architecture

LoomKG is a small, durable knowledge graph built from Markdown files, Obsidian wikilinks, controlled frontmatter, templates, and agent-maintained validation.

## Layers

- **Obsidian** is the human UI over normal files.
- **Agent instructions** define how agents create and maintain nodes.
- **Registries** define valid properties, types, domains, and tags.
- **Templates** keep new notes consistent.
- **GitHub** provides private versioning and backup for each user's living graph.

## Folder model

Domain folders are for human browsing. Frontmatter is semantic truth.

A note should have one primary domain. Use tags and links for overlap instead of duplicating notes across domains.

## Graph invariant

Every normal markdown file must be reachable from [[Root Index]], directly or indirectly.

External corpora are excluded from personal graph validation.

## Capture boundary

- Durable knowledge, decisions, theses, context, and evidence belong in Obsidian.
- Actionable work, status, bugs, and follow-ups belong in a task system if the user uses one.
- Secrets and runtime credentials stay outside the vault.

## Public starter boundary

The public LoomKG repo is a starter. A user's living graph should become their own private repo after setup.

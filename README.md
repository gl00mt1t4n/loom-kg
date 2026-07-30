---
id: readme
type: system
domain: Systems
links:
  - [[AGENTS]]
  - [[Root Index]]
  - [[Graph Architecture]]
  - [[Registries/Properties|Properties]]
  - [[Registries/Tags|Tags]]
  - [[Skills]]
---

# LoomKG

**LOOM = Linked Obsidian Operating Memory.**

LoomKG is a cloneable Obsidian + agent knowledge graph foundation.

It gives you a visible starter vault, note templates, controlled properties/tags, an agent setup guide, and a validator so an AI agent can customize the system into your own private knowledge graph.

## Quick start

1. Install Obsidian from https://obsidian.md/download.
2. Clone this repo:

```bash
git clone https://github.com/<owner>/loom-kg.git
```

3. Open Obsidian.
4. Choose **Open folder as vault**.
5. Select the cloned `loom-kg` folder.
6. Ask your agent: "Read `AGENTS.md` and help initialize this LoomKG vault for me."

Obsidian treats a vault as a normal folder of Markdown files. Opening the cloned folder as a vault is enough to see this structure.

## What this is for

Use LoomKG for durable knowledge:

- concepts and explanations
- decisions and why they were made
- theses and invalidation conditions
- system/workflow notes
- tombstones for dead ends
- distilled source notes
- cross-session context

Do not use it for:

- raw chat dumps
- transient todos
- credentials or tokens
- private runtime config
- copied sources without synthesis

## GitHub-first personal vaults

LoomKG is designed so every person ends with their own private GitHub repo tracking their knowledge graph.

The setup agent should customize this starter vault, then ask whether you are happy with the foundation. If yes, it should re-home Git so normal commits and pushes go to your own repo, not the public LoomKG starter.

Default private repo name: `<github-user>kg` unless you choose another name.

Default Git flow:

```bash
gh repo create <your-user>/<your-user>kg --private --description "Personal LoomKG knowledge graph" || true
git remote rename origin template-upstream
git remote add origin https://github.com/<your-user>/<your-user>kg.git
git push -u origin main
```

Result:

- `origin` points to your private knowledge graph repo.
- `template-upstream` points to the public LoomKG starter for intentional future comparison.
- normal `git push` goes to your repo.

If you want no connection to the starter repo, the agent can instead remove `.git` and initialize a fresh repository.

## How the pieces fit

- Obsidian is the durable knowledge graph UI.
- Your agent maintains the graph with templates, registries, and validation.
- GitHub stores your private versioned backup.
- A task system such as Linear can track actionable work, but LoomKG does not set it up.
- External corpora such as Hikari can be added later as detached references.

## Start here

- [[AGENTS]] — agent setup and maintenance guide.
- [[Root Index]] — root graph entrypoint.
- [[Graph Architecture]] — compact architecture and operating model.
- [[Registries/Properties|Properties]] — frontmatter/property registry.
- [[Registries/Tags|Tags]] — approved tag registry.
- [[Skills]] — agent skill/instruction inventory.

## Public starter policy

This repo is the starter kit. Your living knowledge graph should become your own repo after setup.

Do not blindly merge future LoomKG changes into a living vault. Compare manually and copy only the improvements you want.

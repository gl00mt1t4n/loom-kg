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
  - [[Templates]]
  - [[Skills]]
  - [[CLAUDE]]
---

<div align="center">

<img src="assets/loomkg-banner.jpg" alt="LoomKG banner" width="100%" />

# LoomKG

**Linked Obsidian Operating Memory**

A cloneable Obsidian + agent knowledge graph foundation.

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge&labelColor=0b0b0b&color=ffffff"></a>
  <img alt="Markdown" src="https://img.shields.io/badge/Markdown-native-black?style=for-the-badge&labelColor=0b0b0b&color=ffffff">
  <img alt="Obsidian" src="https://img.shields.io/badge/Obsidian-ready-black?style=for-the-badge&labelColor=0b0b0b&color=ffffff">
  <img alt="Agent ready" src="https://img.shields.io/badge/Agent-ready-black?style=for-the-badge&labelColor=0b0b0b&color=ffffff">
</p>

</div>

---

## Premise

AI chats forget. Note vaults drift. Project docs stay trapped in the repo where they were written.

LoomKG is a small foundation for a different pattern: let an agent preserve durable knowledge, decisions, sources, and context into a normal Markdown/Obsidian graph, then keep that graph versioned in your own private GitHub repository.

The public `loom-kg` repo is only the seed. The living graph becomes yours.

## What LoomKG provides

**A visible starter vault**  
Open the cloned folder in Obsidian and you immediately get a root index, domain maps, registries, templates, skills, and validation script.

**A deterministic agent setup path**  
`AGENTS.md` tells Hermes, Claude Code, Codex, or another coding agent exactly how to ask questions, apply defaults, customize the graph, validate it, and re-home Git.

**A controlled graph shape**  
Properties, note types, domains, and tags are intentionally constrained so the graph remains browseable, searchable, and maintainable.

**A private GitHub endpoint**  
After setup, the agent moves `origin` to your own private repo. Commits become a durable audit trail and cloud backup for the knowledge graph.

**A global capture habit**  
The setup flow can install a short global rule into your agent's own instruction/memory layer so it remembers to ask whether useful work belongs in notes or tasks.

## Start in five minutes

Install Obsidian:

- https://obsidian.md/download

Clone LoomKG:

```bash
git clone https://github.com/gl00mt1t4n/loom-kg.git
cd loom-kg
```

Open it:

1. Open Obsidian.
2. Choose **Open folder as vault**.
3. Select the cloned `loom-kg` folder.
4. Optional but recommended: enable showing unsupported/all file extensions so you can see files such as `scripts/validate_vault.py`.

Then ask your agent:

```text
Read AGENTS.md and help initialize this LoomKG vault for me.
```

Obsidian vaults are just folders of Markdown files. No database import is required.

## Tooling

Required:

- **Obsidian** — https://obsidian.md/download
- **Git** — https://git-scm.com/downloads
- **GitHub account** — https://github.com

Recommended:

- **GitHub CLI** — https://cli.github.com  
  Lets the setup agent create the private repo and push automatically.

- **Hermes Agent** — https://hermes-agent.nousresearch.com/docs  
  Recommended runtime because it supports skills, memory, tools, scheduled work, and cross-session behavior.

Compatible:

- **Claude Code** — https://docs.anthropic.com/en/docs/claude-code  
  Uses the `CLAUDE.md` shim, which points back to `AGENTS.md`.

- **Linear** — https://linear.app  
  Optional task layer for actionable work. LoomKG stores durable knowledge, not transient status.

Hermes is the preferred runtime, not a requirement. The repo is written so any capable coding agent can follow `AGENTS.md`.

## What happens during setup

The setup questions in [[AGENTS]] all include defaults. You can answer only what you care about.

After answers, the agent should:

1. resolve omitted answers from defaults
2. show a compact checklist of the intended setup
3. customize domains, tags, root index, and selected integrations
4. install the approved knowledge-capture rule into the agent's global instruction/memory layer
5. validate the graph
6. ask whether the foundation is good
7. create or connect your private GitHub repo
8. re-home Git so future pushes go to your repo
9. commit and push the initialized graph

## GitHub-first ownership

Every living LoomKG should end up tied to a private repo owned by its user.

Default private repo name:

```text
<github-user>kg
```

Default re-home flow:

```bash
gh repo create <your-user>/<your-user>kg --private --description "Personal LoomKG knowledge graph" || true
git remote rename origin template-upstream
git remote add origin https://github.com/<your-user>/<your-user>kg.git
git push -u origin main
```

Result:

- `origin` points to your private knowledge graph repo.
- `template-upstream` points to this public starter for intentional comparison.
- normal `git push` goes to your private repo.

If you want full detachment, the agent can remove `.git` and initialize a fresh repository instead.

## What belongs here

Good LoomKG material:

- reusable concepts and explanations
- source distillations
- decisions and their reasoning
- falsifiable theses
- systems and workflows
- tombstones for dead ends or superseded ideas
- cross-session context future agents should recover

Keep out:

- raw chat dumps
- transient todos
- secrets, API keys, OAuth tokens, passwords
- local runtime config
- copied sources without synthesis
- task status that belongs in a task system

## Architecture

LoomKG is deliberately simple.

- **Markdown files** are the source of truth.
- **Obsidian** is the human interface.
- **Frontmatter** carries controlled metadata.
- **Wikilinks** create graph edges.
- **Templates** keep notes consistent.
- **Registries** define valid types, domains, and tags.
- **The validator** checks mechanical graph health.
- **Agent instructions** make setup and maintenance repeatable.
- **GitHub** provides private backup and history.

Start with:

- [[Root Index]] — root graph entrypoint
- [[Graph Architecture]] — compact system model and invariants
- [[Registries/Properties|Properties]] — approved frontmatter schema
- [[Registries/Tags|Tags]] — approved broad tags
- [[Templates]] — note templates
- [[Skills]] — agent skill/instruction inventory
- [[AGENTS]] — setup and maintenance instructions for agents

## Validation

Run from the vault root:

```bash
python scripts/validate_vault.py .
```

The validator checks:

- required frontmatter
- approved type/domain/tag values
- wikilink resolution
- duplicate IDs/aliases
- reachability from [[Root Index]]
- exclusion of external corpora from the personal graph

## External corpora

LoomKG does not include Hikari or any other external knowledge base by default.

If you want Hikari or another reference corpus, the setup agent should add it as a detached external folder/submodule, exclude it from validation, and avoid writing personal notes inside it.

## License

MIT. See [`LICENSE`](LICENSE).

## Public starter policy

This repository is the starter kit. A living personal knowledge graph should become the user's own private repository after setup.

Do not blindly merge future LoomKG changes into a living vault. Compare manually and copy only the improvements you want.

---
id: agents
type: system
domain: Systems
links:
  - [[README]]
  - [[Root Index]]
  - [[Graph Architecture]]
  - [[Registries/Properties|Properties]]
  - [[Registries/Tags|Tags]]
  - [[Templates]]
  - [[Skills]]
---

# AGENTS

Use this when an agent is asked to initialize, customize, or maintain a LoomKG knowledge graph.

LoomKG is agent-agnostic. Hermes is recommended because it has native skills and persistent memory, but Claude Code, Codex, and other coding agents can follow this file too.

## First response rule

When starting setup, do not explain between questions. Ask pointed questions back-to-back and end with:

Answer the following questions one by one:

## Setup questions

1. What should this vault be called?
2. What local path should it live at?
3. What should the root index file be named?
4. What GitHub username or organization should own the private knowledge graph repo?
5. What should the private repo be named? Default: `<github-user>kg`.
6. Should I keep this public starter as `template-upstream`, or fully detach Git history and start fresh?
7. What primary domains do you want?
8. Should I include the default support tags `workflow`, `system`, and `research`?
9. Do you want a `College` or school domain?
10. Do you want Hikari or another external reference corpus?
11. Do you use Linear or another task system for actionable work?
12. Should I install/update a global agent rule to consider knowledge/task capture after useful work?
13. If Hermes is available, should I install the LoomKG skill into Hermes runtime skills?
14. Should Obsidian be configured to show unsupported file extensions such as `.py`?
15. After setup, should I create/push the private GitHub repo?

## Agent runtime compatibility

- Canonical instructions: `AGENTS.md`.
- Claude Code shim: `CLAUDE.md` points here.
- Hermes shim: `.hermes.md` points here and can trigger the LoomKG skill.
- Unknown agent: read and follow `AGENTS.md` directly.

If the user wants Hermes and Hermes is not installed, help install Hermes, then tell the user to start a Hermes session in this repo and point it at `AGENTS.md`. Codex users may be able to OAuth through Hermes; Claude users can still use this repo through `CLAUDE.md`.

## Customize the vault

After the user answers:

1. Rename the vault/root index if requested.
2. Create the selected domain folders and domain map notes.
3. Update [[Registries/Tags|Tags]] so approved tags are the selected domain names plus `workflow`, `system`, and `research` when enabled.
4. Keep the property/type schema from [[Registries/Properties|Properties]] unless the user explicitly changes it.
5. Update [[Root Index]] so every non-external markdown file is reachable.
6. Update [[Graph Architecture]] only for architecture-level choices.
7. Keep notes minimal. Do not create personal content unless the user provides it.

## GitHub ownership

Every user's living KG should track their own private GitHub repo. Default repo name: `<github-user>kg` unless the user chooses another name.

After customization and user confirmation, create the private GitHub repo if requested, then default to:

```bash
gh repo create <owner>/<repo> --private --description "Personal LoomKG knowledge graph" || true
git remote rename origin template-upstream
git remote add origin https://github.com/<owner>/<repo>.git
git push -u origin main
```

Use a private repo unless the user explicitly asks for public.

If the user wants full detachment:

```bash
rm -rf .git
git init
git add .
git commit -m "Initialize LoomKG vault"
git branch -M main
gh repo create <owner>/<repo> --private --description "Personal LoomKG knowledge graph" || true
git remote add origin https://github.com/<owner>/<repo>.git
git push -u origin main
```

Do not push to the public LoomKG starter after personalization.

If `gh` is unavailable, ask the user to create a private GitHub repo manually, then add its URL as `origin`.

## Global knowledge-capture rule

Ask before installing this into the user's global agent instructions:

> After useful completed work, consider whether the user's knowledge graph or task system should capture the result. Ask before creating entries. Prefer durable notes for reusable knowledge, decisions, context, and evidence; prefer tasks for follow-up/action/status. Use the vault's templates, registries, and validation rules.

Suggested destinations:

- Hermes: `$HERMES_HOME/SOUL.md`.
- Claude Code: user/project `CLAUDE.md`, depending the user's setup.
- Codex/other agents: persistent user instructions if available, otherwise project `AGENTS.md`.

For Hermes, also install `Skills/personal-knowledge-graph/SKILL.md` into runtime skills if the user approves.

## Obsidian setup

If Obsidian is not installed, direct the user to https://obsidian.md/download.

To open the vault:

1. Open Obsidian.
2. Choose **Open folder as vault**.
3. Select the cloned/customized LoomKG folder.

Command-line opening is not reliable for first-time vault registration; prefer the UI.

## External corpora

Do not include Hikari by default.

If the user wants Hikari or another reference corpus:

- add it as a detached folder or submodule
- exclude it from validation
- keep personal notes out of it
- avoid direct personal-note wikilinks into it by default
- cite with plain paths or distill into personal notes

## Note writing

When creating notes:

1. Search existing notes first.
2. Prefer updating an existing node.
3. Use the closest template from [[Templates]].
4. Remove unused optional fields.
5. Use controlled properties/tags.
6. Link sparsely but enough for reachability.
7. Run validation.

## Validation

Run from the vault root:

```bash
python scripts/validate_vault.py .
```

Validation must pass before setup is done.

## Done criteria

A setup is done when:

- Obsidian can open the vault.
- root index reaches all personal markdown files.
- registries exist and match selected domains/tags.
- templates exist.
- selected global agent rule/skill behavior is installed or clearly declined.
- optional external corpus is detached.
- validation passes.
- Git tracks the user's own repo if GitHub setup was approved.

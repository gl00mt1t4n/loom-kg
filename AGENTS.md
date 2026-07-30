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

When starting setup, do not explain between questions. Ask pointed questions back-to-back. Every question must include a default, and unanswered questions use the default. End with:

Answer the following questions one by one:

## Setup questions

1. What should this vault be called? Default: `<github-user>kg`.
2. What local path should it live at? Default: the current cloned folder.
3. What should the root index file be named? Default: `Root Index.md`.
4. What GitHub username or organization should own the private knowledge graph repo? Default: the authenticated GitHub user.
5. What should the private repo be named? Default: `<github-user>kg`.
6. Should I keep this public starter as `template-upstream`, or fully detach Git history and start fresh? Default: keep starter as `template-upstream`.
7. What primary domains do you want? Default: `Learning`, `Work`, `Systems`, `Decisions`.
8. Should I include the support tags `workflow`, `system`, and `research`? Default: yes.
9. Do you want a `College` or school domain? Default: no.
10. Do you want [Hikari-knowledge](https://github.com/hikarioyama/Hikari-knowledge) or another external reference corpus? Default: no.
11. Do you use Linear or another task system for actionable work? Default: no task system; document the boundary only.
12. Should I install/update a global agent rule to consider knowledge/task capture after useful work? Default: yes, but only after detecting this agent's global instruction file, showing the exact destination/text, and getting confirmation.
13. If Hermes is available, should I install the LoomKG skill into Hermes runtime skills? Default: yes.
14. Should Obsidian be configured to show unsupported file extensions such as `.py`? Default: yes.
15. After setup, should I create/push the private GitHub repo? Default: yes, private repo.

If the user answers briefly, apply defaults for anything omitted. Do not block setup just because the user did not answer every question.

## Agent runtime compatibility

- Canonical instructions: `AGENTS.md`.
- Claude Code shim: `CLAUDE.md` points here.
- Hermes shim: `.hermes.md` points here and can trigger the LoomKG skill.
- Unknown agent: read and follow `AGENTS.md` directly.

If the user wants Hermes and Hermes is not installed, help install Hermes, then tell the user to start a Hermes session in this repo and point it at `AGENTS.md`. Codex users may be able to OAuth through Hermes; Claude users can still use this repo through `CLAUDE.md`.

## After the user answers

Use this procedure. Do not invent a different setup flow unless the user asks.

1. Resolve defaults for unanswered questions.
2. Confirm the resolved setup in a compact checklist.
3. Run the setup preflight below and report blockers before editing.
4. Rename/move the local folder only if the user requested a different path/name.
5. Rename the root index only if requested; otherwise keep `Root Index.md`.
6. Create exactly the selected domain folders and same-name domain map notes.
7. Remove starter domain folders/maps that the user did not select, unless the user asked to keep examples.
8. Update [[Registries/Properties|Properties]] so approved domains match the selected domains.
9. Update [[Registries/Tags|Tags]] so approved tags are selected domain names plus enabled support tags.
10. Update [[Root Index]] so it links to core support files and selected domain maps only.
11. Update [[Graph Architecture]] only for architecture-level choices.
12. Keep notes minimal. Do not create personal content unless the user provides it.
13. If an external corpus is selected, add it as detached/excluded; otherwise leave none.
14. If the global capture rule is approved, install it using the agent-agnostic global-instruction procedure below. It must land in the active agent's user/global instruction layer, not this repo's project files.
15. If Hermes skill installation is approved, install/copy `Skills/personal-knowledge-graph/SKILL.md` into Hermes runtime skills.
16. Run validation and fix failures.
17. Ask whether the user is happy with the customized foundation.
18. If yes and GitHub setup is approved, create the user's private repo, re-home Git, commit, and push.
19. Report the pushed commit concisely.

## Setup preflight

Before making durable setup changes, check the local tools and repo state:

```bash
python --version || python3 --version
git --version
git status --short
git config user.name
git config user.email
```

If private GitHub repo creation/push is approved, also check:

```bash
gh --version
gh auth status
gh api user --jq .login
```

Handle failures explicitly:

- If Python is missing, validation cannot run; install Python or ask the user for their preferred install path.
- If Git is missing, repository setup cannot continue; install Git or ask the user.
- If `user.name` or `user.email` is missing, set repo-local Git identity before committing.
- If `gh` is missing, ask the user to install GitHub CLI or create the private repo manually.
- If `gh auth status` fails, ask the user to authenticate with GitHub before creating/pushing the private repo.
- If the working tree is dirty with user edits, inspect and preserve them; do not overwrite unrelated changes.

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

This rule must go into the active agent's global instruction/memory file: the equivalent of Hermes `SOUL.md` for whatever agent is currently doing setup.

Do not install it only in this repo's `AGENTS.md`, `CLAUDE.md`, or `.hermes.md`, because project-local files apply only when the agent is working inside this knowledge graph repo. The point is cross-project behavior: when the user is working in some unrelated codebase, the agent should still remember to ask whether durable knowledge or tasks should be captured.

Ask before installing this into the user's global agent instructions:

> After useful completed work, consider whether the user's knowledge graph or task system should capture the result. Ask before creating entries. Prefer durable notes for reusable knowledge, decisions, context, and evidence; prefer tasks for follow-up/action/status. Use the vault's templates, registries, and validation rules.

Suggested destinations:

- Hermes: `$HERMES_HOME/SOUL.md`.
- Claude Code: the user's global Claude memory/instructions file, not this repo's `CLAUDE.md` shim.
- Codex/other agents: the agent's documented persistent user/global instructions file, not a project-local shim.

If the active agent has no writable global instruction layer, say that clearly and ask whether to proceed with project-local instructions as a weaker fallback. Do not silently use the project-local fallback.

For Hermes, also install `Skills/personal-knowledge-graph/SKILL.md` into runtime skills if the user approves.

### Agent-agnostic global instruction procedure

Use this procedure instead of hard-coding Hermes behavior:

1. Identify the active agent/runtime: Hermes, Claude Code, Codex, Cursor, OpenCode, or other.
2. Locate that runtime's user/global instruction file from its docs, config, or existing files.
3. If the global file path is uncertain, ask the user instead of guessing.
4. Show the user:
   - detected agent/runtime
   - exact global instruction destination
   - exact rule text to add
   - whether a repo-local fallback would be needed
5. Wait for approval.
6. Append or merge the rule into the global instruction file without duplicating an existing equivalent rule.
7. Do not place secrets, tokens, machine credentials, or project-private details in the global rule.
8. Verify by reading back the relevant non-secret snippet from the global file.

Examples of intent:

- Hermes: add the rule to global `SOUL.md`.
- Claude Code: add the rule to Claude's user/global memory or instruction file.
- Codex/OpenCode/Cursor/other agents: add the rule to that agent's documented global instructions.

If no durable global layer exists, say so and ask whether the user wants to keep only the repo-local instructions. Repo-local instructions are acceptable as a fallback, but they do not create cross-project capture behavior.

## Obsidian setup

If Obsidian is not installed, direct the user to https://obsidian.md/download.

To open the vault:

1. Open Obsidian.
2. Choose **Open folder as vault**.
3. Select the cloned/customized LoomKG folder.

Command-line opening is not reliable for first-time vault registration; prefer the UI.

## External corpora

Do not include Hikari by default.

Credit/reference link: [Hikari-knowledge](https://github.com/hikarioyama/Hikari-knowledge), by Hikari / `hikarioyama`.

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

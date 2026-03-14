# Changelog — Product_lifecycle

All notable changes to this template are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versions follow [Semantic Versioning](https://semver.org/).

Derived projects sync updates with: `copier update`

---

## [Unreleased]

---

## [v1.0.0] — 2026-03-14

First stable release. Establishes the full product lifecycle template with Copier support.

### Added
- `copier.yml` — template configuration; derived projects can now `copier update` to receive future improvements
- `/release` skill — guided release workflow for Product_lifecycle (changelog → tag → push)
- `CHANGELOG.md` — this file; tracks all template changes going forward
- `opportunity-tree` skill — interactive Obsidian Canvas editor for Teresa Torres opportunity trees
- `prd` skill — interactive PRD generation with Q&A in main conversation
- `flow-designer` skill — interactive flow co-design producing Mermaid diagrams
- `repo-structure` skill — file storage conventions and naming protocols
- `skill-creator` skill — guide for creating new Claude Code skills
- `frontendUIAgent` — subagent producing UI specs and Figma prompts
- `backendAgent` — subagent producing API contracts, schema, and logic
- `er-diagram-generator` — subagent producing Mermaid ER diagrams
- `/init-context` command — bootstraps all `context_knowledge/` files interactively
- `/update-*` commands — individual update commands for each knowledge file
- `/commit` command — guided git commit workflow
- `/transcripts` command — interview transcription pipeline

### Changed
- Opportunity tree format migrated from custom JSON (`opportunity_tree.json`) to Obsidian Canvas (`opportunity_tree.canvas` + `opportunity_tree.md`) for visual editing
- `update-opportunity-tree` command now delegates entirely to the `opportunity-tree` skill
- `prd/references/knowledge-schemas.md` uses generic `[Product]` placeholders (previously hardcoded to "Balance")

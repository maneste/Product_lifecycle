# Changelog — Product_lifecycle

All notable changes to this template are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versions follow [Semantic Versioning](https://semver.org/).

Derived projects sync updates with: `copier update`

---

## [Unreleased]

---

## [v1.2.1] — 2026-03-18

### Fixed
- `copier update` now works correctly — replaced nested `questions:` block with flat top-level format in `copier.yml`. The nested format caused copier's internal update worker to treat `questions` as a required user variable, breaking all derived project updates.

---

## [v1.2.0] — 2026-03-16

### Added
- `interview-script` skill — generates Mom Test–compliant 5-phase interview guides (warm-up, user life, current behavior, deep dive, close) from a PRD. Always starts by asking what the PM has — no path assumptions. Determines Discover vs. Validate mode from gap analysis score or PRD evidence, adapts questions to specific feature gaps, and includes an anti-bias checklist for the interviewer

---

## [v1.1.0] — 2026-03-16

### Added
- `gap-analysis` skill — analyzes PRDs to identify and score knowledge gaps before committing to design or development. Implements 14-gap taxonomy (Assumption Mapping, Four Big Risks, Research Mom Test), UK GDS severity scoring (`Risk = Impact × (10 - Confidence)`), unknown-unknown techniques (pre-mortem, Roger Martin's "What would have to be true?", assumption inversion, reverse Five Whys), and recommends Discover vs. Validate research mode per gap profile
- `RESEARCH_ROADMAP.md` — tracks 5 planned improvements to the research module inspired by the Mercadona AI User Story Framework (gap analysis, dynamic interview scripts, Discover/Validate modes, bad-data filtering, JTBD structured output)

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

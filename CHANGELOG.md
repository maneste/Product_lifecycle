# Changelog — Product_lifecycle

All notable changes to this template are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versions follow [Semantic Versioning](https://semver.org/).

Derived projects sync updates with: `copier update`

---

## [Unreleased]

---

## [v2.0.0] — 2026-04-13

### Changed
- `CLAUDE.md` — slimmed from 166 to 58 lines; removed redundant sections (Context Knowledge Commands, Template Management), simplified repo tree to directories only, added reference lines pointing to skills/commands for detail
- `init-context.md`, `update-vision.md`, `init-project.md` — migrated all paths from `context_knowledge/` to canonical locations: `hq/`, `hq/personas/`, `hq/research/`, `hq/decisions/`, `docs/product/`
- `prd/SKILL.md`, `prd/references/knowledge-schemas.md` — updated knowledge base read paths to match new locations
- `opportunity-tree/SKILL.md`, `opportunity-tree/references/canvas-conventions.md` — canvas path updated to `hq/opportunity_tree.canvas`
- `frontend-ui/SKILL.md`, `gap-analysis/SKILL.md` — updated `context_knowledge/` references to `hq/`
- `repo-structure/SKILL.md`, `repo-structure/references/device-setup.md` — command output mapping table rebuilt; removed `context_knowledge/` section

### Removed
- `context_knowledge/` as a concept — files redistributed to their semantic homes in `hq/` and `docs/product/`; the directory no longer exists as a special location

### Migration — required after `copier update`

Your `context_knowledge/` files are not moved automatically. Run these commands from your project root:

```bash
# Vision
mv context_knowledge/Vision_*.md hq/

# Persona
mv context_knowledge/User_persona.md hq/personas/

# App flow
mv context_knowledge/*_App_Flow.md docs/product/

# Opportunity tree
mv context_knowledge/opportunity_tree.canvas hq/
mv context_knowledge/opportunity_tree.md hq/

# Research
mv context_knowledge/*_interview_summary.json hq/research/
mv context_knowledge/Benchmark_*.json hq/research/

# Decisions
mv context_knowledge/Notifications_Touchpoints.json hq/decisions/

# Any other files still in context_knowledge/ → move to the closest hq/ subfolder

# Remove the empty directory
rmdir context_knowledge/
```

Then commit:

```bash
git add hq/ docs/product/ context_knowledge/
git commit -m "chore: migrate context_knowledge/ to hq/ and docs/product/ (v2.0.0)"
```

---

## [v1.5.0] — 2026-04-11

### Added
- `update-roadmap` skill — manages `ROADMAP.md` with two operations: sync checkboxes from file existence and frontmatter `status` field (via `sync_roadmap.js`), and add new feature blocks following the repo naming convention

---

## [v1.4.0] — 2026-03-30

### Added
- `frontend-ui` skill — generates UI specifications from flow canvases and PRDs; detects platform from `docs/architecture/` and applies the correct template (React Native, web app, PWA)
- `backend-spec` skill — generates API contracts, DB schema, and backend logic; detects stack from `docs/architecture/` and applies the correct template (REST+PostgreSQL, Supabase, Firebase)
- `screen-map` skill — derives an Obsidian canvas screen architecture map from a flow canvas; groups screens by section, shows navigation edges
- `frontend-ui/templates/` — React Native, web app, and PWA output templates
- `backend-spec/templates/` — REST+PostgreSQL, Supabase, and Firebase output templates
- `flow-designer/references/canvas-spec.md` — Obsidian canvas JSON format, layout rules, and documentation template
- `flow-designer/references/node-conventions.md` — SCN_, ACT_, DEC_, SYS_ node types with color coding

### Changed
- `flow-designer` skill — outputs Obsidian `.canvas` file instead of Mermaid; product-agnostic (removed Balance/health-specific references); reads context from `docs/` and `hq/`; added iteration protocol for human feedback loop
- `repo-structure` skill — updated paths and output mapping table to reflect new skill structure and `docs/product/` destination
- `CLAUDE.md` — updated feature lifecycle table, context references, and repository structure diagram

### Removed
- `frontendUIAgent` agent — replaced by `frontend-ui` skill
- `backendAgent` agent — replaced by `backend-spec` skill
- `er-diagram-generator` agent — replaced by `screen-map` skill
- `flow-designer/references/output-specs.md` — replaced by `canvas-spec.md` and `node-conventions.md`

---

## [v1.3.0] — 2026-03-18

### Added
- `docs/` and `hq/` folder structure scaffolded in all derived projects — `docs/product/` (prd-drafts, User Discovery), `docs/architecture/`, `docs/design/`, `docs/deployment/`, `hq/research/`, `hq/ideas/`, `hq/personas/`, `hq/decisions/`, `hq/brand/`
- Both folders added to `_skip_if_exists` so `copier update` never overwrites project content
- `claude.md` updated to document the new structure

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

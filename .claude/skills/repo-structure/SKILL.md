---
name: repo-structure
description: File storage conventions, naming protocols, and skill output mappings for the Product_lifecycle repo. Use when saving skill outputs, determining file names, or setting up a new device.
---

# File Storage Conventions

## docs/product/ (Version Controlled - GitHub)

All feature documentation lives here. No staging area — skills save directly to `docs/product/`.

### docs/product/prd-drafts/

Feature artifacts produced during the design phase:

- **PRD:** `[Feature_Name]_PRD.md`
- **Flow canvas:** `[Feature_Name]_Flow.canvas`
- **Flow documentation:** `[Feature_Name]_Flow_Documentation.md`
- **Screen map:** `[Feature_Name]_Screen_Map.canvas`

### docs/product/

Implementation specs produced after design is complete:

- **UI specs:** `[Feature_Name]_UI_Specs.md`
- **API contracts:** `[Feature_Name]_API_Contracts.md`
- **DB schema:** `[Feature_Name]_DB_Schema.sql` (or `.md` for NoSQL)
- **Backend logic:** `[Feature_Name]_Backend_Logic.md`

**Feature name format:** PascalCase with underscores — e.g. `Diet_Generator`, `Weight_Plateau_Support`

---

## Skill Output Mapping

| Skill | Output Files | Path |
|-------|-------------|------|
| `prd` | `[Feature_Name]_PRD.md` | `docs/product/prd-drafts/` |
| `flow-designer` | `[Feature_Name]_Flow.canvas`, `[Feature_Name]_Flow_Documentation.md` | `docs/product/prd-drafts/` |
| `screen-map` | `[Feature_Name]_Screen_Map.canvas` | `docs/product/prd-drafts/` |
| `frontend-ui` | `[Feature_Name]_UI_Specs.md` | `docs/product/` |
| `backend-spec` | `[Feature_Name]_API_Contracts.md`, `[Feature_Name]_DB_Schema.*`, `[Feature_Name]_Backend_Logic.md` | `docs/product/` |

## Command Output Mapping

| Command | Output Destination |
|---------|-------------------|
| `/transcripts` | `features/doc_User_Research/outputs/` |
| `/init-context` | `hq/`, `hq/personas/`, `hq/research/`, `hq/decisions/`, `docs/product/` |
| `/update-vision` | `hq/` |
| `/update-persona` | `hq/personas/` |
| `/update-app-flow` | `docs/product/` |
| `/update-opportunity-tree` | `hq/` |
| `/update-interview-summary` | `hq/research/` |
| `/update-benchmark` | `hq/research/` |
| `/update-notifications` | `hq/decisions/` |

---

## Context Knowledge (Read by Skills)

Skills read project context from these locations before generating output:

| What | Path |
|------|------|
| Tech stack / platform | `docs/architecture/` |
| Design system | `docs/design/` |
| Brand guidelines | `hq/brand/` |
| User personas | `hq/personas/` |
| Research / benchmarks | `hq/research/` |
| Opportunity tree | `hq/opportunity_tree.canvas` |
| App flow | `docs/product/[Product]_App_Flow.md` |
| Product vision | `hq/Vision_[Product].md` |
| Notifications strategy | `hq/decisions/Notifications_Touchpoints.json` |

Use `/init-context` to create these files interactively. Use `/update-*` commands to modify individual files.

## features/ (OneDrive Synced - Not Version Controlled)

Finalized feature documentation copied from `docs/product/` after stakeholder sign-off.

## Transcriptions/ (Google Drive Symlinks - Gitignored)

Raw transcript files via Google Drive symlinks: `transcription_source/` and `1st_consultation_source/`.

---

## Standard File Storage Protocol

All skills generating feature documentation follow this protocol:

1. **Determine Feature Name** — PascalCase format. If unclear, ask: "What would you like to name this feature?"
2. **Verify target folder exists** — `docs/product/prd-drafts/` or `docs/product/` (create if needed)
3. **Save files** — exact path per output mapping table above
4. **Confirm** — inform user where files were saved with relative paths

## Rules

1. Use relative paths from repo root — never hardcode absolute paths
2. Use consistent naming — PascalCase for feature names, underscore separators
3. Create folders if needed — `mkdir -p` to ensure parent directories exist
4. Confirm to user — always state where files were saved
5. Ask if unclear — if feature name is ambiguous, ask the user

## New Device Setup

See `references/device-setup.md` for full setup instructions after cloning.

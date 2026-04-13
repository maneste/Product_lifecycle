# Product Lifecycle - Claude Code Instructions

**Product_lifecycle** is a template repository for managing the full product lifecycle: from user research and discovery, through PRD generation, flow design, UI specs, and backend specs.

**All paths are relative to the repository root.**

---

## Repository Structure

```
Product_lifecycle/
├── .claude/
│   ├── commands/          # Slash commands (/init-context, /update-*, /init-project, etc.)
│   └── skills/            # prd, flow-designer, screen-map, frontend-ui, backend-spec,
│                          # opportunity-tree, gap-analysis, repo-structure, release
├── docs/
│   ├── product/           # PRDs, flow canvases, screen maps, UI specs, backend specs
│   │   └── prd-drafts/    # Feature artifacts (canvas, docs) during design phase
│   ├── architecture/      # Tech stack, DB schema, system design
│   ├── design/            # UI design system, colors, assets
│   └── deployment/        # Local setup, env vars, CI/CD
├── hq/
│   ├── personas/          # User personas
│   ├── research/          # Benchmarks, interview summaries
│   ├── decisions/         # Notifications strategy, product decisions
│   ├── ideas/             # Raw brainstorms
│   └── brand/             # Brand assets
├── User_discovery/        # Interview processing pipeline (Python + OpenAI)
├── feature-template/      # Code and implementation templates
├── features/              # Finalized docs (gitignored, OneDrive symlink)
└── Transcriptions/        # Raw transcripts (gitignored, Google Drive symlinks)
```

---

## Feature Lifecycle

| Step | Skill | Output | Path |
|------|-------|--------|------|
| 1. PRD | `prd` | `[Feature]_PRD.md` | `docs/product/prd-drafts/` |
| 2. Flow Design | `flow-designer` | `[Feature]_Flow.canvas` + `[Feature]_Flow_Documentation.md` | `docs/product/prd-drafts/` |
| 3. Screen Map | `screen-map` | `[Feature]_Screen_Map.canvas` | `docs/product/prd-drafts/` |
| 4. UI Specs | `frontend-ui` | `[Feature]_UI_Specs.md` | `docs/product/` |
| 5. Backend Specs | `backend-spec` | `[Feature]_API_Contracts.md` + `[Feature]_DB_Schema.*` + `[Feature]_Backend_Logic.md` | `docs/product/` |

---

## Context Read by Skills

| What | Path | Used by |
|------|------|---------|
| Tech stack / platform | `docs/architecture/` | `frontend-ui`, `backend-spec` |
| Design system | `docs/design/` | `frontend-ui`, `screen-map` |
| Brand guidelines | `hq/brand/` | `frontend-ui` |
| User personas | `hq/personas/` | `prd`, `flow-designer` |
| Product vision | `hq/Vision_[Product].md` | `prd`, `flow-designer` |
| Opportunity tree | `hq/opportunity_tree.canvas` | `prd`, `opportunity-tree` |
| Interview data | `hq/research/` | `prd` |
| App flow | `docs/product/[Product]_App_Flow.md` | `prd`, `flow-designer` |
| Notifications strategy | `hq/decisions/Notifications_Touchpoints.json` | `prd` |

For file naming conventions and full output mapping → `repo-structure` skill.
For knowledge base setup and update commands → `/init-context` and `/update-*` commands.
For template versioning and Copier workflow → `/release` and `/init-project` commands.

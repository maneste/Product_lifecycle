# Product Lifecycle - Claude Code Instructions

This is the central configuration file for Claude Code in this repository. All agents and commands reference this file as the single source of truth for paths, conventions, and workflows.

## What Is This

**Product_lifecycle** is a template repository for managing the full product lifecycle: from user research and discovery, through PRD generation, flow design, UI specs, and backend specs. Clone and adapt it for any digital product.

**All paths in this file and in agent/command configs are relative to the repository root.**

## Repository Structure

```
Product_lifecycle/
├── .claude/
│   ├── agents/
│   │   ├── frontendUIAgent.md        # Frontend UI specs agent
│   │   ├── backendAgent.md           # Backend specs agent
│   │   └── er-diagram-generator.md   # ER diagram generator agent
│   ├── commands/                      # Slash commands (/update-*, /init-context, etc.)
│   ├── skills/                        # Claude Code skills
│   │   ├── prd/                       # PRD generation (interactive, main conversation)
│   │   ├── flow-designer/             # Flow design (interactive, main conversation)
│   │   ├── opportunity-tree/          # Opportunity tree (Obsidian Canvas, Teresa Torres methodology)
│   │   ├── repo-structure/            # File storage conventions & naming protocols
│   │   ├── skill-creator/             # Skill creation guide
│   │   └── release/                   # Template release workflow (Product_lifecycle only)
│   └── COMMANDS_README.md
├── AI_Output/                         # Agent-generated docs (version controlled, staging area)
│   └── doc_[Feature_Name]/            # Feature documentation folders
├── context_knowledge/                 # Private knowledge base (gitignored)
│   ├── Vision_[Product].md
│   ├── User_persona.md
│   ├── [Product]_App_Flow.md
│   ├── opportunity_tree.canvas
│   ├── opportunity_tree.md
│   ├── *_interview_summary.json
│   ├── Benchmark_[Product].json
│   └── Notifications_Touchpoints.json
├── User_discovery/                    # User interview processing scripts
│   ├── bin/ (run, process, aggregate)
│   ├── scripts/ (process_interviews.py, aggregate_results.py)
│   ├── prompts/ (interview_analysis.promptl)
│   └── requirements.txt
├── feature-template/                  # Code and implementation templates
├── features/                          # Finalized docs (gitignored, OneDrive symlink)
├── Transcriptions/                    # Raw transcripts (gitignored, Google Drive symlinks)
└── CLAUDE.md
```

## Feature Lifecycle

The typical workflow for a new feature follows this pipeline:

1. **PRD** — Use the `prd` skill (interactive Q&A in main conversation)
2. **Flow Design** — Use the `flow-designer` skill (interactive co-design in main conversation)
3. **UI Specs** — Use `frontendUIAgent` (subagent, produces UI specs + Figma prompt)
4. **Backend Specs** — Use `backendAgent` (subagent, produces API contracts + schema + logic)
5. **ER Diagram** — Use `er-diagram-generator` (subagent, optional)

All outputs are saved to `AI_Output/doc_[Feature_Name]/`. For file storage conventions, see the `repo-structure` skill.

---

## Context Knowledge Commands

### /init-context — First-Time Setup

Bootstrap a new repo by creating ALL context_knowledge files interactively.

**Files created (in order):**

| # | File | Format | Purpose |
|---|------|--------|---------|
| 1 | `Vision_[Product].md` | Markdown | Product vision, mission, positioning |
| 2 | `User_persona.md` | Markdown | Primary user persona |
| 3 | `[Product]_App_Flow.md` | Markdown + Mermaid | Complete user journey flowchart |
| 4 | `opportunity_tree.canvas` + `opportunity_tree.md` | Obsidian Canvas + Markdown | Hierarchical opportunity framework |
| 5 | `interview_summary.json` | JSON | User evidence mapped to opportunities |
| 6 | `Benchmark_[Product].json` | JSON | Competitive landscape analysis |
| 7 | `Notifications_Touchpoints.json` | JSON | Notification/touchpoint strategy |

### Individual Update Commands

| Command | File Updated | Description |
|---------|-------------|-------------|
| `/update-vision` | `Vision_[Product].md` | Update product vision, pillars, positioning |
| `/update-persona` | `User_persona.md` | Update user persona demographics, needs, goals |
| `/update-app-flow` | `[Product]_App_Flow.md` | Update user journey Mermaid flowchart |
| `/update-opportunity-tree` | `opportunity_tree.canvas` + `opportunity_tree.md` | Add/modify/remove opportunity nodes (delegates to `opportunity-tree` skill) |
| `/update-interview-summary` | `*_interview_summary.json` | Add/update user evidence and quotes |
| `/update-benchmark` | `Benchmark_[Product].json` | Add/update competitor analysis |
| `/update-notifications` | `Notifications_Touchpoints.json` | Add/update notification touchpoints |

**Cross-file dependencies:**
- After updating `opportunity_tree.canvas`, run `/update-interview-summary` to sync entries
- The interview summary `id` field must match reference numbers extracted from canvas card text (first line, e.g., `"1.1.1  Title"`)
- All agents reference these files — changes propagate to future PRDs, flows, and specs

---

## Template Management (Copier)

This repo is a **Copier template**. New projects are created via **GitHub's "Use this template"** button, then initialised with:

```
/init-project   ← run once, immediately after cloning the new project
```

This command sets up Copier tracking (`.copier-answers.yml`) so future template improvements can be synced with:

```bash
copier update   # run from inside the derived project
```

### Releasing a new template version

Use the `/release` skill. It guides through:
1. Showing commits since last tag
2. Determining version bump (patch / minor / major)
3. Writing the `CHANGELOG.md` entry
4. Creating the git tag and pushing

**Version semantics:**
- `patch` — fixes, wording improvements, small tweaks
- `minor` — new skills, agents, or commands (backwards compatible)
- `major` — breaking changes (renamed files, changed copier.yml variables)

### What gets copied to derived projects

Everything except: `copier.yml`, `CHANGELOG.md`, `README.md`, `Development_and_Deployment_Guide.md`, and `.claude/skills/release/` (the release skill is only useful here).

### Project-specific customisations in derived projects

When a derived project adds something useful (e.g., a new generic skill), the workflow to port it back is:
1. Add a generic version to Product_lifecycle
2. Run `/release` to tag a new version
3. In the derived project: `copier update` — if the project had its own version, resolve the conflict keeping both

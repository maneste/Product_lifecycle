# Product Lifecycle - Claude Code Instructions

This is the central configuration file for Claude Code in this repository. All agents and commands reference this file as the single source of truth for paths, conventions, and workflows.

## Repository Overview

**Repository:** `Product_lifecycle` (`https://github.com/maneste/Product_lifecycle.git`)

This repository manages the full product lifecycle for the Balance app: from user research and discovery, through PRD generation, flow design, UI specs, and backend specs.

**All paths in this file and in agent/command configs are relative to the repository root.**

## Current Repository Structure

```
Product_lifecycle/
├── .claude/
│   ├── agents/
│   │   ├── flowDesignerAgent.md      # Flow design agent
│   │   ├── frontendUIAgent.md        # Frontend UI specs agent
│   │   ├── backendAgent.md           # Backend specs agent
│   │   └── er-diagram-generator.md   # ER diagram generator agent
│   ├── commands/                      # Slash commands (/update-*, /init-context, etc.)
│   └── COMMANDS_README.md
├── AI_Output/                         # Agent-generated docs (version controlled, staging area)
│   └── doc_[Feature_Name]/            # Feature documentation folders
├── context_knowledge/                 # Private knowledge base (gitignored)
│   ├── Balance_App_Flow.md
│   ├── Benchmark_Balance.json
│   ├── Notifications_Touchpoints.json
│   ├── *_interview_summary.json
│   ├── User_persona.md
│   ├── Vision_Balance.md
│   └── opportunity_tree.json
├── User_discovery/                    # User interview processing scripts
│   ├── bin/ (run, process, aggregate)
│   ├── scripts/ (process_interviews.py, aggregate_results.py)
│   ├── prompts/ (interview_analysis.promptl)
│   └── requirements.txt
├── feature-template/                  # Code and implementation templates
├── features/                          # Finalized docs (gitignored, OneDrive symlink)
├── Transcriptions/                    # Raw transcripts (gitignored, Google Drive symlinks)
├── skills/                            # Claude Code skills
│   ├── prd/                           # PRD generation (interactive, main conversation)
│   ├── repo-structure/                # File storage conventions & naming protocols
│   └── skill-creator/                 # Skill creation guide
├── .obsidian/                         # Obsidian workspace config
└── CLAUDE.md
```

## Feature Lifecycle

The typical workflow for a new feature follows this pipeline:

1. **PRD** — Use the `prd` skill (interactive Q&A in main conversation)
2. **Flow Design** — Use `flowDesignerAgent` (subagent, produces flow diagram + docs)
3. **UI Specs** — Use `frontendUIAgent` (subagent, produces UI specs + Figma prompt)
4. **Backend Specs** — Use `backendAgent` (subagent, produces API contracts + schema + logic)
5. **ER Diagram** — Use `er-diagram-generator` (subagent, optional)

All outputs are saved to `AI_Output/doc_[Feature_Name]/`. For file storage conventions, see the `repo-structure` skill.

---

## Context Knowledge Commands

### /init-context - First-Time Setup

Bootstrap a new repo by creating ALL context_knowledge files interactively.

**Files created (in order):**

| # | File | Format | Purpose |
|---|------|--------|---------|
| 1 | `Vision_Balance.md` | Markdown | Product vision, mission, positioning |
| 2 | `User_persona.md` | Markdown | Primary user persona |
| 3 | `Balance_App_Flow.md` | Markdown + Mermaid | Complete user journey flowchart |
| 4 | `opportunity_tree.json` | JSON | Hierarchical opportunity framework |
| 5 | `interview_summary.json` | JSON | User evidence mapped to opportunities |
| 6 | `Benchmark_Balance.json` | JSON | Competitive landscape analysis |
| 7 | `Notifications_Touchpoints.json` | JSON | Notification/touchpoint strategy |

### Individual Update Commands

| Command | File Updated | Description |
|---------|-------------|-------------|
| `/update-vision` | `Vision_Balance.md` | Update product vision, pillars, positioning |
| `/update-persona` | `User_persona.md` | Update user persona demographics, needs, goals |
| `/update-app-flow` | `Balance_App_Flow.md` | Update user journey Mermaid flowchart |
| `/update-opportunity-tree` | `opportunity_tree.json` | Add/modify/remove opportunity nodes |
| `/update-interview-summary` | `*_interview_summary.json` | Add/update user evidence and quotes |
| `/update-benchmark` | `Benchmark_Balance.json` | Add/update competitor analysis |
| `/update-notifications` | `Notifications_Touchpoints.json` | Add/update notification touchpoints |

**Cross-file dependencies:**
- After updating `opportunity_tree.json`, run `/update-interview-summary` to sync entries
- The interview summary `id` and `title` fields must match the opportunity tree exactly
- All agents reference these files - changes propagate to future PRDs, flows, and specs

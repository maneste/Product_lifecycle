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
│   │   ├── prdDiscoveryAgent.md      # PRD generation agent
│   │   ├── flowDesignerAgent.md      # Flow design agent
│   │   ├── frontendUIAgent.md        # Frontend UI specs agent
│   │   ├── backendAgent.md           # Backend specs agent
│   │   └── er-diagram-generator.md   # ER diagram generator agent
│   ├── commands/
│   │   ├── init-context.md               # /init-context - Bootstrap all context_knowledge files
│   │   ├── update-vision.md              # /update-vision - Update product vision
│   │   ├── update-persona.md             # /update-persona - Update user persona
│   │   ├── update-app-flow.md            # /update-app-flow - Update app flow diagram
│   │   ├── update-opportunity-tree.md    # /update-opportunity-tree - Update opportunity tree
│   │   ├── update-interview-summary.md   # /update-interview-summary - Update interview evidence
│   │   ├── update-benchmark.md           # /update-benchmark - Update competitive benchmarks
│   │   ├── update-notifications.md       # /update-notifications - Update touchpoints
│   │   └── transcripts.md               # /transcripts - Run transcription pipelines
│   ├── COMMANDS_README.md
│   └── MIGRATION_NOTES.md
├── AI_Output/                         # Agent-generated docs (version controlled, staging area)
│   └── doc_[Feature_Name]/            # Feature documentation folders
│       ├── [Feature_Name]_PRD.md
│       ├── [Feature_Name]_Flow_Diagram.md
│       ├── [Feature_Name]_Documentation.md
│       ├── [Feature_Name]_UI_Specifications.md
│       ├── [Feature_Name]_Figma_Make_Prompt.json
│       ├── [Feature_Name]_API_Contracts.md
│       ├── [Feature_Name]_Database_Schema.sql
│       └── [Feature_Name]_Backend_Logic.md
├── context_knowledge/                 # Private knowledge base (gitignored)
│   ├── Balance_App_Flow.md
│   ├── Benchmark_Balance.json
│   ├── Notifications_Touchpoints.json
│   ├── *_interview_summary.json
│   ├── User_persona.md
│   ├── Vision_Balance.md
│   └── opportunity_tree.json
├── User_discovery/                    # User interview processing scripts (version controlled)
│   ├── bin/
│   │   ├── run                        # Full pipeline: process + aggregate
│   │   ├── process                    # Process interviews with OpenAI
│   │   └── aggregate                  # Aggregate results into summary
│   ├── scripts/
│   │   ├── process_interviews.py      # Interview processing script
│   │   └── aggregate_results.py       # Results aggregation script
│   ├── prompts/
│   │   └── interview_analysis.promptl # Analysis prompt template
│   ├── requirements.txt
│   └── README.md
├── feature-template/                  # Code and implementation templates (version controlled)
│   ├── src/
│   ├── docs/
│   ├── data/
│   ├── prompts/
│   ├── cloud.md
│   ├── package.json
│   └── README.md
├── features/                          # Finalized docs (gitignored, to be set up as OneDrive symlink)
├── Transcriptions/                    # Raw transcripts (gitignored, to be set up as Google Drive symlinks)
├── .obsidian/                         # Obsidian workspace config
├── Development_and_Deployment_Guide.md
├── .gitignore
└── claude.md                          # This file
```

---

# File Storage Conventions (Single Source of Truth)

## Directory Structure for Outputs

### AI_Output/ (Version Controlled - GitHub)

**Purpose:** Staging area for all agent-generated feature documentation.

**Path:** `AI_Output/`

**Folder Pattern:** `AI_Output/doc_[Feature_Name]/`

**Used by:** prdDiscoveryAgent, flowDesignerAgent, frontendUIAgent, backendAgent

**Naming Convention:**
- PascalCase for feature names: `Diet_Generator`, `Weight_Plateau_Support`
- Folder pattern: `doc_[Feature_Name]`

**File Naming:**
- `[Feature_Name]_PRD.md` - Product Requirements Document
- `[Feature_Name]_Flow_Diagram.md` - Mermaid flow diagram
- `[Feature_Name]_Documentation.md` - Flow documentation
- `[Feature_Name]_UI_Specifications.md` - UI specifications
- `[Feature_Name]_Figma_Make_Prompt.json` - Figma Make prompt
- `[Feature_Name]_API_Contracts.md` - API contracts
- `[Feature_Name]_Database_Schema.sql` - Database schema
- `[Feature_Name]_Backend_Logic.md` - Backend logic documentation

### features/ (OneDrive Synced - Not Version Controlled)

**Purpose:** Finalized feature documentation and user research outputs.

**Path:** `features/`

**Status:** Gitignored. Must be set up as OneDrive symlink on each machine (see Setup section below).

**Used for:**
- Finalized feature docs (moved from AI_Output/ after review)
- User research outputs

### context_knowledge/ (Private - Gitignored)

**Purpose:** Private knowledge base that all agents read from.

**Path:** `context_knowledge/`

**Contains:**
- `opportunity_tree.json` - Hierarchical opportunity framework
- `*_interview_summary.json` - User interview evidence mapped to opportunities
- `Balance_App_Flow.md` - Complete user journey flowchart (Mermaid)
- `Benchmark_Balance.json` - Competitive landscape analysis
- `Notifications_Touchpoints.json` - Notification/touchpoint strategy
- `Vision_Balance.md` - Product vision and positioning
- `User_persona.md` - Primary user persona

**Setup:** Use `/init-context` to create all files interactively. Use `/update-*` commands to modify specific files.

### Transcriptions/ (Google Drive Symlinks - Gitignored)

**Purpose:** Access to raw transcript files via Google Drive symlinks.

**Path:** `Transcriptions/`

**Status:** Gitignored. Must be set up with Google Drive symlinks on each machine (see Setup section below).

**Structure:**
- `transcription_source/` - Symlink to Google Drive user interview transcripts
- `1st_consultation_source/` - Symlink to Google Drive first consultation transcripts

---

## Standard File Storage Protocol for Agents

All agents generating feature documentation must follow this protocol:

### Step 1: Determine Feature Name

Use PascalCase format. Examples: `Diet_Generator`, `Weight_Plateau_Support`

If unclear, ask the user: "What would you like to name this feature folder?"

### Step 2: Check/Create Feature Folder

```bash
mkdir -p AI_Output/doc_[Feature_Name]
```

### Step 3: Save Files

```bash
# Path pattern (relative to repo root):
# AI_Output/doc_[Feature_Name]/[Feature_Name]_[FileType].md
```

### Step 4: Confirm Completion

Inform user where files were saved with paths relative to repo root.

## Agent Output Mapping

| Agent | Outputs | File Names |
|-------|---------|------------|
| prdDiscoveryAgent | PRD | `[Feature_Name]_PRD.md` |
| flowDesignerAgent | Flow diagram, Documentation | `[Feature_Name]_Flow_Diagram.md`, `[Feature_Name]_Documentation.md` |
| frontendUIAgent | UI specs, Figma prompt | `[Feature_Name]_UI_Specifications.md`, `[Feature_Name]_Figma_Make_Prompt.json` |
| backendAgent | API contracts, DB schema, Backend logic | `[Feature_Name]_API_Contracts.md`, `[Feature_Name]_Database_Schema.sql`, `[Feature_Name]_Backend_Logic.md` |
| er-diagram-generator | ER diagrams | Generated from flow specs |

## Command Output Mapping

| Command | Output Destination | Description |
|---------|-------------------|-------------|
| /transcripts | `features/doc_User_Research/outputs/` | Transcription pipeline outputs |
| /init-context | `context_knowledge/` | Bootstrap all context files |
| /update-* | `context_knowledge/` | Update individual context files |

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

---

## AI_Output Workflow

1. **Agents generate** docs in `AI_Output/doc_[Feature_Name]/`
2. **Review and edit** generated documents
3. **Commit to git** for version history
4. **Move to `features/`** when finalized (OneDrive sync)

---

## Important Notes for All Agents

1. **Always check claude.md** for current file storage conventions
2. **Use relative paths** from the repo root - never hardcode absolute paths
3. **Use consistent naming** - PascalCase for feature names, underscore separators
4. **Create folders if needed** - Use `mkdir -p` to ensure parent directories exist
5. **Confirm to user** - Always inform where files were saved
6. **Ask if unclear** - If feature name is ambiguous, ask the user

---

# New Device Setup

After cloning this repository, several folders need to be created because they are gitignored.

## Step 1: Set Up context_knowledge/

```bash
mkdir -p context_knowledge
# Then run /init-context in Claude Code to populate files
```

## Step 2: Set Up features/ (OneDrive Symlink)

```bash
# Create OneDrive folder (first time only)
mkdir -p ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features

# Create symlink from repo root
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features
```

## Step 3: Set Up Transcriptions/ (Google Drive Symlinks)

```bash
mkdir -p Transcriptions

# Link to user interview transcripts (adjust email for your account)
ln -s ~/Library/CloudStorage/GoogleDrive-<your-email>/Mi\ unidad/Meet\ Recordings/Trans_MD Transcriptions/transcription_source

# Link to first consultation transcripts
ln -s ~/Library/CloudStorage/GoogleDrive-<your-email>/Mi\ unidad/Meet\ Recordings/1st_DoctorTranscript Transcriptions/1st_consultation_source
```

## Step 4: Set Up User_discovery/.env

```bash
echo 'OPENAI_API_KEY=your-key-here' > User_discovery/.env
```

## Step 5: Verify Setup

```bash
ls context_knowledge/     # Should have files after /init-context
ls features/              # Should show OneDrive contents
ls Transcriptions/        # Should show symlinks
```

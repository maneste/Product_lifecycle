# Claude Code Documentation Setup

This guide explains how to replicate the documentation folder setup across any device synced with this GitHub repository.

## Current Setup Overview

This repository uses a hybrid storage model for different types of content:

- **`context_knowledge/`** - Private knowledge base (gitignored, locally accessible)
- **`AI_Output/`** - Agent-generated docs staging area (version controlled in GitHub)
- **`features/`** - Finalized feature docs and research data (gitignored, synced to OneDrive)
- **`Transcriptions/`** - User research transcripts (gitignored, symlinked to Google Drive)
- **`feature-template/`** - Code and implementation templates (version controlled)
- **`.claude/agents/`** - Custom agent configurations (version controlled)

This setup keeps sensitive/large files out of version control while maintaining accessibility for Claude Code and providing version control for agent-generated documents.

## Repository Structure

```
Feature_Building/
├── .claude/
│   ├── agents/
│   │   ├── prdDiscoveryAgent.md      # PRD generation agent
│   │   ├── flowDesignerAgent.md      # Flow design agent
│   │   ├── frontendUIAgent.md        # Frontend UI specs agent
│   │   └── backendAgent.md           # Backend specs agent
│   └── commands/
│       ├── init-context.md               # /init-context - Bootstrap all context_knowledge files
│       ├── update-vision.md              # /update-vision - Update product vision
│       ├── update-persona.md             # /update-persona - Update user persona
│       ├── update-app-flow.md            # /update-app-flow - Update app flow diagram
│       ├── update-opportunity-tree.md    # /update-opportunity-tree - Update opportunity tree
│       ├── update-interview-summary.md   # /update-interview-summary - Update interview evidence
│       ├── update-benchmark.md           # /update-benchmark - Update competitive benchmarks
│       ├── update-notifications.md       # /update-notifications - Update touchpoints
│       └── transcripts.md               # /transcripts - Run transcription pipelines
├── context_knowledge/                 # Private knowledge base (gitignored)
│   ├── Balance_App_Flow.md
│   ├── Benchmark_Balance.json
│   ├── Notifications_Touchpoints.json
│   ├── *_interview_summary.json
│   ├── User_persona.md
│   ├── Vision_Balance.md
│   └── opportunity_tree.json
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
├── features/                          # Finalized docs & research data (gitignored, OneDrive synced)
│   ├── doc_[Feature_Name]/            # Feature documentation folders (moved from AI_Output)
│   │   ├── [Feature_Name]_PRD.md
│   │   ├── [Feature_Name]_Flow_Diagram.md
│   │   └── [Feature_Name]_Documentation.md
│   └── doc_User_Research/             # User research feature
│       └── outputs/                   # User research outputs
│           ├── interview_summary_*.json
│           ├── interview_report_*.md
│           └── v*_latitude_output_*.csv
├── Transcriptions/                    # Raw transcript files (gitignored, Google Drive symlinks)
│   ├── transcription_source/          # Symlink to Google Drive Trans_MD folder
│   └── 1st_consultation_source/       # Symlink to Google Drive 1st_DoctorTranscript folder
├── feature-template/                  # Code templates (version controlled)
├── user_research/                     # User research tools and scripts (version controlled)
│   ├── process_interviews.py         # Main interview processing script
│   ├── process_new_transcripts.py    # Transcript processing via Latitude API
│   ├── run_pipeline.py               # Pipeline orchestrator
│   ├── summarize_interviews.py       # Interview summarization
│   ├── process_new_interviews.sh     # Shell script wrapper
│   ├── README.md
│   ├── COMMANDS.md
│   ├── PIPELINE_USAGE.md
│   ├── TRANSCRIPT_PROCESSING.md
│   └── prompts/
│       ├── CHANGELOG.md
│       └── versions/
│           ├── v1.0/Opportunity_tree.md
│           ├── v1.1/Opportunity_tree.md
│           ├── v1.2/Opportunity_tree.md
│           └── v1.3/Opportunity_tree.md
├── .gitignore
└── claude.md                          # This file
```

---

# File Storage Conventions (Single Source of Truth)

This section defines where all agents and commands should store their outputs. **All agents must reference this section** instead of duplicating file path logic.

## Directory Structure for Outputs

### AI_Output/ (Version Controlled - GitHub)

**Purpose:** Staging area for all agent-generated feature documentation with full version control.

**Path:** `/Users/manu/Documents/GitHub/Feature_Building/AI_Output/`

**Folder Pattern:** `AI_Output/doc_[Feature_Name]/`

**Used by:**
- prdDiscoveryAgent
- flowDesignerAgent
- frontendUIAgent
- backendAgent

**Naming Convention:**
- Use PascalCase for feature names (e.g., `Diet_Generator`, `Weight_Plateau_Support`)
- Folder pattern: `doc_[Feature_Name]`
- Example: `doc_Diet_Generator`, `doc_Pre_Consultation_Engagement_Report`

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

**Path:** `/Users/manu/Documents/GitHub/Feature_Building/features/`

**Used for:**
- Finalized feature docs (moved from AI_Output/)
- User research outputs (direct output, no AI_Output staging)

**User Research Structure:**
- Path: `features/doc_User_Research/outputs/`
- Files:
  - `consolidated_user_interviews.csv`
  - `consolidated_first_consultation_interviews.csv`
  - `v[version]_latitude_output_[date].csv`
  - `interview_summary_v[version].json`
  - `interview_report_v[version]_[timestamp].md`

### context_knowledge/ (Private - Gitignored)

**Purpose:** Private knowledge base for agents to read from.

**Path:** `/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/`

**Contains:**
- `opportunity_tree.json` - Hierarchical opportunity framework
- `*_interview_summary.json` - User interview evidence mapped to opportunities
- `Balance_App_Flow.md` - Complete user journey flowchart (Mermaid)
- `Benchmark_Balance.json` - Competitive landscape analysis
- `Notifications_Touchpoints.json` - Notification/touchpoint strategy
- `Vision_Balance.md` - Product vision and positioning
- `User_persona.md` - Primary user persona

**Setup:** Use `/init-context` to create all files interactively. Use individual `/update-*` commands to modify specific files.

### Transcriptions/ (Google Drive Symlinks - Gitignored)

**Purpose:** Access to raw transcript files via Google Drive symlinks.

**Path:** `/Users/manu/Documents/GitHub/Feature_Building/Transcriptions/`

**Structure:**
- `transcription_source/` - Symlink to Google Drive user interview transcripts
- `1st_consultation_source/` - Symlink to Google Drive first consultation transcripts

## Standard File Storage Protocol for Agents

All agents generating feature documentation must follow this protocol:

### Step 1: Determine Feature Name

```bash
# Extract or infer feature name from user request or document title
# Use PascalCase format
# Examples: "Diet_Generator", "Weight_Plateau_Support", "Pre_Consultation_Engagement_Report"
```

If unclear, ask the user: "What would you like to name this feature folder?"

### Step 2: Check/Create Feature Folder

```bash
# Check if folder exists
ls -d AI_Output/doc_[Feature_Name] 2>/dev/null

# If folder doesn't exist, create it
mkdir -p AI_Output/doc_[Feature_Name]

# If folder already exists (e.g., contains PRD), confirm you'll add files to it
```

### Step 3: Save File(s)

```bash
# Use the Write tool to create files following naming conventions
# Full path pattern: /Users/manu/Documents/GitHub/Feature_Building/AI_Output/doc_[Feature_Name]/[Feature_Name]_[FileType].md

# Examples:
# /Users/manu/Documents/GitHub/Feature_Building/AI_Output/doc_Diet_Generator/Diet_Generator_PRD.md
# /Users/manu/Documents/GitHub/Feature_Building/AI_Output/doc_Diet_Generator/Diet_Generator_Flow_Diagram.md
```

### Step 4: Confirm Completion

```bash
# Inform user where files were saved
# Provide full file paths for reference
```

## Agent Output Mapping

| Agent | Outputs | File Names |
|-------|---------|------------|
| prdDiscoveryAgent | PRD | `[Feature_Name]_PRD.md` |
| flowDesignerAgent | Flow diagram, Documentation | `[Feature_Name]_Flow_Diagram.md`, `[Feature_Name]_Documentation.md` |
| frontendUIAgent | UI specs, Figma prompt | `[Feature_Name]_UI_Specifications.md`, `[Feature_Name]_Figma_Make_Prompt.json` |
| backendAgent | API contracts, DB schema, Backend logic | `[Feature_Name]_API_Contracts.md`, `[Feature_Name]_Database_Schema.sql`, `[Feature_Name]_Backend_Logic.md` |

## Command Output Mapping

| Command | Output Destination | File Pattern |
|---------|-------------------|--------------|
| /transcripts | `features/doc_User_Research/outputs/` | `v[version]_latitude_output_[date].csv`, `interview_summary_v[version].json`, `interview_report_v[version]_[timestamp].md`, `consolidated_first_consultation_interviews.csv` |

## Context Knowledge Commands

These commands manage the `context_knowledge/` folder - the private knowledge base that all agents read from.

### /init-context - First-Time Setup

**Purpose:** Bootstrap a new repo by creating ALL context_knowledge files from scratch.

**When to use:** After cloning the repository for the first time, or when setting up a new product context.

**What it does:**
1. Checks which files already exist in `context_knowledge/`
2. Guides the user through creating each file interactively (one at a time)
3. Validates JSON files and cross-references between files
4. Provides a completion summary

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

**Usage:** Run `/init-context` in Claude Code.

### Individual Update Commands

Each context file has a dedicated update command:

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

## Example: Complete Feature Documentation Flow

For a feature called "Diet_Generator":

```bash
# Step 1: prdDiscoveryAgent generates PRD
AI_Output/doc_Diet_Generator/Diet_Generator_PRD.md

# Step 2: flowDesignerAgent generates flows
AI_Output/doc_Diet_Generator/Diet_Generator_Flow_Diagram.md
AI_Output/doc_Diet_Generator/Diet_Generator_Documentation.md

# Step 3: frontendUIAgent generates UI specs
AI_Output/doc_Diet_Generator/Diet_Generator_UI_Specifications.md
AI_Output/doc_Diet_Generator/Diet_Generator_Figma_Make_Prompt.json

# Step 4: backendAgent generates backend specs
AI_Output/doc_Diet_Generator/Diet_Generator_API_Contracts.md
AI_Output/doc_Diet_Generator/Diet_Generator_Database_Schema.sql
AI_Output/doc_Diet_Generator/Diet_Generator_Backend_Logic.md

# Step 5: Review and commit to git
git add AI_Output/doc_Diet_Generator/
git commit -m "Add Diet Generator complete feature documentation"
git push

# Step 6: When ready, move to features/
mv AI_Output/doc_Diet_Generator/ features/
```

## Important Notes for All Agents

1. **Always check CLAUDE.md** for current file storage conventions
2. **Never hardcode paths** - use the base paths defined here
3. **Use consistent naming** - PascalCase for feature names, underscore separators
4. **Create folders if needed** - Use `mkdir -p` to ensure parent directories exist
5. **Confirm to user** - Always inform where files were saved with full paths
6. **Ask if unclear** - If feature name is ambiguous, ask the user

## Path Updates

If paths need to change in the future, update this section only. All agents reference this section as the single source of truth.

**Current base path:** `/Users/manu/Documents/GitHub/Feature_Building/`

**To update for a different machine:**
1. Update the base path in this section
2. All agents will automatically use the new path when they reference CLAUDE.md

---

## Step 1: Clone the Repository

On any new device, start by cloning the repository:

```bash
git clone <your-repo-url>
cd Feature_Building
```

## Step 2: Create the Context Knowledge Folder

Since `context_knowledge/` is gitignored, you need to recreate it manually:

```bash
mkdir context_knowledge
```

## Step 3: Populate Context Knowledge Files

You have three options for populating the context_knowledge folder:

### Option A: Manual Sync (Cloud Storage)
Store your context_knowledge folder in a cloud service (Dropbox, Google Drive, iCloud, etc.) and copy it into each cloned repository:

```bash
# Example with Dropbox
cp -r ~/Dropbox/Feature_Building_Docs/* context_knowledge/
```

### Option B: Private Git Repository
Create a separate private repository for context_knowledge and clone it into the folder:

```bash
# One-time setup on first device
cd context_knowledge
git init
git remote add origin <private-docs-repo-url>
git add .
git commit -m "Initial context_knowledge"
git push -u origin main

# On new devices
cd Feature_Building
git clone <private-docs-repo-url> context_knowledge
```

### Option C: Encrypted Archive
Keep an encrypted archive of the context_knowledge folder in the repository:

```bash
# Create encrypted archive (on source device)
tar czf - context_knowledge | openssl enc -aes-256-cbc -pbkdf2 -out context_knowledge.tar.gz.enc

# Add to git (one time)
git add context_knowledge.tar.gz.enc
git commit -m "Add encrypted context_knowledge archive"
git push

# Extract on new device
openssl enc -d -aes-256-cbc -pbkdf2 -in context_knowledge.tar.gz.enc | tar xzf -
```

## Step 4: Verify Context Knowledge Structure

Ensure your context_knowledge folder contains the expected files:

```bash
ls -la context_knowledge/
```

Expected files:
- `Balance_App_Flow.md` - Application flow documentation
- `Benchmark_Balance.json` - Competitive benchmarking data
- `20251012_interview_summary.json` - User interview data
- `User_persona.md` - User persona definitions
- `Vision_Balance.md` - Product vision document
- `WA_Users.md` - User analysis
- `opportunity_tree.json` - Opportunity tree structure

## Step 5: Configure Claude Code Knowledge Base

Claude Code automatically detects the `context_knowledge/` folder. To verify it's working:

1. Open Claude Code in this directory
2. The context_knowledge folder should be indexed as a private knowledge base
3. Test by asking Claude about content in your context_knowledge files

## Step 6: Verify .gitignore Configuration

Ensure the context_knowledge folder stays private:

```bash
git status
```

The `context_knowledge/` folder should NOT appear in untracked files. Verify `.gitignore` contains:

```
# Context Knowledge (private knowledge base)
context_knowledge/
```

## Maintenance

### Keeping Context Knowledge in Sync

If using Option B (private git repo):

```bash
cd context_knowledge
git pull  # Get latest changes
# Make updates
git add .
git commit -m "Update context_knowledge"
git push
```

If using Option A (cloud storage):

```bash
# Periodically sync changes
rsync -av context_knowledge/ ~/Dropbox/Feature_Building_Docs/
```

### Adding New Context Knowledge Files

Add new files to the context_knowledge folder and sync using your chosen method:

```bash
# Create new file
echo "# New Document" > context_knowledge/new_file.md

# Sync according to your chosen method (A, B, or C)
```

## Troubleshooting

### Context Knowledge Not Detected by Claude

1. Check folder exists: `ls -la context_knowledge/`
2. Check file permissions: `chmod -R 755 context_knowledge/`
3. Restart Claude Code

### Context Knowledge Accidentally Committed to Git

If context_knowledge files appear in git:

```bash
# Remove from git but keep locally
git rm -r --cached context_knowledge/
git commit -m "Remove context_knowledge from version control"
git push

# Verify .gitignore includes context_knowledge/
```

### Sync Conflicts

If using Option B and encountering conflicts:

```bash
cd context_knowledge
git fetch
git status
# Resolve conflicts manually
git add .
git commit -m "Resolve sync conflicts"
git push
```

## Security Considerations

- Context Knowledge folder contains private/sensitive information
- Never commit context_knowledge to public repositories
- Use encryption (Option C) for maximum security
- Regularly backup context_knowledge folder
- Review .gitignore before each commit to prevent accidental exposure

## Recommended Workflow

1. **New repo setup**: Run `/init-context` to create all context_knowledge files interactively
2. **Daily**: Start work session, sync context_knowledge (pull/copy latest)
3. **During work**: Use `/update-*` commands to modify specific context files
4. **End of day**: Sync context_knowledge (push/copy changes)
5. **New device**: Follow setup steps 1-4, then run `/init-context` or sync existing files
6. **Monthly**: Verify context_knowledge backups exist

## File Naming Conventions

Follow these conventions when adding new context_knowledge:

- Use PascalCase for markdown files: `NewFeature_Analysis.md`
- Use snake_case for JSON files: `user_research_data.json`
- Use descriptive names that indicate content purpose
- Group related files with common prefixes: `Balance_*`, `User_*`

---

# Features Folder Setup (OneDrive Sync)

## Overview

The `features/` folder stores agent-generated outputs (PRDs, flows, documentation) that are too large for version control but need to be synced across devices and accessible to Claude Code.

**Key differences from `context_knowledge/`:**

| Folder | Purpose | Content Type | Sync Method |
|--------|---------|--------------|-------------|
| `context_knowledge/` | Research & knowledge base | User interviews, benchmarks, vision | Local or private git |
| `features/` | Agent outputs | PRDs, flows, feature docs | OneDrive symlink |
| `feature-template/` | Code templates | Implementation prompts, code | Version controlled (git) |

## Setup Instructions

### Step 1: Create OneDrive Folder

On your main device, create a dedicated folder in OneDrive:

```bash
# Using OneDrive desktop app (recommended)
# Create folder: "Claude_Balance_Features"
mkdir -p ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features
```

### Step 2: Create Symlink in Repository

Link the OneDrive folder to your repository:

```bash
cd Feature_Building

# Create symlink to OneDrive folder
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features

# Verify symlink
ls -la features/
```

### Step 3: Verify .gitignore

Ensure the features folder is excluded from version control:

```bash
git status
```

The `features/` folder should NOT appear in untracked files. The `.gitignore` file should contain:

```
# Private knowledge base and feature documentation
context_knowledge/
features/
```

### Step 4: Test Agent Output

Ask Claude to create a PRD or flow. The agents will automatically:
1. Create `features/doc_[Feature_Name]/` folder
2. Save outputs there (PRD, flow diagram, documentation)
3. Files sync to OneDrive automatically

Example:
```
features/
└── doc_Diet_Generator/
    ├── Diet_Generator_PRD.md
    ├── Diet_Generator_Flow_Diagram.md
    └── Diet_Generator_Documentation.md
```

## Setting Up on New Devices

When cloning the repository on a new device:

```bash
# 1. Clone repository
git clone <your-repo-url>
cd Feature_Building

# 2. Ensure OneDrive desktop app is installed and synced

# 3. Create symlink to OneDrive folder
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features

# 4. Verify access
ls features/
```

## Agent Behavior

Both `prdDiscoveryAgent` and `flowDesignerAgent` are configured to:

1. **Automatically create feature folders** with naming pattern: `features/doc_[Feature_Name]/`
2. **Save all outputs** to the feature-specific folder
3. **Use PascalCase** for feature names (e.g., `doc_Pre_Consultation_Engagement_Report`)

Example workflow:
```
User: "Create a PRD for weight plateau support"
Agent: Creates features/doc_Weight_Plateau_Support/
       Saves: Weight_Plateau_Support_PRD.md
```

## When to Use features/ vs feature-template/

**Use `features/` (OneDrive synced) for:**
- PRDs (Product Requirements Documents)
- Flow diagrams (Mermaid charts)
- Feature documentation and specifications
- Long-form research outputs from agents
- Files that are too large for git or change frequently

**Use `feature-template/` (version controlled) for:**
- Code implementation templates
- Specific prompts for building features
- Reusable components and snippets
- Files that should be tracked in git history

## Troubleshooting

### Symlink Broken

If `ls features/` shows "No such file or directory":

```bash
# Remove broken symlink
rm features

# Recreate symlink to correct OneDrive path
ln -s ~/Library/CloudStorage/OneDrive-Personal/Claude_Balance_Features features
```

### OneDrive Not Syncing

1. Check OneDrive desktop app is running
2. Verify folder exists in OneDrive web interface
3. Check sync status in OneDrive menu bar icon

### Features Accidentally Committed to Git

If features folder appears in git:

```bash
# Remove from git but keep locally
git rm -r --cached features/
git commit -m "Remove features from version control"
git push

# Verify .gitignore includes features/
cat .gitignore | grep features
```

## Maintenance

### Syncing Across Devices

OneDrive handles syncing automatically. To manually verify:

```bash
# Check sync status
ls -la features/

# All files should show recent modification dates if synced
```

### Backup Strategy

Since features/ is in OneDrive:
- Files are automatically backed up to Microsoft's cloud
- Access version history via OneDrive web interface
- Consider periodic exports for critical PRDs

### Cleaning Up Old Features

Periodically review and archive completed features:

```bash
# Move completed features to archive subfolder
mkdir -p features/archive
mv features/doc_Old_Feature features/archive/
```

## Additional Resources

- Claude Code Documentation: https://docs.claude.com/claude-code
- Custom Agents: See `.claude/agents/prdDiscovery.md` for example
- Feature Template: See `feature-template/` for structured feature development

## Questions?

If you encounter issues or need to modify this setup, refer to:
- Claude Code docs for knowledge base configuration
- This repository's commit history for setup evolution
- Your chosen sync method's documentation

---

# AI_Output Folder Workflow (Version Controlled Staging)

## Overview

The `AI_Output/` folder serves as a version-controlled staging area for all agent-generated feature documentation. This folder provides full git history tracking before documents are moved to the OneDrive-synced `features/` folder.

**Key characteristics:**

| Folder | Purpose | Version Control | Sync Method | Workflow Stage |
|--------|---------|-----------------|-------------|----------------|
| `AI_Output/` | Agent outputs staging | Yes (GitHub) | Git | Initial generation |
| `features/` | Finalized feature docs | No (gitignored) | OneDrive | After review/approval |

## Why Use AI_Output?

1. **Version Control**: Track every change made by agents with full git history
2. **Review Before Sync**: Examine and modify documents before syncing to OneDrive
3. **Collaboration**: Share agent outputs via git pull requests
4. **Rollback**: Revert to previous versions if needed
5. **Documentation**: Keep a record of how features evolved

## Workflow

### Step 1: Agents Generate Documents in AI_Output

All custom agents automatically output to `AI_Output/`:

```bash
# When you ask an agent to create a PRD:
AI_Output/doc_[Feature_Name]/[Feature_Name]_PRD.md

# When you ask for flows:
AI_Output/doc_[Feature_Name]/[Feature_Name]_Flow_Diagram.md
AI_Output/doc_[Feature_Name]/[Feature_Name]_Documentation.md

# When you ask for UI specs:
AI_Output/doc_[Feature_Name]/[Feature_Name]_UI_Specifications.md
AI_Output/doc_[Feature_Name]/[Feature_Name]_Figma_Make_Prompt.json

# When you ask for backend specs:
AI_Output/doc_[Feature_Name]/[Feature_Name]_API_Contracts.md
AI_Output/doc_[Feature_Name]/[Feature_Name]_Database_Schema.sql
AI_Output/doc_[Feature_Name]/[Feature_Name]_Backend_Logic.md
```

### Step 2: Review and Modify

After agents generate documents, you can:

```bash
# View the generated files
ls -la AI_Output/doc_[Feature_Name]/

# Edit files if needed
# Use Claude Code or your preferred editor to make changes

# Check git status to see what changed
git status

# View specific changes
git diff AI_Output/doc_[Feature_Name]/
```

### Step 3: Commit to Git (Version Control)

Once you're satisfied with the documents:

```bash
# Stage the new feature folder
git add AI_Output/doc_[Feature_Name]/

# Commit with descriptive message
git commit -m "Add [Feature_Name] PRD and flow diagrams"

# Push to GitHub
git push
```

### Step 4: Move to Features Folder (When Ready)

When the feature documentation is approved and ready for broader access:

```bash
# Move the entire feature folder to features/
mv AI_Output/doc_[Feature_Name]/ features/

# Or copy if you want to keep the AI_Output version
cp -r AI_Output/doc_[Feature_Name]/ features/

# The features/ folder will sync to OneDrive automatically
```

### Step 5: Clean Up AI_Output (Optional)

After moving to features/, you can remove from AI_Output:

```bash
# Remove the feature folder from AI_Output
rm -rf AI_Output/doc_[Feature_Name]/

# Commit the removal
git add AI_Output/
git commit -m "Moved [Feature_Name] to features folder"
git push
```

## Agent Configuration

All agents are configured to output to `AI_Output/`:

- **prdDiscoveryAgent** → `AI_Output/doc_[Feature_Name]/[Feature_Name]_PRD.md`
- **flowDesignerAgent** → `AI_Output/doc_[Feature_Name]/[Feature_Name]_Flow_Diagram.md` + Documentation
- **frontendUIAgent** → `AI_Output/doc_[Feature_Name]/[Feature_Name]_UI_Specifications.md` + Figma prompt
- **backendAgent** → `AI_Output/doc_[Feature_Name]/[Feature_Name]_API_Contracts.md` + Database schema + Backend logic

You don't need to specify the output path - agents handle this automatically.

## Example Complete Workflow

```bash
# 1. Ask agent to create a PRD for "Weight_Plateau_Support"
# Agent creates: AI_Output/doc_Weight_Plateau_Support/Weight_Plateau_Support_PRD.md

# 2. Review the generated PRD
cat AI_Output/doc_Weight_Plateau_Support/Weight_Plateau_Support_PRD.md

# 3. Make any edits if needed
# (edit the file)

# 4. Check what changed
git status
git diff AI_Output/doc_Weight_Plateau_Support/

# 5. Commit to version control
git add AI_Output/doc_Weight_Plateau_Support/
git commit -m "Add Weight Plateau Support PRD"
git push

# 6. Ask agent to create flow diagrams
# Agent creates flow files in same folder

# 7. Commit the flows
git add AI_Output/doc_Weight_Plateau_Support/
git commit -m "Add Weight Plateau Support flow diagrams"
git push

# 8. When ready for broader access, move to features/
mv AI_Output/doc_Weight_Plateau_Support/ features/

# 9. Clean up
git add AI_Output/ features/
git commit -m "Moved Weight Plateau Support to features folder"
git push
```

## Folder Structure in AI_Output

Each feature gets its own folder following this pattern:

```
AI_Output/
├── doc_Feature_Name_1/
│   ├── Feature_Name_1_PRD.md
│   ├── Feature_Name_1_Flow_Diagram.md
│   ├── Feature_Name_1_Documentation.md
│   ├── Feature_Name_1_UI_Specifications.md
│   ├── Feature_Name_1_Figma_Make_Prompt.json
│   ├── Feature_Name_1_API_Contracts.md
│   ├── Feature_Name_1_Database_Schema.sql
│   └── Feature_Name_1_Backend_Logic.md
├── doc_Feature_Name_2/
│   ├── Feature_Name_2_PRD.md
│   └── ...
└── doc_Feature_Name_3/
    └── ...
```

## Benefits Over Direct Features Output

**Before (direct to features/):**
- No version history
- Can't track changes over time
- Difficult to collaborate via git
- No ability to rollback

**Now (AI_Output → features/):**
- Full git history for all agent outputs
- Track how features evolved
- Collaborate via pull requests
- Rollback to any previous version
- Review before syncing to OneDrive

## When to Use AI_Output vs Features

**Use `AI_Output/` for:**
- Initial agent-generated documents
- Work in progress
- Documents that need review
- Tracking version history

**Use `features/` for:**
- Approved and finalized documents
- Documents ready for team access
- Documents that need OneDrive sync
- User research outputs (these skip AI_Output)

**Note:** User research outputs from `/process-UserResearch` and `/process-FirstConsultation` commands continue to go directly to `features/doc_User_Research/outputs/` since they're research data, not feature specifications.

## Git Best Practices

### Commit Messages

Use descriptive commit messages:

```bash
# Good
git commit -m "Add Diet Generator PRD with user evidence and success metrics"
git commit -m "Update Weight Plateau flow diagram with locked states"
git commit -m "Add UI specifications for MainEvents calendar view"

# Less helpful
git commit -m "Update PRD"
git commit -m "Add files"
```

### Branching Strategy (Optional)

For major features, consider using branches:

```bash
# Create feature branch
git checkout -b feature/diet-generator

# Work on the feature
# Agents output to AI_Output/doc_Diet_Generator/

# Commit your work
git add AI_Output/doc_Diet_Generator/
git commit -m "Add Diet Generator PRD and flows"

# Push to GitHub
git push -u origin feature/diet-generator

# Create pull request on GitHub for review
# After approval, merge to main
```

## Troubleshooting

### AI_Output Folder Not Showing in Git

If `AI_Output/` appears in `.gitignore`:

```bash
# Check .gitignore
cat .gitignore | grep AI_Output

# If it's there, remove that line
# Edit .gitignore and remove "AI_Output/"

# Verify AI_Output is now tracked
git status
```

### Agent Still Outputs to Features Folder

If an agent outputs to `features/` instead of `AI_Output/`:

```bash
# Check agent configuration
cat .claude/agents/[agent_name].md | grep -A 5 "File Storage Protocol"

# Ensure paths reference AI_Output/
# Update agent configuration if needed
```

### Merge Conflicts

If you get conflicts when pulling from GitHub:

```bash
# View conflicting files
git status

# Resolve conflicts manually
# Edit files to keep desired changes

# Mark as resolved
git add AI_Output/

# Complete the merge
git commit
git push
```

## Maintenance

### Periodic Cleanup

Clean up old feature folders that have been moved to features/:

```bash
# List all features in AI_Output
ls -la AI_Output/

# Remove features that are already in features/
rm -rf AI_Output/doc_Old_Feature/

# Commit the cleanup
git add AI_Output/
git commit -m "Clean up old feature folders from AI_Output"
git push
```

### Archive Completed Features

For long-term storage of completed features:

```bash
# Create archive folder
mkdir -p AI_Output/archive/

# Move completed features
mv AI_Output/doc_Completed_Feature/ AI_Output/archive/

# Commit
git add AI_Output/
git commit -m "Archive completed feature documentation"
git push
```

---

# Transcriptions Folder Setup (Google Drive Sync)

## Overview

The `Transcriptions/` folder provides access to raw transcript files stored in Google Drive. This folder uses symlinks to connect to Google Drive folders, keeping large transcript files out of version control while maintaining easy access for processing scripts.

**Key differences from other folders:**

| Folder | Purpose | Content Type | Sync Method |
|--------|---------|--------------|-------------|
| `context_knowledge/` | Research & knowledge base | User interviews, benchmarks, vision | Local or private git |
| `features/` | Agent outputs | PRDs, flows, feature docs | OneDrive symlink |
| `Transcriptions/` | Raw transcript files | Google Meet recordings, transcripts | Google Drive symlinks |

## Setup Instructions

### Step 1: Ensure Google Drive is Synced

Make sure Google Drive desktop app is installed and syncing:

```bash
# Check if Google Drive is mounted
ls ~/Library/CloudStorage/GoogleDrive-*/
```

### Step 2: Create Transcriptions Folder

In your repository, create the Transcriptions folder:

```bash
cd Feature_Building
mkdir Transcriptions
```

### Step 3: Create Symlinks to Google Drive

Link the Google Drive transcript folders to your repository:

```bash
cd Transcriptions

# Link to general transcriptions folder (Trans_MD)
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/Trans_MD transcription_source

# Link to first consultation transcripts folder
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/1st_DoctorTranscript 1st_consultation_source

# Verify symlinks
ls -la
```

### Step 4: Verify .gitignore

Ensure the Transcriptions folder is excluded from version control:

```bash
git status
```

The `Transcriptions/` folder should NOT appear in untracked files. The `.gitignore` file should contain:

```
# Private knowledge base and feature documentation
context_knowledge/
features/
Transcriptions/
```

### Step 5: Test Access

Verify you can access transcript files:

```bash
# List files in transcription source
ls Transcriptions/transcription_source/

# List files in first consultation source
ls Transcriptions/1st_consultation_source/
```

## Setting Up on New Devices

When cloning the repository on a new device:

```bash
# 1. Clone repository
git clone <your-repo-url>
cd Feature_Building

# 2. Ensure Google Drive desktop app is installed and synced
# Wait for sync to complete before proceeding

# 3. Create Transcriptions folder
mkdir Transcriptions

# 4. Create symlinks (adjust email if different)
cd Transcriptions
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/Trans_MD transcription_source
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/1st_DoctorTranscript 1st_consultation_source

# 5. Verify access
ls -la
ls transcription_source/
ls 1st_consultation_source/
```

## Usage with Processing Scripts

The `Transcriptions/` folder is used by scripts in `user_research/`:

```bash
# Process new transcripts from transcription_source
python user_research/process_new_transcripts.py

# Process first consultation interviews
# Scripts automatically read from Transcriptions/1st_consultation_source/
```

The scripts expect the following structure:
- `Transcriptions/transcription_source/` - General user research transcripts
- `Transcriptions/1st_consultation_source/` - First consultation doctor interviews

## When to Use Transcriptions/ vs features/

**Use `Transcriptions/` (Google Drive symlinks) for:**
- Raw transcript files from Google Meet recordings
- Original audio/video recordings
- Unprocessed interview data
- Files that live primarily in Google Drive
- Source material for processing pipelines

**Use `features/doc_User_Research/outputs/` (OneDrive synced) for:**
- Processed transcript outputs (CSV, JSON)
- Interview summaries and reports
- Analyzed data and insights
- Final deliverables from processing scripts

## Troubleshooting

### Symlink Broken

If `ls Transcriptions/transcription_source/` shows "No such file or directory":

```bash
# Remove broken symlink
rm Transcriptions/transcription_source

# Recreate symlink with correct Google Drive path
cd Transcriptions
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/Meet\ Recordings/Trans_MD transcription_source
```

### Google Drive Not Syncing

1. Check Google Drive desktop app is running
2. Verify folders exist in Google Drive web interface
3. Check sync status in Google Drive menu bar icon
4. Ensure sufficient disk space for sync

### Different Google Account

If using a different Google account, adjust the path:

```bash
# List available Google Drive accounts
ls ~/Library/CloudStorage/ | grep GoogleDrive

# Use the correct path for your account
ln -s ~/Library/CloudStorage/GoogleDrive-YOUR_EMAIL/Mi\ unidad/Meet\ Recordings/Trans_MD transcription_source
```

### Transcriptions Accidentally Committed to Git

If Transcriptions folder appears in git:

```bash
# Remove from git but keep locally
git rm -r --cached Transcriptions/
git commit -m "Remove Transcriptions from version control"
git push

# Verify .gitignore includes Transcriptions/
cat .gitignore | grep Transcriptions
```

## Maintenance

### Adding New Transcript Sources

To add additional Google Drive folders:

```bash
cd Transcriptions

# Create new symlink for additional source
ln -s ~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi\ unidad/NEW_FOLDER_PATH new_source_name

# Verify
ls -la
```

### Verifying Sync Status

Google Drive handles syncing automatically. To check:

```bash
# Check if files are accessible
ls -la Transcriptions/transcription_source/

# Recent modification dates indicate successful sync
```

### Storage Considerations

Since transcripts are stored in Google Drive:
- Files don't consume local repository space
- Google Drive manages storage and backups
- Access requires active internet connection (unless files are available offline)
- Consider marking important folders for offline access in Google Drive settings

## Security Considerations

- Transcriptions contain sensitive user interview data
- Never commit transcript files to version control
- Symlinks point to Google Drive, which has its own access controls
- Ensure Google Drive sharing settings are appropriate for your team
- Review .gitignore before commits to prevent accidental exposure

## Integration with Processing Pipeline

The processing pipeline in `user_research/` automatically uses these folders:

```bash
# Process new transcripts
# Reads from: Transcriptions/transcription_source/
# Outputs to: features/doc_User_Research/outputs/

# Process first consultations
# Reads from: Transcriptions/1st_consultation_source/
# Outputs to: features/doc_User_Research/outputs/
```

See `user_research/README.md` for more details on processing workflows.

---
name: repo-structure
description: File storage conventions, naming protocols, and agent output mappings for the Product_lifecycle repo. Use when saving agent outputs, creating feature folders, determining file names, or setting up a new device.
---

# File Storage Conventions

## AI_Output/ (Version Controlled - GitHub)

Staging area for all agent-generated feature documentation.

- **Folder pattern:** `AI_Output/doc_[Feature_Name]/`
- **Naming:** PascalCase with underscores: `Diet_Generator`, `Weight_Plateau_Support`
- **Used by:** prdDiscoveryAgent, flowDesignerAgent, frontendUIAgent, backendAgent

**File naming per feature folder:**
- `[Feature_Name]_PRD.md` - Product Requirements Document
- `[Feature_Name]_Flow_Diagram.md` - Mermaid flow diagram
- `[Feature_Name]_Documentation.md` - Flow documentation
- `[Feature_Name]_UI_Specifications.md` - UI specifications
- `[Feature_Name]_Figma_Make_Prompt.json` - Figma Make prompt
- `[Feature_Name]_API_Contracts.md` - API contracts
- `[Feature_Name]_Database_Schema.sql` - Database schema
- `[Feature_Name]_Backend_Logic.md` - Backend logic documentation

## features/ (OneDrive Synced - Not Version Controlled)

Finalized feature documentation moved from AI_Output/ after review.

## context_knowledge/ (Private - Gitignored)

Private knowledge base all agents read from. Use `/init-context` to create, `/update-*` commands to modify.

## Transcriptions/ (Google Drive Symlinks - Gitignored)

Raw transcript files via Google Drive symlinks: `transcription_source/` and `1st_consultation_source/`.

---

## Standard File Storage Protocol

All agents generating feature documentation follow this protocol:

1. **Determine Feature Name** - PascalCase format. If unclear, ask: "What would you like to name this feature folder?"
2. **Create Feature Folder** - `mkdir -p AI_Output/doc_[Feature_Name]`
3. **Save Files** - Path pattern: `AI_Output/doc_[Feature_Name]/[Feature_Name]_[FileType].md`
4. **Confirm** - Inform user where files were saved with relative paths.

## Agent Output Mapping

| Agent | File Names |
|-------|------------|
| prdDiscoveryAgent | `[Feature_Name]_PRD.md` |
| flowDesignerAgent | `[Feature_Name]_Flow_Diagram.md`, `[Feature_Name]_Documentation.md` |
| frontendUIAgent | `[Feature_Name]_UI_Specifications.md`, `[Feature_Name]_Figma_Make_Prompt.json` |
| backendAgent | `[Feature_Name]_API_Contracts.md`, `[Feature_Name]_Database_Schema.sql`, `[Feature_Name]_Backend_Logic.md` |
| er-diagram-generator | Generated from flow specs |

## Command Output Mapping

| Command | Output Destination |
|---------|-------------------|
| /transcripts | `features/doc_User_Research/outputs/` |
| /init-context | `context_knowledge/` |
| /update-* | `context_knowledge/` |

## AI_Output Workflow

1. Agents generate docs in `AI_Output/doc_[Feature_Name]/`
2. Review and edit generated documents
3. Commit to git for version history
4. Move to `features/` when finalized (OneDrive sync)

## Rules

1. Use relative paths from repo root - never hardcode absolute paths
2. Use consistent naming - PascalCase for feature names, underscore separators
3. Create folders if needed - `mkdir -p` to ensure parent directories exist
4. Confirm to user - always inform where files were saved
5. Ask if unclear - if feature name is ambiguous, ask the user

## New Device Setup

See `references/device-setup.md` for full setup instructions after cloning.

# File Storage Conventions for Agents

**Single Source of Truth for all agent file storage logic**

This document defines where ALL agents should store their outputs. All agents must reference this file instead of duplicating file path logic.

---

## Directory Structure Overview

### agents_output/ (Version Controlled - GitHub)

**Purpose:** Staging area for all agent-generated feature documentation with full version control.

**Path:** `/Users/manu/Documents/GitHub/Feature_Building/agents_output/`

**Folder Pattern:** `agents_output/doc_[Feature_Name]/`

**Used by:**
- prdDiscoveryAgent
- flowDesignerAgent
- frontendUIAgent
- backendAgent

**Naming Convention:**
- Use PascalCase for feature names (e.g., `Diet_Generator`, `Weight_Plateau_Support`)
- Folder pattern: `doc_[Feature_Name]`
- Example: `doc_Diet_Generator`, `doc_Pre_Consultation_Engagement_Report`

---

## Standard File Storage Protocol for Agents

**ALL agents generating feature documentation MUST follow this protocol:**

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
ls -d agents_output/doc_[Feature_Name] 2>/dev/null

# If folder doesn't exist, create it
mkdir -p agents_output/doc_[Feature_Name]

# If folder already exists (e.g., contains PRD), confirm you'll add files to it
```

### Step 3: Save File(s)

```bash
# Use the Write tool to create files following naming conventions
# Full path pattern: /Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_[Feature_Name]/[Feature_Name]_[FileType].md

# Examples:
# /Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_PRD.md
# /Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_Flow_Diagram.md
```

### Step 4: Confirm Completion

```bash
# Inform user where files were saved
# Provide full file paths for reference
```

---

## Agent-Specific File Naming Conventions

### prdDiscoveryAgent

**Output file:** `[Feature_Name]_PRD.md`

**Location:** `agents_output/doc_[Feature_Name]/`

**Full path example:** `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_PRD.md`

**Workflow:**
1. Follow "Standard File Storage Protocol for Agents" above
2. Use the paths and naming patterns defined in this file
3. Confirm file location to user after saving

---

### flowDesignerAgent

**Output files:**
- `[Feature_Name]_Flow_Diagram.md` (flow diagram only)
- `[Feature_Name]_Documentation.md` (documentation)

**Location:** `agents_output/doc_[Feature_Name]/`

**Full path examples:**
- `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_Flow_Diagram.md`
- `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_Documentation.md`

**Workflow:**
1. Follow "Standard File Storage Protocol for Agents" above
2. Save BOTH files (diagram and documentation)
3. Confirm file locations to user after saving

---

### frontendUIAgent

**Output files:**
- `[Feature_Name]_UI_Specifications.md` (UI specs document)
- `[Feature_Name]_Figma_Make_Prompt.json` (Figma Make prompt)

**Location:** `agents_output/doc_[Feature_Name]/`

**Full path examples:**
- `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_UI_Specifications.md`
- `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_Figma_Make_Prompt.json`

**Workflow:**
1. Follow "Standard File Storage Protocol for Agents" above
2. Save BOTH files (UI specs and Figma prompt)
3. Confirm file locations to user after saving

---

### backendAgent

**Output files:**
- `[Feature_Name]_API_Contracts.md` (API contracts and data exchange)
- `[Feature_Name]_Database_Schema.sql` (database schema)
- `[Feature_Name]_Backend_Logic.md` (backend logic documentation)

**Location:** `agents_output/doc_[Feature_Name]/`

**Full path examples:**
- `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_API_Contracts.md`
- `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_Database_Schema.sql`
- `/Users/manu/Documents/GitHub/Feature_Building/agents_output/doc_Diet_Generator/Diet_Generator_Backend_Logic.md`

**Workflow:**
1. Follow "Standard File Storage Protocol for Agents" above
2. Save ALL THREE files (API contracts, database schema, backend logic)
3. Confirm file locations to user after saving

---

## Complete Feature Documentation Example

For a feature called "Diet_Generator", the final folder structure should be:

```
agents_output/doc_Diet_Generator/
├── Diet_Generator_PRD.md                      # from prdDiscoveryAgent
├── Diet_Generator_Flow_Diagram.md             # from flowDesignerAgent
├── Diet_Generator_Documentation.md            # from flowDesignerAgent
├── Diet_Generator_UI_Specifications.md        # from frontendUIAgent
├── Diet_Generator_Figma_Make_Prompt.json      # from frontendUIAgent
├── Diet_Generator_API_Contracts.md            # from backendAgent
├── Diet_Generator_Database_Schema.sql         # from backendAgent
└── Diet_Generator_Backend_Logic.md            # from backendAgent
```

---

## Agent Output Mapping (Quick Reference)

| Agent | Outputs | File Names |
|-------|---------|------------|
| prdDiscoveryAgent | PRD | `[Feature_Name]_PRD.md` |
| flowDesignerAgent | Flow diagram, Documentation | `[Feature_Name]_Flow_Diagram.md`, `[Feature_Name]_Documentation.md` |
| frontendUIAgent | UI specs, Figma prompt | `[Feature_Name]_UI_Specifications.md`, `[Feature_Name]_Figma_Make_Prompt.json` |
| backendAgent | API contracts, DB schema, Backend logic | `[Feature_Name]_API_Contracts.md`, `[Feature_Name]_Database_Schema.sql`, `[Feature_Name]_Backend_Logic.md` |

---

## Important Notes for All Agents

1. **Always check this file** for current file storage conventions
2. **Never hardcode paths** - use the base paths defined here
3. **Use consistent naming** - PascalCase for feature names, underscore separators
4. **Create folders if needed** - Use `mkdir -p` to ensure parent directories exist
5. **Confirm to user** - Always inform where files were saved with full paths
6. **Ask if unclear** - If feature name is ambiguous, ask the user

---

## Path Updates

If paths need to change in the future, update this section only. All agents reference this file as the single source of truth.

**Current base path:** `/Users/manu/Documents/GitHub/Feature_Building/`

**To update for a different machine:**
1. Update the base path in this section
2. All agents will automatically use the new path when they reference this file

---

## Workflow After Generation

### Step 1: Review Generated Files
```bash
# View the generated files
ls -la agents_output/doc_[Feature_Name]/

# Check git status
git status
```

### Step 2: Commit to Version Control
```bash
# Stage the new feature folder
git add agents_output/doc_[Feature_Name]/

# Commit with descriptive message
git commit -m "Add [Feature_Name] complete feature documentation"

# Push to GitHub
git push
```

### Step 3: Move to Features Folder (Optional, When Finalized)
```bash
# When the feature documentation is approved, move to features/
mv agents_output/doc_[Feature_Name]/ features/

# The features/ folder will sync to OneDrive automatically
```

---

## Related Documentation

- **CLAUDE.md** - Complete repository documentation and setup
- **features/** - Finalized feature documentation (OneDrive synced)
- **context_knowledge/** - Private knowledge base for agents to read
- **Transcriptions/** - Raw transcript files (Google Drive symlinks)

---

**Last Updated:** 2025-01-05
**Version:** 1.0

---
description: Update the app flow diagram in context_knowledge
---

# Update App Flow

You are helping the user update `/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Balance_App_Flow.md`.

## Your Task

### Step 1: Read Current Flow

Read the current flow file:

```
/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Balance_App_Flow.md
```

Present a summary of the current flow sections:
- List all stage groups (e.g., "Web Path", "Subscription", "Medication", etc.)
- Count total nodes
- Highlight key decision points

### Step 2: Ask What to Update

Ask the user: "What would you like to update in the app flow?"

**Common updates:**
1. **Add a new stage/module** - New feature area in the user journey
2. **Modify existing stage** - Change steps within a section
3. **Add alternative paths** - New user paths (dotted lines)
4. **Remove a stage** - Feature removed or consolidated
5. **Rename nodes** - Better labels or terminology
6. **Update flow explanations** - Better descriptions of each section
7. **Full rewrite** - Rebuild the entire flow

### Step 3: Make the Changes

Based on user input:
- For Mermaid diagram changes, ensure valid syntax
- Preserve the comment structure (`%% ─── Section Name`)
- Use SCREAMING_SNAKE_CASE for node IDs
- Use `-->` for main flows, `-.->` for alternative paths
- Update both the Mermaid diagram AND the "Flow Sections Explained" text below

### Step 4: Validate Mermaid Syntax

After saving, verify the Mermaid is valid by checking:
- All node references exist (no orphan connections)
- No duplicate node IDs
- Labels use double quotes for multi-word text
- No special characters that break Mermaid (em-dashes, unescaped parentheses)

Present the updated flow sections to the user.

Remind the user: "This flow is used by flowDesignerAgent to ensure new feature flows integrate with the existing user journey. Changes here affect how new features connect to the app."

## Structure Reference

The flow file follows this structure:
- `# [Product] App Flow - Complete User Journey`
- Mermaid `flowchart TD` code block
- `## Flow Sections Explained` with numbered subsections

## Mermaid Conventions

- `flowchart TD` (top-down direction)
- Node IDs: SCREAMING_SNAKE_CASE (e.g., `HOME`, `APP_LOGIN`)
- `-->` main flow, `-.->` alternative path
- `--|label|` for conditional edges
- `%% ─── N. SECTION NAME` for section comments

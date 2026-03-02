---
name: opportunity-tree
description: Read, add, edit, or reorganize the Opportunity Tree (Obsidian Canvas). Encodes all canvas format and Teresa Torres methodology conventions.
---

# Opportunity Tree Skill

Invoked when the user wants to read, add, edit, or restructure the Opportunity Tree.

## Workflow

1. Read canvas from `context_knowledge/opportunity_tree.canvas` using the `Read` tool
2. Load `references/canvas-conventions.md` for format rules
3. Load `references/methodology.md` for content rules
4. Present current tree structure to user (areas and children — hierarchy, not counts)
5. Ask what to update: add area, add sub-opportunity, edit content, restructure, full review
6. Apply changes following the loaded references
7. Write full canvas JSON back via `Write` tool (always full rewrite — no partial edits)
8. Sync `context_knowledge/opportunity_tree.md` if content changed

## Key principles

- Always load both reference files before making any edits
- Always do a full rewrite of the canvas JSON — never partial edits
- Keep the markdown file in sync after any content change
- Preserve y-level alignment and color codes strictly (see canvas-conventions.md)
- Apply methodology rules before accepting any new node content (see methodology.md)

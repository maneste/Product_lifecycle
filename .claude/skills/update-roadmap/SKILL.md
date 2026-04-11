---
name: update-roadmap
description: Manage ROADMAP.md — sync checkbox states from file frontmatter, add new features, or show progress. Use when the user says "update roadmap", "sync roadmap", "add feature to roadmap", "check roadmap status", or after completing a product/spec document.
---

# Update Roadmap

Manages `ROADMAP.md` at the repo root. Two operations:

1. **Sync** — run the script to update checkboxes from file status (no LLM needed)
2. **Add feature** — append a new feature block following the naming convention

## Checkbox Convention

| Checkbox | Meaning | Condition |
|---|---|---|
| `[ ]` | Not started | File does not exist |
| `[-]` | In progress | File exists (any content, or `status: draft`) |
| `[x]` | Done | File exists with `status: done` in YAML frontmatter |

To mark a doc as done, add to the top of the file:
```markdown
---
status: done
---
```

## Operation 1 — Sync Checkboxes

Run the script from the repo root:

```bash
node .claude/skills/update-roadmap/scripts/sync_roadmap.js
```

Options:
- `--dry-run` — preview changes without writing
- `--root <path>` — repo root if running from elsewhere
- `--roadmap <path>` — path to ROADMAP.md relative to root (default: `ROADMAP.md`)

The script reads each linked file path in ROADMAP.md, checks existence and frontmatter, and updates checkboxes in-place. Always run the script; do not manually update checkboxes.

## Operation 2 — Add a New Feature

When the user wants to add a feature to the roadmap, append this block to `ROADMAP.md` using the file naming conventions from `repo-structure` skill:

```markdown
## Feature: [Name]
_One-line description_

### Product
- [ ] PRD — `docs/product/[Name]_PRD.md`
- [ ] Gap Analysis — `docs/product/[Name]_Gap_Analysis.md`

### Flow Design
- [ ] Flow Narrative — `AI_Output/doc_[Name]/[Name]_Documentation.md`
- [ ] Flow Diagram — `AI_Output/doc_[Name]/[Name]_Flow_Diagram.md`

### UI Specs
- [ ] UI Specs — `AI_Output/doc_[Name]/[Name]_UI_Specs.md`
- [ ] Figma Prompt — `AI_Output/doc_[Name]/[Name]_Figma_Prompt.md`

### Backend Specs
- [ ] Backend Spec — `AI_Output/doc_[Name]/[Name]_Backend_Spec.md`

### Implementation
- [ ] Code — _batch implementation once specs are complete_
```

File naming: use `PascalCase` with underscores for spaces (e.g., `GLP1_Assessment`, `Onboarding_Flow`). Match the feature folder name in `AI_Output/doc_[Name]/`.

After adding, run the sync script to verify the new `[ ]` items are correctly detected (files should not exist yet).

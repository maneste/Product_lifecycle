---
name: prototype
description: Create or modify a feature's external prototype (Lovable, Replit, Bolt, v0, etc.). Use when the user asks to create a new prototype, or to add, modify, or remove any feature, behavior, state, or visual element from an existing prototype. Triggers on: "crea prototipo", "crear prototipo", "init prototype", "añade", "cambia", "quita", "modifica", "agrega", "prototype", "prototipo", or anything related to the prototype UI.
---

# Prototype Skill

Generate and iterate on specs for external prototyping tools. Specs are **self-contained prompts** — the user copies them and pastes into Lovable, Replit, Bolt, v0, or similar to produce a functional prototype.

Write every spec as if it were a standalone prompt for the target tool. Include all context the tool needs — layout, tokens, data, interactions — so the user never has to add missing information manually.

## Files Location

All files live in `prototypes/[Feature_Name]/`:

| File | Purpose |
|------|---------|
| `prototype-config.md` | Tool, URL, design tokens, constraints — created once at bootstrap |
| `prototype-changelog.md` | Source of truth — always read first |
| `prototype-spec-v1.md` | Base spec (full layout, tokens, mock data) |
| `v1.N-modifications.md` | Incremental modification batches |

## Spec Writing Rules

Apply to every spec and modification file:

- Use design tokens from `prototype-config.md` — never invent new values unless necessary
- All dimensions in px, consistent with UI Specs
- Be explicit about which states show/hide each element
- If adding UI elements, calculate layout impact against constraints in `prototype-config.md`
- Mock data must cover: happy path, empty states, error states, edge cases

---

## Bootstrap (First Invocation)

Run when `prototypes/[Feature_Name]/` does not exist yet. Read `references/bootstrap.md` for file templates.

### 1. Gather info

Ask the user:
- **Feature name** — must match existing feature name in `docs/product/prd-drafts/` if one exists
- **Prototyping tool** — Lovable, Replit, Bolt, v0, or other
- **Prototype URL** — link to the live prototype (can be added later)

### 2. Read project context

| Source | Path | What to extract |
|--------|------|-----------------|
| PRD | `docs/product/prd-drafts/[Feature]_PRD.md` | Requirements, user stories, acceptance criteria |
| Flow | `docs/product/prd-drafts/[Feature]_Flow.canvas` + `_Flow_Documentation.md` | Interaction flows, states, transitions |
| Screen Map | `docs/product/prd-drafts/[Feature]_Screen_Map.canvas` | Screen inventory, navigation |
| UI Specs | `docs/product/[Feature]_UI_Specs.md` | Component specs, layout rules |
| Backend Specs | `docs/product/[Feature]_API_Contracts.md`, `[Feature]_Backend_Logic.md` | API contracts, data model |
| Design system | `docs/design/` | Colors, typography, spacing, tokens |
| Tech stack | `docs/architecture/` | Platform, frameworks |
| Brand | `hq/brand/` | Brand colors, assets |

Proceed with whatever is available. The more specs exist, the better the prototype.

### 3. Create files

Follow templates in `references/bootstrap.md` to create:

1. **`prototype-config.md`** — tool, design tokens (from `docs/design/`), layout constraints, mock data definition
2. **`prototype-spec-v1.md`** — full base spec built from project context
3. **`prototype-changelog.md`** — initial apply order and contents summary

---

## Incremental Changes (Subsequent Invocations)

Read `references/incremental.md` for the modifications template and changelog entry format.

### STEP 1 — Read state

Read `prototypes/[Feature_Name]/prototype-changelog.md`:
- Current apply order
- Highest version number (e.g., v1.3)
- Pending changes

Also read `prototype-config.md` for design tokens and constraints.

### STEP 2 — Create modifications file

Next version = current highest + 0.1 (e.g., v1.3 → v1.4). Create `prototypes/[Feature_Name]/v[X.Y]-modifications.md` following the template in `references/incremental.md`.

### STEP 3 — Update changelog

Update `prototype-changelog.md` following the format in `references/incremental.md`: add the new file to the apply order and insert a changelog entry.

### STEP 4 — Update feature canvases

If the feature has canvases in `docs/product/prd-drafts/`, update relevant nodes and edges:

**Flow Canvas** (`[Feature]_Flow.canvas`):

| Change type | What to update |
|-------------|---------------|
| New UI element | Update the relevant screen/panel node |
| New interaction | Add/update edge + possibly new node |
| New outcome / terminal state | Update relevant outcome node |
| Removed interaction | Delete edge, update source node |
| New filter/navigation | Update the relevant container node |

**Screen Map** (`[Feature]_Screen_Map.canvas`):

| Change type | What to update |
|-------------|---------------|
| New screen | Add node with connections |
| Screen removed | Remove node and edges |
| Navigation change | Update edges between screens |
| Screen content change | Update screen node text |

---

## Checklist Before Finishing

- [ ] Spec or modifications file created with full detail
- [ ] `prototype-changelog.md` — apply order + entry updated
- [ ] Flow canvas — relevant nodes/edges updated (if exists)
- [ ] Screen map — relevant nodes updated (if exists)

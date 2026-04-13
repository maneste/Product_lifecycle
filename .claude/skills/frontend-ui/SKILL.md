---
name: frontend-ui
description: Generate UI specifications from flow canvases and PRDs. Use after flow-designer has produced a flow canvas, when the user asks to design the UI, create component specs, or prepare implementation-ready frontend documentation. Detects tech stack from docs/architecture/ and applies the correct template.
---

# Frontend UI Skill

You are a senior frontend designer translating user flows into implementation-ready UI specifications. Given a flow canvas and PRD, you produce a detailed UI specs document that frontend developers can implement directly.

## Workflow

### Step 1: Detect Tech Stack

Read `docs/architecture/` — look for any file describing the tech stack (e.g. `tech-stack.md`, `stack.md`, `architecture.md`).

Extract:
- **Platform:** mobile native (React Native / iOS / Android) | web app | PWA
- **Framework:** React Native, Next.js, Vue, etc.
- **Design tool:** Figma, Pencil, other — check if `Instructions_Figma_Make.json` exists in `hq/`

If no tech stack file exists, ask the user before proceeding:
> "I couldn't find a tech stack definition in docs/architecture/. What platform and framework is this project using?"

### Step 2: Read Context

1. **Flow canvas** — `docs/product/prd-drafts/[Feature_Name]_Flow.canvas`
   - Extract all SCN_ nodes (screens), ACT_ nodes (interactions), navigation edges
2. **PRD** — `docs/product/prd-drafts/[Feature_Name]_PRD.md`
   - Extract feature context, goals, success metrics, acceptance criteria
3. **Design system** — `docs/design/` (read any file present)
   - Extract colors, typography, spacing, component conventions
4. **Brand** — `hq/brand/` (read any file present)
   - Extract brand voice, visual identity guidelines
5. **Personas** — `hq/personas/` (read any file present)
   - Extract who the user is, accessibility needs

### Step 3: Select Template

Based on detected platform, read the matching template from `templates/`:

| Platform | Template |
|----------|----------|
| React Native / iOS / Android | `templates/react-native.md` |
| Web app (Next.js, Vue, etc.) | `templates/web-app.md` |
| Progressive Web App | `templates/pwa.md` |

The template defines the output structure, component naming conventions, and format for that platform.

### Step 4: Generate UI Specifications

Following the template, produce `[Feature_Name]_UI_Specs.md` with:

- **Feature context** — problem, goal, personas, scope
- **Component hierarchy** — Atomic Design (atoms → molecules → organisms → templates → pages)
- **Screen-by-screen breakdown** — for each SCN_ node:
  - Description and purpose
  - Components present and their states (default, loading, error, empty)
  - Interaction patterns (taps, swipes, inputs)
  - Navigation triggers (what leads where)
  - Responsive / platform-specific behavior
  - Accessibility requirements (ARIA labels, focus order, screen reader notes)
- **Edge cases** — empty states, error states, offline behavior
- **Design system usage** — which tokens/components apply to this feature

### Step 5: Save

Save to `docs/product/[Feature_Name]_UI_Specs.md`.

Confirm file path to the user.

## Output

**One file:** `[Feature_Name]_UI_Specs.md`

Platform-specific extras (e.g. Figma Make JSON) are defined in the template — only generate them if the template specifies them AND the relevant tool is in use.

## Notes

- Focus on USER-FACING screens only — no backend logic
- Use `lowercase_snake_case` for all component IDs
- Reference component IDs consistently across all screens
- Do not invent design system values — if not found in docs/design/, note them as `[TO DEFINE]`

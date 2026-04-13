# Bootstrap Templates

Templates for files created during first invocation of the prototype skill for a feature.

---

## prototype-config.md

```markdown
# Prototype Configuration — [Feature_Name]

## Tool
- **Platform:** [Lovable / Replit / Bolt / v0 / other]
- **URL:** [prototype URL or "TBD"]

## Design Tokens

[Extract from docs/design/ — list all color tokens, spacing, typography, border radii, shadows, etc. Format as CSS custom properties]

## Layout Constraints

[Extract from UI Specs or define based on the tool — e.g., viewport size, panel heights, max widths, breakpoints]

## Mock Data

[Define mock data sets based on PRD — entities, counts, realistic sample values]
```

---

## prototype-spec-v1.md

```markdown
# V1 Prototype Spec — [Feature_Name]

Target tool: [tool name]

Builds from: [Feature]_PRD.md, [Feature]_Flow_Documentation.md, [Feature]_UI_Specs.md

---

## 1. Global Layout

[Full layout structure — panels, sections, dimensions, flex/grid rules, using tokens from prototype-config.md]

## 2. Components

### 2.1 [Component Name]

#### Layout / Visual
[Exact CSS properties using design tokens — colors, dimensions, spacing, borders]

#### Content
[Text, icons, data bindings, placeholder content]

#### States
[All visual states — default, hover, active, disabled, loading, error, empty]

#### Interactions
[Click, hover, drag, keyboard — what triggers what]

### 2.2 [Next Component]
…

## 3. Data Model

### TypeScript Interfaces
[All interfaces/types needed for the prototype]

### Mock Data
[Full mock dataset — enough records to show all states and edge cases]

## 4. Interaction Flows

[Step-by-step flows matching the Flow canvas — state transitions, triggers, outcomes]

## 5. Responsive Behavior

[Breakpoints, what changes at each size — or "desktop only" if applicable]
```

---

## prototype-changelog.md

```markdown
# Prototype Changelog — [Feature_Name]

**Tool:** [Lovable / Replit / etc.]
**URL:** [prototype URL]

Apply order: prototype-spec-v1.md

---

## V1 — Base Spec
**File:** `prototype-spec-v1.md`

### Contents
- [Summary of what the base spec covers]

---

## Pending / Not yet built

- [Any known gaps or planned additions]
```

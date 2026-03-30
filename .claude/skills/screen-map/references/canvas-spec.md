# Screen Map — Canvas Specification

## Purpose

The screen map canvas shows the architecture of screens in a feature — what screens exist and how they connect. It is derived from the flow canvas, not designed independently.

## Node Types

### Screen Node

```json
{
  "id": "SCN_HOME",
  "type": "text",
  "text": "SCN_HOME - Home Screen",
  "x": 0,
  "y": 0,
  "width": 260,
  "height": 80,
  "color": "5"
}
```

All screens use color `5` (cyan) — same as in the flow canvas for visual consistency.

### Group Node

Groups organise screens by section of the app (e.g. Onboarding, Main App, Settings).

```json
{
  "id": "group_onboarding",
  "type": "group",
  "label": "Onboarding",
  "x": -60,
  "y": -60,
  "width": 600,
  "height": 400,
  "color": "3"
}
```

Groups use color `3` (yellow) background. Place them BEFORE the screens they contain in the JSON so Obsidian renders them as backgrounds.

## Edge Schema

```json
{
  "id": "edge_SCN_HOME_SCN_DETAIL",
  "fromNode": "SCN_HOME",
  "toNode": "SCN_DETAIL",
  "fromSide": "right",
  "toSide": "left",
  "label": "tap card"
}
```

Edge labels come from the ACT_ node that connected the two SCN_ nodes in the flow canvas. Keep them short (2-4 words).

---

## Layout Rules

### Grid

- **Arrange by section** — screens within the same group cluster together
- **Section columns** — each logical section occupies a column or row zone
- **Screen size:** 260×80px for all screens
- **Horizontal gap between screens:** 80px → column step = 340px
- **Vertical gap between screens:** 80px → row step = 160px
- **Group padding:** 60px around contained screens

### Direction

- Primary navigation flows **left to right** (entry → core → exit/deeper)
- Modals float **above** their parent screen (negative y offset)
- Settings / secondary sections go **below** the main flow

### Example Layout (3 sections)

```
[Group: Onboarding]          [Group: Main App]         [Group: Settings]
  SCN_SPLASH                   SCN_HOME                   SCN_SETTINGS
  SCN_SIGNUP       →→→         SCN_DETAIL        →→→      SCN_PROFILE
  SCN_ONBOARDING               SCN_CONFIRM
```

---

## Derivation from Flow Canvas

To build the screen map from a flow canvas:

1. Extract all nodes where `text` starts with `SCN_`
2. Build a navigation graph: for each `SCN_A → ACT_X → SCN_B` path in the flow edges, create a direct edge `SCN_A → SCN_B` with label = ACT_X description
3. Also include any direct `SCN_A → SCN_B` edges from the flow
4. Deduplicate edges (same source + target = one edge, combine labels if needed)
5. Identify groups by naming patterns or ask the user if unclear
6. Apply layout rules

---

## Deliverables Checklist

- [ ] Valid JSON (no comments, no trailing commas)
- [ ] All group nodes appear BEFORE screen nodes in the JSON
- [ ] All screen nodes have `"color": "5"`
- [ ] All edges reference existing node IDs
- [ ] Edge labels are present and concise
- [ ] Screens are visually grouped by section
- [ ] No ACT_, DEC_, or SYS_ nodes present (screens only)

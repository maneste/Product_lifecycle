# Flow Designer — Canvas Specification

## Obsidian Canvas Format

A `.canvas` file is a JSON document with two arrays: `nodes` and `edges`.

```json
{
  "nodes": [...],
  "edges": [...]
}
```

---

## Node Schema

```json
{
  "id": "unique_string",
  "type": "text",
  "text": "NODE_ID - Label",
  "x": 0,
  "y": 0,
  "width": 250,
  "height": 80,
  "color": "5"
}
```

**Fields:**
- `id` — unique string, use the node ID (e.g. `"SCN_HOME"`)
- `type` — always `"text"` for flow nodes
- `text` — `"NODE_ID - Human readable label"` (e.g. `"SCN_HOME - Home Dashboard"`)
- `x`, `y` — position in pixels (integers, can be negative)
- `width`, `height` — size in pixels
- `color` — Obsidian color string (see node-conventions.md for mapping)

---

## Edge Schema

```json
{
  "id": "edge_SCN_HOME_ACT_TAP",
  "fromNode": "SCN_HOME",
  "toNode": "ACT_TAP",
  "fromSide": "bottom",
  "toSide": "top",
  "label": "optional label"
}
```

**Fields:**
- `id` — unique string, convention: `"edge_FROMID_TOID"`
- `fromNode` / `toNode` — node IDs
- `fromSide` / `toSide` — `"top"`, `"bottom"`, `"left"`, `"right"`
- `label` — optional, use for decision branches (e.g. `"Yes"`, `"No"`, `"Skip"`)

---

## Layout Rules

These rules ensure Claude generates a readable, consistent layout that serves as a useful starting point for the user to adjust in Obsidian.

### Node Sizes

| Node type | Width | Height |
|-----------|-------|--------|
| SCN_      | 250   | 80     |
| ACT_      | 220   | 60     |
| DEC_      | 200   | 80     |
| SYS_      | 220   | 60     |

### Grid System

- **Primary axis:** top-to-bottom (y increases downward)
- **Column width:** 320px (node width + 70px gap)
- **Row height:** 160px (node height + 80px gap)
- **Origin:** start at `x: 0, y: 0` for the first node
- **Happy path:** flows down the center column (x = 0)
- **Alternate paths / branches:** shift right (+320px per branch column)
- **Return paths:** use edges with `fromSide: "left"` pointing back up

### Positioning Formula

For a linear sequence:
```
node[0]: x=0,   y=0
node[1]: x=0,   y=160
node[2]: x=0,   y=320
...
node[n]: x=0,   y=n*160
```

For a decision branch (DEC_ splits into two paths):
```
DEC_ node:       x=0,    y=N
Left branch:     x=-320, y=N+160
Right branch:    x=+320, y=N+160
Merge back:      x=0,    y=N+320
```

### Edge Direction

- Main path: `fromSide: "bottom"`, `toSide: "top"`
- Branch left: `fromSide: "left"`, `toSide: "top"`
- Branch right: `fromSide: "right"`, `toSide: "top"`
- Return / loop: `fromSide: "left"`, `toSide: "left"` or use a long bottom-to-top edge

---

## File Structure

### File 1: `[Feature_Name]_Flow.canvas`

Pure JSON. No markdown. No comments.

```json
{
  "nodes": [
    {
      "id": "SCN_HOME",
      "type": "text",
      "text": "SCN_HOME - Home Screen",
      "x": 0,
      "y": 0,
      "width": 250,
      "height": 80,
      "color": "5"
    },
    {
      "id": "ACT_TAP_START",
      "type": "text",
      "text": "ACT_TAP_START - Tap Start Button",
      "x": 0,
      "y": 160,
      "width": 220,
      "height": 60,
      "color": "4"
    }
  ],
  "edges": [
    {
      "id": "edge_SCN_HOME_ACT_TAP_START",
      "fromNode": "SCN_HOME",
      "toNode": "ACT_TAP_START",
      "fromSide": "bottom",
      "toSide": "top"
    }
  ]
}
```

### File 2: `[Feature_Name]_Flow_Documentation.md`

Contains everything EXCEPT the canvas:

1. **Flow Narrative** — overview of the user journey
2. **Step-by-Step Specs** — per-node explanations
3. **Improvements & Trade-offs** — table of proposals
4. **Open Questions** — ambiguities, edge cases, constraints

---

## Step-by-Step Spec Template (File 2)

For each node:

```
#### [NodeID] - [Short Title]
**Type:** Screen | Action | Decision | System
**Purpose:** Why this step exists for the user.
**What User Sees:** Describe the visual state/content.
**What User Does:** Key interactions available.
**What Happens Next:** Where the flow goes after this step.
**Edge Cases:** Exceptions or alternate paths (still user-facing).
**Emotional Goal:** How this step should make the user feel.

**Technical Notes:** (optional) Backend connections, API calls, webhooks for developer handoff.
```

---

## Improvements & Trade-offs Table

| Area | Proposal | Rationale | Impact | Risk/Cost |
|------|----------|-----------|--------|-----------|
| [UX area] | [Suggested change] | [Why this helps] | [High/Med/Low] | [Effort/Risk] |

---

## Open Questions

1. [Ambiguity or missing context]
2. [Potential edge case or constraint]
3. [Dependency on another feature or external system]

---

## Deliverables Checklist

**File 1 — Flow Canvas:**
- [ ] Valid JSON (no comments, no trailing commas)
- [ ] All node IDs follow convention (see node-conventions.md)
- [ ] All edge `fromNode` / `toNode` reference existing node IDs
- [ ] Decision nodes (DEC_) have at least 2 outgoing edges with labels
- [ ] Node positions follow the grid layout rules
- [ ] Color codes match node type

**File 2 — Documentation:**
- [ ] Has markdown header `# [Feature Name] - Flow Documentation`
- [ ] Contains: narrative, step specs, improvements table, open questions
- [ ] Does NOT contain canvas JSON
- [ ] References nodes by their IDs
- [ ] Technical Notes present for nodes that require backend interaction

---

## What Belongs Where

**Canvas (user journey only):**
- Screens the user sees (SCN_*)
- Actions the user takes (ACT_*)
- Decisions based on user choice or visible app state (DEC_*)
- Brief system feedback shown to user (SYS_*)
- Navigation paths between all of the above

**NOT in canvas:**
- Backend APIs, webhooks, events
- Database operations
- Server-side processing
- External service integrations
- Data models or state management

**Documentation file:**
- Flow narrative
- Step-by-step specs for each node
- Optional Technical Notes for backend details
- Improvements, trade-offs, open questions

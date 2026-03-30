---
name: screen-map
description: Generate a screen architecture map from a flow canvas. Use after flow-designer has produced a flow canvas, when you need a clean visual map of all screens and their navigation connections. Produces an Obsidian canvas showing only screens and the navigation paths between them.
---

# Screen Map Skill

You are a product designer creating a clean architectural overview of an app's screen structure. Given a flow canvas produced by the flow-designer skill, you extract all screens and their navigation relationships and produce a spatial, human-navigable Obsidian canvas.

The screen map is not a user journey — it does not show actions, decisions, or system feedback. It shows **what screens exist** and **which screens lead to which**, at a glance.

## When to Use

Run this skill AFTER `flow-designer` has produced `[Feature_Name]_Flow.canvas`. The screen map is a derived artifact — it is built from the flow, not designed from scratch.

Use cases:
- Developer handoff: quick reference for all screens in scope
- Navigation audit: verify no screen is orphaned or unreachable
- Stakeholder overview: high-level picture without journey complexity

## Workflow

### Step 1: Read the Flow Canvas

Read `docs/product/prd-drafts/[Feature_Name]_Flow.canvas`.

Extract:
- All nodes with prefix `SCN_` — these become screen-map nodes
- All edges where both `fromNode` and `toNode` are `SCN_` nodes — these become direct navigation edges
- All indirect navigation paths: `SCN_A → ACT_ → SCN_B` → simplify to `SCN_A → SCN_B` with the ACT_ label as the edge label

Also read `docs/design/` if a design system exists, to apply correct brand colors to screen groups.

### Step 2: Group Screens

Identify logical groups (e.g. Onboarding, Main App, Settings, Modals) and create a group node for each. Use Obsidian canvas group nodes to contain the screens visually.

### Step 3: Generate the Canvas

Read `references/canvas-spec.md` for the canvas JSON format and layout rules.

Produce `[Feature_Name]_Screen_Map.canvas` with:
- One node per screen (`SCN_` nodes only)
- Group nodes for logical sections
- Directed edges for all navigation paths
- Edge labels indicating what triggers the navigation (the ACT_ node that connected them in the flow)

### Step 4: Save

Save to `docs/product/prd-drafts/[Feature_Name]_Screen_Map.canvas`.

Confirm the file path to the user.

## Iteration Protocol

When the user modifies the flow canvas (adds/removes screens, changes navigation):
1. Re-read the updated flow canvas
2. Regenerate the screen map from scratch (do not patch — derive fresh)
3. Save the updated file

## Output

**One file only:** `[Feature_Name]_Screen_Map.canvas`

No documentation file needed — the screen map is self-explanatory. If the user wants annotations, they add them directly in Obsidian.

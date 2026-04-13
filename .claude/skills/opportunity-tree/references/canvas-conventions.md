# Canvas Conventions — Opportunity Tree

## Files

- **Canvas (source of truth):** `hq/opportunity_tree.canvas`
- **Markdown reference:** `hq/opportunity_tree.md` (keep in sync after content changes)

## Format

Obsidian Canvas JSON — `nodes[]` and `edges[]` arrays at root level.

## Node ID convention

Concatenated digit strings: `n1`, `n11`, `n12`, `n13`, `n111`, `n121`, `n1211`, `n1441`, etc.

- Root desired outcome: `n1`
- Opportunity areas: `n11`, `n12`, `n13`, `n14` …
- Specific opportunities under 1.1: `n111`, `n112`, `n113` …
- Sub-opportunities under 1.1.1: `n1111`, `n1112` …

## Numeric reference in card text

Every card begins with its reference number, followed by two spaces, then the title:

```
"1.2.3  Title of the opportunity\n\n..."
```

The number is the human coordinate system. It must match the node's position in the hierarchy.

This reference number (e.g., `1.2.3`) is what the interview summary and PRD skill use to cross-reference opportunities — extract it from the first line of node text before the `\n\n`.

## Y-level alignment

All nodes at the same depth share the same `y` value — never mix levels:

| Level | Example nodes | Approximate y |
|-------|--------------|---------------|
| Desired Outcome | n1 | -175 |
| Opportunity Areas | n11, n12, n13… | ~480 |
| Specific Opportunities | n111, n121… | ~740 |
| Sub-opportunities | n1111, n1211… | ~1020 |

**Note:** Obsidian may shift y values on save. Always re-align after writing.

## Color codes (Obsidian color field, values 1–6)

| Node type | Color value | Obsidian label |
|-----------|-------------|----------------|
| Title + Desired Outcome | `"6"` | Purple |
| Opportunity Areas (1.1, 1.2, 1.3…) | `"1"` | Red |
| 1.1.x nodes | `"2"` | Orange |
| 1.2.x nodes | `"3"` | Yellow |
| 1.3.x nodes | `"4"` | Green |
| 1.4.x nodes | `"5"` | Cyan |

New branches: continue the cycle (1→2→3→4→5→1…) or ask the user.

## Card dimensions

| Level | Width | Height |
|-------|-------|--------|
| Area nodes (1.x) | 450px | adapts to text (~20px per line) |
| Level-2 nodes (1.x.x) | 380px | adapts to text |
| Level-3+ nodes (1.x.x.x) | 300px | adapts to text |

## Edges

- `fromSide: "bottom"`, `toSide: "top"` — always parent→child, top-down
- Edge ID convention: `e` + parent node ID + child node ID (e.g., `en1n11`)

## Full rewrite rule

Always write the entire canvas JSON when saving. Never attempt partial edits to the JSON. Read the file first, apply changes in memory, write the full result.

## Minimal canvas scaffold (for init-context)

Use this as the starting template when creating the canvas from scratch:

```json
{
  "nodes": [
    {
      "id": "n1",
      "type": "text",
      "text": "Desired Outcome\n\n[North star metric — what the product exists to create for the business]",
      "x": 0,
      "y": -175,
      "width": 450,
      "height": 100,
      "color": "6"
    }
  ],
  "edges": []
}
```

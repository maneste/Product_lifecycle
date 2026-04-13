# Knowledge Base Schemas

## opportunity_tree.canvas

Obsidian Canvas format — `nodes[]` and `edges[]` arrays at root level.

Each node is a card with:
- `id` — internal canvas node ID (e.g., `n111`)
- `text` — card content; first line is `"1.1.1  Title of opportunity\n\n...explanation..."`
- `color` — visual color code (see canvas-conventions.md)
- `x`, `y` — spatial position (y encodes depth level)

**To extract reference numbers and titles:**
- Read the first line of `text` before `\n\n`
- Parse the leading `N.N.N` number (two spaces after it, then the title)
- Example: `"2.3.1  Motivation loss after plateau\n\nUsers feel demotivated..."` → id `2.3.1`, title `Motivation loss after plateau`

```json
{
  "nodes": [
    {
      "id": "n1",
      "type": "text",
      "text": "Desired Outcome\n\nNorth star metric for the business.",
      "color": "6",
      "x": 0, "y": -175, "width": 450, "height": 100
    },
    {
      "id": "n11",
      "type": "text",
      "text": "1.1  First opportunity area\n\nWhy this matters to users.",
      "color": "1",
      "x": -600, "y": 480, "width": 450, "height": 80
    },
    {
      "id": "n111",
      "type": "text",
      "text": "1.1.1  Specific opportunity\n\nDetailed description of the need.",
      "color": "2",
      "x": -600, "y": 740, "width": 380, "height": 80
    }
  ],
  "edges": [
    { "id": "en1n11", "fromNode": "n1", "fromSide": "bottom", "toNode": "n11", "toSide": "top" },
    { "id": "en11n111", "fromNode": "n11", "fromSide": "bottom", "toNode": "n111", "toSide": "top" }
  ]
}
```

A human-readable sync file is also maintained at `hq/opportunity_tree.md`.

## *_interview_summary.json

The filename includes a date prefix (e.g., `20251012_interview_summary.json`). Use glob to find the current file.

```json
{
  "metadata": {
    "generated_at": "timestamp",
    "source_csv": "filename",
    "opportunity_tree_version": "version",
    "total_opportunities": 0,
    "opportunities_with_validations": 0,
    "total_validations": 0
  },
  "opportunities": [
    {
      "id": "1.1.1",
      "title": "Opportunity title",
      "interview_count": 5,
      "interview_count_text": "5 interviews",
      "interview_names": ["Name1", "Name2"],
      "evidence": [
        {
          "interview_name": "Name1",
          "quote": "direct user quote"
        }
      ]
    }
  ]
}
```

**How to use:**
- Match `id` field with opportunity_tree nodes to find evidence
- `interview_count` shows validation strength
- Use `interview_name` to cite specific users in the PRD
- Evidence is organized by opportunity, not by interview

## Cross-referencing

To build a complete picture for a PRD:
1. Find the opportunity node in `hq/opportunity_tree.canvas` — extract reference number from first line of `text` (e.g., `"1.2.3  Title\n\n..."` → id `1.2.3`)
2. Look up the same ID in `hq/research/*_interview_summary.json` for user evidence
3. Check `hq/research/Benchmark_[Product].json` for competitive context
4. Verify alignment with `hq/Vision_[Product].md` pillars
5. Check `docs/product/[Product]_App_Flow.md` for where the feature fits in the current journey

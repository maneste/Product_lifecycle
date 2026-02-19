# Knowledge Base Schemas

## opportunity_tree.json

- Root key: `"opportunity_tree"`
- Main array: `"opportunities"` — top-level opportunity areas
- Each node has: `id`, `title`, `explanation`, optional `children`
- ID defines hierarchy: `2.3.1` belongs under `2.3`, inside `2`

```json
{
  "id": "2.3.1",
  "title": "Motivation loss after plateau",
  "explanation": "Users feel demotivated when weight stagnates.",
  "children": []
}
```

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
1. Find the opportunity node in `opportunity_tree.json` by ID
2. Look up the same ID in `*_interview_summary.json` for user evidence
3. Check `Benchmark_Balance.json` for competitive context
4. Verify alignment with `Vision_Balance.md` pillars
5. Check `Balance_App_Flow.md` for where the feature fits in the current journey

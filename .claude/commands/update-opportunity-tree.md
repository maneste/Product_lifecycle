---
description: Update the opportunity tree in context_knowledge
---

# Update Opportunity Tree

You are helping the user update `context_knowledge/opportunity_tree.json`.

## Your Task

### Step 1: Read Current Tree

Read the current opportunity tree:

```
context_knowledge/opportunity_tree.json
```

Present a summary to the user:
- List all top-level opportunities (Level 1) with their IDs
- Count of Level 2 and Level 3 nodes
- Total number of opportunities

### Step 2: Ask What to Update

Ask the user: "What would you like to update in the opportunity tree?"

**Common updates:**
1. **Add a new top-level opportunity** - New research theme discovered
2. **Add sub-opportunities** - Drill deeper into an existing theme
3. **Edit titles or explanations** - Better wording from new research
4. **Remove an opportunity** - No longer relevant
5. **Reorganize hierarchy** - Move nodes to different parents
6. **Merge opportunities** - Combine similar items
7. **Full review** - Go through all nodes to update based on latest research

### Step 3: Make the Changes

Based on user input, modify the JSON file. Follow these rules strictly:

**ID hierarchy rules:**
- Level 1: `"1"`, `"2"`, `"3"`, etc.
- Level 2: `"1.1"`, `"1.2"`, `"2.1"`, etc.
- Level 3: `"1.1.1"`, `"1.1.2"`, `"2.1.1"`, etc.
- IDs must be sequential within their parent
- When adding a new node, use the next available ID at that level

**Required fields for every node:**
- `id` (string) - Hierarchical ID
- `title` (string) - Short, descriptive title
- `explanation` (string) - 2-3 sentence description of why this matters to users

**Optional fields:**
- `children` (array) - Sub-opportunities. Omit for leaf nodes.

### Step 4: Validate

After saving, validate the JSON:

```bash
python3 -c "
import json
tree = json.load(open('context_knowledge/opportunity_tree.json'))
def count_nodes(nodes):
    c = len(nodes)
    for n in nodes:
        if 'children' in n:
            c += count_nodes(n['children'])
    return c
total = count_nodes(tree['opportunity_tree']['opportunities'])
top_level = len(tree['opportunity_tree']['opportunities'])
print(f'Valid JSON. {top_level} top-level opportunities, {total} total nodes.')
"
```

### Step 5: Sync Interview Summary

**IMPORTANT:** After modifying the opportunity tree, the interview summary may need updating too. Check:

```bash
python3 -c "
import json, os
tree = json.load(open('context_knowledge/opportunity_tree.json'))
summary_files = [f for f in os.listdir('context_knowledge/') if 'interview_summary' in f]
if not summary_files:
    print('No interview summary found. Run /update-interview-summary to create one.')
else:
    summary = json.load(open(f'context_knowledge/{summary_files[0]}'))
    def get_ids(nodes):
        ids = set()
        for n in nodes:
            ids.add(n['id'])
            if 'children' in n:
                ids.update(get_ids(n['children']))
        return ids
    tree_ids = get_ids(tree['opportunity_tree']['opportunities'])
    summary_ids = set(o['id'] for o in summary['opportunities'])
    new_ids = tree_ids - summary_ids
    removed_ids = summary_ids - tree_ids
    if new_ids:
        print(f'New opportunities not in interview summary: {new_ids}')
        print('Run /update-interview-summary to add empty entries for these.')
    if removed_ids:
        print(f'Removed opportunities still in interview summary: {removed_ids}')
        print('Run /update-interview-summary to clean these up.')
    if not new_ids and not removed_ids:
        print('Interview summary is in sync with opportunity tree.')
"
```

Tell the user if the interview summary needs updating and suggest running `/update-interview-summary`.

## Structure Reference

```json
{
  "opportunity_tree": {
    "opportunities": [
      {
        "id": "1",
        "title": "Theme title",
        "explanation": "Why this matters...",
        "children": [
          {
            "id": "1.1",
            "title": "Sub-theme",
            "explanation": "Description...",
            "children": [
              {
                "id": "1.1.1",
                "title": "Specific problem",
                "explanation": "Details..."
              }
            ]
          }
        ]
      }
    ]
  }
}
```

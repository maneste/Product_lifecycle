---
description: Update the interview summary evidence in context_knowledge
---

# Update Interview Summary

You are helping the user update the interview summary JSON file in `/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/`.

The interview summary file links real user evidence (quotes from interviews) to opportunity tree nodes.

## Your Task

### Step 1: Find and Read Current File

Look for the interview summary file (may have a date prefix):

```bash
ls /Users/manu/Documents/GitHub/Feature_Building/context_knowledge/*interview_summary*
```

Read both the interview summary and the opportunity tree:
- Interview summary: the file found above
- Opportunity tree: `/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/opportunity_tree.json`

Present a summary:
- Metadata (version, source, counts)
- Number of opportunities with evidence vs. without
- Top 5 most-validated opportunities (by interview count)
- Any opportunities missing from the summary that exist in the tree

### Step 2: Ask What to Update

Ask the user: "What would you like to update in the interview summary?"

**Common updates:**
1. **Add evidence to an opportunity** - New quote from a user interview
2. **Sync with opportunity tree** - Add entries for new tree nodes, remove old ones
3. **Update metadata** - New version, source file, etc.
4. **Remove evidence** - Delete inaccurate or irrelevant quotes
5. **Bulk import** - Import evidence from a CSV or processed interview data
6. **Rename file** - Update the date prefix for a new version

### Step 3: Make the Changes

**Adding evidence to an opportunity:**

Ask the user:
1. "Which opportunity ID? (e.g., 1.1.1)"
2. "Who said it? (interviewee name)"
3. "What's the quote?"

Then add the evidence entry:
```json
{
  "interview_name": "[Name]",
  "quote": "'[Direct quote]'"
}
```

Also update:
- `interview_count`: recalculate from unique `interview_names`
- `interview_count_text`: update text (e.g., "5 interviews")
- `interview_names`: add name if not already in list

**Syncing with opportunity tree:**

For each opportunity in the tree that's missing from the summary, add:
```json
{
  "id": "[matching id]",
  "title": "[matching title from tree]",
  "interview_count": 0,
  "interview_count_text": "0 interviews",
  "interview_names": [],
  "evidence": []
}
```

Remove entries whose IDs no longer exist in the tree.

**Updating metadata:**

Update the `metadata` object with:
- `generated_at`: current ISO timestamp
- `total_opportunities`: count all entries
- `opportunities_with_validations`: count entries where `interview_count > 0`
- `total_validations`: sum of all `evidence` array lengths

### Step 4: Validate

After saving, validate:

```bash
python3 -c "
import json, os
# Find summary file
files = [f for f in os.listdir('/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/') if 'interview_summary' in f]
summary = json.load(open(f'/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/{files[0]}'))
tree = json.load(open('/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/opportunity_tree.json'))

# Validate structure
assert 'metadata' in summary, 'Missing metadata'
assert 'opportunities' in summary, 'Missing opportunities'

# Check sync with tree
def get_ids(nodes):
    ids = set()
    for n in nodes:
        ids.add(n['id'])
        if 'children' in n:
            ids.update(get_ids(n['children']))
    return ids

tree_ids = get_ids(tree['opportunity_tree']['opportunities'])
summary_ids = set(o['id'] for o in summary['opportunities'])

with_evidence = sum(1 for o in summary['opportunities'] if o['interview_count'] > 0)
total_evidence = sum(len(o['evidence']) for o in summary['opportunities'])

print(f'Valid JSON.')
print(f'Total opportunities: {len(summary[\"opportunities\"])}')
print(f'With evidence: {with_evidence}')
print(f'Total evidence entries: {total_evidence}')
print(f'Synced with tree: {tree_ids == summary_ids}')
if tree_ids != summary_ids:
    print(f'  Missing: {tree_ids - summary_ids}')
    print(f'  Extra: {summary_ids - tree_ids}')
"
```

Show the validation results to the user.

## Structure Reference

```json
{
  "metadata": {
    "generated_at": "2025-10-20T12:55:23.553557",
    "source_csv": "v1.2_latitude_output_2025-10-17.csv",
    "opportunity_tree_version": "v1.2",
    "total_opportunities": 49,
    "opportunities_with_validations": 34,
    "total_validations": 301
  },
  "opportunities": [
    {
      "id": "1.1.1",
      "title": "Difficulty perceiving physical evolution",
      "interview_count": 13,
      "interview_count_text": "13 interviews",
      "interview_names": ["name1", "name2"],
      "evidence": [
        {
          "interview_name": "name1",
          "quote": "'Direct quote from interview'"
        }
      ]
    }
  ]
}
```

## Important Notes

- Quotes should be in the interviewee's original language
- Wrap quotes in single quotes inside the JSON string
- Keep `interview_names` as an array of unique names
- The `id` and `title` fields must match `opportunity_tree.json` exactly
- When adding evidence, always check if the interview name already exists in `interview_names`

---
description: Initialize context_knowledge folder - create all knowledge base files for a new repo setup
---

# Initialize Context Knowledge Command

You are helping the user set up the `context_knowledge/` folder from scratch. This is the first step when starting with a new clone of the Product_lifecycle repository or when creating a new product context.

## Overview

The `context_knowledge/` folder is the private knowledge base that all agents (prdDiscoveryAgent, flowDesignerAgent, frontendUIAgent, backendAgent) read from to generate informed feature documentation. Without these files, agents cannot produce evidence-based outputs.

## Required Files

The following files must be created in `context_knowledge/`:

| # | File | Format | Purpose |
|---|------|--------|---------|
| 1 | `Vision_Balance.md` | Markdown | Product vision, mission, and strategic positioning |
| 2 | `User_persona.md` | Markdown | Primary user persona with demographics, motivations, frustrations |
| 3 | `Balance_App_Flow.md` | Markdown + Mermaid | Complete user journey flowchart |
| 4 | `opportunity_tree.json` | JSON | Hierarchical opportunity framework from user research |
| 5 | `interview_summary.json` | JSON | User interview evidence mapped to opportunities |
| 6 | `Benchmark_Balance.json` | JSON | Competitive landscape analysis |
| 7 | `Notifications_Touchpoints.json` | JSON | Notification and touchpoint strategy |

## Your Task

### Step 0: Check Existing State

First, check what already exists:

```bash
ls -la context_knowledge/ 2>/dev/null
```

If the folder doesn't exist:
```bash
mkdir -p context_knowledge
```

Report to the user which files already exist and which are missing. Ask if they want to:
1. **Create only missing files** (recommended if some exist)
2. **Start fresh** (recreate all files from scratch)
3. **Skip specific files** for now

### Step 1: Product Vision (`Vision_Balance.md`)

Ask the user to describe their product. Guide them with these questions (ask ONE at a time, conversationally):

1. "What problem does your product solve? Who suffers from this problem?"
2. "What is your solution? What makes it different from existing alternatives?"
3. "What are the core pillars of your approach? (e.g., medicine, nutrition, technology, etc.)"
4. "How does your product deliver value? What's the model? (e.g., app, platform, service)"
5. "What's your vision statement? Where do you see this product in 3-5 years?"

**Template structure to generate:**

```markdown
# [Product Name]: [Tagline]

### Where the Market Is Today
[Current market landscape and gaps]

## The Problem We're Solving
[Core problem statement]

## The [Product Domain] Challenge
[Specific challenges users face - numbered list]

## Our Vision
[Vision statement and core pillars]

### [Pillar 1 Name]
[Description]

### [Pillar 2 Name]
[Description]

### [Pillar 3 Name]
[Description]

### [Pillar 4 Name]
[Description]

## How We Make It Possible
[Delivery model, technology approach, team structure]

## [Product Name]: The New Standard
[Closing vision statement]
```

**Save to:** `context_knowledge/Vision_Balance.md`

---

### Step 2: User Persona (`User_persona.md`)

Ask the user about their primary user. Guide with these questions (ONE at a time):

1. "Who is your primary user? Give me a name, age, gender, and occupation."
2. "What's their household situation? Income level?"
3. "What health condition or core challenge are they dealing with?"
4. "What's their background story? How did they get to this point?"
5. "What motivates them to seek a solution now?"
6. "What are their biggest frustrations with current solutions?"
7. "What are their specific goals?"
8. "What are their daily pain points?"
9. "What do they need from an ideal solution?"

**Template structure to generate:**

```markdown
**User Persona: [Name]**

- Age: [age]
- Gender: [gender]
- Occupation: [occupation]
- Household: [family situation]
- [Key metric]: [value] (e.g., BMI: 32)
- Health Status: [condition]
- Income Level: [level]

Background:
[2-3 paragraph narrative about their journey]

Motivations:
- [Motivation 1]: [Description]
- [Motivation 2]: [Description]
- [Motivation 3]: [Description]
- [Motivation 4]: [Description]

Frustrations:
- Behavioral Challenges: [Description]
- [Category] Barriers: [Description]
- Long-Term Maintenance: [Description]

Goals:
- [Goal 1]
- [Goal 2]
- [Goal 3]
- [Goal 4]

Pain Points:
- [Pain point 1]
- [Pain point 2]
- [Pain point 3]
- [Pain point 4]

What They Need from a Solution:
- [Need 1]
- [Need 2]
- [Need 3]
- [Need 4]
```

**Save to:** `context_knowledge/User_persona.md`

---

### Step 3: App Flow (`Balance_App_Flow.md`)

Ask the user to walk you through the user journey. Guide with these questions (ONE at a time):

1. "How does a user first discover your product? (e.g., landing page, ad, referral)"
2. "What's the registration/onboarding process?"
3. "What happens after onboarding? What's the core activation step?"
4. "What does the main product experience look like? What are the key modules/features?"
5. "How do users retain and come back? What's the loop?"
6. "Are there parallel paths? (e.g., web vs app, different user types)"

**Template structure to generate:**

```markdown
# [Product Name] App Flow - Complete User Journey

\`\`\`mermaid
flowchart TD

%% ─── 1. [FIRST STAGE NAME]
[NODE_ID]["[Label]"]
[NODE_ID] --> [NODE_ID]

%% ─── 2. [SECOND STAGE NAME]
[NODE_ID]["[Label]"]
[NODE_ID] --> [NODE_ID]

%% (continue for each stage)
\`\`\`

## Flow Sections Explained

### 1. [Stage Name]
- [Bullet point explanation]

### 2. [Stage Name]
- [Bullet point explanation]

(continue for each stage)
```

**Mermaid conventions:**
- Use `flowchart TD` (top-down)
- Use descriptive node IDs in SCREAMING_SNAKE_CASE (e.g., `LANDING`, `APP_LOGIN`, `HOME`)
- Use `-->` for main flows, `-.->` for alternative/optional paths
- Group with `%% ─── Section Name` comments
- Add a "Flow Sections Explained" section below the diagram

**Save to:** `context_knowledge/Balance_App_Flow.md`

---

### Step 4: Opportunity Tree (`opportunity_tree.json`)

This is the most critical file. It structures all user needs into a hierarchy.

Ask the user: "What are the main areas of opportunity or need for your users? These are the big themes from your research."

Then for each theme, drill down:
1. "Under [theme], what questions do users have?" (Level 2)
2. "For each question, what specific problems do they face?" (Level 3)

**Template structure to generate:**

```json
{
  "opportunity_tree": {
    "opportunities": [
      {
        "id": "1",
        "title": "[Top-level opportunity theme]",
        "explanation": "[Why this matters to users - 2-3 sentences]",
        "children": [
          {
            "id": "1.1",
            "title": "[User question or sub-theme]",
            "explanation": "[Specific user need - 2-3 sentences]",
            "children": [
              {
                "id": "1.1.1",
                "title": "[Specific problem or pain point]",
                "explanation": "[Detailed description of the problem - 2-3 sentences]"
              },
              {
                "id": "1.1.2",
                "title": "[Another specific problem]",
                "explanation": "[Detailed description]"
              }
            ]
          },
          {
            "id": "1.2",
            "title": "[Another sub-theme]",
            "explanation": "[Description]",
            "children": [...]
          }
        ]
      },
      {
        "id": "2",
        "title": "[Second top-level theme]",
        "explanation": "[Description]",
        "children": [...]
      }
    ]
  }
}
```

**ID hierarchy rules:**
- Level 1: `"1"`, `"2"`, `"3"`, etc.
- Level 2: `"1.1"`, `"1.2"`, `"2.1"`, etc.
- Level 3: `"1.1.1"`, `"1.1.2"`, `"2.1.1"`, etc.
- Each node MUST have: `id`, `title`, `explanation`
- `children` array is optional (leaf nodes don't need it)

**Save to:** `context_knowledge/opportunity_tree.json`

---

### Step 5: Interview Summary (`interview_summary.json`)

This file maps real user evidence to opportunity tree nodes.

Ask the user:
1. "Do you have interview data already? (If yes, they can provide it or point to a CSV)"
2. "If not, we can create an empty structure that matches your opportunity tree and you'll populate it later."

**If they have data**, help them structure it. **If not**, generate an empty scaffold from the opportunity tree.

**Template structure to generate:**

```json
{
  "metadata": {
    "generated_at": "[ISO timestamp]",
    "source_csv": "[source file or 'manual_input']",
    "opportunity_tree_version": "v1.0",
    "total_opportunities": [count from opportunity_tree],
    "opportunities_with_validations": 0,
    "total_validations": 0
  },
  "opportunities": [
    {
      "id": "1",
      "title": "[Same title as opportunity_tree id 1]",
      "interview_count": 0,
      "interview_count_text": "0 interviews",
      "interview_names": [],
      "evidence": []
    },
    {
      "id": "1.1",
      "title": "[Same title as opportunity_tree id 1.1]",
      "interview_count": 0,
      "interview_count_text": "0 interviews",
      "interview_names": [],
      "evidence": []
    }
  ]
}
```

**Evidence format (when populated):**
```json
{
  "interview_name": "[Person's name]",
  "quote": "'[Direct quote from interview]'"
}
```

**Rules:**
- Every opportunity tree node MUST have a corresponding entry
- `id` and `title` must match `opportunity_tree.json` exactly
- `interview_count` = length of unique `interview_names`
- `interview_count_text` = human-readable format (e.g., "5 interviews")

**Save to:** `context_knowledge/interview_summary.json`

**Naming convention:** The file name should include the date if it's generated from real data: `YYYYMMDD_interview_summary.json`. If it's an empty scaffold, just use `interview_summary.json`.

---

### Step 6: Competitive Benchmark (`Benchmark_Balance.json`)

Ask the user about their competitive landscape:

1. "Who are your main competitors? List 5-10."
2. For each competitor:
   - "What category are they? (e.g., 'Prescription-Focused Program', 'Lifestyle & Coaching App')"
   - "What's their one-line description?"
   - "What features do they offer?" (use consistent feature keys across competitors)
   - "What are their strengths and weaknesses?"
   - "What's their pricing?"
   - "How does your product differentiate from them?"

**Template structure to generate:**

```json
{
  "benchmark": {
    "competitors": {
      "[competitor_key]": {
        "name": "[Display Name]",
        "category": "[Category]",
        "description": "[One paragraph description]",
        "features": {
          "medication": "[Yes/No/Partial - description]",
          "nutrition_fitness": "[Yes/No/Partial - description]",
          "mental_support": "[Yes/No/Partial - description]",
          "ai": "[Yes/No/Partial - description]",
          "continuous_biometrics": "[Yes/No/Partial - description]",
          "human_coach": "[Yes/No/Partial - description]",
          "maintenance_support": "[Yes/No/Partial - description]"
        },
        "strengths": [
          "[Strength 1]",
          "[Strength 2]"
        ],
        "weaknesses": [
          "[Weakness 1]",
          "[Weakness 2]"
        ],
        "pricing": "[Pricing info or 'Not specified']",
        "differentiation_vs_balance": "[How your product is different/better]"
      }
    }
  }
}
```

**Feature keys should be consistent across all competitors.** Ask the user what feature dimensions matter most for comparison.

**Save to:** `context_knowledge/Benchmark_Balance.json`

---

### Step 7: Notifications & Touchpoints (`Notifications_Touchpoints.json`)

Ask the user about their communication strategy:

1. "What stages does a user go through? (e.g., Acquisition, Activation, Retention)"
2. "For each stage, what touchpoints/notifications exist?"
3. For each touchpoint:
   - "What channel? (Email, Push, WA, SMS)"
   - "What platform/tool sends it? (SendGrid, Make, custom)"
   - "What triggers it?"
   - "What's the goal?"
   - "Who owns it? (Marketing, Product, Medical)"
   - "Is it active or paused?"

**Template structure to generate:**

```json
[
  {
    "Touchpoint Name": "[Name]",
    "Stage": "[Acquisition/Activation/Retention/etc.]",
    "Channel": "[Email/WA/Push/SMS]",
    "Tool / Platform": "[SendGrid/Make/Custom/etc.]",
    "Condition / rules": "[When this triggers or null]",
    "Trigger / Timing": "[Timing details or null]",
    "Purpose / Goal": "[What this achieves or null]",
    "Owner": "[Marketing/Tech/Product/Medical]",
    "Audience Segment": "[Leads/Subscribers/Active Users/etc.]",
    "Status": "[Active/Paused/Planned]",
    "Link": "[URL to automation or null]",
    "need a change? ": "[Yes/No]",
    "Notes": "[Any notes or null]"
  }
]
```

**Save to:** `context_knowledge/Notifications_Touchpoints.json`

---

### Step 8: Validation & Summary

After creating all files, validate:

1. **Check all files exist:**
```bash
ls -la context_knowledge/
```

2. **Validate JSON files are valid:**
```bash
python3 -c "import json; json.load(open('context_knowledge/opportunity_tree.json'))" && echo "opportunity_tree.json: Valid"
python3 -c "import json; json.load(open('context_knowledge/Benchmark_Balance.json'))" && echo "Benchmark_Balance.json: Valid"
python3 -c "import json; json.load(open('context_knowledge/Notifications_Touchpoints.json'))" && echo "Notifications_Touchpoints.json: Valid"
```

3. **Validate interview_summary matches opportunity_tree:**
```bash
python3 -c "
import json
tree = json.load(open('context_knowledge/opportunity_tree.json'))
summary_file = [f for f in __import__('os').listdir('context_knowledge/') if 'interview_summary' in f][0]
summary = json.load(open(f'context_knowledge/{summary_file}'))

# Extract all IDs from tree
def get_ids(nodes):
    ids = set()
    for n in nodes:
        ids.add(n['id'])
        if 'children' in n:
            ids.update(get_ids(n['children']))
    return ids

tree_ids = get_ids(tree['opportunity_tree']['opportunities'])
summary_ids = set(o['id'] for o in summary['opportunities'])
missing = tree_ids - summary_ids
extra = summary_ids - tree_ids
print(f'Tree IDs: {len(tree_ids)}, Summary IDs: {len(summary_ids)}')
if missing: print(f'Missing from summary: {missing}')
if extra: print(f'Extra in summary: {extra}')
if not missing and not extra: print('All IDs match!')
"
```

4. **Show summary to user:**

Present a table showing:
- File name
- Status (Created / Already existed / Skipped)
- Size (lines or entries count)

Tell the user:
- "Your context_knowledge is ready! All agents (prdDiscoveryAgent, flowDesignerAgent, frontendUIAgent, backendAgent) will now use these files to generate evidence-based feature documentation."
- "To update individual files later, use the specific update commands: `/update-vision`, `/update-persona`, `/update-app-flow`, `/update-opportunity-tree`, `/update-interview-summary`, `/update-benchmark`, `/update-notifications`."

## Important Notes

- **Ask questions ONE at a time** - Don't overwhelm the user with all questions at once
- **Be conversational** - This is a guided setup, not a form
- **Use user's words** - Reflect their language in the generated content
- **Validate as you go** - Check JSON validity after creating each JSON file
- **Don't skip steps** - Each file builds context for the next (Vision → Persona → Flow → Opportunities → Evidence → Benchmark → Notifications)
- **Save after each file** - Don't wait until the end to save everything
- **The context_knowledge/ folder is gitignored** - Remind the user these files stay local and need to be synced separately (see claude.md for sync options)

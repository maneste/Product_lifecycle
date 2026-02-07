---
description: Update the competitive benchmark data in context_knowledge
---

# Update Competitive Benchmark

You are helping the user update `/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Benchmark_Balance.json`.

## Your Task

### Step 1: Read Current Benchmark

Read the current benchmark file:

```
/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Benchmark_Balance.json
```

Present a summary:
- List all competitors with their category
- Feature dimensions being compared
- Count of competitors

### Step 2: Ask What to Update

Ask the user: "What would you like to update in the benchmark?"

**Common updates:**
1. **Add a new competitor** - Discovered a new player in the market
2. **Update competitor info** - Features, pricing, or positioning changed
3. **Remove a competitor** - No longer relevant
4. **Add feature dimensions** - New comparison criteria
5. **Update differentiation** - How your product differs has evolved
6. **Full refresh** - Re-evaluate all competitors

### Step 3: Make the Changes

**Adding a new competitor:**

Ask the user for each field:
1. "What's the competitor name?"
2. "What category? (e.g., 'Prescription-Focused Program', 'Lifestyle & Coaching App', 'Digital Therapeutics')"
3. "One-paragraph description?"
4. For each feature dimension in the existing benchmark: "Does [competitor] offer [feature]? (Yes/No/Partial - explain)"
5. "What are their 2-3 strengths?"
6. "What are their 2-3 weaknesses?"
7. "What's their pricing?"
8. "How does your product differentiate from them?"

**Competitor key format:** lowercase, underscores (e.g., `noom_core`, `yazen_health`)

**Updating existing competitor:**

Show current data and ask what to change. Use Edit tool for targeted updates.

### Step 4: Validate

After saving, validate the JSON:

```bash
python3 -c "
import json
data = json.load(open('/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Benchmark_Balance.json'))
competitors = data['benchmark']['competitors']
print(f'Valid JSON. {len(competitors)} competitors:')
for key, comp in competitors.items():
    print(f'  - {comp[\"name\"]} ({comp[\"category\"]})')
# Check feature consistency
all_features = set()
for comp in competitors.values():
    all_features.update(comp['features'].keys())
for key, comp in competitors.items():
    missing = all_features - set(comp['features'].keys())
    if missing:
        print(f'  Warning: {comp[\"name\"]} missing features: {missing}')
"
```

Remind the user: "This benchmark is used by prdDiscoveryAgent to position features relative to competitors. Updates here improve competitive analysis in PRDs."

## Structure Reference

```json
{
  "benchmark": {
    "competitors": {
      "competitor_key": {
        "name": "Display Name",
        "category": "Category",
        "description": "One paragraph",
        "features": {
          "feature_key": "Yes/No/Partial - description"
        },
        "strengths": ["Strength 1", "Strength 2"],
        "weaknesses": ["Weakness 1", "Weakness 2"],
        "pricing": "Pricing info",
        "differentiation_vs_balance": "How your product is different"
      }
    }
  }
}
```

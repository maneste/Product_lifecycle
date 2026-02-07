---
description: Update the notifications and touchpoints strategy in context_knowledge
---

# Update Notifications & Touchpoints

You are helping the user update `/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Notifications_Touchpoints.json`.

## Your Task

### Step 1: Read Current Touchpoints

Read the current file:

```
/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Notifications_Touchpoints.json
```

Present a summary:
- Group touchpoints by Stage (Acquisition, Activation, Retention, etc.)
- Count by channel (Email, WA, Push, SMS)
- Count by status (Active, Paused, Planned)
- List any marked as "need a change? Yes"

### Step 2: Ask What to Update

Ask the user: "What would you like to update in the notification touchpoints?"

**Common updates:**
1. **Add a new touchpoint** - New notification or communication
2. **Update existing touchpoint** - Change trigger, timing, status, etc.
3. **Change status** - Activate, pause, or plan a touchpoint
4. **Remove a touchpoint** - No longer needed
5. **Add a new stage** - New lifecycle stage
6. **Bulk status update** - Activate/pause multiple at once

### Step 3: Make the Changes

**Adding a new touchpoint:**

Ask the user:
1. "What's the touchpoint name?"
2. "What stage? (Acquisition/Activation/Retention/Reactivation/etc.)"
3. "What channel? (Email/WA/Push/SMS)"
4. "What tool/platform sends it?"
5. "What triggers it? (conditions/rules)"
6. "When does it fire? (timing)"
7. "What's the goal?"
8. "Who owns it? (Marketing/Tech/Product/Medical)"
9. "Who receives it? (audience segment)"
10. "Is it Active, Paused, or Planned?"

Create the entry:
```json
{
  "Touchpoint Name": "[name]",
  "Stage": "[stage]",
  "Channel": "[channel]",
  "Tool / Platform": "[tool]",
  "Condition / rules": "[conditions or null]",
  "Trigger / Timing": "[timing or null]",
  "Purpose / Goal": "[goal or null]",
  "Owner": "[owner]",
  "Audience Segment": "[segment]",
  "Status": "[status]",
  "Link": "[URL or null]",
  "need a change? ": "[Yes/No]",
  "Notes": "[notes or null]"
}
```

**Note:** Use `null` (not `"null"` or `NaN`) for empty fields in JSON.

### Step 4: Validate

After saving, validate:

```bash
python3 -c "
import json
data = json.load(open('/Users/manu/Documents/GitHub/Feature_Building/context_knowledge/Notifications_Touchpoints.json'))
stages = {}
channels = {}
statuses = {}
for tp in data:
    stage = tp.get('Stage', 'Unknown')
    channel = tp.get('Channel', 'Unknown')
    status = tp.get('Status', 'Unknown')
    stages[stage] = stages.get(stage, 0) + 1
    channels[channel] = channels.get(channel, 0) + 1
    statuses[status] = statuses.get(status, 0) + 1
print(f'Valid JSON. {len(data)} touchpoints.')
print(f'By stage: {dict(stages)}')
print(f'By channel: {dict(channels)}')
print(f'By status: {dict(statuses)}')
needs_change = [tp['Touchpoint Name'] for tp in data if tp.get('need a change? ') == 'Yes']
if needs_change:
    print(f'Need changes: {needs_change}')
"
```

Remind the user: "This touchpoints data helps agents understand the communication strategy when designing features that involve notifications or user engagement."

## Structure Reference

The file is a JSON array of touchpoint objects:

```json
[
  {
    "Touchpoint Name": "Welcome to Balance",
    "Stage": "Activation",
    "Channel": "Email",
    "Tool / Platform": "Sendgrid",
    "Condition / rules": "When user subscribes",
    "Trigger / Timing": "Instantly",
    "Purpose / Goal": "Welcome and onboard",
    "Owner": "Marketing",
    "Audience Segment": "New Subscribers",
    "Status": "Active",
    "Link": "https://...",
    "need a change? ": "No",
    "Notes": null
  }
]
```

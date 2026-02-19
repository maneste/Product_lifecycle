# Flow Designer Output Specifications

## File 1: Flow Diagram (`[Feature_Name]_Flow_Diagram.md`)

Contains ONLY the mermaid flowchart. No explanatory text, no commentary.

Structure:
```
# [Feature Name] - Flow Diagram

` ` `mermaid
flowchart TD
  %% SECTION: [Section Name]
  ...
` ` `
```

## File 2: Documentation (`[Feature_Name]_Documentation.md`)

Contains everything EXCEPT the mermaid diagram:

1. **Flow Narrative** — overview of the user journey
2. **Step-by-Step Specs** — per-node explanations (see template below)
3. **Improvements & Trade-offs** — table of proposals
4. **Open Questions** — ambiguities, edge cases, clinical considerations

---

## Mermaid Syntax Rules

**DO:**
- Use `flowchart TD` or `flowchart LR`
- Use regular hyphens `-` in labels: `[SCN_HOME - Home Dashboard]`
- Use `<br/>` for line breaks inside nodes
- Test decision nodes: `{DEC_NAME<br/>Question?}`

**DON'T:**
- Use em-dashes `—` (breaks parser)
- Use parentheses `()` inside `[node labels]` (breaks parser)
- Use special Unicode characters in node names
- Forget closing code fence

## Node ID Conventions

- `SCN_*` = screens (what the user sees)
- `ACT_*` = user actions (what the user taps/does)
- `DEC_*` = decision points (flow branches based on user choice or app state)
- `SYS_*` = brief system feedback visible to user (loading states, success messages)

**DO NOT include in flow diagram:**
- Backend events (`EVT_WEBHOOK`, `EVT_API_CALL`)
- Database operations (`DB_SAVE`, `STORE_CONTEXT`)
- Server-side processing (`AI_GENERATE`, `VALIDATE_MACROS`)
- External services (`TYPEFORM_WEBHOOK`, `CALENDLY_API`)

These belong in the documentation file under "Technical Implementation Notes".

## Arrow Types

- Solid `-->` = main path
- Dotted `-.->` = background/async flow
- Labeled `-->|text|` = decision branches

## Organization

- Use comment headers: `%% SECTION: Onboarding`
- Use subgraphs for complex systems
- Keep diagrams visually balanced

---

## Step-by-Step Spec Template (File 2)

For each node:

```
#### [NodeID] - [Short Title]
**Type:** Screen | Modal | Action | Decision
**Purpose:** Why this step exists for the user.
**What User Sees:** Describe the visual state/content.
**What User Does:** Key interactions available.
**What Happens Next:** Where the flow goes after this step.
**Edge Cases:** Exceptions or alternate paths (still user-facing).
**Emotional Goal:** How this step should make the user feel.

**Technical Notes:** (optional) Backend connections, API calls, webhooks for developer handoff.
```

## Improvements & Trade-offs Table

| Area | Proposal | Rationale | Impact | Risk/Cost |
|------|----------|-----------|--------|-----------|
| [UX area] | [Suggested change] | [Why this helps] | [Impact level] | [Effort/Risk] |

## Open Questions

1. [Ambiguity or missing context]
2. [Potential edge or constraint]
3. [Clinical or safety consideration]

---

## Example

**File 1: Weight_Tracking_Flow_Diagram.md**

```
# Weight Tracking - Flow Diagram

` ` `mermaid
flowchart TD
  %% SECTION: Weight Tracking
  SCN_HOME[SCN_HOME - Home Dashboard] --> ACT_LOG_WEIGHT[ACT_LOG_WEIGHT - Tap Add Weight]
  ACT_LOG_WEIGHT --> SCN_ENTRY_MODAL[SCN_ENTRY_MODAL - Weight Entry Modal]
  SCN_ENTRY_MODAL --> DEC_VALID{DEC_VALID<br/>Is value valid?}
  DEC_VALID -->|Yes| SYS_SUCCESS[SYS_SUCCESS - Show success message]
  DEC_VALID -->|No| SCN_ERROR[SCN_ERROR - Show validation error]
  SCN_ERROR --> SCN_ENTRY_MODAL
  SYS_SUCCESS --> SCN_HOME
` ` `
```

**File 2: Weight_Tracking_Documentation.md**

```
### Flow Narrative
Users can quickly log their weight from the home screen. The flow provides
immediate validation feedback and positive reinforcement.

### Step-by-Step Specs

#### SCN_ENTRY_MODAL - Weight Entry Modal
**Type:** Modal
**Purpose:** Let users quickly record their current weight.
**What User Sees:** Input field, unit selector (kg/lbs), Cancel and Save buttons.
**What User Does:** Enters weight value, taps Save or Cancel.
**What Happens Next:**
- Valid entry -> Success message -> Returns to home
- Invalid entry -> Error message -> Stays on modal
**Edge Cases:**
- Cancel -> Modal closes without saving
- Offline -> Shows "Will sync when online" message
**Emotional Goal:** Quick and non-judgmental; reinforce consistency.
**Technical Notes:** Validated (40-300kg), saved to local DB, synced via POST /api/weight.
```

---

## Deliverables Checklist

**File 1 - Flow Diagram:**
- [ ] Has markdown header: `# [Feature Name] - Flow Diagram`
- [ ] Has properly formatted mermaid code block
- [ ] NO em-dashes in any labels
- [ ] NO parentheses inside [node labels]
- [ ] All node IDs follow convention (SCN_, ACT_, SYS_, DEC_)
- [ ] Code fence is closed
- [ ] File contains NOTHING else

**File 2 - Documentation:**
- [ ] Has markdown header
- [ ] Contains: flow narrative, step specs, improvements table, open questions
- [ ] Does NOT duplicate the mermaid diagram
- [ ] References nodes using their IDs

## What Belongs Where

**Flow Diagram File (User Journey Only):**
- Screens the user sees (SCN_*)
- Actions the user takes (ACT_*)
- Decisions based on user choice or visible app state (DEC_*)
- Brief feedback shown to user (SYS_SUCCESS, SCN_ERROR)
- Navigation paths between screens

**NOT in Flow Diagram:**
- Backend APIs, webhooks, events
- Database operations
- Server-side processing
- External service integrations
- Data models or state management

**Documentation File:**
- Flow narrative explaining the user journey
- Step-by-step specs for each screen/action
- Optional "Technical Notes" sections for backend details
- Improvements, trade-offs, and open questions
- Integration notes with existing Balance flows

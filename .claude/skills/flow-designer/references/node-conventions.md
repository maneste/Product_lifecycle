# Flow Designer — Node Conventions

## Node Types

| Prefix | Type | Meaning | Color |
|--------|------|---------|-------|
| `SCN_` | Screen | A screen or modal the user sees | `5` (cyan) |
| `ACT_` | Action | Something the user actively does (tap, swipe, type, submit) | `4` (green) |
| `DEC_` | Decision | A branch point — flow splits based on user choice or visible app state | `3` (yellow) |
| `SYS_` | System | Brief system feedback visible to the user (loading, success, error message) | `6` (purple) |

## Obsidian Color Reference

| Code | Color |
|------|-------|
| `1`  | Red |
| `2`  | Orange |
| `3`  | Yellow |
| `4`  | Green |
| `5`  | Cyan |
| `6`  | Purple |

No color field = default (gray/white depending on theme).

---

## Naming Rules

- All node IDs are `UPPERCASE_SNAKE_CASE`
- Format: `PREFIX_DESCRIPTIVE_NAME`
- Be specific — name describes exactly what the user sees or does

**Examples:**
```
SCN_HOME               ✅  Home screen
SCN_ONBOARDING_STEP2   ✅  Second onboarding screen
ACT_TAP_SUBMIT         ✅  User taps submit button
ACT_SWIPE_DISMISS      ✅  User swipes to dismiss
DEC_HAS_ACCOUNT        ✅  Decision: does user have an account?
DEC_FORM_VALID         ✅  Decision: is form input valid?
SYS_LOADING            ✅  Loading spinner shown
SYS_SUCCESS_TOAST      ✅  Success confirmation shown
```

**Avoid:**
```
SCN_1                  ❌  Not descriptive
ACTION_1               ❌  Wrong prefix format
BUTTON_SUBMIT          ❌  Describes a UI element, not a user action
BACKEND_CALL           ❌  Backend — does not belong in the canvas
```

---

## Node Text Format

The `text` field in the canvas JSON combines the ID and a human-readable label:

```
"SCN_HOME - Home Screen"
"ACT_TAP_SUBMIT - Tap Submit Button"
"DEC_HAS_ACCOUNT - Has existing account?"
"SYS_LOADING - Loading spinner"
```

---

## Decision Nodes (DEC_)

Decision nodes always have **at least 2 outgoing edges**, each with a label:

```json
{ "fromNode": "DEC_HAS_ACCOUNT", "toNode": "SCN_DASHBOARD", "label": "Yes" },
{ "fromNode": "DEC_HAS_ACCOUNT", "toNode": "SCN_SIGNUP",    "label": "No"  }
```

Label values should be concise and exhaustive:
- Binary: `"Yes"` / `"No"` or `"Valid"` / `"Invalid"`
- Multi-path: `"Option A"` / `"Option B"` / `"Skip"`
- Conditional: `"First time"` / `"Returning user"`

---

## What Does NOT Belong in the Canvas

These node types should never appear:

| What | Example | Where it belongs |
|------|---------|-----------------|
| API calls | `API_SUBMIT_FORM` | Documentation — Technical Notes |
| Database ops | `DB_SAVE_USER` | Documentation — Technical Notes |
| Backend events | `EVT_WEBHOOK_RECEIVED` | Documentation — Technical Notes |
| External services | `STRIPE_CHECKOUT` | Documentation — Technical Notes |
| Server processing | `AI_GENERATE_PLAN` | Documentation — Technical Notes |

The canvas is the user's world only. Everything else lives in the Documentation file.

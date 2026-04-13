# Incremental Change Templates

Templates and rules for adding modifications to an existing prototype.

---

## v[X.Y]-modifications.md

```markdown
# V[X.Y] Modifications — [Feature_Name]

Builds on top of [list all previous modification files]. Apply all files together.

---

## 1. [Change title]

[Clear description of what changes and why]

### Layout / Visual

[Exact CSS properties using design tokens from prototype-config.md — colors, dimensions, flex rules]

### Behavior / Interactions

[State changes, triggers, conditions, edge cases]

### TypeScript interface changes (if any)

[New fields, updated interfaces, mock data additions]

### Visibility rules (if applicable)

| State | [Element] visible? |
|-------|-------------------|
| `state-a` | ✅/❌ |
| `state-b` | ✅/❌ |
| … |

### Layout impact (if adding UI elements)

[Estimate new dimensions, confirm stays within constraints defined in prototype-config.md]

---

## [N+1]. Update apply order in changelog
```

---

## Changelog entry format

Insert before "Pending / Not yet built" in `prototype-changelog.md`:

```markdown
---

## V[X.Y] Modifications — Batch [N]
**File:** `v[X.Y]-modifications.md`

### Changes
1. **[Change name]** — [one-line summary]
```

Also update the apply order line:

```
Apply order: prototype-spec-v1.md → v1.1-modifications.md → … → v[X.Y]-modifications.md
```

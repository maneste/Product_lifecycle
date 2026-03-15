---
description: Check if this project is up to date with the Product_lifecycle template. Shows current version, latest version, and what changed in between.
---

# Template Status

Shows how far behind (or ahead) this project is from the local Product_lifecycle template.

---

## Step 1 — Read current state

```bash
ls .copier-answers.yml 2>/dev/null || echo "ERROR: .copier-answers.yml not found — run /init-project first"
cat .copier-answers.yml
```

Extract:
- `_commit` → current template version this project is on
- `product_name`, `product_slug`

---

## Step 2 — Get latest template version

```bash
git -C ../Product_lifecycle describe --tags --abbrev=0 2>/dev/null || echo "none"
```

If `../Product_lifecycle` is not found, ask the user for the correct local path.

---

## Step 3 — Compare and report

If current == latest:
> "✅ Up to date — you're on the latest template version (`[version]`)."

If current < latest:
> "⚠️ Your project is on `[current]`. The latest template version is `[latest]`.
> Run `/productlifecycle-update` to sync."

Show what's missing by reading the local CHANGELOG:

```bash
CURRENT=$(grep '_commit:' .copier-answers.yml | awk '{print $2}')
LATEST=$(git -C ../Product_lifecycle describe --tags --abbrev=0)
awk "/## \[$LATEST\]/,/## \[$CURRENT\]/" ../Product_lifecycle/CHANGELOG.md | grep -v "## \[$CURRENT\]"
```

Format output as:
```
Template status for [product_name]
──────────────────────────────────
Your version  : v1.0.0
Latest version: v1.2.0
Versions behind: 2

What you're missing:
  [CHANGELOG entries between versions]

Run /productlifecycle-update to apply these changes.
```

---

## Step 4 — Check for local contributions not yet sent

Compare `.claude/` files against `../Product_lifecycle/.claude/`:

```bash
# New files (in project but not in template)
find .claude -type f | while read f; do
  [ ! -f "../Product_lifecycle/$f" ] && echo "NEW: $f"
done

# Modified files (differ from template)
find .claude -type f | while read f; do
  [ -f "../Product_lifecycle/$f" ] && ! diff -q "$f" "../Product_lifecycle/$f" > /dev/null 2>&1 && echo "MODIFIED: $f"
done
```

If changes found:
```
Local changes not yet contributed to template:
  + .claude/skills/my-new-skill/SKILL.md   (new)
  ~ .claude/skills/prd/SKILL.md            (modified)

Run /contribute-productlifecycle to send these back.
```

If no changes: "No local `.claude/` changes detected."

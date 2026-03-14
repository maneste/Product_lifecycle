---
description: Check if this project is up to date with the Product_lifecycle template. Shows current version, latest version, and what changed in between.
---

# Template Status

Shows how far behind (or ahead) this project is from the Product_lifecycle template.

---

## Step 1 — Read current state

```bash
ls .copier-answers.yml 2>/dev/null || echo "ERROR: .copier-answers.yml not found — run /init-project first"
cat .copier-answers.yml
```

Extract:
- `_commit` → current template version this project is on
- `_src_path` → template repo URL
- `product_name`, `product_slug`

---

## Step 2 — Get latest template version

```bash
git ls-remote --tags https://github.com/manu/Product_lifecycle \
  | grep -v '{}' \
  | awk '{print $2}' \
  | sed 's|refs/tags/||' \
  | sort -V \
  | tail -1
```

---

## Step 3 — Compare and report

If current == latest:
> "✅ Up to date — you're on the latest template version (`[version]`)."

If current < latest:
> "⚠️ Your project is on `[current]`. The latest template version is `[latest]`.
> Run `/productlifecycle-update` to sync."

Then fetch and display the CHANGELOG between both versions:

```bash
curl -s https://raw.githubusercontent.com/manu/Product_lifecycle/main/CHANGELOG.md \
  | awk "/## \[$LATEST\]/,/## \[$CURRENT\]/{print}" \
  | grep -v "## \[$CURRENT\]"
```

Format the output as:
```
Template status for [product_name]
──────────────────────────────────
Your version  : v1.0.0
Latest version: v1.2.0
Versions behind: 2

What you're missing:
  v1.2.0 — [summary from CHANGELOG]
  v1.1.0 — [summary from CHANGELOG]

Run /productlifecycle-update to apply these changes.
```

---

## Step 4 — Check for local contributions not yet sent

Run the same file comparison logic as `/contribute-productlifecycle` Step 2, but only report — don't offer to contribute:

```
Local changes not yet contributed to template:
  + .claude/skills/my-new-skill/SKILL.md   (new)
  ~ .claude/skills/prd/SKILL.md            (modified)

Run /contribute-productlifecycle to send these back.
```

If no local changes: "No local `.claude/` changes detected."

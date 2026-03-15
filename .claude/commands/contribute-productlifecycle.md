---
description: Contribute a new or improved skill, agent, or command from this project back to Product_lifecycle. Handles generalization, writes files, updates CHANGELOG, tags, and pushes — all without leaving this project.
---

# Contribute to Product Lifecycle

Contributes improvements from this project's `.claude/` directly to the local Product_lifecycle — including the release. You don't need to open Product_lifecycle at all.

---

## Step 1 — Verify preconditions

```bash
# Must be a derived project, not Product_lifecycle itself
ls copier.yml 2>/dev/null && echo "ERROR: you are inside Product_lifecycle — use /release instead"

# Must have Copier tracking
ls .copier-answers.yml 2>/dev/null || echo "ERROR: run /init-project first"

# Product_lifecycle must exist locally
ls ../Product_lifecycle/copier.yml 2>/dev/null || echo "ERROR: Product_lifecycle not found at ../Product_lifecycle"

# Working tree must be clean
git status --short
```

If `../Product_lifecycle` is not found, ask the user for the correct local path.
Read `.copier-answers.yml` to extract `product_name` and `product_slug`.

---

## Step 2 — Detect what has changed in .claude/

Compare directly against `../Product_lifecycle/.claude/`:

```bash
# New files (in this project but not in template)
echo "=== NEW FILES ==="
find .claude -type f | while read f; do
  [ ! -f "../Product_lifecycle/$f" ] && echo "  + $f"
done

# Modified files (exist in both but differ)
echo "=== MODIFIED FILES ==="
find .claude -type f | while read f; do
  [ -f "../Product_lifecycle/$f" ] && ! diff -q "$f" "../Product_lifecycle/$f" > /dev/null 2>&1 && echo "  ~ $f"
done
```

If both lists are empty: "No changes detected in `.claude/`. Nothing to contribute."

---

## Step 3 — Select what to contribute

Present the two lists and ask which files to contribute.

For each selected file, confirm: "Is `[filename]` a generic improvement useful for any project, or specific to [product_name]?"

Only proceed with files confirmed as generic or generalizable.

---

## Step 4 — Generalize content

For each selected file, replace project-specific strings:

- `product_name` value → `[Product]`
- `product_slug` value → `[product_slug]`

Show the before/after diff and ask: "Anything else to replace before contributing?"

---

## Step 5 — Write files to Product_lifecycle

Write each generalized file directly to `../Product_lifecycle/` using the Write tool.

Confirm what was written:
```
Written to ../Product_lifecycle:
  + .claude/skills/my-new-skill/SKILL.md   (new)
  ~ .claude/skills/prd/SKILL.md            (updated)
```

---

## Step 6 — Determine version bump

Ask the user:
> "What type of release is this?
> - **patch** — fixes or wording improvements to existing skills
> - **minor** — new skills, agents, or commands
> - **major** — breaking changes (renamed files, restructured directories)"

Calculate next version:

```bash
git -C ../Product_lifecycle describe --tags --abbrev=0 2>/dev/null || echo "none"
```

---

## Step 7 — Write CHANGELOG entry in Product_lifecycle

Read `../Product_lifecycle/CHANGELOG.md` and write a new entry below `## [Unreleased]`:

```markdown
## [vX.Y.Z] — YYYY-MM-DD

### Added / Changed / Fixed
- `skill-name`: [what changed and why, in generic terms]
```

Use the Write tool to update `../Product_lifecycle/CHANGELOG.md`.

---

## Step 8 — Commit, tag, and push Product_lifecycle

```bash
git -C ../Product_lifecycle add .
git -C ../Product_lifecycle commit -m "chore: release vX.Y.Z"
git -C ../Product_lifecycle tag -a vX.Y.Z -m "vX.Y.Z"
git -C ../Product_lifecycle push origin main --tags
```

Show the commands and ask for confirmation before running.

---

## Step 9 — Update .copier-answers.yml in this project

```bash
sed -i '' 's/_commit: .*/_commit: vX.Y.Z/' .copier-answers.yml
git add .copier-answers.yml
git commit -m "chore: update template tracking to vX.Y.Z"
```

---

## Step 10 — Confirm

Tell the user:
- What was contributed and to which files
- New Product_lifecycle version: `vX.Y.Z`
- This project is now tracking `vX.Y.Z`
- Other derived projects can now run `/productlifecycle-update` to receive these changes

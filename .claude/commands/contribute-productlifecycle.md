---
description: Contribute a new or improved skill, agent, or command from this project back to Product_lifecycle. Handles generalization, writes files, updates CHANGELOG, tags, and pushes — all without leaving this project.
---

# Contribute to Product Lifecycle

Contributes improvements from this project's `.claude/` directly to Product_lifecycle — including the release. You don't need to open Product_lifecycle at all.

---

## Step 1 — Verify preconditions

```bash
# Must be a derived project, not Product_lifecycle itself
ls copier.yml 2>/dev/null && echo "ERROR: you are inside Product_lifecycle — use /release instead"

# Must have Copier tracking
ls .copier-answers.yml 2>/dev/null || echo "ERROR: run /init-project first"

# Working tree must be clean
git status --short
```

Read `.copier-answers.yml` to extract `product_name`, `product_slug`, `_src_path`.

Find Product_lifecycle locally:

```bash
# Try common sibling path first
ls ../Product_lifecycle/copier.yml 2>/dev/null && echo "Found at ../Product_lifecycle" || echo "Not found at default path"
```

If not found at `../Product_lifecycle`, ask the user for the local path.

---

## Step 2 — Detect what has changed in .claude/

Compare current `.claude/` against the template version stored in `_commit`:

```bash
TEMPLATE_DIR=$(mktemp -d)
git clone --quiet --branch $(grep '_commit:' .copier-answers.yml | awk '{print $2}') \
  $(grep '_src_path:' .copier-answers.yml | awk '{print $2}') $TEMPLATE_DIR 2>/dev/null || \
git clone --quiet $(grep '_src_path:' .copier-answers.yml | awk '{print $2}') $TEMPLATE_DIR

# New files
find .claude -type f | while read f; do
  [ ! -f "$TEMPLATE_DIR/$f" ] && echo "NEW: $f"
done

# Modified files
find .claude -type f | while read f; do
  [ -f "$TEMPLATE_DIR/$f" ] && ! diff -q "$f" "$TEMPLATE_DIR/$f" > /dev/null 2>&1 && echo "MODIFIED: $f"
done

rm -rf $TEMPLATE_DIR
```

If nothing changed: "No changes detected in `.claude/` since the last template sync. Nothing to contribute."

---

## Step 3 — Select what to contribute

Present the two lists (new files, modified files) and ask the user which ones to contribute.

For each selected file, confirm: "Is `[filename]` a generic improvement useful for any project, or specific to [product_name]?"

Only proceed with files confirmed as generic or generalizable.

---

## Step 4 — Generalize content

For each selected file, replace project-specific strings using values from `.copier-answers.yml`:

- `product_name` value → `[Product]`
- `product_slug` value → `[product_slug]`

Show the before/after diff and ask: "Anything else to replace before contributing?"

---

## Step 5 — Write files to Product_lifecycle

Write each generalized file directly to the Product_lifecycle repo using the Write tool.

```
[product_lifecycle_path]/.claude/skills/my-skill/SKILL.md
[product_lifecycle_path]/.claude/commands/my-command.md
etc.
```

Confirm what was written:
```
Written to Product_lifecycle:
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

Calculate the next version from the latest tag in Product_lifecycle:

```bash
git -C [product_lifecycle_path] describe --tags --abbrev=0 2>/dev/null || echo "none"
```

---

## Step 7 — Write CHANGELOG entry in Product_lifecycle

Read `[product_lifecycle_path]/CHANGELOG.md`.

Write a new entry below `## [Unreleased]`:

```markdown
## [vX.Y.Z] — YYYY-MM-DD

### Added / Changed / Fixed
- `skill-name`: [what changed and why, in generic terms]
```

Use the Write tool to update the file.

---

## Step 8 — Commit, tag, and push Product_lifecycle

```bash
cd [product_lifecycle_path]

git add .
git commit -m "chore: release vX.Y.Z"
git tag -a vX.Y.Z -m "vX.Y.Z"
git push origin main --tags
```

Show the commands and ask for confirmation before running.

---

## Step 9 — Update .copier-answers.yml in this project

Update `_commit` to the new version:

```bash
sed -i '' 's/_commit: .*/_commit: vX.Y.Z/' .copier-answers.yml
```

Commit:

```bash
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

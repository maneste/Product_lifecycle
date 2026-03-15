---
description: Sync the latest improvements from Product_lifecycle template into this project. Explains what changed and helps resolve conflicts.
---

# Product Lifecycle Update

Brings the latest skills, agents, and commands from the local Product_lifecycle template into this project.

---

## Step 1 — Verify preconditions

```bash
# Must have Copier tracking set up
ls .copier-answers.yml 2>/dev/null || echo "ERROR: .copier-answers.yml not found — run /init-project first"

# Product_lifecycle must exist at sibling path
ls ../Product_lifecycle/copier.yml 2>/dev/null || echo "ERROR: Product_lifecycle not found at ../Product_lifecycle"

# Working tree must be clean
git status --short
```

If `.copier-answers.yml` is missing, stop: "Run `/init-project` first."
If `../Product_lifecycle` is not found, ask the user for the correct local path.
If there are uncommitted changes, stop: "Commit or stash your changes before updating."

---

## Step 2 — Show what's changed in the template

```bash
CURRENT=$(grep '_commit:' .copier-answers.yml | awk '{print $2}')
LATEST=$(git -C ../Product_lifecycle describe --tags --abbrev=0 2>/dev/null || echo "none")
echo "Your version : $CURRENT"
echo "Latest       : $LATEST"
```

If `$CURRENT == $LATEST`, tell the user and stop: "You're already on the latest template version ($LATEST). Nothing to update."

Show what changed by reading the local CHANGELOG:

```bash
awk "/## \[$LATEST\]/,/## \[$CURRENT\]/" ../Product_lifecycle/CHANGELOG.md | grep -v "## \[$CURRENT\]"
```

Ask the user: "These changes will be merged into your project. Continue?"

---

## Step 3 — Run copier update

```bash
copier update --trust --defaults
```

If `copier` is not installed:
```bash
pip install copier && copier update --trust --defaults
```

Copier reads `_src_path` from `.copier-answers.yml` — since it points to `../Product_lifecycle`, it works entirely locally with no network needed.

---

## Step 4 — Handle conflicts

Scan for conflict markers:

```bash
grep -rl "<<<<<<" .claude/ claude.md 2>/dev/null
```

For each file with conflicts:
- Lines between `<<<<<<< UPDATED` and `=======` → new template version
- Lines between `=======` and `>>>>>>> CURRENT` → your version

Guide the user through each conflict:
> "In `[filename]`, the template changed [section]. Your version has [description]. Which do you want to keep?"

After resolving:

```bash
git add .
git commit -m "chore: sync template $LATEST"
```

---

## Step 5 — Confirm

Tell the user:
- Updated from `$CURRENT` → `$LATEST`
- Files that changed cleanly
- Files that had conflicts and how they were resolved
- If major version bump: "Check that your project-specific skills still work as expected."

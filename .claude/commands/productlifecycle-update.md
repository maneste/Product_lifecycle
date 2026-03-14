---
description: Sync the latest improvements from Product_lifecycle template into this project. Runs copier update, explains what changed, and helps resolve conflicts.
---

# Product Lifecycle Update

Brings the latest skills, agents, and commands from the Product_lifecycle template into this project.

---

## Step 1 — Verify preconditions

```bash
# Must have Copier tracking set up
ls .copier-answers.yml 2>/dev/null || echo "ERROR: .copier-answers.yml not found — run /init-project first"

# Working tree must be clean
git status --short
```

If `.copier-answers.yml` is missing, stop: "Run `/init-project` first to set up template tracking."
If there are uncommitted changes, stop: "Commit or stash your changes before updating."

---

## Step 2 — Show what's changed in the template

Read `.copier-answers.yml` to get the current version (`_commit`) and template URL (`_src_path`).

```bash
# Get latest version from template
LATEST=$(git ls-remote --tags https://github.com/manu/Product_lifecycle | grep -v '{}' | awk '{print $2}' | sed 's|refs/tags/||' | sort -V | tail -1)
CURRENT=$(grep '_commit:' .copier-answers.yml | awk '{print $2}')
echo "Your version : $CURRENT"
echo "Latest       : $LATEST"
```

If already on latest version, tell the user and stop: "You're already on the latest template version ($LATEST). Nothing to update."

Fetch and display the relevant CHANGELOG sections between `$CURRENT` and `$LATEST`:

```bash
curl -s https://raw.githubusercontent.com/manu/Product_lifecycle/main/CHANGELOG.md | \
  awk "/## \[$LATEST\]/,/## \[$CURRENT\]/" | head -60
```

Ask the user: "These changes will be merged into your project. Continue?"

---

## Step 3 — Run copier update

```bash
copier update --trust
```

If `copier` is not installed:
```bash
pip install copier
copier update --trust
```

---

## Step 4 — Handle conflicts

If the update produces conflict markers, scan for them:

```bash
grep -rl "<<<<<<" .claude/ claude.md 2>/dev/null
```

For each file with conflicts, explain what happened:
- Lines between `<<<<<<< UPDATED` and `=======` are the **new template version**
- Lines between `=======` and `>>>>>>> CURRENT` are **your version**

Guide the user through each conflict:
> "In `[filename]`, the template changed [section]. Your version has [description]. Which do you want to keep — the template version, yours, or a combination?"

After resolving all conflicts:

```bash
git add .
git commit -m "chore: sync template [LATEST version]"
```

---

## Step 5 — Confirm

Tell the user:
- Updated from `$CURRENT` → `$LATEST`
- List of files that changed (clean merges)
- List of files that had conflicts and how they were resolved
- If this was a major version bump, warn: "Check that your project-specific skills still work as expected."

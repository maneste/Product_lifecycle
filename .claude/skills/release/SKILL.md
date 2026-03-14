---
name: release
description: Release a new version of the Product_lifecycle template. Guides through changelog, version bump, git tag, and push. Only run from inside the Product_lifecycle repo.
---

# Product_lifecycle Release Workflow

This skill manages releases of the Product_lifecycle template. Every release:
1. Documents what changed in `CHANGELOG.md`
2. Creates a git tag (`v1.2.3`)
3. Pushes the tag so derived projects can `copier update` to the new version

---

## Step 1 — Verify preconditions

Run these checks before anything else:

```bash
# Must be in Product_lifecycle
ls copier.yml 2>/dev/null || echo "ERROR: not in Product_lifecycle — stop here"

# Working tree must be clean
git status --short
```

If there are uncommitted changes, stop and tell the user: "Commit or stash all changes before releasing."

---

## Step 2 — Show what changed since last release

```bash
# Get current version
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "none")
echo "Current version: $LAST_TAG"
echo ""

# Show commits since last tag
if [ "$LAST_TAG" = "none" ]; then
  git log --oneline
else
  git log ${LAST_TAG}..HEAD --oneline
fi
```

Present the commit list to the user and ask:

> "Based on these commits, what type of release is this?
> - **patch** (v1.0.X) — bug fixes, wording improvements, small tweaks to existing skills
> - **minor** (v1.X.0) — new skills, new agents, new commands, backwards-compatible changes
> - **major** (vX.0.0) — breaking changes (renamed files, changed copier.yml variables, restructured directories)"

---

## Step 3 — Calculate next version

Given the current tag and the user's choice, calculate the new version:

| Current | patch | minor | major |
|---------|-------|-------|-------|
| none | — | — | `v1.0.0` (first release) |
| v1.2.3 | v1.2.4 | v1.3.0 | v2.0.0 |
| v1.2.3 | v1.2.4 | v1.3.0 | v2.0.0 |

Confirm with the user: "Next version will be **vX.Y.Z** — proceed?"

---

## Step 4 — Write CHANGELOG entry

Read `CHANGELOG.md`. Find the `## [Unreleased]` section (or insert one at the top if it doesn't exist).

Ask the user: "Give me a one-line summary per change, or I'll generate them from the commits."

If generating from commits, group them:
- **Added** — new skills, agents, commands, features
- **Changed** — modifications to existing skills or agents
- **Fixed** — bug fixes, corrections
- **Removed** — deleted files or deprecated features

Write the new entry in this format:

```markdown
## [vX.Y.Z] — YYYY-MM-DD

### Added
- New `skill-name` skill for [purpose]

### Changed
- `prd/SKILL.md`: improved [what and why]

### Fixed
- `update-opportunity-tree`: fixed [what]
```

Insert it **below** `## [Unreleased]` (or at the top of the changelog if no Unreleased section exists).

---

## Step 5 — Commit changelog + create tag

```bash
# Commit the changelog
git add CHANGELOG.md
git commit -m "chore: release vX.Y.Z"

# Create annotated tag
git tag -a vX.Y.Z -m "vX.Y.Z"

# Push commit and tag together
git push origin main --tags
```

Show the exact commands before running them and ask for confirmation.

---

## Step 6 — Confirm and summarise

After pushing:

```bash
git describe --tags --abbrev=0
```

Tell the user:
- The new version tag (e.g., `v1.3.0`)
- How derived projects can update: `copier update` from inside their repo
- Whether this is a breaking change (major bump) — if so, warn that projects may have conflicts on update

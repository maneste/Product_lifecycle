---
description: Initialize a new project created from the Product_lifecycle GitHub template. Sets up Copier tracking so future template updates can be synced with /productlifecycle-update.
---

# Init Project

Run this **once**, immediately after creating a new project from the Product_lifecycle GitHub template.

## What this does

1. Asks for product name and slug
2. Replaces `[Product]` placeholders in `claude.md`
3. Creates `.copier-answers.yml` so future syncs work
4. Commits both files

---

## Step 1 — Check preconditions

```bash
# Confirm we're NOT inside Product_lifecycle itself
ls copier.yml 2>/dev/null && echo "ERROR: run this from the derived project, not from Product_lifecycle" || echo "OK"

# Check if already initialised
ls .copier-answers.yml 2>/dev/null && echo "WARN: already initialised" || echo "OK: not yet initialised"

# Confirm Product_lifecycle is accessible locally
ls ../Product_lifecycle/copier.yml 2>/dev/null && echo "Product_lifecycle found at ../Product_lifecycle" || echo "WARN: not found at ../Product_lifecycle"
```

If `.copier-answers.yml` already exists, stop: "This project is already initialised. Run `/productlifecycle-update` to sync the latest changes."
If `../Product_lifecycle` is not found, ask the user for the correct local path.

---

## Step 2 — Ask for project details

Ask the user:

1. **Product name** — human-readable (e.g., `Balance`, `RaudaAI`, `WellNest`)
2. **Product slug** — lowercase with underscores (e.g., `balance`, `rauda_ai`); suggest a default derived from the product name

Confirm: "I'll set up this project as **[product_name]** (`[product_slug]`). Continue?"

---

## Step 3 — Get current template version

```bash
git -C ../Product_lifecycle describe --tags --abbrev=0 2>/dev/null || echo "v1.0.0"
```

If no tags exist yet, use `v1.0.0` and tell the user.

---

## Step 4 — Replace [Product] placeholders in claude.md

```bash
python3 -c "
content = open('claude.md').read()
content = content.replace('[Product]', 'PRODUCT_NAME')
content = content.replace('[product_slug]', 'PRODUCT_SLUG')
open('claude.md', 'w').write(content)
print('claude.md updated.')
"
```

Replace `PRODUCT_NAME` and `PRODUCT_SLUG` with the actual values from Step 2 before running.

---

## Step 5 — Create .copier-answers.yml

Write this file to the project root:

```yaml
# Tracks which version of Product_lifecycle this project was created from.
# Required for /productlifecycle-update to sync future template improvements.
# Do not edit manually.
_commit: [version_from_step_3]
_src_path: ../Product_lifecycle
product_name: [product_name]
product_slug: [product_slug]
```

The `_src_path: ../Product_lifecycle` points to the local template — no network needed for syncs.

---

## Step 6 — Commit

```bash
git add claude.md .copier-answers.yml
git commit -m "chore: init project from Product_lifecycle template [version]"
```

---

## Step 7 — Confirm

Tell the user:
- Project is now tracked as **[product_name]** on template version **[version]**
- To sync future improvements: run `/productlifecycle-update`
- Next step: run `/init-context` to create the `context_knowledge/` files

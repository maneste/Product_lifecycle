---
description: Initialize a new project created from the Product_lifecycle GitHub template. Sets up Copier tracking so future template updates can be synced with `copier update`.
---

# Init Project

Run this **once**, immediately after creating a new project from the Product_lifecycle GitHub template.

## What this does

1. Asks for product name and slug
2. Replaces `[Product]` placeholders in `claude.md`
3. Creates `.copier-answers.yml` so `copier update` works in the future
4. Commits both files

---

## Step 1 — Check preconditions

```bash
# Confirm we're NOT inside Product_lifecycle itself
ls copier.yml 2>/dev/null && echo "ERROR: run this from the derived project, not from Product_lifecycle" || echo "OK"

# Check if already initialised
ls .copier-answers.yml 2>/dev/null && echo "WARN: .copier-answers.yml already exists — already initialised?" || echo "OK: not yet initialised"
```

If `.copier-answers.yml` already exists, stop and tell the user: "This project is already initialised. Run `copier update` to sync the latest template changes."

---

## Step 2 — Ask for project details

Ask the user:

1. **Product name** — the human-readable name (e.g., `Balance`, `RaudaAI`, `WellNest`)
2. **Product slug** — lowercase with underscores for filenames; suggest a default derived from the product name (e.g., `Balance` → `balance`, `RaudaAI` → `rauda_ai`)

Confirm: "I'll set up this project as **[product_name]** (`[product_slug]`). Continue?"

---

## Step 3 — Get current template version

```bash
# Read the latest tag from the remote template repo
git ls-remote --tags https://github.com/manu/Product_lifecycle | grep -v '{}' | awk '{print $2}' | sed 's|refs/tags/||' | sort -V | tail -1
```

If the command fails (no network, or no tags yet), use `v1.0.0` as the default and tell the user.

---

## Step 4 — Replace [Product] placeholders in claude.md

```bash
python3 -c "
content = open('claude.md').read()
content = content.replace('[Product]', '[product_name]')
content = content.replace('[product_slug]', '[product_slug]')
open('claude.md', 'w').write(content)
print('claude.md updated.')
"
```

Replace `[product_name]` and `[product_slug]` in the command above with the actual values from Step 2 before running.

---

## Step 5 — Create .copier-answers.yml

Write this file to the project root:

```yaml
# Tracks which version of Product_lifecycle this project was created from.
# Required for `copier update` to sync future template improvements.
# Do not edit manually.
_commit: [version_from_step_3]
_src_path: https://github.com/manu/Product_lifecycle
product_name: [product_name]
product_slug: [product_slug]
```

Replace the bracketed values with the actual values collected above.

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
- To sync future template improvements: `copier update` (requires [Copier](https://copier.readthedocs.io/) installed: `pip install copier`)
- Next step: run `/init-context` to create the `context_knowledge/` files

# Prompts Directory

Feature-specific prompt templates, overrides, and customizations.

## Subdirectories

### `current/`
Currently active prompts for this feature.

Place custom prompts here that override or extend the shared-agents library prompts.

**Example:**
```
custom-user-research.md
feature-specific-prd.md
```

### `templates/`
Reusable prompt templates specific to this feature.

Use this when you need to create variants or specialized versions of prompts.

**Example:**
```
healthcare-compliance-prompt.md
mobile-app-design-prompt.md
```

### `snippets/`
Small, reusable prompt fragments.

**Examples:**
- Feature-specific context snippets
- Domain-specific terminology
- Custom brand voice modifications
- Technical constraints snippets

### `versions/`
Historical versions of prompts for tracking changes.

**Structure:**
```
versions/
├── v1.0/
│   ├── custom-prd.md
│   └── custom-research.md
├── v1.1/
│   └── custom-prd.md
└── v2.0/
    └── custom-prd.md
```

## Workflow

1. **Start with shared-agents prompts** - Use default prompts from the library
2. **Customize if needed** - Copy to `current/` and modify
3. **Create templates** - If you reuse patterns, create templates
4. **Version changes** - When updating prompts, copy old version to `versions/`

## When to Override Shared Prompts

Override when:
- Feature has unique domain requirements (e.g., healthcare, finance)
- Need industry-specific terminology
- Require additional compliance constraints
- Want to emphasize certain aspects

**Don't override if:**
- Small tweaks can be done via input context
- Shared prompt works well as-is
- Changes would benefit all features (contribute back to shared-agents!)

## Example: Creating Custom Prompt

```bash
# Copy shared prompt
cp ../shared-agents/agents/prd/prompt.md prompts/current/custom-prd.md

# Edit for your feature
vim prompts/current/custom-prd.md

# Use in your agent script
const prompt = fs.readFileSync('prompts/current/custom-prd.md', 'utf-8');
```

## Version Control

```bash
# Before updating a prompt, archive the current version
cp prompts/current/custom-prd.md prompts/versions/v1.0/custom-prd.md

# Update the prompt
vim prompts/current/custom-prd.md

# Commit with clear message
git add prompts/
git commit -m "Update custom-prd prompt to v1.1: Add compliance requirements"
```

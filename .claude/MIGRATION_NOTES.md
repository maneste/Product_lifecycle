# Claude Commands Migration

## What Changed

### Before (2 commands)
```
.claude/commands/
├── process-FirstConsultation.md
└── process-UserResearch.md
```

### After (1 command)
```
.claude/commands/
└── transcripts.md
```

---

## New Command: `/transcripts`

**Replaces:**
- `/process-FirstConsultation`
- `/process-UserResearch`

**Features:**
- Single command handles both workflows
- Guides user to run standalone scripts first (recommended)
- Can still execute through Claude Code if requested
- Includes troubleshooting and documentation references
- Aligned with current `bin/` script structure

---

## Migration Guide for Users

### Old Way
```
/process-FirstConsultation    # For first consultations
/process-UserResearch         # For user research
```

### New Way
```
/transcripts                  # For everything
```

Then select which pipeline you want when prompted.

---

## Command Behavior

The `/transcripts` command will:

1. **Ask which pipeline** you want to run
2. **Provide terminal commands** to run scripts directly (recommended approach)
3. **Explain what the script does** and what outputs to expect
4. **Offer to run it for you** if you prefer using Claude Code
5. **Include troubleshooting** if issues arise

---

## Why This Change?

### Problems with Old Approach
- Two separate commands to remember
- Commands executed workflows through Claude Code (slower)
- Harder to automate
- Duplicated documentation

### Benefits of New Approach
- **Simpler** - One command to remember
- **Smarter** - Guides to standalone execution first
- **Faster** - Running scripts directly is quicker
- **Automatable** - Can schedule standalone scripts with cron
- **Flexible** - Still can use Claude if needed
- **Consistent** - Aligned with reorganized folder structure

---

## Standalone Scripts (No Claude Needed)

The recommended approach for user research is to run scripts directly:

**Full Pipeline (process + aggregate):**
```bash
cd User_discovery
bin/run
```

**Process Interviews Only:**
```bash
cd User_discovery
bin/process
```

**Aggregate Results Only:**
```bash
cd User_discovery
bin/aggregate
```

See `User_discovery/README.md` for full documentation.

**Note:** The first consultation pipeline does not have a standalone script — use `/transcripts` and select option 1.

---

## When to Use `/transcripts` Command

Use the Claude command when you:
- Need guidance on which pipeline to use
- Want help troubleshooting
- Prefer Claude to execute it for you
- Are unsure about available options
- Need the first consultation pipeline

Run scripts directly when you:
- Know which pipeline you need
- Want faster execution
- Want to automate with cron
- Prefer terminal control

---

## Documentation References

- **Command definition:** `.claude/commands/transcripts.md`
- **Command docs:** `.claude/COMMANDS_README.md`
- **User discovery docs:** `User_discovery/README.md`

---

## Breaking Changes

**None.** The old commands are removed but their functionality is preserved in:
1. The new `/transcripts` command
2. The standalone `bin/` scripts (recommended for user research)

---

## Rollback Instructions

If you need to restore the old commands:

```bash
# Restore from git history
git log --all --full-history -- ".claude/commands/process-*.md"
git checkout <commit-hash> -- .claude/commands/process-FirstConsultation.md
git checkout <commit-hash> -- .claude/commands/process-UserResearch.md
```

But this is **not recommended** as the new structure is cleaner and more maintainable.

# Claude Code Custom Commands

## Available Commands

### `/transcripts` - Run Transcription Pipelines

**Description:** Run first consultation or user research transcription pipelines

**What it does:**
- Guides you to run standalone pipeline scripts
- Helps you choose between first consultation or user research workflows
- Can run the scripts for you if requested
- Provides documentation and troubleshooting help

**Usage:**
```
/transcripts
```

Claude will ask which pipeline you want to run:
1. First Consultation Pipeline (move + consolidate to CSV)
2. User Research Pipeline (move + process via Latitude + generate reports)
3. Show me how to run them myself

**Recommendation:** The command will guide you to run scripts directly in your terminal (faster and can be automated) rather than through Claude Code.

---

## Direct Script Usage (No Claude Code Needed)

You can bypass Claude Code entirely and run scripts directly:

### First Consultation Pipeline
```bash
cd /Users/manuelnunezlema/Documents/GitHub/Feature_Building/user_research
bin/first_consultation
```

### User Research Pipeline
```bash
cd /Users/manuelnunezlema/Documents/GitHub/Feature_Building/user_research
bin/user_research
```

### Quick Reference
See: `user_research/CHEATSHEET.md`

### Complete Guide
See: `user_research/docs/RUN_WITHOUT_AI.md`

---

## Why Use the Command?

Use `/transcripts` when you:
- Want guidance on which pipeline to run
- Need help troubleshooting
- Want Claude to execute it for you
- Are unsure about the available options

Run scripts directly when you:
- Know which pipeline you need
- Want faster execution
- Want to automate with cron
- Prefer command-line control

---

## Command Changes

**Before:** Two separate commands
- `/process-FirstConsultation`
- `/process-UserResearch`

**Now:** Single unified command
- `/transcripts` (handles both workflows)

**Benefits:**
- Simpler - one command to remember
- Smarter - guides you to run scripts directly
- Flexible - can still run through Claude if needed
- Up-to-date - references new bin/ structure

---

## Implementation Details

**Location:** `.claude/commands/transcripts.md`

**Key features:**
- Detects user intent (first consultation vs user research)
- Provides terminal commands for direct execution
- Offers to run scripts via Claude Code if requested
- Includes troubleshooting guidance
- References new organized folder structure

**Documentation:**
- Uses new `bin/` executables
- Points to `docs/` for detailed guides
- References `CHEATSHEET.md` for quick help
- Aligned with reorganized structure

---

## Related Documentation

- `user_research/README.md` - Main documentation entry point
- `user_research/CHEATSHEET.md` - Quick command reference
- `user_research/STRUCTURE.md` - Folder organization
- `user_research/docs/RUN_WITHOUT_AI.md` - Complete standalone guide

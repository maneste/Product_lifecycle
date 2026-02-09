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
2. User Research Pipeline (process + aggregate via OpenAI)
3. Show me how to run them myself

**Recommendation:** The command will guide you to run scripts directly in your terminal (faster and can be automated) rather than through Claude Code.

---

## Direct Script Usage (No Claude Code Needed)

You can bypass Claude Code entirely and run user research scripts directly:

### User Research Pipeline (full)
```bash
cd User_discovery
bin/run
```

### Process Interviews Only
```bash
cd User_discovery
bin/process
```

### Aggregate Results Only
```bash
cd User_discovery
bin/aggregate
```

### Documentation
See: `User_discovery/README.md`

---

## Why Use the Command?

Use `/transcripts` when you:
- Want guidance on which pipeline to run
- Need help troubleshooting
- Want Claude to execute it for you
- Are unsure about the available options
- Need the first consultation pipeline (no standalone script)

Run scripts directly when you:
- Know which pipeline you need
- Want faster execution
- Want to automate with cron
- Prefer command-line control

---

## Command History

**Before:** Two separate commands
- `/process-FirstConsultation`
- `/process-UserResearch`

**Now:** Single unified command
- `/transcripts` (handles both workflows)

**Benefits:**
- Simpler - one command to remember
- Smarter - guides you to run scripts directly
- Flexible - can still run through Claude if needed
- Up-to-date - references current bin/ structure

---

## Implementation Details

**Location:** `.claude/commands/transcripts.md`

**Key features:**
- Detects user intent (first consultation vs user research)
- Provides terminal commands for direct execution
- Offers to run scripts via Claude Code if requested
- Includes troubleshooting guidance

**Documentation:**
- Uses `bin/run`, `bin/process`, `bin/aggregate` executables
- Points to `User_discovery/README.md` for detailed documentation

---

## Related Documentation

- `User_discovery/README.md` - Main documentation entry point

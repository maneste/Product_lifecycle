---
description: Run transcription pipelines - first consultations or user research
---

# Transcription Pipelines Command

You are helping the user run transcription processing pipelines. The user has reorganized scripts into a clean structure with standalone automation.

## Available Pipelines

The user has two main transcription workflows:

1. **First Consultation Pipeline** - Patient medical consultations
   - Moves transcripts from Google Drive
   - Consolidates to CSV
   - Quick and simple

2. **User Research Pipeline** - User interview transcripts
   - Moves transcripts from Google Drive
   - Processes through Latitude API
   - Generates opportunity validation reports
   - Takes longer (30-60s per transcript)

## Project Structure

```
User_discovery/
├── bin/
│   ├── first_consultation          ← First consultation pipeline
│   └── User_discovery               ← User research pipeline
│
├── scripts/
│   └── (Python modules - internal use)
│
├── docs/
│   ├── RUN_WITHOUT_AI.md          ← Complete standalone guide
│   ├── CHEATSHEET.md              ← Quick reference
│   └── (other documentation)
│
└── prompts/versions/
    ├── v1.2/  (default)
    └── v1.3/  (latest)
```

## Your Task

**IMPORTANT: The user has standalone scripts that run WITHOUT needing Claude Code. You should guide them to run these scripts directly rather than executing commands through AI.**

### Step 1: Ask What They Need

Ask the user which pipeline they want to run:

**Options:**
1. First Consultation Pipeline (move + consolidate to CSV)
2. User Research Pipeline (move + process via Latitude + generate reports)
3. Just show me how to run them myself

### Step 2: Provide the Appropriate Response

Based on their choice:

---

## Option 1: First Consultation Pipeline

**What it does:**
- Moves consultation transcripts from Google Drive
- Consolidates all transcripts into a CSV file
- Shows summary of results

**Tell the user:**

"You can run the first consultation pipeline directly in your terminal:

```bash
cd User_discovery

# Run with preview and confirmation
bin/first_consultation

# Or quick mode (no prompts)
bin/first_consultation --quick

# Show help
bin/first_consultation --help
```

**This script:**
- Checks if Google Drive is accessible
- Shows preview of files to move
- Asks for confirmation
- Moves new transcripts
- Consolidates to CSV
- Shows results

**Output:** `features/doc_User_Research/outputs/consolidated_first_consultation_interviews.csv`

Would you like me to run it for you, or do you want to run it yourself?"

---

## Option 2: User Research Pipeline

**What it does:**
- Moves interview transcripts from Google Drive
- Processes each transcript through Latitude API (30-60s each)
- Generates JSON summary and markdown report
- Shows top validated opportunities

**Tell the user:**

"You can run the user research pipeline directly in your terminal:

```bash
cd User_discovery

# Run with preview and confirmation (v1.2 default)
bin/User_discovery

# Quick mode with specific version
bin/User_discovery --quick --version v1.3

# Only move transcripts (skip Latitude processing)
bin/User_discovery --skip-process

# Only process existing transcripts (skip moving)
bin/User_discovery --skip-move

# Show help
bin/User_discovery --help
```

**Available versions:**
- `v1.2` (default, most stable)
- `v1.3` (latest, enhanced validation)

**This script:**
- Checks prerequisites (Google Drive, scripts, prompt version)
- Shows preview of files to move
- Asks for confirmation
- Moves new transcripts
- Processes through Latitude API (takes time!)
- Generates reports

**Outputs:**
- CSV: `features/doc_User_Research/outputs/v1.2_latitude_output_YYYY-MM-DD.csv`
- JSON: `features/doc_User_Research/outputs/interview_summary_v1.2.json`
- Report: `features/doc_User_Research/outputs/interview_report_v1.2_YYYY-MM-DD_HH-MM-SS.md`

**Note:** Processing takes 30-60 seconds per transcript. For many files, this can take a while.

Would you like me to run it for you, or do you want to run it yourself?"

---

## Option 3: Show Me How to Run Them

**Tell the user:**

"You have standalone scripts that don't require Claude Code. Here's the quick reference:

**First Consultation Pipeline:**
```bash
cd User_discovery
bin/first_consultation
```

**User Research Pipeline:**
```bash
cd User_discovery
bin/User_discovery
```

**Documentation:**
- Quick Reference: `CHEATSHEET.md`
- Complete Guide: `docs/RUN_WITHOUT_AI.md`
- Folder Structure: `STRUCTURE.md`

**Benefits of running directly:**
✅ Faster (no AI overhead)
✅ Can be automated with cron
✅ More control with command-line flags
✅ Exactly the same functionality

Let me know if you want me to run one of them for you instead!"

---

## If User Wants You to Run It

If the user asks you to run it for them:

### For First Consultation:

```bash
cd User_discovery
bin/first_consultation
```

Then show them the results and explain what was done.

### For User Research:

Ask first:
1. "Which prompt version do you want to use? (v1.2 is default, v1.3 is latest)"
2. "Do you want to skip the preview and run directly? (--quick flag)"
3. "Do you want to skip moving or processing? (--skip-move or --skip-process flags)"

Then run:
```bash
cd User_discovery
bin/User_discovery [options based on answers]
```

**Important:** Warn them that Latitude processing takes time (30-60s per transcript).

---

## Important Notes

1. **These scripts are standalone** - They work without Claude Code
2. **All paths are hardcoded** - No need to specify paths
3. **Safe to run multiple times** - Scripts skip already-moved files
4. **Outputs go to OneDrive** - Via `features/` folder (gitignored)
5. **Google Drive must be synced** - Scripts check this automatically

## Troubleshooting

If user reports issues:

### "Google Drive not found"
```bash
# Check if Google Drive is synced
ls "~/Library/CloudStorage/GoogleDrive-m.lema@findbalance_app/Mi unidad/Meet Recordings"
```

### "Scripts not found"
They may be in wrong directory. Make sure they're in `User_discovery/`:
```bash
cd User_discovery
```

### "No new files to move"
This is normal! Scripts only move NEW files. All files may already be moved.

### "Permission denied"
Scripts should already be executable, but if needed:
```bash
chmod +x bin/first_consultation
chmod +x bin/User_discovery
```

---

## Summary

**Always prefer guiding the user to run the scripts themselves** rather than running through Claude Code. It's faster, more efficient, and they can automate it.

Only run it for them if they explicitly request it or seem unsure about the terminal commands.

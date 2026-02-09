---
description: Run transcription pipelines - first consultations or user research
---

# Transcription Pipelines Command

You are helping the user run transcription processing pipelines. The user has standalone scripts for processing user research interviews.

## Available Pipelines

The user has two main transcription workflows:

1. **First Consultation Pipeline** - Patient medical consultations
   - Moves transcripts from Google Drive
   - Consolidates to CSV
   - Quick and simple
   - **No standalone script** — run through Claude Code

2. **User Research Pipeline** - User interview transcripts
   - Processes each transcript through OpenAI
   - Aggregates results into summary reports
   - Has standalone scripts in `bin/`

## Project Structure

```
User_discovery/
├── bin/
│   ├── run                            ← Full pipeline: process + aggregate
│   ├── process                        ← Process interviews (OpenAI)
│   └── aggregate                      ← Aggregate results into summary
│
├── scripts/
│   ├── process_interviews.py          ← Interview processing script
│   └── aggregate_results.py           ← Results aggregation script
│
├── prompts/
│   └── interview_analysis.promptl     ← Analysis prompt template
│
├── requirements.txt
└── README.md
```

## Your Task

**IMPORTANT: For the user research pipeline, guide the user to run standalone scripts directly rather than executing through AI. For first consultations, assist directly since there is no standalone script.**

### Step 1: Ask What They Need

Ask the user which pipeline they want to run:

**Options:**
1. First Consultation Pipeline (move + consolidate to CSV)
2. User Research Pipeline (process + aggregate via OpenAI)
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

"The first consultation pipeline does not have a standalone script. I can help you run it directly.

**Steps:**
1. Check Google Drive transcripts are accessible at `Transcriptions/1st_consultation_source/`
2. Move new transcripts to local folder
3. Consolidate into CSV

Would you like me to proceed?"

---

## Option 2: User Research Pipeline

**What it does:**
- Processes interview transcripts through OpenAI
- Aggregates results into a summary JSON and report
- Shows top validated opportunities

**Tell the user:**

"You can run the user research pipeline directly in your terminal:

```bash
cd User_discovery

# Run full pipeline (process + aggregate)
bin/run

# Or run steps separately:
bin/process                    # Process interviews only
bin/aggregate                  # Aggregate results only
```

**This runs:**
1. `process_interviews.py` — sends each transcript through OpenAI for analysis
2. `aggregate_results.py` — combines results into a summary

**Prerequisites:**
- `.env` file with `OPENAI_API_KEY` in `User_discovery/`
- Interview transcripts available

Would you like me to run it for you, or do you want to run it yourself?"

---

## Option 3: Show Me How to Run Them

**Tell the user:**

"You have standalone scripts for user research that don't require Claude Code:

**User Research Pipeline (full):**
```bash
cd User_discovery
bin/run
```

**Process interviews only:**
```bash
cd User_discovery
bin/process
```

**Aggregate results only:**
```bash
cd User_discovery
bin/aggregate
```

**Documentation:**
- See `User_discovery/README.md` for full documentation

**Benefits of running directly:**
- Faster (no AI overhead)
- Can be automated with cron
- More control with command-line flags

**Note:** The first consultation pipeline doesn't have a standalone script — use `/transcripts` and select option 1 for that.

Let me know if you want me to run one of them for you instead!"

---

## If User Wants You to Run It

If the user asks you to run it for them:

### For First Consultation:

Help them directly — there is no standalone script. Assist with moving files from `Transcriptions/1st_consultation_source/` and consolidating to CSV.

### For User Research:

```bash
cd User_discovery
bin/run
```

Or run steps separately if they prefer:
```bash
cd User_discovery
bin/process    # Step 1: Process interviews
bin/aggregate  # Step 2: Aggregate results
```

**Important:** Processing takes time depending on the number of transcripts and OpenAI response times.

---

## Important Notes

1. **User research scripts are standalone** — they work without Claude Code
2. **First consultation has no standalone script** — use this command
3. **Safe to run multiple times** — scripts handle already-processed files
4. **Google Drive must be synced** — transcripts come from Google Drive symlinks
5. **OpenAI API key required** — must be set in `User_discovery/.env`

## Troubleshooting

If user reports issues:

### "Scripts not found"
They may be in wrong directory. Make sure they're in `User_discovery/`:
```bash
cd User_discovery
```

### "Permission denied"
Scripts should already be executable, but if needed:
```bash
chmod +x bin/run bin/process bin/aggregate
```

### "OpenAI API key not found"
```bash
echo 'OPENAI_API_KEY=your-key-here' > User_discovery/.env
```

### "Google Drive not found"
Check if Google Drive is synced and symlinks are set up in `Transcriptions/`.

---

## Summary

**Always prefer guiding the user to run the scripts themselves** rather than running through Claude Code. It's faster, more efficient, and they can automate it.

Only run it for them if they explicitly request it or seem unsure about the terminal commands.

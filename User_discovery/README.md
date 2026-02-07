# User Discovery

Simple workflow for processing user interview transcriptions with OpenAI to discover and validate opportunities.

## Overview

This module processes interview transcriptions to:
1. Filter and identify target interview files
2. Analyze each interview with OpenAI using opportunity tree schema
3. Generate JSON and Markdown outputs
4. Aggregate results into a summary JSON file

## Quick Start

**Super Simple - One Command:**

```bash
cd User_discovery
bin/run
```

That's it! This will:
1. Process all interviews automatically
2. Aggregate results into summary
3. Show you where the outputs are

**Or use individual commands:**

```bash
# Just process interviews
bin/process

# Just aggregate (after processing)
bin/aggregate
```

## Prerequisites

1. **OpenAI API Key**:
   - **Recommended**: Add to `.env` file in `User_discovery/` folder:
     ```bash
     OPENAI_API_KEY=your-api-key-here
     ```
   - Option 2: Set as environment variable:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - Option 3: Pass as argument: `--api-key "your-key"`
   - Option 4: Enter when prompted (script will ask if not found)

2. **Opportunity Tree**: Should exist at `context_knowledge/opportunity_tree.json`
   - The script will auto-generate the system prompt from this file
   - If you want a custom prompt, use `--prompt-path`

3. **Source Transcripts**: Interview files should be in:
   ```
   Transcriptions/transcription_source/
   ```
   This is a symlink to Google Drive. See [Repository Setup](../Development_and_Deployment_Guide.md#repository-setup-after-cloning) for setup instructions.

4. **Transcriptions folder must exist**: The `Transcriptions/` folder at project root must be set up. Processed outputs go to `Transcriptions/processed_interviews/`.

## Workflow

### Step 1: Process Interviews

Process interview transcriptions with OpenAI:

```bash
# Auto-generate prompt from opportunity tree (recommended - no prompt needed!)
bin/process

# With custom prompt file (optional)
bin/process --prompt-path path/to/system_prompt.txt

# With custom filter
bin/process --filter "Consigue un 50%"

# With API key (if not set in environment)
bin/process --api-key "your-key-here"

# Preview without processing
bin/process --dry-run
```

**What it does:**
- Scans `Transcriptions/transcription_source/` for interview files
- Filters for target interviews (default: "Consigue un 50% de descuento")
- **Auto-generates system prompt** from `context_knowledge/opportunity_tree.json` (no manual prompt needed!)
- Processes each interview with OpenAI
- Saves outputs to `Transcriptions/processed_interviews/`:
  - JSON: `[Date(YYYMMDD) opportunities: user_name].json`
  - Markdown: `Date(YYYMMDD) Opportunities for user_name.md`

### Step 2: Aggregate Results

Aggregate all processed interviews into a summary:

```bash
# Aggregate all results
bin/aggregate

# Custom output filename
bin/aggregate --output my_summary.json
```

**What it does:**
- Reads all JSON files from `Transcriptions/processed_interviews/`
- Aggregates opportunities with counts
- Creates summary JSON similar to `interview_summary.json` format
- Saves to `outputs/YYYYMMDD_interview_summary.json`

## Folder Structure

```
Feature_Building/
├── User_discovery/
│   ├── README.md                    # This file
│   ├── .env                         # OpenAI API key (gitignored)
│   ├── bin/                         # Executable wrappers
│   │   ├── process                  # Process interviews
│   │   ├── aggregate                # Aggregate results
│   │   └── run                      # Run full pipeline
│   ├── scripts/                     # Python scripts
│   │   ├── process_interviews.py    # Main processing script
│   │   └── aggregate_results.py     # Aggregation script
│   ├── prompts/                     # Prompt templates
│   │   └── interview_analysis.promptl
│   └── outputs/                     # Aggregated summaries (created on demand)
│       └── YYYYMMDD_interview_summary.json
│
├── Transcriptions/                  # Gitignored - see setup guide
│   ├── transcription_source/        # Symlink → Google Drive (input)
│   ├── 1st_consultation_source/     # Symlink → Google Drive (input)
│   └── processed_interviews/        # Output from User_discovery processing
│       ├── YYYYMMDD Analysis for user_name.md
│       └── YYYYMMDD opportunities: user_name.json
│
└── context_knowledge/               # Knowledge base
    └── opportunity_tree.json        # Used to auto-generate prompts
```

**Note:** `Transcriptions/` is gitignored. After cloning, you must set it up manually. See the [Repository Setup Guide](../Development_and_Deployment_Guide.md#repository-setup-after-cloning).

## System Prompt

**Good news: You don't need to create a prompt manually!**

The script **auto-generates** the system prompt from `context_knowledge/opportunity_tree.json`. It:
1. Loads the opportunity tree structure
2. Generates a prompt that includes the full tree
3. Instructs OpenAI to validate opportunities against the tree

**If you want a custom prompt** (optional):
- Use `--prompt-path` to provide your own prompt file
- See `prompts/system_prompt_template.txt` for a template

## File Naming

### Input Files
Expected format: `"Consigue un 50% de descuento (Ane Tamayo) - 2025 11 11 15:00 CET - Notes by Gemini"`

The script extracts:
- **User name**: From parentheses `(Ane Tamayo)`
- **Date**: From pattern `YYYY MM DD` → `20251111`

### Output Files

**JSON**: `[Date(YYYMMDD) opportunities: user_name].json`
- Example: `20251111 opportunities: Ane Tamayo.json`

**Markdown**: `Date(YYYMMDD) Opportunities for user_name.md`
- Example: `20251111 Opportunities for Ane Tamayo.md`

**Location**: `Transcriptions/processed_interviews/`

## Configuration

### Filter Pattern

Default filter looks for files containing:
- "Consigue un 50% de descuento"
- "Entrevista Usuario Balance"
- "User Interview"

Custom filter:
```bash
bin/process --filter "your pattern here"
```

### OpenAI Model

Default: `gpt-4o-mini` (cost-efficient)

To change, edit `scripts/process_interviews.py`:
```python
model="gpt-4o-mini"  # Change to "gpt-4" or other model
```

## Output Format

### Individual Interview JSON

```json
{
  "summary": "Brief interview summary",
  "validated_opportunities": [
    {
      "id": "1.1.1",
      "title": "Difficulty perceiving physical evolution",
      "evidence": [
        "Quote from user validating this opportunity"
      ]
    }
  ],
  "new_opportunities": []
}
```

### Aggregated Summary JSON

```json
{
  "metadata": {
    "generated_at": "2025-11-11T12:00:00",
    "total_opportunities": 49,
    "opportunities_with_validations": 15,
    "total_validations": 42,
    "total_interviews": 5,
    "source_files": ["20251111 opportunities: Ane Tamayo.json", ...]
  },
  "opportunities": [
    {
      "id": "1.1.1",
      "title": "Difficulty perceiving physical evolution",
      "interview_count": 3,
      "interview_count_text": "3 interviews",
      "interview_names": ["Ane Tamayo", "User 2", "User 3"],
      "evidence": [
        {
          "interview_name": "Ane Tamayo",
          "quote": "Quote from interview"
        }
      ]
    }
  ]
}
```

## Troubleshooting

### No interviews found

**Problem**: Script says "No matching interview files found"

**Solutions**:
- Check that files are in `Transcriptions/transcription_source/`
- Verify the symlink is working: `ls -la Transcriptions/transcription_source/`
- Verify filenames contain the filter pattern
- Use `--filter` to specify a custom pattern
- Use `--dry-run` to preview what files would be processed

### OpenAI API Key not found

**Problem**: Error about OPENAI_API_KEY

**Solution**:
1. **Best**: Add to `.env` file in `User_discovery/` folder:
   ```bash
   OPENAI_API_KEY=your-key-here
   ```

2. Or set as environment variable:
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

3. Or pass directly:
   ```bash
   bin/process --api-key "your-key-here"
   ```

### Prompt file not found

**Problem**: Error loading system prompt

**Solution**:
- Provide full path: `bin/process --prompt-path /full/path/to/prompt.txt`
- Or use relative path from User_discovery folder
- Make sure file exists and is readable

### Opportunity tree not found

**Problem**: Aggregate script can't find opportunity tree

**Solution**:
- Ensure `context_knowledge/opportunity_tree.json` exists
- Check that the file is at the project root level

### Transcriptions folder not found

**Problem**: Script can't find source transcripts or can't write processed output

**Solution**:
- Set up the `Transcriptions/` folder. See [Repository Setup Guide](../Development_and_Deployment_Guide.md#repository-setup-after-cloning)
- The processed_interviews folder is created automatically if Transcriptions/ exists

## Examples

### Complete Workflow

```bash
# 1. Process interviews
bin/process

# 2. Aggregate results
bin/aggregate

# 3. Review summary
cat outputs/YYYYMMDD_interview_summary.json
```

### Process Specific Interviews

```bash
# Only process files matching pattern
bin/process --filter "Ane Tamayo"
```

### Preview Before Processing

```bash
# See what would be processed
bin/process --dry-run
```

## Integration with User Research

This module is separate from `user_research/` and uses a simpler workflow:
- **User_discovery**: Direct OpenAI processing, simpler structure
- **user_research**: Latitude API, more complex pipeline

Both can coexist and serve different purposes.

## Related Documentation

- **Repository Setup**: `Development_and_Deployment_Guide.md` (for Transcriptions folder setup)
- **Opportunity Tree**: `context_knowledge/opportunity_tree.json`
- **User Research Module**: `user_research/README.md`

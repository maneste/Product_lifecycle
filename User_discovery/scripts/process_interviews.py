#!/usr/bin/env python3
"""
Process User Interviews with OpenAI

This script:
1. Reads interview transcriptions from Transcriptions/transcription_source
2. Filters for specific interview types (e.g., "Consigue un 50% de descuento")
3. Asks you interactively which prompt file to use (or press Enter for default)
4. Processes each interview with OpenAI using the selected prompt
5. Saves JSON and Markdown outputs to Transcriptions/processed_interviews/

Usage:
    # Interactive mode - will ask for prompt path
    python3 process_interviews.py

    # Skip prompt selection by passing --prompt-path
    python3 process_interviews.py --prompt-path prompts/interview_analysis_markdown.promptl

    # With custom filter
    python3 process_interviews.py --filter "Consigue un 50%"

When prompted, you can:
    - Press Enter to use default (prompts/interview_analysis.promptl)
    - Type just the filename (e.g., "interview_analysis_markdown.promptl")
    - Copy-paste the full path to any .promptl file
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(Path(__file__).parent.parent / '.env')


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_header(message):
    """Print a formatted header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{message.center(80)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}\n")


def print_success(message):
    """Print a success message"""
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")


def print_error(message):
    """Print an error message"""
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")


def print_info(message):
    """Print an info message"""
    print(f"{Colors.OKCYAN}ℹ {message}{Colors.ENDC}")


def print_warning(message):
    """Print a warning message"""
    print(f"{Colors.WARNING}⚠ {message}{Colors.ENDC}")


class InterviewProcessor:
    """Process user interviews with OpenAI"""

    def __init__(self, base_path=None, prompt_path=None, api_key=None):
        # Always use absolute paths to avoid issues when called from different directories
        if base_path:
            self.base_path = Path(base_path).resolve()
        else:
            # Get absolute path: User_discovery/scripts/process_interviews.py -> User_discovery
            self.base_path = Path(__file__).parent.parent.resolve()

        # Project root is always Feature_Building (parent of User_discovery)
        self.project_root = self.base_path.parent.resolve()
        
        # Source directory - use absolute path
        self.source_dir = Path("/Users/manuelnunezlema/Documents/GitHub/Feature_Building/Transcriptions/transcription_source").resolve()
        self.processed_dir = self.project_root / "Transcriptions" / "processed_interviews"
        self.processed_dir.mkdir(parents=True, exist_ok=True)

        # Initialize OpenAI client
        # Priority: 1) argument, 2) .env file, 3) environment variable, 4) prompt user
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print_warning("OPENAI_API_KEY not found.")
            print_info("You can:")
            print_info("  1. Add it to .env file: OPENAI_API_KEY='your-key-here'")
            print_info("  2. Set it: export OPENAI_API_KEY='your-key-here'")
            print_info("  3. Pass it: --api-key 'your-key-here'")
            print_info("  4. Enter it now (will not be saved):")
            api_key_input = input("OpenAI API Key: ").strip()
            if not api_key_input:
                print_error("API key is required to process interviews")
                sys.exit(1)
            self.api_key = api_key_input

        self.client = OpenAI(api_key=self.api_key)

        # Load system prompt
        self.system_prompt = self._load_system_prompt(prompt_path)

    def _load_system_prompt(self, prompt_path=None):
        """Load system prompt from file"""
        # Default prompt file
        default_prompt = self.base_path / "prompts" / "interview_analysis.promptl"

        # If no prompt_path provided via argument, ask interactively
        if not prompt_path:
            print_header("Select Prompt File")
            print_info(f"Default prompt: {default_prompt}")
            print_info("Available prompts in prompts/ directory:")

            # List available prompts
            prompts_dir = self.base_path / "prompts"
            if prompts_dir.exists():
                for prompt_file in sorted(prompts_dir.glob("*.promptl")):
                    print(f"  - {prompt_file.name}")

            print()
            print(f"{Colors.OKCYAN}Enter prompt file path (or press Enter for default):{Colors.ENDC}")
            print(f"{Colors.OKCYAN}You can copy-paste the full path or just the filename:{Colors.ENDC}")

            user_input = input("Prompt path: ").strip()

            if user_input:
                # User provided a path
                prompt_path = user_input
            else:
                # User pressed Enter, use default
                prompt_file = default_prompt
                print_success(f"Using default prompt: {prompt_file.name}")

        # Determine which prompt file to use
        if prompt_path:
            # Custom prompt path provided (via argument or interactive input)
            prompt_file = Path(prompt_path).expanduser().resolve()

            # If only filename provided, look in prompts directory
            if not prompt_file.exists() and not prompt_file.is_absolute():
                prompt_file = self.base_path / "prompts" / prompt_path
        else:
            # Use default
            prompt_file = default_prompt

        # Check if file exists
        if not prompt_file.exists():
            print_error(f"Prompt file not found: {prompt_file}")
            print_info("Expected default location: User_discovery/prompts/interview_analysis.promptl")
            sys.exit(1)

        # Read the prompt file
        print_info(f"Loading prompt from: {prompt_file.name}")
        with open(prompt_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract system prompt from PromptL format
        if "<system>" in content and "</system>" in content:
            system_start = content.find("<system>")
            system_end = content.find("</system>")
            if system_start != -1 and system_end != -1:
                prompt = content[system_start+8:system_end].strip()
                print_success("System prompt loaded successfully")
                return prompt

        # If no tags found, return entire content
        print_warning("No <system> tags found, using entire file content")
        return content

    def is_target_interview(self, filename, filter_pattern=None):
        """Check if file matches target interview pattern"""
        if filter_pattern:
            return filter_pattern.lower() in filename.lower()
        
        # Default pattern: "Consigue un 50% de descuento"
        default_patterns = [
            "consigue un 50% de descuento",
            "entrevista usuario balance",
            "user interview"
        ]
        
        filename_lower = filename.lower()
        return any(pattern in filename_lower for pattern in default_patterns)

    def is_already_processed(self, user_name, date_str):
        """Check if interview has already been processed"""
        # Check for any of the possible output file patterns
        patterns = [
            f"{date_str} opportunities: {user_name}.json",
            f"{date_str} Opportunities for {user_name}.md",
            f"{date_str} Analysis for {user_name}.md"
        ]

        for pattern in patterns:
            if (self.processed_dir / pattern).exists():
                return True
        return False

    def find_interviews(self, filter_pattern=None):
        """Find interview files in source directory"""
        if not self.source_dir or not self.source_dir.exists():
            print_error(f"Source directory not found: {self.source_dir}")
            print_info("Expected location: /Users/manuelnunezlema/Documents/GitHub/Feature_Building/Transcriptions/transcription_source")
            print_info("Please check that the Transcriptions folder exists and contains transcription_source/")
            return []

        # Check if we can access the directory
        try:
            # Test access
            list(self.source_dir.iterdir())
        except PermissionError as e:
            print_error(f"Permission denied accessing: {self.source_dir}")
            print_warning("This appears to be a Google Drive folder that requires special permissions.")
            print_info("Solutions:")
            print_info("  1. Make sure Google Drive is synced and the folder is accessible")
            print_info("  2. Grant Full Disk Access to Terminal/Python in System Preferences > Privacy & Security")
            print_info("  3. Or copy files to a local folder and update the path")
            return []
        except Exception as e:
            print_error(f"Error accessing directory {self.source_dir}: {e}")
            return []

        interviews = []
        try:
            for file_path in self.source_dir.iterdir():
                if file_path.is_file() and self.is_target_interview(file_path.name, filter_pattern):
                    interviews.append(file_path)
        except PermissionError as e:
            print_error(f"Permission denied while reading files: {e}")
            print_warning("Cannot read files from Google Drive folder. Check permissions.")
            return []
        except Exception as e:
            print_error(f"Error reading files: {e}")
            return []

        return sorted(interviews)

    def extract_user_name_and_date(self, filename):
        """Extract user name and date from filename"""
        # Pattern 1: "Consigue un 50% de descuento (Ane Tamayo) - 2025 11 11 15:00 CET - Notes by Gemini"
        # Pattern 2: "Entrevista Usuario Balance (Diana Villar) - 2025_07_09 13_59 CEST - Notes by Gemini"

        # Extract name from parentheses
        name_match = re.search(r'\(([^)]+)\)', filename)
        user_name = name_match.group(1) if name_match else "Unknown"

        # Extract date - try multiple patterns
        date_str = None

        # Pattern 1: YYYY MM DD (spaces)
        date_match = re.search(r'(\d{4})\s+(\d{1,2})\s+(\d{1,2})', filename)
        if date_match:
            year, month, day = date_match.groups()
            date_str = f"{year}{month.zfill(2)}{day.zfill(2)}"
        else:
            # Pattern 2: YYYY_MM_DD (underscores)
            date_match = re.search(r'(\d{4})_(\d{1,2})_(\d{1,2})', filename)
            if date_match:
                year, month, day = date_match.groups()
                date_str = f"{year}{month.zfill(2)}{day.zfill(2)}"

        # Fallback to current date if no match found
        if not date_str:
            date_str = datetime.now().strftime("%Y%m%d")

        return user_name, date_str

    def read_transcript(self, file_path):
        """Read transcript file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print_error(f"Error reading {file_path.name}: {e}")
            return None

    def _clean_markdown_output(self, text):
        """Remove code fence delimiters from markdown output"""
        # Remove opening code fence (```markdown or ```)
        if text.startswith('```markdown'):
            text = text[len('```markdown'):].lstrip('\n')
        elif text.startswith('```'):
            text = text[3:].lstrip('\n')

        # Remove closing code fence (```)
        if text.endswith('```'):
            text = text[:-3].rstrip('\n')

        return text

    def process_with_openai(self, transcript, user_name):
        """Process transcript with OpenAI"""
        try:
            # Check if prompt requests JSON format
            use_json_mode = 'json' in self.system_prompt.lower()

            # Build API call parameters
            api_params = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Interview transcript:\n\n{transcript}"}
                ],
                "temperature": 0.3
            }

            # Only use JSON mode if prompt mentions JSON
            if use_json_mode:
                api_params["response_format"] = {"type": "json_object"}
                print_info("Using JSON response mode (detected 'json' in prompt)")
            else:
                print_info("Using text/markdown response mode")

            response = self.client.chat.completions.create(**api_params)
            result = response.choices[0].message.content

            # Try to parse as JSON, if it fails return as text
            try:
                return {"format": "json", "content": json.loads(result)}
            except json.JSONDecodeError:
                # Clean markdown code fences before returning
                cleaned_result = self._clean_markdown_output(result)
                return {"format": "text", "content": cleaned_result}

        except Exception as e:
            print_error(f"OpenAI API error: {e}")
            return None

    def save_results(self, user_name, date_str, result_data):
        """Save outputs based on format (JSON or text/markdown)"""
        output_format = result_data.get("format", "text")
        content = result_data.get("content")

        saved_files = []

        if output_format == "json":
            # Save JSON: [Date(YYYMMDD) opportunities: user_name].json
            json_filename = f"{date_str} opportunities: {user_name}.json"
            json_path = self.processed_dir / json_filename

            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=2, ensure_ascii=False)
            saved_files.append(json_path)

            # Try to convert JSON to markdown if it has expected structure
            md_filename = f"{date_str} Opportunities for {user_name}.md"
            md_path = self.processed_dir / md_filename
            try:
                self._convert_to_markdown(content, user_name, date_str, md_path)
                saved_files.append(md_path)
            except Exception as e:
                print_warning(f"Could not convert JSON to markdown: {e}")

        else:
            # Save as markdown/text: Date(YYYMMDD) Analysis for user_name.md
            md_filename = f"{date_str} Analysis for {user_name}.md"
            md_path = self.processed_dir / md_filename

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(content)
            saved_files.append(md_path)

        return saved_files

    def _convert_to_markdown(self, result_json, user_name, date_str, output_path):
        """Convert JSON result to readable markdown"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Opportunities for {user_name}\n\n")
            f.write(f"**Date:** {date_str}\n\n")
            f.write("---\n\n")

            # Add summary if available
            if 'summary' in result_json:
                f.write(f"## Summary\n\n{result_json['summary']}\n\n---\n\n")

            # Add validated opportunities
            if 'validated_opportunities' in result_json:
                f.write("## Validated Opportunities\n\n")
                for opp in result_json['validated_opportunities']:
                    opp_id = opp.get('id', 'N/A')
                    title = opp.get('title', 'N/A')
                    evidence = opp.get('evidence', [])

                    f.write(f"### [{opp_id}] {title}\n\n")
                    f.write(f"**{user_name}:**\n\n")
                    for quote in evidence:
                        f.write(f"- \"{quote}\"\n\n")
                    f.write("---\n\n")

            # Add new opportunities if any
            if 'new_opportunities' in result_json and result_json['new_opportunities']:
                f.write("## New Opportunities Discovered\n\n")
                for opp in result_json['new_opportunities']:
                    title = opp.get('title', 'N/A')
                    explanation = opp.get('explanation', '')
                    f.write(f"### {title}\n\n")
                    if explanation:
                        f.write(f"{explanation}\n\n")
                    f.write("---\n\n")

    def process_interview(self, file_path, filter_pattern=None):
        """Process a single interview file"""
        print_info(f"Processing: {file_path.name}")

        # Extract user name and date
        user_name, date_str = self.extract_user_name_and_date(file_path.name)

        # Read transcript
        transcript = self.read_transcript(file_path)
        if not transcript:
            return None

        # Process with OpenAI
        print_info("Sending to OpenAI...")
        result = self.process_with_openai(transcript, user_name)

        if not result:
            print_error(f"Failed to process {file_path.name}")
            return None

        # Save results
        saved_files = self.save_results(user_name, date_str, result)
        for file_path in saved_files:
            print_success(f"Saved: {file_path.name}")

        return {
            'user_name': user_name,
            'date': date_str,
            'saved_files': saved_files,
            'result': result
        }

    def run(self, filter_pattern=None, dry_run=False):
        """Run the complete processing workflow"""
        print_header("User Discovery - Process Interviews")

        # Find interviews
        print_info("Scanning for interview files...")
        all_interviews = self.find_interviews(filter_pattern)

        if not all_interviews:
            print_warning("No matching interview files found")
            if filter_pattern:
                print_info(f"Filter pattern: {filter_pattern}")
            else:
                print_info("Looking for files containing: 'Consigue un 50% de descuento'")
            return False

        print_success(f"Found {len(all_interviews)} interview file(s)")

        # Filter out already processed interviews
        print_info("Checking for already processed interviews...")
        new_interviews = []
        skipped_interviews = []

        for interview in all_interviews:
            user_name, date_str = self.extract_user_name_and_date(interview.name)
            if self.is_already_processed(user_name, date_str):
                skipped_interviews.append((interview, user_name, date_str))
            else:
                new_interviews.append(interview)

        if skipped_interviews:
            print_warning(f"Skipping {len(skipped_interviews)} already processed interview(s):")
            for interview, user_name, date_str in skipped_interviews:
                print(f"  - {user_name} ({date_str})")

        if not new_interviews:
            print()
            print_success("All interviews have already been processed!")
            print_info(f"Processed interviews location: {self.processed_dir}")
            return True

        print_success(f"Found {len(new_interviews)} new interview(s) to process")
        print()

        if dry_run:
            print_info("DRY RUN MODE - No files will be processed")
            for interview in new_interviews:
                user_name, date_str = self.extract_user_name_and_date(interview.name)
                print(f"  - {interview.name} → {user_name} ({date_str})")
            return True

        # Process each new interview
        processed = []
        for i, interview in enumerate(new_interviews, 1):
            print(f"\n[{i}/{len(new_interviews)}] Processing interview...")
            result = self.process_interview(interview, filter_pattern)
            if result:
                processed.append(result)

        print()
        print_header("Processing Complete!")
        print_success(f"Processed {len(processed)}/{len(new_interviews)} new interview(s)")
        if skipped_interviews:
            print_info(f"Skipped {len(skipped_interviews)} already processed interview(s)")
        print_info(f"Outputs saved to: {self.processed_dir}")

        return len(processed) > 0


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Process User Interviews with OpenAI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default prompt (prompts/interview_analysis.promptl)
  python3 process_interviews.py

  # With custom prompt file
  python3 process_interviews.py --prompt-path prompts/custom_prompt.txt

  # With custom filter
  python3 process_interviews.py --filter "Consigue un 50%"

  # Dry run (preview only)
  python3 process_interviews.py --dry-run

  # With API key
  python3 process_interviews.py --api-key "your-key-here"
        """
    )

    parser.add_argument(
        '--prompt-path',
        type=str,
        help='Path to system prompt file'
    )

    parser.add_argument(
        '--filter',
        type=str,
        help='Filter pattern for interview filenames (default: "Consigue un 50% de descuento")'
    )

    parser.add_argument(
        '--api-key',
        type=str,
        help='OpenAI API key (or set OPENAI_API_KEY environment variable)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview files without processing'
    )

    parser.add_argument(
        '--base-path',
        type=str,
        default=None,
        help='Base path to User_discovery folder (default: script location)'
    )

    args = parser.parse_args()

    # Create processor
    processor = InterviewProcessor(
        base_path=args.base_path,
        prompt_path=args.prompt_path,
        api_key=args.api_key
    )

    # Run processing
    success = processor.run(filter_pattern=args.filter, dry_run=args.dry_run)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()


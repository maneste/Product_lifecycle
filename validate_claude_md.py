#!/usr/bin/env python3
"""
Validate CLAUDE.md Documentation

This script validates that CLAUDE.md accurately reflects the actual repository structure.
It checks:
1. Repository folder structure
2. Documentation files
3. .claude folder contents (agents, commands)
4. References to cloud storage (OneDrive vs Google Drive)

Usage:
    python3 validate_claude_md.py
    python3 validate_claude_md.py --fix  # Auto-fix issues (future feature)

Exit codes:
    0 - All validations passed
    1 - Validation errors found
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict

class Colors:
    """ANSI color codes for terminal output"""
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    HEADER = '\033[95m'

def print_success(message):
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")

def print_error(message):
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")

def print_warning(message):
    print(f"{Colors.WARNING}⚠ {message}{Colors.ENDC}")

def print_header(message):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{message}{Colors.ENDC}")

class CLAUDEValidator:
    """Validates CLAUDE.md against actual repository structure"""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.claude_md = repo_root / "claude.md"
        self.errors = []
        self.warnings = []

    def validate_all(self) -> bool:
        """Run all validations"""
        print_header("Validating CLAUDE.md...")

        if not self.claude_md.exists():
            print_error(f"CLAUDE.md not found at {self.claude_md}")
            return False

        self.validate_cloud_storage_references()
        self.validate_folder_structure()
        self.validate_documentation_files()
        self.validate_claude_folder()
        self.validate_user_research_paths()

        return self.print_results()

    def validate_cloud_storage_references(self):
        """Ensure OneDrive is referenced, not Google Drive"""
        print_header("Checking cloud storage references...")

        with open(self.claude_md, 'r') as f:
            content = f.read()

        # Check for incorrect "Google Drive" references
        google_drive_matches = re.findall(r'Google Drive', content, re.IGNORECASE)
        if google_drive_matches:
            self.errors.append(
                f"Found {len(google_drive_matches)} reference(s) to 'Google Drive' "
                "in CLAUDE.md. Should be 'OneDrive'."
            )
        else:
            print_success("No incorrect 'Google Drive' references found")

        # Verify OneDrive is mentioned
        if 'OneDrive' not in content:
            self.warnings.append("No mention of 'OneDrive' found in CLAUDE.md")
        else:
            print_success("OneDrive correctly referenced")

    def validate_folder_structure(self):
        """Validate main folder structure matches documentation"""
        print_header("Checking folder structure...")

        expected_folders = {
            '.claude': True,
            '.claude/agents': True,
            '.claude/commands': True,
            'documentation': True,
            'features': True,
            'feature-template': True,
            'user_research': True,
        }

        for folder, should_exist in expected_folders.items():
            folder_path = self.repo_root / folder
            if should_exist and not folder_path.exists():
                self.errors.append(f"Expected folder not found: {folder}")
            elif should_exist:
                print_success(f"Found: {folder}")

        # Check if structure is documented
        with open(self.claude_md, 'r') as f:
            content = f.read()

        for folder in ['.claude/agents', '.claude/commands', 'user_research']:
            if folder not in content:
                self.errors.append(f"Folder '{folder}' not documented in CLAUDE.md")

    def validate_documentation_files(self):
        """Validate documentation files match what's documented"""
        print_header("Checking documentation files...")

        doc_folder = self.repo_root / "documentation"
        if not doc_folder.exists():
            self.warnings.append("Documentation folder doesn't exist")
            return

        # Get actual files
        actual_files = {f.name for f in doc_folder.iterdir() if f.is_file() and not f.name.startswith('.')}

        # Get documented files from CLAUDE.md
        with open(self.claude_md, 'r') as f:
            content = f.read()

        # Extract documented files (between "Expected files:" and next section)
        doc_files_section = re.search(
            r'Expected files:(.+?)(?=##|\Z)',
            content,
            re.DOTALL
        )

        if doc_files_section:
            documented_files = set(re.findall(r'`([^`]+\.\w+)`', doc_files_section.group(1)))

            # Check for missing files
            missing_in_repo = documented_files - actual_files
            missing_in_docs = actual_files - documented_files

            if missing_in_repo:
                for file in missing_in_repo:
                    self.errors.append(f"File documented but not found: documentation/{file}")

            if missing_in_docs:
                for file in missing_in_docs:
                    self.warnings.append(f"File exists but not documented: documentation/{file}")

            if not missing_in_repo and not missing_in_docs:
                print_success("All documentation files match")

    def validate_claude_folder(self):
        """Validate .claude folder contents"""
        print_header("Checking .claude folder contents...")

        claude_folder = self.repo_root / ".claude"

        # Check agents
        agents_folder = claude_folder / "agents"
        if agents_folder.exists():
            agents = list(agents_folder.glob("*.md"))
            print_success(f"Found {len(agents)} agent(s)")

            # Check if documented
            with open(self.claude_md, 'r') as f:
                content = f.read()

            for agent in agents:
                if agent.name not in content:
                    self.warnings.append(f"Agent '{agent.name}' not documented in CLAUDE.md")

        # Check commands
        commands_folder = claude_folder / "commands"
        if commands_folder.exists():
            commands = list(commands_folder.glob("*.md"))
            print_success(f"Found {len(commands)} command(s)")

            for command in commands:
                if command.name not in content:
                    self.warnings.append(f"Command '{command.name}' not documented in CLAUDE.md")

    def validate_user_research_paths(self):
        """Validate user research output paths"""
        print_header("Checking user research output paths...")

        user_research = self.repo_root / "user_research"

        # Check Python scripts for correct output paths
        scripts = [
            user_research / "process_interviews.py",
            user_research / "process_new_transcripts.py",
            user_research / "run_pipeline.py"
        ]

        expected_path = 'features" / "doc_User_Research" / "outputs'
        old_path = '"outputs"'

        for script in scripts:
            if script.exists():
                with open(script, 'r') as f:
                    content = f.read()

                if old_path in content and expected_path not in content:
                    self.errors.append(
                        f"{script.name}: Still uses old outputs path. "
                        "Should use features/doc_User_Research/outputs/"
                    )
                elif expected_path in content:
                    print_success(f"{script.name}: Uses correct output path")

    def print_results(self) -> bool:
        """Print validation results"""
        print_header("Validation Results")

        if self.errors:
            print(f"\n{Colors.FAIL}{Colors.BOLD}Errors:{Colors.ENDC}")
            for error in self.errors:
                print_error(error)

        if self.warnings:
            print(f"\n{Colors.WARNING}{Colors.BOLD}Warnings:{Colors.ENDC}")
            for warning in self.warnings:
                print_warning(warning)

        if not self.errors and not self.warnings:
            print_success("All validations passed!")
            return True
        elif not self.errors:
            print(f"\n{Colors.WARNING}Validation passed with warnings{Colors.ENDC}")
            return True
        else:
            print(f"\n{Colors.FAIL}Validation failed with {len(self.errors)} error(s){Colors.ENDC}")
            return False

def main():
    """Main entry point"""
    repo_root = Path(__file__).parent
    validator = CLAUDEValidator(repo_root)

    success = validator.validate_all()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

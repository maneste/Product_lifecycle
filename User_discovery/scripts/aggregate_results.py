#!/usr/bin/env python3
"""
Aggregate Interview Results

This script aggregates all processed interview JSON files into a summary JSON file
with opportunity counts, similar to the interview_summary.json format.

Usage:
    python3 aggregate_results.py
    python3 aggregate_results.py --output summary.json
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict


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


class ResultAggregator:
    """Aggregate processed interview results"""

    def __init__(self, base_path=None):
        # Always use absolute paths
        if base_path:
            self.base_path = Path(base_path).resolve()
        else:
            # Get absolute path: User_discovery/scripts/aggregate_results.py -> User_discovery
            self.base_path = Path(__file__).parent.parent.resolve()

        # Project root is Feature_Building (parent of User_discovery)
        self.project_root = self.base_path.parent.resolve()
        self.processed_dir = self.project_root / "Transcriptions" / "processed_interviews"
        self.outputs_dir = self.base_path / "outputs"
        self.outputs_dir.mkdir(parents=True, exist_ok=True)

    def find_json_files(self):
        """Find all JSON result files"""
        if not self.processed_dir.exists():
            print_error(f"Processed interviews directory not found: {self.processed_dir}")
            return []

        json_files = list(self.processed_dir.glob("*.json"))
        # Filter for result files (not other JSON files)
        result_files = [f for f in json_files if "opportunities:" in f.name]

        return sorted(result_files)

    def load_opportunity_tree(self):
        """Load opportunity tree structure from context_knowledge"""
        # Use absolute path
        tree_path = Path("/Users/manuelnunezlema/Documents/GitHub/Feature_Building/context_knowledge/opportunity_tree.json").resolve()
        
        if not tree_path.exists():
            print_error(f"Opportunity tree not found: {tree_path}")
            return None

        try:
            with open(tree_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print_error(f"Error loading opportunity tree: {e}")
            return None

    def extract_opportunity_structure(self, tree_data):
        """Extract flat opportunity structure from tree"""
        opportunities = {}

        def extract_recursive(opp_list, parent_id=""):
            for opp in opp_list:
                opp_id = opp.get('id', '')
                title = opp.get('title', '')
                if opp_id and title:
                    opportunities[opp_id] = {
                        'id': opp_id,
                        'title': title,
                        'explanation': opp.get('explanation', '')
                    }
                if 'children' in opp:
                    extract_recursive(opp['children'], opp_id)

        if tree_data and 'opportunity_tree' in tree_data:
            if 'opportunities' in tree_data['opportunity_tree']:
                extract_recursive(tree_data['opportunity_tree']['opportunities'])

        return opportunities

    def aggregate_results(self, json_files):
        """Aggregate results from all JSON files"""
        # Structure: opportunity_id -> {count, interview_names, evidence}
        opportunity_data = defaultdict(lambda: {
            'interview_count': 0,
            'interview_names': [],
            'evidence': []
        })

        total_interviews = 0
        processed_files = []

        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Extract user name from filename: "20251111 opportunities: Ane Tamayo.json"
                user_name = json_file.stem.split('opportunities: ')[-1] if 'opportunities:' in json_file.name else "Unknown"
                total_interviews += 1

                # Process validated opportunities
                validated_opps = data.get('validated_opportunities', [])
                for opp in validated_opps:
                    opp_id = opp.get('id', '')
                    if opp_id:
                        opportunity_data[opp_id]['interview_count'] += 1
                        if user_name not in opportunity_data[opp_id]['interview_names']:
                            opportunity_data[opp_id]['interview_names'].append(user_name)

                        # Add evidence
                        evidence_list = opp.get('evidence', [])
                        for quote in evidence_list:
                            opportunity_data[opp_id]['evidence'].append({
                                'interview_name': user_name,
                                'quote': quote
                            })

                processed_files.append(json_file.name)

            except Exception as e:
                print_error(f"Error processing {json_file.name}: {e}")
                continue

        return opportunity_data, total_interviews, processed_files

    def create_summary(self, opportunity_tree, opportunity_data, total_interviews, processed_files):
        """Create summary JSON in the same format as interview_summary.json"""
        # Get all opportunities from tree
        tree_opportunities = self.extract_opportunity_structure(opportunity_tree)

        # Build summary list
        summary_list = []
        
        # Sort opportunities by ID
        sorted_ids = sorted(tree_opportunities.keys(), key=lambda x: [int(n) for n in x.split('.') if n.isdigit()])

        for opp_id in sorted_ids:
            opp_info = tree_opportunities[opp_id]
            data = opportunity_data.get(opp_id, {
                'interview_count': 0,
                'interview_names': [],
                'evidence': []
            })

            summary_list.append({
                'id': opp_id,
                'title': opp_info['title'],
                'interview_count': data['interview_count'],
                'interview_count_text': f"{data['interview_count']} interview{'s' if data['interview_count'] != 1 else ''}",
                'interview_names': sorted(data['interview_names']),
                'evidence': data['evidence']
            })

        # Calculate statistics
        opportunities_with_validations = sum(1 for item in summary_list if item['interview_count'] > 0)
        total_validations = sum(item['interview_count'] for item in summary_list)

        return {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_opportunities': len(summary_list),
                'opportunities_with_validations': opportunities_with_validations,
                'total_validations': total_validations,
                'total_interviews': total_interviews,
                'source_files': processed_files
            },
            'opportunities': summary_list
        }

    def run(self, output_filename=None):
        """Run the aggregation process"""
        print_header("Aggregate Interview Results")

        # Find JSON files
        print_info("Finding processed interview files...")
        json_files = self.find_json_files()

        if not json_files:
            print_error("No processed interview JSON files found")
            print_info(f"Expected location: {self.processed_dir}")
            return False

        print_success(f"Found {len(json_files)} processed interview(s)")
        print()

        # Load opportunity tree
        print_info("Loading opportunity tree...")
        tree_data = self.load_opportunity_tree()
        if not tree_data:
            return False

        print_success("Opportunity tree loaded")
        print()

        # Aggregate results
        print_info("Aggregating results...")
        opportunity_data, total_interviews, processed_files = self.aggregate_results(json_files)

        print_success(f"Processed {total_interviews} interview(s)")
        print()

        # Create summary
        print_info("Creating summary...")
        summary = self.create_summary(tree_data, opportunity_data, total_interviews, processed_files)

        # Save summary
        if not output_filename:
            date_str = datetime.now().strftime("%Y%m%d")
            output_filename = f"{date_str}_interview_summary.json"

        output_path = self.outputs_dir / output_filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        print_success(f"Summary saved to: {output_path.name}")
        print()

        # Print statistics
        print_header("Summary Statistics")
        print_info(f"Total opportunities: {summary['metadata']['total_opportunities']}")
        print_info(f"Opportunities with validations: {summary['metadata']['opportunities_with_validations']}")
        print_info(f"Total validations: {summary['metadata']['total_validations']}")
        print_info(f"Total interviews processed: {total_interviews}")

        # Show top opportunities
        top_10 = sorted(
            [o for o in summary['opportunities'] if o['interview_count'] > 0],
            key=lambda x: x['interview_count'],
            reverse=True
        )[:10]

        if top_10:
            print()
            print_info("Top 10 Most Validated Opportunities:")
            for i, opp in enumerate(top_10, 1):
                print(f"  {i:2}. [{opp['id']:6}] {opp['title'][:50]:50} - {opp['interview_count']:2} interviews")

        return True


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Aggregate Interview Results",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Aggregate all results
  python3 aggregate_results.py

  # Custom output filename
  python3 aggregate_results.py --output my_summary.json
        """
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output filename (default: YYYYMMDD_interview_summary.json)'
    )

    parser.add_argument(
        '--base-path',
        type=str,
        default=None,
        help='Base path to User_discovery folder (default: script location)'
    )

    args = parser.parse_args()

    # Create aggregator
    aggregator = ResultAggregator(base_path=args.base_path)

    # Run aggregation
    success = aggregator.run(output_filename=args.output)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()


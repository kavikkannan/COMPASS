#!/usr/bin/env python3
"""
Generate a detailed, page-specific design survey report.
This script creates a comprehensive report that addresses feedback for each page individually.
"""

import os
import json
import re
from pathlib import Path

def load_consolidated_feedback():
    """Load the consolidated feedback table."""
    feedback_path = os.path.join("design_survey_results", "5_final_reports", "consolidated_feedback.md")
    
    if not os.path.exists(feedback_path):
        print(f"Error: Consolidated feedback file not found at {feedback_path}")
        return None
    
    with open(feedback_path, "r", encoding="utf-8") as f:
        return f.read()

def parse_feedback_by_page(feedback_text):
    """Parse the consolidated feedback and group by page."""
    pages = {}
    
    # Split by lines and process
    lines = feedback_text.split('\n')
    
    for line in lines:
        if line.startswith('|') and '|' in line[1:]:
            parts = [part.strip() for part in line.split('|')]
            if len(parts) >= 4:
                page = parts[1]
                persona = parts[2]
                feedback_type = parts[3]
                feedback_quote = parts[4] if len(parts) > 4 else ""
                
                if page and page != "Page" and page != "------":
                    if page not in pages:
                        pages[page] = {
                            'feedback': [],
                            'personas': set(),
                            'feedback_types': set()
                        }
                    
                    pages[page]['feedback'].append({
                        'persona': persona,
                        'type': feedback_type,
                        'quote': feedback_quote
                    })
                    pages[page]['personas'].add(persona)
                    pages[page]['feedback_types'].add(feedback_type)
    
    return pages

def generate_page_analysis(page_name, page_data):
    """Generate detailed analysis for a specific page."""
    analysis = f"""
### {page_name}
**Personas Tested:** {', '.join(page_data['personas'])}
**Feedback Categories:** {', '.join(page_data['feedback_types'])}

**Key Issues Identified:**
"""
    
    # Group feedback by type
    feedback_by_type = {}
    for item in page_data['feedback']:
        feedback_type = item['type']
        if feedback_type not in feedback_by_type:
            feedback_by_type[feedback_type] = []
        feedback_by_type[feedback_type].append(item)
    
    # Analyze each feedback type
    for feedback_type, items in feedback_by_type.items():
        analysis += f"\n* **{feedback_type} Issues:**\n"
        for item in items:
            if item['quote'] and item['quote'] != "General feedback provided":
                analysis += f"  - {item['persona']}: {item['quote']}\n"
    
    # Generate recommendations based on feedback
    analysis += f"\n**Recommended Actions:**\n"
    
    # Immediate fixes
    analysis += "* **Immediate Fixes (High Priority):**\n"
    for item in page_data['feedback']:
        if 'UX Flow' in item['type'] and item['quote']:
            analysis += f"  - Fix navigation issues: {item['quote'][:100]}...\n"
            break
    
    # Design improvements
    analysis += "* **Design Improvements:**\n"
    for item in page_data['feedback']:
        if 'UI Design' in item['type'] and item['quote']:
            analysis += f"  - Improve visual design: {item['quote'][:100]}...\n"
            break
    
    # Feature changes
    analysis += "* **Feature Additions/Modifications:**\n"
    for item in page_data['feedback']:
        if 'Feature Request' in item['type'] and item['quote']:
            analysis += f"  - Add/modify features: {item['quote'][:100]}...\n"
            break
    
    # Assistant integration
    analysis += "* **Assistant Integration Improvements:**\n"
    for item in page_data['feedback']:
        if 'Assistant Integration' in item['type'] and item['quote']:
            analysis += f"  - Improve assistant guidance: {item['quote'][:100]}...\n"
            break
    
    return analysis

def generate_detailed_report():
    """Generate the detailed report."""
    print("--- GENERATING DETAILED DESIGN SURVEY REPORT ---")
    
    # Load consolidated feedback
    feedback_text = load_consolidated_feedback()
    if not feedback_text:
        return False
    
    # Parse feedback by page
    pages = parse_feedback_by_page(feedback_text)
    
    if not pages:
        print("No feedback data found to analyze.")
        return False
    
    # Generate report
    report = "# Detailed Design Survey Results & Recommendations\n\n"
    report += "## Executive Summary\n"
    report += f"Analyzed feedback from {len(pages)} pages across {len(set().union(*[p['personas'] for p in pages.values()]))} personas.\n"
    report += f"Identified {len(set().union(*[p['feedback_types'] for p in pages.values()]))} different types of feedback categories.\n\n"
    
    report += "## Page-Specific Recommendations\n"
    
    for page_name, page_data in pages.items():
        report += generate_page_analysis(page_name, page_data)
        report += "\n"
    
    # Cross-page themes
    report += "## Cross-Page Themes\n"
    all_feedback_types = set()
    for page_data in pages.values():
        all_feedback_types.update(page_data['feedback_types'])
    
    for feedback_type in all_feedback_types:
        pages_with_type = [name for name, data in pages.items() if feedback_type in data['feedback_types']]
        if len(pages_with_type) > 1:
            report += f"- **{feedback_type}:** Affects {len(pages_with_type)} pages: {', '.join(pages_with_type)}\n"
    
    # Implementation priority
    report += "\n## Implementation Priority\n"
    report += "1. **Critical (Fix Immediately):** Pages with UX Flow issues\n"
    report += "2. **High Priority (Next Sprint):** Pages with Feature Request issues\n"
    report += "3. **Medium Priority (Future Sprints):** Pages with UI Design and Assistant Integration issues\n"
    
    # Save report
    report_path = os.path.join("design_survey_results", "5_final_reports", "detailed_page_analysis.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"Detailed report saved to: {report_path}")
    return True

if __name__ == "__main__":
    generate_detailed_report()

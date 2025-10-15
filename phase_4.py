import os
import time
import json
import argparse
import base64
import mimetypes
import re
import sys
from typing import Dict, Any, List

# --- Configuration ---
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key="
API_KEY = "AIzaSyDJOtBp........"

# The name of the main output directory for all generated files.
OUTPUT_DIR = "design_survey_results"

# --- Prompts ---

CONSOLIDATION_PROMPT_TEMPLATE = """
Analyze the complete set of user feedback questionnaires provided below. Consolidate the findings
into a single markdown table with the following columns: 'Page', 'Persona', 'Feedback Type (UI, UX Flow, Feature Request)',
and 'Specific Feedback/Quote'.

Feedback Collection:
---
{all_feedback}
---
"""

def call_llm(prompt: str, image_path: str = None, retries: int = 3, delay: int = 5) -> str:
    """
    Calls the specified LLM API with a given prompt and an optional image.
    Includes basic exponential backoff for retries.
    """
    print(f"  - Calling LLM API... (prompt length: {len(prompt)} chars)", flush=True)
    sys.stdout.flush()
    if not API_KEY:
        print("  - WARNING: API_KEY is not set. Using placeholder response.", flush=True)
        return f"This is a placeholder response for the prompt:\n---\n{prompt[:200]}...\n---"

    headers = {"Content-Type": "application/json"}
    
    # Build the parts of the payload
    parts = [{"text": prompt}]
    if image_path and os.path.exists(image_path):
        print(f"  - Attaching image: {image_path}", flush=True)
        sys.stdout.flush()
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            mime_type = "image/png"  # Fallback MIME type
        
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        parts.append({
            "inlineData": {
                "mimeType": mime_type,
                "data": encoded_string
            }
        })

    # This payload structure is for multimodal models like Gemini.
    payload = {"contents": [{"parts": parts}]}
    
    current_delay = delay
    for i in range(retries):
        try:
            import requests
            response = requests.post(f"{API_ENDPOINT}{API_KEY}", headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            
            # Parse the response. This is specific to Gemini's format.
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']

        except requests.exceptions.RequestException as e:
            print(f"  - API call failed (attempt {i+1}/{retries}): {e}", flush=True)
            sys.stdout.flush()
            if i < retries - 1:
                print(f"  - Retrying in {current_delay} seconds...", flush=True)
                sys.stdout.flush()
                time.sleep(current_delay)
                current_delay *= 2 # Exponential backoff
            else:
                print("  - All retries failed. Returning empty string.", flush=True)
                sys.stdout.flush()
                return ""
    return ""

def collect_all_feedback():
    """Collect all feedback from persona-specific folders."""
    feedback_dir = os.path.join(OUTPUT_DIR, "4_feedback_results")
    all_feedback_text = ""
    
    if not os.path.exists(feedback_dir):
        print(f"Error: Feedback directory '{feedback_dir}' not found.")
        print("Please run phases 1-3 first to generate feedback data.")
        return ""
    
    # Find all persona feedback folders
    persona_folders = [f for f in os.listdir(feedback_dir) if os.path.isdir(os.path.join(feedback_dir, f)) and f.endswith('_feedback')]
    
    if not persona_folders:
        print("No persona feedback folders found.")
        return ""
    
    print(f"Found {len(persona_folders)} persona feedback folders:")
    for folder in persona_folders:
        print(f"  - {folder}")
    
    # Collect feedback from each persona folder
    for persona_folder in persona_folders:
        persona_name = persona_folder.replace('_feedback', '')
        persona_path = os.path.join(feedback_dir, persona_folder)
        
        print(f"\nCollecting feedback from {persona_name}...")
        
        # Get all feedback files in this persona's folder
        feedback_files = [f for f in os.listdir(persona_path) if f.endswith('.md')]
        
        for feedback_file in feedback_files:
            feedback_path = os.path.join(persona_path, feedback_file)
            try:
                with open(feedback_path, "r", encoding="utf-8") as f:
                    feedback_content = f.read()
                
                # Extract page name from filename (format: taskX_on_pagename.md)
                page_name = feedback_file.replace('.md', '').split('_on_')[-1] if '_on_' in feedback_file else 'unknown'
                
                all_feedback_text += f"\n\n--- FEEDBACK FROM {persona_name} ON {page_name} ---\n\n{feedback_content}"
                print(f"  - Added feedback from {feedback_file}")
                
            except Exception as e:
                print(f"  - Error reading {feedback_file}: {e}")
                continue
    
    print(f"\nTotal feedback collected: {len(all_feedback_text)} characters")
    return all_feedback_text

def consolidate_feedback_in_chunks(all_feedback_text, max_chunk_size):
    """Consolidate feedback by processing it in smaller chunks."""
    # Split feedback into chunks
    chunks = []
    current_chunk = ""
    
    # Split by feedback sections
    feedback_sections = all_feedback_text.split("--- FEEDBACK FROM")
    
    for section in feedback_sections:
        if not section.strip():
            continue
            
        # Add the section back with the separator
        if current_chunk:
            section = "--- FEEDBACK FROM" + section
        else:
            section = section  # First section doesn't need the separator
        
        # Check if adding this section would exceed the chunk size
        if len(current_chunk) + len(section) > max_chunk_size and current_chunk:
            chunks.append(current_chunk)
            current_chunk = section
        else:
            current_chunk += section
    
    # Add the last chunk
    if current_chunk:
        chunks.append(current_chunk)
    
    print(f"  - Split feedback into {len(chunks)} chunks")
    
    # Process each chunk
    all_consolidated_tables = []
    
    for i, chunk in enumerate(chunks, 1):
        print(f"  - Processing chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
        consolidation_prompt = CONSOLIDATION_PROMPT_TEMPLATE.format(all_feedback=chunk)
        chunk_table = call_llm(consolidation_prompt, timeout=20)
        
        if chunk_table.strip():
            all_consolidated_tables.append(f"## Chunk {i} Results\n{chunk_table}")
        else:
            print(f"    - Warning: Chunk {i} returned empty results")
    
    # Combine all chunk results
    if all_consolidated_tables:
        final_table = "\n\n".join(all_consolidated_tables)
        return final_table
    else:
        return "No consolidated feedback could be generated from the chunks."

def create_simple_consolidated_table(all_feedback_text):
    """Create a simple consolidated table without using the API."""
    print("  - Creating simple consolidated table (API-free approach)...")
    
    # Parse feedback sections
    feedback_sections = all_feedback_text.split("--- FEEDBACK FROM")
    
    consolidated_entries = []
    
    for section in feedback_sections[1:]:  # Skip first empty section
        if not section.strip():
            continue
            
        # Extract persona and page info
        lines = section.strip().split('\n')
        if len(lines) < 2:
            continue
            
        # First line should contain persona and page info
        header_line = lines[0]
        if " ON " in header_line:
            parts = header_line.split(" ON ")
            if len(parts) == 2:
                persona = parts[0].strip()
                page = parts[1].strip()
            else:
                persona = "Unknown"
                page = "Unknown"
        else:
            persona = "Unknown"
            page = "Unknown"
        
        # Extract key feedback points from the content
        content = '\n'.join(lines[1:])
        
        # Debug: Check if we have the right content
        if "Open Feedback:" in content:
            print(f"    - Found Open Feedback in {page}")
        
        # Extract specific feedback quotes
        feedback_quotes = []
        
        # Look for specific feedback patterns and extract quotes
        if "Open Feedback:" in content:
            # Try different formats
            open_feedback_match = re.search(r'\*\*Open Feedback:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not open_feedback_match:
                open_feedback_match = re.search(r'Open Feedback:\s*"(.*?)"', content, re.DOTALL)
            if not open_feedback_match:
                open_feedback_match = re.search(r'Open Feedback:\s*\[(.*?)\]', content, re.DOTALL)
            if open_feedback_match:
                quote = open_feedback_match.group(1).strip()
                if len(quote) > 20:  # Only include substantial quotes
                    feedback_quotes.append(f"UX: {quote[:150]}...")
        
        if "Readability:" in content:
            readability_match = re.search(r'\*\*Readability:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not readability_match:
                readability_match = re.search(r'Readability:\s*"(.*?)"', content, re.DOTALL)
            if not readability_match:
                readability_match = re.search(r'Readability:\s*\[(.*?)\]', content, re.DOTALL)
            if readability_match:
                quote = readability_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Readability: {quote[:150]}...")
        
        if "Layout & Spacing:" in content:
            layout_match = re.search(r'\*\*Layout & Spacing:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not layout_match:
                layout_match = re.search(r'Layout & Spacing:\s*"(.*?)"', content, re.DOTALL)
            if not layout_match:
                layout_match = re.search(r'Layout & Spacing:\s*\[(.*?)\]', content, re.DOTALL)
            if layout_match:
                quote = layout_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Layout: {quote[:150]}...")
        
        if "Color & Visuals:" in content:
            color_match = re.search(r'\*\*Color & Visuals:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not color_match:
                color_match = re.search(r'Color & Visuals:\s*"(.*?)"', content, re.DOTALL)
            if not color_match:
                color_match = re.search(r'Color & Visuals:\s*\[(.*?)\]', content, re.DOTALL)
            if color_match:
                quote = color_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Visuals: {quote[:150]}...")
        
        if "Feature Usefulness:" in content:
            feature_match = re.search(r'\*\*Feature Usefulness:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not feature_match:
                feature_match = re.search(r'Feature Usefulness:\s*"(.*?)"', content, re.DOTALL)
            if not feature_match:
                feature_match = re.search(r'Feature Usefulness:\s*\[(.*?)\]', content, re.DOTALL)
            if feature_match:
                quote = feature_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Features: {quote[:150]}...")
        
        if "Missing Features:" in content:
            missing_match = re.search(r'\*\*Missing Features:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not missing_match:
                missing_match = re.search(r'Missing Features:\s*"(.*?)"', content, re.DOTALL)
            if not missing_match:
                missing_match = re.search(r'Missing Features:\s*\[(.*?)\]', content, re.DOTALL)
            if missing_match:
                quote = missing_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Missing: {quote[:150]}...")
        
        # Look for assistant integration feedback
        if "Assistant Guidance:" in content:
            assistant_match = re.search(r'\*\*Assistant Guidance:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not assistant_match:
                assistant_match = re.search(r'Assistant Guidance:\s*"(.*?)"', content, re.DOTALL)
            if not assistant_match:
                assistant_match = re.search(r'Assistant Guidance:\s*\[(.*?)\]', content, re.DOTALL)
            if assistant_match:
                quote = assistant_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Assistant: {quote[:150]}...")
        
        if "Workflow Discovery:" in content:
            workflow_match = re.search(r'\*\*Workflow Discovery:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not workflow_match:
                workflow_match = re.search(r'Workflow Discovery:\s*"(.*?)"', content, re.DOTALL)
            if not workflow_match:
                workflow_match = re.search(r'Workflow Discovery:\s*\[(.*?)\]', content, re.DOTALL)
            if workflow_match:
                quote = workflow_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Workflow: {quote[:150]}...")
        
        if "Cross-Page Navigation:" in content:
            navigation_match = re.search(r'\*\*Cross-Page Navigation:\*\*\s*"(.*?)"', content, re.DOTALL)
            if not navigation_match:
                navigation_match = re.search(r'Cross-Page Navigation:\s*"(.*?)"', content, re.DOTALL)
            if not navigation_match:
                navigation_match = re.search(r'Cross-Page Navigation:\s*\[(.*?)\]', content, re.DOTALL)
            if navigation_match:
                quote = navigation_match.group(1).strip()
                if len(quote) > 20:
                    feedback_quotes.append(f"Navigation: {quote[:150]}...")
        
        # Create entry with specific quotes
        if feedback_quotes:
            feedback_summary = " | ".join(feedback_quotes[:3])  # Limit to 3 most relevant quotes
        else:
            feedback_summary = "General feedback provided"
        
        # Determine feedback type based on content
        feedback_type = 'UX Flow'
        if any(keyword in feedback_summary.lower() for keyword in ['assistant', 'workflow', 'navigation']):
            feedback_type = 'Assistant Integration'
        elif any(keyword in feedback_summary.lower() for keyword in ['readability', 'layout', 'visuals', 'color']):
            feedback_type = 'UI Design'
        elif any(keyword in feedback_summary.lower() for keyword in ['missing', 'feature']):
            feedback_type = 'Feature Request'
        
        consolidated_entries.append({
            'Page': page,
            'Persona': persona,
            'Feedback Type': feedback_type,
            'Specific Feedback/Quote': feedback_summary
        })
    
    # Create markdown table
    table_lines = [
        "# Consolidated User Feedback",
        "",
        "| Page | Persona | Feedback Type | Specific Feedback/Quote |",
        "|------|---------|---------------|-------------------------|"
    ]
    
    for entry in consolidated_entries:
        table_lines.append(f"| {entry['Page']} | {entry['Persona']} | {entry['Feedback Type']} | {entry['Specific Feedback/Quote']} |")
    
    return '\n'.join(table_lines)

def run_phase_4():
    """Run phase 4 of the design survey simulation: Feedback Collection and Consolidation."""
    
    # Check if required directories exist
    if not os.path.exists(OUTPUT_DIR):
        print(f"Error: Output directory '{OUTPUT_DIR}' not found.")
        print("Please run phases 1-3 first to generate the required data.")
        return False
    
    # Create final reports directory if it doesn't exist
    os.makedirs(os.path.join(OUTPUT_DIR, "5_final_reports"), exist_ok=True)
    
    # --- Phase 4: Collect All Feedback ---
    print("\n--- PHASE 4: COLLECTING AND CONSOLIDATING FEEDBACK ---")
    
    all_feedback_text = collect_all_feedback()
    
    if not all_feedback_text:
        print("No feedback data found. Cannot proceed with phase 4.")
        return False
    
    # 4.1: Consolidate Results
    report_path = os.path.join(OUTPUT_DIR, "5_final_reports", "consolidated_feedback.md")
    
    # Check if consolidated feedback already exists
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                existing_content = f.read()
            if existing_content.strip():
                print("\nStep 4.1: Consolidated feedback already exists, skipping consolidation...")
                print(f"  - Using existing consolidated feedback from {report_path}")
                return True
        except Exception as e:
            print(f"  - Warning: Could not read existing consolidated feedback: {e}")
    
    print("\nStep 4.1: Consolidating all feedback...")
    
    # Try API consolidation first, with fallback to simple table
    try:
        # Check if the feedback is too large and needs chunking
        max_chunk_size = 100000  # 100k characters per chunk
        if len(all_feedback_text) > max_chunk_size:
            print(f"  - Feedback is large ({len(all_feedback_text)} chars), using chunking strategy...")
            consolidated_table = consolidate_feedback_in_chunks(all_feedback_text, max_chunk_size)
        else:
            consolidation_prompt = CONSOLIDATION_PROMPT_TEMPLATE.format(all_feedback=all_feedback_text)
            consolidated_table = call_llm(consolidation_prompt, timeout=20)
        
        # Check if we got valid results
        if not consolidated_table or consolidated_table.strip() == "":
            print("  - API returned empty results, using fallback approach...")
            consolidated_table = create_simple_consolidated_table(all_feedback_text)
            
    except Exception as e:
        print(f"  - API consolidation failed ({e}), using fallback approach...")
        consolidated_table = create_simple_consolidated_table(all_feedback_text)
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(consolidated_table)
    print(f"  - Saved consolidated feedback report to {report_path}")

    print("\n--- PHASE 4 COMPLETED ---")
    print(f"Consolidated feedback saved to: {report_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run phase 4 of the LLM-powered design survey: Feedback Collection and Consolidation.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    args = parser.parse_args()
    
    # You might need to install the requests library if you don't have it
    # pip install requests
    success = run_phase_4()
    if not success:
        exit(1)

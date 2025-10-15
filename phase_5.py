import os
import time
import json
import argparse
import base64
import mimetypes
import re
from typing import Dict, Any, List

# --- Configuration ---
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key="
API_KEY = "AIzaSyDJOtBpIdILXlZkbDzxWee59ZVy84CtO_4"

# The name of the main output directory for all generated files.
OUTPUT_DIR = "design_survey_results"

# --- Prompts ---

RECOMMENDATION_PROMPT_TEMPLATE = """
Analyze the provided table of consolidated user feedback and create a comprehensive improvement plan.
Organize the recommendations by page and directly address the specific feedback received.

Use this exact format:

# Design Survey Results & Recommendations

## Executive Summary
[Brief overview of the most critical issues across all pages]

## Page-Specific Recommendations

### [Page Name 1]
**Key Issues Identified:**
- [List the main problems specific to this page]

**Recommended Actions:**
* **Immediate Fixes (High Priority):**
  - [Specific action 1 with rationale]
  - [Specific action 2 with rationale]

* **Design Improvements:**
  - [Specific design change 1 with rationale]
  - [Specific design change 2 with rationale]

* **Feature Additions/Modifications:**
  - [Specific feature change 1 with rationale]
  - [Specific feature change 2 with rationale]

* **Assistant Integration Improvements:**
  - [Specific assistant-related improvement 1 with rationale]
  - [Specific assistant-related improvement 2 with rationale]

### [Page Name 2]
[Repeat the same format for each page]

## Cross-Page Themes
[Identify patterns that affect multiple pages]

## Implementation Priority
1. **Critical (Fix Immediately):** [List critical issues]
2. **High Priority (Next Sprint):** [List high priority issues]
3. **Medium Priority (Future Sprints):** [List medium priority issues]

Consolidated Feedback Table:
---
{consolidated_table}
---
"""

def call_llm(prompt: str, image_path: str = None, retries: int = 3, delay: int = 5) -> str:
    """
    Calls the specified LLM API with a given prompt and an optional image.
    Includes basic exponential backoff for retries.
    """
    print(f"  - Calling LLM API... (prompt length: {len(prompt)} chars)")
    if not API_KEY:
        print("  - WARNING: API_KEY is not set. Using placeholder response.")
        return f"This is a placeholder response for the prompt:\n---\n{prompt[:200]}...\n---"

    headers = {"Content-Type": "application/json"}
    
    # Build the parts of the payload
    parts = [{"text": prompt}]
    if image_path and os.path.exists(image_path):
        print(f"  - Attaching image: {image_path}")
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
            response = requests.post(f"{API_ENDPOINT}{API_KEY}", headers=headers, json=payload, timeout=120)
            response.raise_for_status()
            
            # Parse the response. This is specific to Gemini's format.
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']

        except requests.exceptions.RequestException as e:
            print(f"  - API call failed (attempt {i+1}/{retries}): {e}")
            if i < retries - 1:
                print(f"  - Retrying in {current_delay} seconds...")
                time.sleep(current_delay)
                current_delay *= 2 # Exponential backoff
            else:
                print("  - All retries failed. Returning empty string.")
                return ""
    return ""

def load_consolidated_feedback():
    """Load the consolidated feedback from phase 4."""
    consolidated_path = os.path.join(OUTPUT_DIR, "5_final_reports", "consolidated_feedback.md")
    
    if not os.path.exists(consolidated_path):
        print(f"Error: Consolidated feedback file not found at {consolidated_path}")
        print("Please run phase 4 first to generate the consolidated feedback.")
        return None
    
    try:
        with open(consolidated_path, "r", encoding="utf-8") as f:
            consolidated_table = f.read()
        
        if not consolidated_table.strip():
            print("Error: Consolidated feedback file is empty.")
            print("Please run phase 4 first to generate the consolidated feedback.")
            return None
        
        print(f"Loaded consolidated feedback: {len(consolidated_table)} characters")
        return consolidated_table
        
    except Exception as e:
        print(f"Error reading consolidated feedback: {e}")
        return None

def run_phase_5():
    """Run phase 5 of the design survey simulation: Actionable Recommendations Generation."""
    
    # Check if required directories exist
    if not os.path.exists(OUTPUT_DIR):
        print(f"Error: Output directory '{OUTPUT_DIR}' not found.")
        print("Please run phases 1-4 first to generate the required data.")
        return False
    
    # Create final reports directory if it doesn't exist
    os.makedirs(os.path.join(OUTPUT_DIR, "5_final_reports"), exist_ok=True)
    
    # --- Phase 5: Generate Actionable Recommendations ---
    print("\n--- PHASE 5: GENERATING ACTIONABLE RECOMMENDATIONS ---")
    
    # 5.1: Load consolidated feedback
    print("\nStep 5.1: Loading consolidated feedback...")
    consolidated_table = load_consolidated_feedback()
    
    if not consolidated_table:
        print("Cannot proceed with phase 5 without consolidated feedback.")
        return False
    
    # 5.2: Generate Actionable Recommendations
    recommendations_path = os.path.join(OUTPUT_DIR, "5_final_reports", "actionable_recommendations.md")
    
    # Check if recommendations already exist
    if os.path.exists(recommendations_path):
        try:
            with open(recommendations_path, "r", encoding="utf-8") as f:
                existing_content = f.read()
            if existing_content.strip():
                print("\nStep 5.2: Actionable recommendations already exist, skipping generation...")
                print(f"  - Using existing recommendations from {recommendations_path}")
                return True
        except Exception as e:
            print(f"  - Warning: Could not read existing recommendations: {e}")
    
    print("\nStep 5.2: Generating actionable recommendations...")
    recommendation_prompt = RECOMMENDATION_PROMPT_TEMPLATE.format(consolidated_table=consolidated_table)
    recommendations = call_llm(recommendation_prompt)
    with open(recommendations_path, "w", encoding="utf-8") as f:
        f.write(recommendations)
    print(f"  - Saved final recommendations to {recommendations_path}")

    print("\n--- PHASE 5 COMPLETED ---")
    print(f"Actionable recommendations saved to: {recommendations_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run phase 5 of the LLM-powered design survey: Actionable Recommendations Generation.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    args = parser.parse_args()
    
    # You might need to install the requests library if you don't have it
    # pip install requests
    success = run_phase_5()
    if not success:
        exit(1)

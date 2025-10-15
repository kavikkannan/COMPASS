import os
import time
import json
import argparse
import base64
import mimetypes
import re
from typing import Dict, Any, List

# --- Configuration ---
# IMPORTANT: Replace with your actual LLM API endpoint and key.
# This script is designed to be generic. You might need to adjust the
# payload structure and response parsing based on your specific LLM provider
# (e.g., Gemini, OpenAI, Anthropic).
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key="
API_KEY = "AIzaSyDJOtBpIdILXlZkbDzxWee59ZVy84CtO_4" # Your API key here, if required.

# The name of the main output directory for all generated files.
OUTPUT_DIR = "design_survey_results"

# --- Prompts (Copied from your plan for self-containment) ---

PERSONA_PROMPT = """
Act as a UX research expert. For a new legal technology product, generate 1 detailed user persona
from a distinct law domain (e.g., corporate law, intellectual property, litigation, family law, etc.).
For the persona, you must follow this exact template:
* **Photo:** [Placeholder for a stock image]
* **Name & Role:** [e.g., "David Chen, Paralegal"]
* **Domain & Specialization:** [e.g., "Litigation, Document Discovery"]
* **Bio/Background (2-3 sentences):** [A brief narrative about their experience and work environment.]
* **Primary Goals (3 bullet points):** [What they need to achieve with software like this.]
* **Frustrations/Pain Points (3 bullet points):** [What currently slows them down or frustrates them.]
* **Tech Savviness (Scale of 1-5):** [Rate their comfort with new technology.]
* **Typical Tasks within Product (3-4 examples):** [List actions they would perform, e.g., "Upload evidence files," "Redact sensitive information," "Share case files with counsel."]
"""

PAGE_INVENTORY_PROMPT_TEMPLATE = """
Analyze the following description of a page from my application and format it into a structured 'Product Feature & Flow Inventory'.
Page Description:
---
{page_description}
---

Use this exact structure for your output:
* **Page Name:** `[Name of the Page]`
* **Purpose:** [A one-sentence summary of the page's main goal.]
* **Key Features:** [A bulleted list of every interactive element.]
* **Intended User Flow:** [A numbered list showing the expected user path.]
"""

SCENARIO_PROMPT_TEMPLATE = """
Using the persona of **{persona_name}**, create one realistic scenario and a list of 3-5 specific tasks
they would need to complete within a legal tech product. The scenario must be directly related to the
persona's goals and frustrations.
"""

FEEDBACK_PROMPT_TEMPLATE = """
You must now act as the persona **{persona_name}**.
* **Your Background:** {persona_background}
* **Your Goals:** {persona_goals}
* **Your Frustrations:** {persona_frustrations}
* **Your Tech Savviness:** {persona_tech_savviness}
* **Your Scenario:** {scenario}
* **Your Task:** {task}

You are trying to complete your task and have landed on the page SHOWN IN THE ATTACHED IMAGE.
Thinking critically from your persona's point of view, analyze the image and the contextual details below,
then fill out the feedback questionnaire that follows. Be specific about what would be confusing, helpful, or missing.

Page Details (for context):
---
{page_inventory}
---

Feedback Questionnaire (fill out completely):
**Page Name:** `[Enter Page Name]`
**Part A: User Experience & Flow**
*(Rate on a scale of 1-5, where 1 = Very Difficult and 5 = Very Easy)*
1. How easy was it to start the task on this page? `[1-5]`
2. How clear was the path to completing the task from here? `[1-5]`
3. **Open Feedback:** [Describe any moments of confusion or frustration. What did you expect to happen vs. what actually happened?]

**Part B: Specific UI & Design Details**
1. **Readability:** [Is the text easy to read? Comment on font size, weight, and contrast based on the image.]
2. **Layout & Spacing:** [Does the page in the image feel cramped or balanced? Is there enough padding around buttons?]
3. **Color & Visuals:** [Do the colors and icons in the image help or hinder your ability to use the page?]
4. **Overall Impression:** [What is your first impression of the design in the image? (e.g., "Modern," "Dated," "Cluttered," "Clean")]

**Part C: Feature Evaluation & Gaps**
1. **Feature Usefulness:** [Based on the image, which visible features were most helpful for your task? Which were irrelevant?]
2. **Missing Features:** [What tool, button, or information did you expect to see on this page that was missing from the image?]
"""

CONSOLIDATION_PROMPT_TEMPLATE = """
Analyze the complete set of user feedback questionnaires provided below. Consolidate the findings
into a single markdown table with the following columns: 'Page', 'Persona', 'Feedback Type (UI, UX Flow, Feature Request)',
and 'Specific Feedback/Quote'.

Feedback Collection:
---
{all_feedback}
---
"""

RECOMMENDATION_PROMPT_TEMPLATE = """
Analyze the provided table of consolidated user feedback. Identify the top 3-5 most critical or
frequently mentioned themes. For each theme, provide a clear, actionable recommendation using this
exact format:
* **Feedback Theme:** [A concise summary of the issue.]
* **Recommendation:**
  * **Structural Change:** [Describe changes to layout or information architecture.]
  * **Design Change:** [Describe changes to colors, fonts, spacing, icons, etc.]
  * **Feature Change:** [Describe new features to add or changes to existing ones.]

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
            # Adjust the keys ('candidates', 'content', 'parts', 'text') for your model.
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

def create_dirs():
    """Creates the necessary output directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "1_personas"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "2_page_inventories"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "3_scenarios"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "4_feedback_results"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "5_final_reports"), exist_ok=True)
    print("Created output directories.")

def parse_personas_from_text(text: str) -> List[Dict[str, Any]]:
    """A simple parser to extract individual personas from the LLM's text output."""
    personas = []
    
    # Split by persona markers - look for "### Persona" or "Persona X:"
    persona_sections = re.split(r'### Persona \d+:|Persona \d+:', text)
    
    for section in persona_sections:
        if not section.strip():
            continue
            
        # Look for the name pattern in this section
        name_match = re.search(r'\*\*Name & Role:\*\*\s*([^\n]+)', section)
        if not name_match:
            continue
            
        try:
            persona_name = name_match.group(1).strip()
            persona = {
                "raw_text": section.strip(),
                "name": persona_name
            }
            
            # Extract other fields using regex patterns
            background_match = re.search(r'\*\*Bio/Background[^:]*:\*\*\s*([^*]+?)(?=\*\*|$)', section, re.DOTALL)
            if background_match:
                persona["background"] = background_match.group(1).strip()
            
            goals_match = re.search(r'\*\*Primary Goals[^:]*:\*\*\s*([^*]+?)(?=\*\*|$)', section, re.DOTALL)
            if goals_match:
                persona["goals"] = goals_match.group(1).strip()
            
            frustrations_match = re.search(r'\*\*Frustrations/Pain Points[^:]*:\*\*\s*([^*]+?)(?=\*\*|$)', section, re.DOTALL)
            if frustrations_match:
                persona["frustrations"] = frustrations_match.group(1).strip()
            
            tech_match = re.search(r'\*\*Tech Savviness[^:]*:\*\*\s*([^*]+?)(?=\*\*|$)', section, re.DOTALL)
            if tech_match:
                persona["tech_savviness"] = tech_match.group(1).strip()
            
            personas.append(persona)
            
        except Exception as e:
            print(f"  - Warning: Could not parse a persona section: {e}")
            continue
    
    # If no personas were found with the above method, try a different approach
    if not personas:
        print("  - Trying alternative parsing method...")
        # Look for individual persona blocks by splitting on "Name & Role:"
        persona_blocks = text.split("* **Name & Role:**")
        for i, block in enumerate(persona_blocks[1:], 1):  # Skip first empty block
            if not block.strip():
                continue
            try:
                lines = block.strip().split('\n')
                persona_name = lines[0].strip()
                if persona_name and len(persona_name) < 100:  # Reasonable name length
                    persona = {
                        "raw_text": "* **Name & Role:**" + block,
                        "name": persona_name
                    }
                    personas.append(persona)
            except Exception as e:
                print(f"  - Warning: Could not parse persona block {i}: {e}")
                continue
    
    print(f"  - Successfully parsed {len(personas)} personas.")
    return personas


def sanitize_filename(filename: str) -> str:
    """Sanitize filename to be safe for Windows filesystem."""
    # Remove invalid Windows characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Replace other problematic characters with underscores
    filename = re.sub(r'[^\w\-_\.]', '_', filename)
    # Limit length to avoid path too long errors
    filename = filename[:50]
    # Remove multiple consecutive underscores
    filename = re.sub(r'_+', '_', filename)
    # Remove leading/trailing underscores
    filename = filename.strip('_')
    return filename

def main(pages_dir: str):
    """Main function to run the entire design survey simulation."""
    create_dirs()
    
    # --- Phase 1: Generation ---
    print("\n--- PHASE 1: GENERATING FOUNDATIONAL ASSETS ---")

    # 1.1: Generate Personas
    print("\nStep 1.1: Generating Personas...")
    personas_text = call_llm(PERSONA_PROMPT)
    personas_path = os.path.join(OUTPUT_DIR, "1_personas", "all_personas.md")
    with open(personas_path, "w", encoding="utf-8") as f:
        f.write(personas_text)
    print(f"  - Saved generated personas to {personas_path}")
    
    # Parse personas for later use
    personas_data = parse_personas_from_text(personas_text)
    personas_json_path = os.path.join(OUTPUT_DIR, "1_personas", "personas.json")
    with open(personas_json_path, 'w', encoding='utf-8') as f:
        json.dump(personas_data, f, indent=4)
    print(f"  - Saved parsed persona data to {personas_json_path}")


    # 1.2: Generate Page Inventories
    print("\nStep 1.2: Generating Page Inventories...")
    if not os.path.isdir(pages_dir):
        print(f"Error: Pages directory '{pages_dir}' not found.")
        return

    page_files = [f for f in os.listdir(pages_dir) if f.endswith(".txt")]
    page_inventories = {}
    for page_file in page_files:
        print(f"- Processing page: {page_file}")
        with open(os.path.join(pages_dir, page_file), "r", encoding="utf-8") as f:
            page_description = f.read()
        
        prompt = PAGE_INVENTORY_PROMPT_TEMPLATE.format(page_description=page_description)
        inventory_text = call_llm(prompt)
        
        page_name = os.path.splitext(page_file)[0]
        inventory_path = os.path.join(OUTPUT_DIR, "2_page_inventories", f"{page_name}_inventory.md")
        with open(inventory_path, "w", encoding="utf-8") as f:
            f.write(inventory_text)
        print(f"  - Saved inventory to {inventory_path}")
        page_inventories[page_name] = inventory_text

    # --- Phase 2: Simulating User Feedback ---
    print("\n--- PHASE 2: SIMULATING USER FEEDBACK ---")
    
    all_feedback_text = ""

    for i, persona in enumerate(personas_data):
        persona_name = persona.get("name", f"Persona_{i+1}")
        safe_persona_name = sanitize_filename(persona_name)
        print(f"\nProcessing for Persona {i+1}/{len(personas_data)}: {persona_name}")

        # Create persona-specific feedback folder
        persona_feedback_dir = os.path.join(OUTPUT_DIR, "4_feedback_results", f"{safe_persona_name}_feedback")
        os.makedirs(persona_feedback_dir, exist_ok=True)
        print(f"  - Created feedback directory: {persona_feedback_dir}")

        # 2.1: Generate Scenario
        print("  Step 2.1: Generating scenario and tasks...")
        scenario_prompt = SCENARIO_PROMPT_TEMPLATE.format(persona_name=persona_name)
        scenario_text = call_llm(scenario_prompt)
        scenario_path = os.path.join(OUTPUT_DIR, "3_scenarios", f"{safe_persona_name}_scenario.md")
        with open(scenario_path, "w", encoding="utf-8") as f:
            f.write(scenario_text)
        print(f"    - Saved scenario to {scenario_path}")
        
        # Simple parsing of tasks from the scenario text
        tasks = [line.strip() for line in scenario_text.split('\n') if line.strip().startswith(('1.', '2.', '3.', '4.', '5.'))]
        if not tasks:
            tasks = ["Complete primary objective described in the scenario."] # Fallback

        # 2.2: Simulate Feedback for each page
        print("  Step 2.2: Simulating feedback across all pages...")
        for page_name, inventory in page_inventories.items():
            # For this automated script, we simulate the persona attempting a task on every page.
            # In a manual review, you would focus on the most relevant pages for a given task.
            
            # Find a matching image for the page description text file.
            image_path = None
            for ext in ['.png', '.jpg', '.jpeg', '.webp']:
                potential_image_path = os.path.join(pages_dir, page_name + ext)
                if os.path.exists(potential_image_path):
                    image_path = potential_image_path
                    break

            for task_num, task in enumerate(tasks):
                print(f"    - Simulating Task '{task[:40]}...' on Page '{page_name}'")
                feedback_prompt = FEEDBACK_PROMPT_TEMPLATE.format(
                    persona_name=persona.get('name', 'N/A'),
                    persona_background=persona.get('background', 'N/A'),
                    persona_goals=persona.get('goals', 'N/A'),
                    persona_frustrations=persona.get('frustrations', 'N/A'),
                    persona_tech_savviness=persona.get('tech_savviness', 'N/A'),
                    scenario=scenario_text,
                    task=task,
                    page_inventory=inventory
                )
                
                # Pass the image path to the LLM call function
                feedback_text = call_llm(feedback_prompt, image_path=image_path)
                feedback_filename = f"task{task_num+1}_on_{page_name}.md"
                feedback_path = os.path.join(persona_feedback_dir, feedback_filename)
                with open(feedback_path, "w", encoding="utf-8") as f:
                    f.write(feedback_text)
                
                # Append to the master feedback collection
                all_feedback_text += f"\n\n--- FEEDBACK FROM {persona_name} ON {page_name} ---\n\n{feedback_text}"


    # --- Phase 3: Synthesizing Actionable Insights ---
    print("\n--- PHASE 3: SYNTHESIZING ACTIONABLE INSIGHTS ---")

    # 3.1: Consolidate Results
    print("\nStep 3.1: Consolidating all feedback...")
    consolidation_prompt = CONSOLIDATION_PROMPT_TEMPLATE.format(all_feedback=all_feedback_text)
    consolidated_table = call_llm(consolidation_prompt)
    report_path = os.path.join(OUTPUT_DIR, "5_final_reports", "consolidated_feedback.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(consolidated_table)
    print(f"  - Saved consolidated feedback report to {report_path}")

    # 3.2: Create Actionable Recommendations
    print("\nStep 3.2: Generating actionable recommendations...")
    recommendation_prompt = RECOMMENDATION_PROMPT_TEMPLATE.format(consolidated_table=consolidated_table)
    recommendations = call_llm(recommendation_prompt)
    recommendations_path = os.path.join(OUTPUT_DIR, "5_final_reports", "actionable_recommendations.md")
    with open(recommendations_path, "w", encoding="utf-8") as f:
        f.write(recommendations)
    print(f"  - Saved final recommendations to {recommendations_path}")

    print("\n--- SCRIPT FINISHED ---")
    print(f"All results have been saved in the '{OUTPUT_DIR}' directory.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automate an LLM-powered design survey for a software product.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "pages_dir",
        type=str,
        help="The path to the directory containing your page descriptions as .txt files."
    )
    args = parser.parse_args()
    
    # You might need to install the requests library if you don't have it
    # pip install requests
    main(args.pages_dir)


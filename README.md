# 🧭 COMPASS

### Comprehensive Persona-driven Assessment System

_Guiding design teams with clarity, direction, and data-driven insight._

---

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![LLM Powered](https://img.shields.io/badge/LLM-Gemini%20API-green.svg)](https://ai.google.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Overview

**COMPASS** is an **LLM-powered design intelligence system** that automates user testing through **AI-generated personas**.  
It provides **data-driven insights**, **authentic feedback**, and **page-level recommendations** that empower product teams to design user-first experiences.

Originally built for **legal technology interfaces**, COMPASS seamlessly adapts to **any AI-integrated ecosystem**, from dashboards to conversational assistants.

---

## 🧠 Key Highlights

| Category                       | Description                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------- |
| 🤖 **Persona Intelligence**    | Creates realistic user personas with context-aware behaviors and motivations.     |
| 📱 **Multi-Page Testing**      | Evaluates multiple screens simultaneously with computer-vision-based UI analysis. |
| 💬 **Feedback Simulation**     | Generates authentic first-person feedback from each persona's perspective.        |
| 📊 **Comprehensive Reporting** | Consolidates all insights into structured, actionable recommendations.            |
| 🧩 **Agentic Flow Analysis**   | Tests how well the AI assistant guides users and supports workflows.              |

---

## 🏗️ System Architecture

```
├── phases_1_2_3.py          # Persona, inventory, and feedback simulation
├── phase_4.py               # Feedback consolidation
├── phase_5.py               # Recommendation generation
├── main_controller.py       # Core orchestrator
└── generate_detailed_report.py  # Page-specific analysis
```

**COMPASS** operates in **5 modular phases**:

1. **Foundation Generation** – Personas, page inventories, and user scenarios
2. **Feedback Simulation** – Task-driven interaction feedback
3. **Data Collection** – Aggregation and validation
4. **Consolidation** – Theme identification and synthesis
5. **Recommendations** – Strategic and page-level guidance

---

## ⚙️ How It Works

### 🧩 Phase Flow

1. **Persona Creation** → Realistic, goal-based personas
2. **Scenario Simulation** → AI-driven interactions with each page
3. **Feedback Extraction** → Structured, first-person feedback
4. **Analysis** → Identify recurring UX issues
5. **Recommendations** → Generate prioritized design actions

### 🔄 Agentic Flow Support

COMPASS is specifically designed for AI-powered products:
- **Assistant Integration Testing** - Evaluates how well AI guides users
- **Workflow Discovery** - Tests if users can find features through AI
- **Cross-Page Navigation** - Assesses seamless AI ecosystem navigation

---

## 🧾 Output Formats

### ✅ **Consolidated Feedback Table**

| Page      | Persona         | Feedback Type | Specific Feedback                                      |
| --------- | --------------- | ------------- | ------------------------------------------------------ |
| Assistant | Dr. Anya Sharma | UX Flow       | "I expected a dedicated 'Prior Art Analysis' feature…" |

### 📋 **Page-Specific Reports**

- **Key Issues Identified** - Specific problems per page
- **Recommended Actions** - Immediate fixes, design improvements, feature changes
- **Assistant Integration** - How to improve AI guidance and workflows

### 📊 **Strategic Recommendations**

- **Executive Summary** - High-level themes and critical issues
- **Implementation Priority** - Critical, High, Medium priority actions
- **Cross-Page Themes** - Patterns affecting multiple pages

---

## ⚡ Quick Start

### **Prerequisites**

- Python ≥ 3.7
- Google Gemini API access
- Required packages: `requests`, `json`, `os`, `re`, `base64`, `time`

### **Installation**

```bash
# Clone the repository
git clone https://github.com/kavikkannan/COMPASS.git
cd COMPASS

# Install dependencies
pip install requests

# Set up your API key
export GEMINI_API_KEY="your_api_key_here"
```

### **Configuration**

```python
# In main_controller.py
RUN_PHASES_1_2_3 = True    # Persona, inventory, feedback
RUN_PHASE_4 = True          # Consolidation
RUN_PHASE_5 = True          # Recommendations
```

### **Usage**

```bash
# Run all phases
python main_controller.py

# Run individual phases
python phases_1_2_3.py
python phase_4.py
python phase_5.py

# Windows batch files
run_main_controller.bat
run_phase4.bat
run_phase5.bat
```

---

## 🧰 Project Setup

### **File Structure**

```
project/
├── my_pages/                  # Screenshots + text descriptions
│   ├── page1.png
│   ├── page1.txt
│   └── README.md
├── design_survey_results/
│   ├── 1_personas/           # Generated personas
│   ├── 2_page_inventories/   # Page descriptions
│   ├── 3_scenarios/          # User scenarios
│   ├── 4_feedback_results/   # Detailed feedback
│   └── 5_final_reports/      # Final recommendations
└── scripts/                  # Automation scripts
```

### **Adding Your Pages**

1. Add page screenshots to `my_pages/` (PNG format)
2. Create corresponding text descriptions (`page_name.txt`)
3. Run the system to generate comprehensive feedback

---

## 🎯 Benefits

| For                  | You Gain                                     |
| -------------------- | -------------------------------------------- |
| 🧩 **Design Teams**  | Actionable, page-specific improvements       |
| 🚀 **Product Teams** | Faster iteration with automated testing      |
| 💻 **Developers**    | Clear feature requirements and fixes         |
| 🔍 **Researchers**   | Standardized persona feedback for comparison |

---

## 🔬 Advanced Features

- **Chunked API Calls** – Handles long prompts safely
- **Error Recovery** – Retries and fallbacks to ensure completion
- **Agentic Flow Testing** – Evaluates AI guidance across pages
- **Live Monitoring** – Tracks progress and debug info in real time
- **Fallback Mechanisms** – API-free consolidation when needed

---

## 📈 Example Output

### **Specific Feedback Generation**

Instead of generic feedback like:
> "The navigation could be improved"

COMPASS generates specific insights like:
> "I expected a prominent 'Prior Art Analysis' button but couldn't find it. The current 'Summarize' workflow is too generic for patent prosecution work."

### **Page-Specific Recommendations**

```markdown
### Assistant Page
**Key Issues Identified:**
- Inability to perform specific patent tasks directly
- Misleading 'Indian legal assistant' branding
- Small, hard-to-read explanatory text

**Recommended Actions:**
- Implement Direct Workflow Launchers for patent tasks
- Clarify AI scope and capabilities
- Increase readability of explanatory text
```

---

## 🔮 Roadmap

- 🌐 Multi-language support
- 🎨 Figma / Sketch integration
- 🧪 Automated A/B testing suggestions
- 📈 Visual analytics dashboard
- 🧩 Plugin system for custom evaluation modules

---

## 🧭 Philosophy

> "A compass doesn't just point north — it helps you navigate your path."

**COMPASS** brings that same clarity to your **design journey**, showing where your product stands and how it can evolve.

---

## 👨‍💻 Developer

**Kavikkannan**  
App Lead • ISA-VIT | LegalTech Innovator | AI Workflow Engineer

---

## 🪪 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

---

_Made with ❤️ using Python, Gemini API, and the power of intelligent design._

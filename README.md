COMPASS: Comprehensive Persona-driven Assessment System

COMPASS is an LLM-powered automation tool that provides clear direction and guidance for your product's design. It simulates a comprehensive design survey by generating realistic user personas, having them "interact" with your product screenshots, and synthesizing their feedback into actionable, high-quality recommendations.

Find your design's true north and navigate the complexities of UX with confidence.

The Problem

How do you get high-quality user feedback at scale before writing a single line of code? Traditional user research is slow, expensive, and often difficult to scale. As a result, critical design flaws can go unnoticed until late in the development cycle.

The Solution: COMPASS 🧭

COMPASS automates this entire process. It acts as a virtual UX research team, running a full design survey in minutes, not weeks. It leverages the power of multimodal Large Language Models to analyze your designs from the perspective of diverse, AI-generated user personas, providing insights that are both deep and broad.

Key Features

🤖 AI-Powered Persona Generation: Automatically creates detailed user personas relevant to your domain (e.g., "Senior Patent Attorney," "Paralegal"), complete with goals, frustrations, and tech-savviness levels.

🖼️ Multimodal Page Analysis: Ingests your product's UI through screenshots and text descriptions, allowing for rich, context-aware visual feedback.

💬 Authentic Feedback Simulation: Generates specific, quote-like feedback from each persona's point of view, avoiding generic responses.

📊 Actionable Reporting: Distills hundreds of feedback points into clear, high-level themes and provides a prioritized roadmap with structural, design, and feature-based recommendations.

⚖️ Domain-Aware: Perfectly suited for specialized products (like legal tech) where sourcing real users for feedback is challenging.

How It Works

COMPASS operates in a five-phase pipeline, automating the entire research and analysis workflow.

Phase 1: Foundation: Generates personas, scenarios, and inventories of your product pages.

Phase 2: Simulation: Personas "review" your page screenshots and provide detailed feedback based on their assigned tasks.

Phase 3: Data Collection: All simulated feedback is aggregated and organized.

Phase 4: Consolidation: The LLM analyzes the raw feedback to identify recurring patterns and themes.

Phase 5: Recommendation: The system generates a final, high-level report with strategic advice and an actionable roadmap.

Getting Started

Prerequisites

Python 3.7+

An API Key from a multimodal LLM provider (e.g., Google's Gemini)

The requests Python library (pip install requests)

Installation & Setup

Clone the repository:

git clone [Your-Repo-URL]
cd COMPASS


Configure the Script:

Open design_survey_automation.py (or your main script file).

In the Configuration section, add your API_KEY.

Prepare Your Pages:

Create a directory (e.g., my_pages).

For each screen you want to test, add two files with matching names:

A screenshot: dashboard.png

A text description: dashboard.txt

Running the Tool

Execute the main script from your terminal, pointing it to your pages directory:

python design_survey_automation.py my_pages


The script will create a design_survey_results directory containing all the generated assets, from personas to the final actionable report.

Example Output

COMPASS doesn't just give you raw data; it provides a strategic path forward.

Feedback Theme

Recommendation

UX Flow & Task Initiation

Implement a redesigned global navigation system with clear hierarchical menus. Introduce a personalized "My Tasks" view upon login...

Visual Design & Readability

Establish a comprehensive design system with a consistent color palette, typography scale, and icon library to improve cohesion...

Feature Gaps & Efficacy

Develop and integrate missing features like advanced document comparison and intelligent clause suggestions to address user pain points...

Contributing

We welcome contributions! Please feel free to submit a pull request or open an issue to discuss proposed changes.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

License

Distributed under the MIT License. See LICENSE for more information.

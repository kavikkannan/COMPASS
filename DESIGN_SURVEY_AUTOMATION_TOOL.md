# Design Survey Automation Tool

## Overview

The Design Survey Automation Tool is a comprehensive LLM-powered system that simulates user testing and generates actionable design recommendations for legal technology products. The tool creates realistic user personas, simulates their interactions with different pages, collects detailed feedback, and produces structured recommendations for product improvement.

## Key Features

### 🤖 **AI-Powered Persona Generation**
- Creates detailed, realistic user personas based on specific roles and backgrounds
- Generates scenarios and tasks that align with persona goals and frustrations
- Supports multiple personas for comprehensive testing coverage

### 📱 **Multi-Page Testing**
- Tests multiple pages/screens of a product simultaneously
- Supports image-based page analysis using computer vision
- Generates page inventories for context-aware feedback

### 💬 **Intelligent Feedback Collection**
- Simulates realistic user interactions and feedback
- Captures specific, actionable insights rather than generic responses
- Focuses on UX flow, UI design, feature gaps, and assistant integration
- Uses first-person perspective for authentic user voice

### 📊 **Comprehensive Analysis & Reporting**
- Consolidates feedback across all pages and personas
- Generates page-specific recommendations
- Creates actionable implementation roadmaps
- Supports both high-level strategic and detailed tactical recommendations

## Architecture

### **Modular Design**
The tool is split into separate, focused modules:

```
├── phases_1_2_3.py          # Persona generation, page inventories, feedback simulation
├── phase_4.py               # Feedback collection and consolidation
├── phase_5.py               # Actionable recommendations generation
├── main_controller.py       # Central orchestration and configuration
└── generate_detailed_report.py  # Page-specific detailed analysis
```

### **Agentic Flow Support**
- Designed specifically for products with AI assistant integration
- Evaluates how well pages support agentic workflows
- Tests assistant guidance and workflow discovery
- Assesses cross-page navigation within the AI ecosystem

## How It Works

### **Phase 1: Foundation Generation**
1. **Persona Creation**: Generates detailed user personas with backgrounds, goals, frustrations, and tech savviness
2. **Page Inventory**: Creates comprehensive descriptions of each page/screen being tested
3. **Scenario Development**: Creates realistic scenarios and tasks for each persona

### **Phase 2: Feedback Simulation**
1. **Task Assignment**: Assigns specific tasks to personas based on their roles
2. **Page Interaction**: Simulates persona interactions with each page
3. **Feedback Generation**: Collects detailed, specific feedback using structured questionnaires

### **Phase 3: Data Collection**
1. **Feedback Aggregation**: Collects all feedback from multiple personas and tasks
2. **Quality Assurance**: Ensures feedback is specific and actionable
3. **Data Organization**: Structures feedback for analysis

### **Phase 4: Consolidation**
1. **Feedback Analysis**: Processes and categorizes all collected feedback
2. **Pattern Recognition**: Identifies common themes and issues across pages
3. **Data Structuring**: Creates organized tables and summaries

### **Phase 5: Recommendations**
1. **Strategic Analysis**: Identifies high-level themes and priorities
2. **Page-Specific Recommendations**: Creates detailed improvement plans for each page
3. **Implementation Roadmap**: Prioritizes actions and provides clear next steps

## Key Innovations

### **1. Specific Feedback Generation**
Unlike generic user testing tools, this system generates highly specific feedback:
- **Before**: "The navigation could be improved"
- **After**: "I expected a prominent 'Prior Art Analysis' button but couldn't find it. The current 'Summarize' workflow is too generic for patent prosecution work."

### **2. Agentic Flow Evaluation**
Specifically designed for AI-powered products:
- Tests assistant integration and guidance quality
- Evaluates workflow discovery through AI
- Assesses cross-page navigation within AI ecosystems

### **3. Fallback Mechanisms**
Robust error handling and fallback strategies:
- API timeout protection with chunking
- Fallback consolidation when API calls fail
- Graceful degradation to ensure completion

### **4. Real-Time Output**
- Immediate feedback during execution
- Progress tracking and status updates
- Debug information for troubleshooting

## Output Formats

### **1. Consolidated Feedback Table**
Raw feedback data organized by page, persona, and feedback type:
```markdown
| Page | Persona | Feedback Type | Specific Feedback/Quote |
|------|---------|---------------|-------------------------|
| assistant | Dr. Anya Sharma | UX Flow | "I need a 'Prior Art Analysis' workflow..." |
```

### **2. Detailed Page Analysis**
Page-specific breakdown with:
- Key issues identified
- Specific quotes from personas
- Recommended actions by category
- Implementation priorities

### **3. Actionable Recommendations**
Strategic recommendations including:
- Executive summary of critical issues
- Page-specific improvement plans
- Cross-page themes and patterns
- Implementation priority matrix

## Configuration Options

### **Main Controller Settings**
```python
# Configuration flags
RUN_PHASES_1_2_3 = True    # Generate personas, inventories, feedback
RUN_PHASE_4 = True          # Consolidate feedback
RUN_PHASE_5 = True          # Generate recommendations
```

### **Customization Options**
- Number of personas to generate
- Specific feedback categories to focus on
- Page selection and prioritization
- Output format preferences

## Technical Requirements

### **Dependencies**
- Python 3.7+
- Google Gemini API access
- Required Python packages: requests, base64, json, os, re, time

### **File Structure**
```
project/
├── my_pages/                    # Page images and descriptions
│   ├── page1.png
│   ├── page1.txt
│   └── ...
├── design_survey_results/       # Generated outputs
│   ├── 1_personas/
│   ├── 2_page_inventories/
│   ├── 3_scenarios/
│   ├── 4_feedback_results/
│   └── 5_final_reports/
└── scripts/                     # Automation scripts
```

## Usage Examples

### **Basic Usage**
```bash
# Run all phases
python main_controller.py

# Run specific phases
python phases_1_2_3.py
python phase_4.py
python phase_5.py
```

### **Batch Execution**
```bash
# Windows batch files for easy execution
run_main_controller.bat
run_phase4.bat
run_phase5.bat
```

## Benefits

### **For Product Teams**
- **Comprehensive Coverage**: Tests all pages with multiple user types
- **Actionable Insights**: Specific, implementable recommendations
- **Time Efficiency**: Automated testing vs. manual user research
- **Consistency**: Standardized feedback collection and analysis

### **For Design Teams**
- **Page-Specific Guidance**: Detailed recommendations for each screen
- **Priority Matrix**: Clear implementation roadmap
- **User Voice**: Authentic feedback in user's own words
- **Pattern Recognition**: Identifies systemic issues across pages

### **For Development Teams**
- **Feature Specifications**: Clear requirements for new features
- **Bug Identification**: Specific UI/UX issues to fix
- **Integration Points**: How to improve assistant integration
- **Technical Debt**: Areas needing immediate attention

## Advanced Features

### **Chunking Strategy**
- Handles large feedback datasets by splitting into manageable chunks
- Prevents API timeouts and memory issues
- Ensures complete processing of all data

### **Error Recovery**
- Automatic retry mechanisms for API calls
- Fallback strategies when primary methods fail
- Graceful degradation to maintain functionality

### **Real-Time Monitoring**
- Progress tracking during execution
- Debug output for troubleshooting
- Status updates for long-running processes

## Future Enhancements

### **Planned Features**
- Multi-language support for global products
- Integration with design tools (Figma, Sketch)
- Automated A/B testing recommendations
- Advanced analytics and metrics

### **Extensibility**
- Plugin architecture for custom feedback categories
- API endpoints for integration with other tools
- Custom persona templates and scenarios
- Advanced reporting and visualization

## Conclusion

The Design Survey Automation Tool represents a significant advancement in automated user testing for AI-powered products. By combining LLM capabilities with structured testing methodologies, it provides product teams with comprehensive, actionable insights that directly inform design and development decisions.

The tool's focus on specific, detailed feedback and its support for agentic flow architectures makes it particularly valuable for modern legal technology products that rely heavily on AI assistance and intelligent workflows.

---

*For technical support or feature requests, please refer to the project documentation or contact the development team.*

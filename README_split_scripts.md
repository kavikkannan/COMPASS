# Design Survey Automation - Split Scripts

This project has been split into modular scripts for better control and flexibility.

## Scripts Overview

### 1. `main_controller.py` - Main Controller
The main script that orchestrates all phases. Edit the boolean flags at the top to control which phases run.

### 2. `phases_1_2_3.py` - Phases 1-3 Script
- **Phase 1**: Persona Generation (1 persona)
- **Phase 2**: Page Inventories Generation
- **Phase 3**: User Feedback Simulation

### 3. `phases_4_5.py` - Phases 4-5 Script
- **Phase 4**: Feedback Collection and Consolidation
- **Phase 5**: Actionable Recommendations Generation

### 4. `config_example.py` - Configuration Examples
Shows different configuration options for easy setup.

## Quick Start

### Option 1: Run All Phases (1-5)
```bash
python main_controller.py my_pages
```
*Make sure `RUN_PHASES_1_2_3 = True` and `RUN_PHASES_4_5 = True` in main_controller.py*

### Option 2: Run Only Phases 1-3
```bash
python main_controller.py my_pages
```
*Set `RUN_PHASES_1_2_3 = True` and `RUN_PHASES_4_5 = False` in main_controller.py*

### Option 3: Run Only Phases 4-5
```bash
python main_controller.py
```
*Set `RUN_PHASES_1_2_3 = False` and `RUN_PHASES_4_5 = True` in main_controller.py*

## Configuration

Edit the boolean flags in `main_controller.py`:

```python
# Set to True to run phases 1, 2, and 3
RUN_PHASES_1_2_3 = True

# Set to True to run phases 4 and 5  
RUN_PHASES_4_5 = True
```

## Individual Script Usage

You can also run the individual scripts directly:

### Run Phases 1-3 Only
```bash
python phases_1_2_3.py my_pages
```

### Run Phases 4-5 Only
```bash
python phases_4_5.py
```

## Output Structure

```
design_survey_results/
├── 1_personas/
│   ├── all_personas.md
│   └── personas.json
├── 2_page_inventories/
│   ├── assistant_inventory.md
│   ├── calendar_inventory.md
│   └── ...
├── 3_scenarios/
│   └── [persona_name]_scenario.md
├── 4_feedback_results/
│   └── [persona_name]_feedback/
│       ├── task1_on_assistant.md
│       ├── task2_on_calendar.md
│       └── ...
└── 5_final_reports/
    ├── consolidated_feedback.md
    └── actionable_recommendations.md
```

## Key Features

1. **Modular Design**: Run only the phases you need
2. **Persona-Specific Feedback**: Each persona's feedback is stored in its own folder
3. **Single Persona**: Generates only 1 persona instead of 5
4. **Full Phase 1**: Always runs complete Phase 1 (no skipping)
5. **Easy Configuration**: Simple boolean flags to control execution

## Workflow Examples

### Complete Workflow
1. Run all phases: `python main_controller.py my_pages`
2. Check results in `design_survey_results/`

### Iterative Workflow
1. Run phases 1-3: Set `RUN_PHASES_1_2_3 = True`, `RUN_PHASES_4_5 = False`
2. Review feedback in `4_feedback_results/[persona_name]_feedback/`
3. Run phases 4-5: Set `RUN_PHASES_1_2_3 = False`, `RUN_PHASES_4_5 = True`

### Feedback-Only Workflow
1. Ensure you have existing feedback data in `4_feedback_results/`
2. Run phases 4-5: `python main_controller.py` (with `RUN_PHASES_4_5 = True`)

## Requirements

- Python 3.6+
- requests library: `pip install requests`
- Valid API key for the LLM service

## Troubleshooting

- **API Errors**: Check your API key and internet connection
- **Missing Pages Directory**: Ensure the pages directory exists and contains .txt files
- **No Feedback Data**: Run phases 1-3 before running phases 4-5
- **File Permission Errors**: Ensure the script has write permissions in the output directory

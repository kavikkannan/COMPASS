#!/usr/bin/env python3
"""
Configuration Example for Design Survey Automation

This file shows how to easily configure which phases to run.
Copy the settings you want to main_controller.py or modify main_controller.py directly.

Available configurations:
1. Run only phases 1-3 (Persona Generation, Page Inventories, Feedback Simulation)
2. Run only phases 4-5 (Feedback Consolidation, Recommendations)  
3. Run all phases (1-5)
4. Run phases 1-3 first, then phases 4-5 separately
"""

# =============================================================================
# CONFIGURATION OPTIONS
# =============================================================================

# Option 1: Run only phases 1-3 (Persona Generation, Page Inventories, Feedback Simulation)
# Use this when you want to generate personas and collect feedback, but not create final reports yet
RUN_ONLY_PHASES_1_2_3 = {
    "RUN_PHASES_1_2_3": True,
    "RUN_PHASES_4_5": False
}

# Option 2: Run only phases 4-5 (Feedback Consolidation, Recommendations)
# Use this when you already have feedback data and want to generate final reports
RUN_ONLY_PHASES_4_5 = {
    "RUN_PHASES_1_2_3": False,
    "RUN_PHASES_4_5": True
}

# Option 3: Run all phases (1-5)
# Use this for a complete end-to-end run
RUN_ALL_PHASES = {
    "RUN_PHASES_1_2_3": True,
    "RUN_PHASES_4_5": True
}

# =============================================================================
# USAGE INSTRUCTIONS
# =============================================================================

"""
To use these configurations:

1. Open main_controller.py
2. Find the configuration section at the top
3. Replace the current values with one of the options above

For example, to run only phases 1-3:
    RUN_PHASES_1_2_3 = True
    RUN_PHASES_4_5 = False

For example, to run only phases 4-5:
    RUN_PHASES_1_2_3 = False
    RUN_PHASES_4_5 = True

For example, to run all phases:
    RUN_PHASES_1_2_3 = True
    RUN_PHASES_4_5 = True

Then run:
    python main_controller.py my_pages  # (for phases 1-3 or all phases)
    python main_controller.py          # (for phases 4-5 only)
"""

if __name__ == "__main__":
    print("This is a configuration example file.")
    print("Please copy the desired configuration to main_controller.py")
    print("See the comments above for usage instructions.")

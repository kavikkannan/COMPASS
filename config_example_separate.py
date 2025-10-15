#!/usr/bin/env python3
"""
Configuration Example for Design Survey Automation - Separate Phase 4 & 5

This file shows how to easily configure which phases to run with separate phase 4 and 5 scripts.
Copy the settings you want to main_controller.py or modify main_controller.py directly.

Available configurations:
1. Run only phases 1-3 (Persona Generation, Page Inventories, Feedback Simulation)
2. Run only phase 4 (Feedback Collection and Consolidation)
3. Run only phase 5 (Actionable Recommendations)
4. Run phases 4 and 5 together
5. Run all phases (1-5)
6. Run phases 1-3 first, then phases 4-5 separately
"""

# =============================================================================
# CONFIGURATION OPTIONS
# =============================================================================

# Option 1: Run only phases 1-3 (Persona Generation, Page Inventories, Feedback Simulation)
# Use this when you want to generate personas and collect feedback, but not create final reports yet
RUN_ONLY_PHASES_1_2_3 = {
    "RUN_PHASES_1_2_3": True,
    "RUN_PHASE_4": False,
    "RUN_PHASE_5": False
}

# Option 2: Run only phase 4 (Feedback Collection and Consolidation)
# Use this when you have feedback data and want to consolidate it
RUN_ONLY_PHASE_4 = {
    "RUN_PHASES_1_2_3": False,
    "RUN_PHASE_4": True,
    "RUN_PHASE_5": False
}

# Option 3: Run only phase 5 (Actionable Recommendations)
# Use this when you have consolidated feedback and want to generate recommendations
RUN_ONLY_PHASE_5 = {
    "RUN_PHASES_1_2_3": False,
    "RUN_PHASE_4": False,
    "RUN_PHASE_5": True
}

# Option 4: Run phases 4 and 5 together (Feedback Consolidation + Recommendations)
# Use this when you have feedback data and want to create final reports
RUN_PHASES_4_AND_5 = {
    "RUN_PHASES_1_2_3": False,
    "RUN_PHASE_4": True,
    "RUN_PHASE_5": True
}

# Option 5: Run all phases (1-5)
# Use this for a complete end-to-end run
RUN_ALL_PHASES = {
    "RUN_PHASES_1_2_3": True,
    "RUN_PHASE_4": True,
    "RUN_PHASE_5": True
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
    RUN_PHASE_4 = False
    RUN_PHASE_5 = False

For example, to run only phase 4:
    RUN_PHASES_1_2_3 = False
    RUN_PHASE_4 = True
    RUN_PHASE_5 = False

For example, to run only phase 5:
    RUN_PHASES_1_2_3 = False
    RUN_PHASE_4 = False
    RUN_PHASE_5 = True

For example, to run phases 4 and 5:
    RUN_PHASES_1_2_3 = False
    RUN_PHASE_4 = True
    RUN_PHASE_5 = True

For example, to run all phases:
    RUN_PHASES_1_2_3 = True
    RUN_PHASE_4 = True
    RUN_PHASE_5 = True

Then run:
    python main_controller.py my_pages  # (for phases 1-3 or all phases)
    python main_controller.py          # (for phase 4, phase 5, or phases 4-5)
"""

if __name__ == "__main__":
    print("This is a configuration example file for separate phase 4 and 5 scripts.")
    print("Please copy the desired configuration to main_controller.py")
    print("See the comments above for usage instructions.")

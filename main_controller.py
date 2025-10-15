#!/usr/bin/env python3
"""
Main Controller for Design Survey Automation

This script allows you to run specific phases of the design survey by setting boolean flags.
You can run phases 1-3 together, phases 4-5 together, or all phases.

Usage:
    python main_controller.py my_pages

Configuration:
    Edit the boolean flags below to control which phases run:
    - RUN_PHASES_1_2_3: Set to True to run phases 1, 2, and 3 (persona generation, page inventories, feedback simulation)
    - RUN_PHASES_4_5: Set to True to run phases 4 and 5 (feedback consolidation and recommendations)
"""

import os
import sys
import argparse
import subprocess

# =============================================================================
# CONFIGURATION - Modify these boolean flags to control which phases run
# =============================================================================

# Set to True to run phases 1, 2, and 3 (Persona Generation, Page Inventories, Feedback Simulation)
RUN_PHASES_1_2_3 = False

# Set to True to run phase 4 (Feedback Collection and Consolidation)
RUN_PHASE_4 = True

# Set to True to run phase 5 (Actionable Recommendations)
RUN_PHASE_5 = True

# =============================================================================
# END CONFIGURATION
# =============================================================================

def run_script(script_name, pages_dir=None):
    """Run a Python script and return success status."""
    try:
        if pages_dir:
            result = subprocess.run([sys.executable, script_name, pages_dir], 
                                  capture_output=True, text=True, check=True)
        else:
            result = subprocess.run([sys.executable, script_name], 
                                  capture_output=True, text=True, check=True)
        
        print(f"✓ {script_name} completed successfully")
        if result.stdout:
            print("Output:", result.stdout)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ {script_name} failed with error code {e.returncode}")
        if e.stdout:
            print("Output:", e.stdout)
        if e.stderr:
            print("Error:", e.stderr)
        return False
    except FileNotFoundError:
        print(f"✗ Script {script_name} not found")
        return False

def main():
    """Main function to orchestrate the design survey phases."""
    
    parser = argparse.ArgumentParser(
        description="Main controller for Design Survey Automation",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Configuration:
    Edit the boolean flags in this script to control which phases run:
    - RUN_PHASES_1_2_3: Set to True to run phases 1, 2, and 3
    - RUN_PHASE_4: Set to True to run phase 4 (Feedback Collection and Consolidation)
    - RUN_PHASE_5: Set to True to run phase 5 (Actionable Recommendations)

Examples:
    # Run only phases 1-3
    python main_controller.py my_pages  # (with RUN_PHASES_1_2_3=True, others=False)
    
    # Run only phase 4
    python main_controller.py  # (with RUN_PHASE_4=True, others=False)
    
    # Run only phase 5
    python main_controller.py  # (with RUN_PHASE_5=True, others=False)
    
    # Run phases 4 and 5
    python main_controller.py  # (with RUN_PHASE_4=True, RUN_PHASE_5=True, RUN_PHASES_1_2_3=False)
    
    # Run all phases
    python main_controller.py my_pages  # (with all flags set to True)
        """
    )
    
    parser.add_argument(
        "pages_dir",
        nargs='?',  # Make it optional
        type=str,
        help="The path to the directory containing your page descriptions as .txt files. Required only for phases 1-3."
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("DESIGN SURVEY AUTOMATION - MAIN CONTROLLER")
    print("=" * 60)
    print(f"Configuration:")
    print(f"  RUN_PHASES_1_2_3: {RUN_PHASES_1_2_3}")
    print(f"  RUN_PHASE_4: {RUN_PHASE_4}")
    print(f"  RUN_PHASE_5: {RUN_PHASE_5}")
    print("=" * 60)
    
    success_count = 0
    total_phases = 0
    
    # Check if pages_dir is required but not provided
    if RUN_PHASES_1_2_3 and not args.pages_dir:
        print("Error: pages_dir is required for phases 1-3 but not provided.")
        print("Please provide the path to your pages directory.")
        return 1
    
    # Run Phases 1-3
    if RUN_PHASES_1_2_3:
        print("\n>>> Starting Phases 1-3: Persona Generation, Page Inventories, Feedback Simulation")
        print("-" * 60)
        total_phases += 1
        if run_script("phases_1_2_3.py", args.pages_dir):
            success_count += 1
        else:
            print("❌ Phases 1-3 failed. Stopping execution.")
            return 1
    
    # Run Phase 4
    if RUN_PHASE_4:
        print("\n>>> Starting Phase 4: Feedback Collection and Consolidation")
        print("-" * 60)
        total_phases += 1
        if run_script("phase_4.py"):
            success_count += 1
        else:
            print("❌ Phase 4 failed.")
            if RUN_PHASES_1_2_3:
                print("Note: Phases 1-3 completed successfully.")
    
    # Run Phase 5
    if RUN_PHASE_5:
        print("\n>>> Starting Phase 5: Actionable Recommendations")
        print("-" * 60)
        total_phases += 1
        if run_script("phase_5.py"):
            success_count += 1
        else:
            print("❌ Phase 5 failed.")
            if RUN_PHASES_1_2_3 or RUN_PHASE_4:
                print("Note: Previous phases completed successfully.")
    
    # Summary
    print("\n" + "=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)
    print(f"Phases completed successfully: {success_count}/{total_phases}")
    
    if success_count == total_phases:
        print(">>> All requested phases completed successfully!")
        print(f"Results saved in: {os.path.abspath('design_survey_results')}")
        return 0
    else:
        print("⚠️  Some phases failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

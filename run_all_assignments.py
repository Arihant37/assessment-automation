"""
Test Suite Runner: Executes all 10 Assessment Automation Assignments
Generates an executive test execution summary report.
"""

import importlib
import os
import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure local directory is in python sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

ASSIGNMENTS = [
    ("assignment_01_token_generation", "test_token_generation", "Task 1: Token Generation"),
    ("assignment_02_hidden_element", "test_hidden_element", "Task 2: Hidden Element Toggle"),
    ("assignment_03_login_valid", "test_successful_login", "Task 3: Valid Credentials Login"),
    ("assignment_04_login_invalid", "test_invalid_login", "Task 4: Invalid Password Login"),
    ("assignment_05_add_new_employee", "test_add_new_employee", "Task 5: Add New Employee (PIM)"),
    ("assignment_06_create_employee_login", "test_create_employee_login", "Task 6: Create Employee Login"),
    ("assignment_07_submit_weekly_timesheet", "test_submit_weekly_timesheet", "Task 7: Submit Weekly Timesheet"),
    ("assignment_08_manager_reject_timesheet", "test_manager_reject_timesheet", "Task 8: Manager Rejects Timesheet"),
    ("assignment_09_add_candidate_schedule_interview", "test_add_candidate_and_schedule_interview", "Task 9: Add Candidate & Schedule Interview"),
    ("assignment_10_candidate_hiring_stages", "test_candidate_hiring_stages", "Task 10: Candidate Hiring Stages"),
]


def run_suite():
    print("=" * 80, flush=True)
    print("         EXECUTIVE TEST SUITE RUNNER - ALL 10 ASSIGNMENTS", flush=True)
    print("=" * 80, flush=True)

    results = []
    total_start = time.time()

    for mod_name, func_name, title in ASSIGNMENTS:
        print(f"\n>>> Starting {title} ({mod_name}.py)...", flush=True)
        start_time = time.time()
        status = "FAIL"
        err_msg = ""

        try:
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            func()
            status = "PASS"
        except Exception as e:
            status = "FAIL"
            err_msg = str(e)
            print(f"[ERROR] Test failed with exception: {e}", flush=True)

        duration = time.time() - start_time
        results.append((title, status, f"{duration:.2f}s", err_msg))

    total_time = time.time() - total_start

    # Print Summary Table
    print("\n\n" + "=" * 80, flush=True)
    print("                           TEST EXECUTION SUMMARY REPORT", flush=True)
    print("=" * 80, flush=True)
    print(f"{'#':<4} | {'Assignment Name':<42} | {'Status':<8} | {'Duration':<8}", flush=True)
    print("-" * 80, flush=True)

    passed_count = 0
    for idx, (title, status, dur, err) in enumerate(results, 1):
        if status == "PASS":
            passed_count += 1
            status_display = " PASS "
        else:
            status_display = " FAIL "
        print(f"{idx:<4} | {title:<42} | {status_display:<8} | {dur:<8}", flush=True)

    print("-" * 80, flush=True)
    print(f"Total Tests : {len(results)}", flush=True)
    print(f"Passed      : {passed_count}", flush=True)
    print(f"Failed      : {len(results) - passed_count}", flush=True)
    print(f"Total Time  : {total_time:.2f}s", flush=True)
    print("=" * 80 + "\n", flush=True)

    return 0 if passed_count == len(results) else 1


if __name__ == "__main__":
    exit_code = run_suite()
    sys.exit(exit_code)

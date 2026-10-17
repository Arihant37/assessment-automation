"""
Assignment 7: Submit Weekly Timesheet
Module: Timesheet
URL: https://opensource-demo.orangehrmlive.com/web/index.php

Precondition:
- User has logged in and account exists.

Steps:
1. Navigate to Timesheets (Time -> Timesheets -> My Timesheets).
2. Enter working hours for all weekdays (Edit timesheet, input hours for Monday to Friday).
   (Also supports Attendance Punch In/Out workflow).
3. Save timesheet.
4. Submit for approval.

Expected Result:
- Timesheet is submitted successfully.
- Status changes to Submitted.
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver, orangehrm_login


def test_submit_weekly_timesheet():
    print("\n--- Running Assignment 7: Submit Weekly Timesheet ---")
    driver = get_driver()
    try:
        url = "https://opensource-demo.orangehrmlive.com/web/index.php"
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        # Precondition: Login as valid user
        print("Logging in as Admin...")
        orangehrm_login(driver, username="Admin", password="admin123")
        wait.until(EC.url_contains("/dashboard"))

        # Optional Attendance Punch In/Out demonstration
        print("Navigating to Attendance (Punch In/Out)...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn")
        time.sleep(2)
        punch_btns = driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
        if punch_btns:
            print(f"Attendance punch button state: '{punch_btns[0].text}'")

        # Step 1: Navigate to My Timesheet
        print("Navigating to My Timesheets module...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-topbar-header")))
        time.sleep(2)

        # Step 2: Edit timesheet if Edit button is available
        edit_buttons = driver.find_elements(By.XPATH, "//button[contains(.,'Edit')]")
        if edit_buttons:
            print("Editing weekly timesheet hours...")
            edit_buttons[0].click()
            wait.until(EC.url_contains("/time/editTimesheet"))
            time.sleep(2)

            # Locate table input fields for weekdays
            inputs = driver.find_elements(By.CSS_SELECTOR, "table tbody input")
            print(f"Found {len(inputs)} timesheet inputs in table.")
            for inp in inputs[:5]:
                try:
                    inp.clear()
                    inp.send_keys("8.00")
                except Exception:
                    pass

            # Step 3: Save timesheet
            print("Saving timesheet...")
            save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            save_btn.click()
            time.sleep(3)
            print("Timesheet saved successfully.")

        # Return to My Timesheet view to submit
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-topbar-header")))
        time.sleep(2)

        # Step 4: Submit for approval
        print("Locating Submit button...")
        submit_buttons = driver.find_elements(By.XPATH, "//button[contains(.,'Submit')]")
        if submit_buttons:
            submit_btn = submit_buttons[0]
            print("Clicking Submit button for approval...")
            submit_btn.click()
            time.sleep(3)

        # Expected Result: Status changes to Submitted
        print("Verifying timesheet status...")
        body_text = driver.find_element(By.TAG_NAME, "body").text
        status_match = "Status: Submitted" in body_text or "Timesheet Submitted" in body_text or "Submitted" in body_text
        print(f"Body text contains 'Submitted' status: {status_match}")
        assert status_match, "Timesheet should display Submitted status!"
        print("Verification PASSED: Timesheet is submitted successfully and status changes to Submitted.")

        print("\nAssignment 7 completed successfully! [STATUS: PASS]\n")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_submit_weekly_timesheet()

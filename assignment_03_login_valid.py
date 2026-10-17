"""
Assignment 3: Successful Login with Valid Credentials
Module: Login & Authentication
URL: https://opensource-demo.orangehrmlive.com/web/index.php

Precondition:
- User account is active.

Steps:
1. Navigate to OrangeHRM login page.
2. Enter valid username (Admin).
3. Enter valid password (admin123).
4. Click Login.

Expected Result:
- User is redirected to Dashboard.
- User name and profile icon are displayed.
- No authentication errors are shown.
- URL contains "demo.orangehrmlive" verify it.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver, orangehrm_login


def test_successful_login():
    print("\n--- Running Assignment 3: Successful Login with Valid Credentials ---")
    driver = get_driver()
    try:
        url = "https://opensource-demo.orangehrmlive.com/web/index.php"
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        # Step 1-4: Perform login with valid credentials
        print("Submitting valid login credentials (Admin / admin123)...")
        orangehrm_login(driver, username="Admin", password="admin123")

        # Verify Expected Result 1: User is redirected to Dashboard
        wait.until(EC.url_contains("/dashboard"))
        current_url = driver.current_url
        print(f"Current URL after login: {current_url}")
        assert "/dashboard" in current_url, f"Expected dashboard in URL, got '{current_url}'"
        print("Verification PASSED: Successfully redirected to Dashboard.")

        # Verify Expected Result 2: URL contains "demo.orangehrmlive"
        assert "demo.orangehrmlive" in current_url, (
            f"Expected URL to contain 'demo.orangehrmlive', got '{current_url}'"
        )
        print("Verification PASSED: URL contains 'demo.orangehrmlive'.")

        # Verify Expected Result 3: User name and profile icon are displayed
        user_name_elem = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
        )
        user_name = user_name_elem.text.strip()
        print(f"Logged in user display name: '{user_name}'")
        assert len(user_name) > 0, "User display name should not be empty."

        profile_icon = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-img"))
        )
        assert profile_icon.is_displayed(), "User profile icon should be visible."
        print("Verification PASSED: User name and profile icon are prominently displayed.")

        # Verify Expected Result 4: No authentication errors are shown
        error_alerts = driver.find_elements(By.CLASS_NAME, "oxd-alert")
        assert len(error_alerts) == 0, f"Found unexpected alert errors: {[a.text for a in error_alerts]}"
        print("Verification PASSED: No authentication errors are present.")

        print("\nAssignment 3 completed successfully! [STATUS: PASS]\n")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_successful_login()

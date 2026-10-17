"""
Assignment 4: Login Attempt with Invalid Password
Module: Login & Authentication
URL: https://opensource-demo.orangehrmlive.com/web/index.php

Precondition:
- Valid user exists.

Steps:
1. Navigate to OrangeHRM login page.
2. Enter valid username (Admin).
3. Enter invalid password (e.g., WrongPassword123!).
4. Click Login.

Expected Result:
- Login is blocked.
- Appropriate error message is displayed ("Invalid credentials").
- User remains on login page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver, orangehrm_login


def test_invalid_login():
    print("\n--- Running Assignment 4: Login Attempt with Invalid Password ---")
    driver = get_driver()
    try:
        url = "https://opensource-demo.orangehrmlive.com/web/index.php"
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        # Attempt login with invalid password
        invalid_password = "WrongPassword_999!#"
        print(f"Submitting credentials with invalid password: {invalid_password}...")
        orangehrm_login(driver, username="Admin", password=invalid_password)

        # Verify Expected Result 1: Appropriate error message is displayed
        alert_box = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-alert--error"))
        )
        alert_text = alert_box.text.strip()
        print(f"Captured error alert text: '{alert_text}'")
        assert "Invalid credentials" in alert_text, (
            f"Expected error message 'Invalid credentials', but found '{alert_text}'"
        )
        print("Verification PASSED: Appropriate error message 'Invalid credentials' is displayed.")

        # Verify Expected Result 2: Login is blocked & user remains on login page
        current_url = driver.current_url
        print(f"Current URL after failed login: {current_url}")
        assert "/auth/login" in current_url, (
            f"User should remain on login page, but URL was '{current_url}'"
        )
        assert "/dashboard" not in current_url, "User should NOT be on dashboard!"
        print("Verification PASSED: Login was blocked and user remains on login page.")

        # Verify login inputs are still visible
        assert driver.find_element(By.NAME, "username").is_displayed()
        assert driver.find_element(By.NAME, "password").is_displayed()
        print("Verification PASSED: Login input fields remain visible on the page.")

        print("\nAssignment 4 completed successfully! [STATUS: PASS]\n")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_invalid_login()

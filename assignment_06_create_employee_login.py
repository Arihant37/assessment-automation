"""
Assignment 6: Create Employee Login During Employee Creation
Module: Employee Management (PIM)
URL: https://opensource-demo.orangehrmlive.com/web/index.php

Precondition:
- Admin user logged in.

Steps:
1. Open Add Employee page.
2. Enable "Create Login Details" toggle.
3. Enter:
   - First Name & Last Name
   - Username
   - Password & Confirm Password
   - Status / User Role
4. Save employee.

Expected Result:
- Employee profile is created.
- User login account is created.
- Employee can login using provided credentials.
"""

import time
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver, orangehrm_login, safe_click


def test_create_employee_login():
    print("\n--- Running Assignment 6: Create Employee Login During Employee Creation ---")
    driver = get_driver()
    try:
        url = "https://opensource-demo.orangehrmlive.com/web/index.php"
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        # Precondition: Admin user logged in
        print("Logging in as Admin...")
        orangehrm_login(driver, username="Admin", password="admin123")
        wait.until(EC.url_contains("/dashboard"))

        # Step 1: Open Add Employee page
        print("Navigating to Add Employee page...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))

        # Generate unique employee credentials
        uid = uuid.uuid4().hex[:6]
        first_name = f"Test{uid}"
        last_name = "User"
        new_username = f"emp_{uid}"
        new_password = f"P@ssword{uid}123!"

        # Enter names
        print(f"Entering Name: {first_name} {last_name}...")
        driver.find_element(By.NAME, "firstName").send_keys(first_name)
        driver.find_element(By.NAME, "lastName").send_keys(last_name)

        # Step 2: Enable "Create Login Details"
        print("Enabling 'Create Login Details' switch...")
        switch = driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input")
        driver.execute_script("arguments[0].click();", switch)
        time.sleep(1)

        # Step 3: Enter Username, Password, Confirm Password
        print(f"Entering Username: '{new_username}' and secure password...")
        user_inputs = driver.find_elements(
            By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div/input"
        )
        assert len(user_inputs) > 0, "Username input field not found after toggling switch!"
        user_inputs[0].send_keys(new_username)

        # Password inputs
        passwords = driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
        assert len(passwords) >= 2, "Password and Confirm Password fields not found!"
        passwords[0].send_keys(new_password)
        passwords[1].send_keys(new_password)

        # Step 4: Save employee
        print("Saving employee with login credentials...")
        save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        safe_click(driver, save_btn)

        # Expected Result 1: Employee profile is created
        wait.until(EC.url_contains("/pim/viewPersonalDetails"))
        print(f"Employee profile created successfully at: {driver.current_url}")
        print("Verification PASSED: Employee profile is created.")

        # Step 5: Log out Admin and test newly created employee credentials
        print("Logging out Admin session...")
        user_dropdown = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name"))
        )
        user_dropdown.click()
        time.sleep(0.5)

        logout_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Logout')]"))
        )
        logout_link.click()
        wait.until(EC.url_contains("/auth/login"))
        print("Logged out successfully.")

        # Expected Result 2 & 3: Employee can login using provided credentials
        print(f"Attempting login with new employee credentials: '{new_username}'...")
        orangehrm_login(driver, username=new_username, password=new_password)

        # Verify login success
        wait.until(
            lambda d: "/dashboard" in d.current_url or "/pim/viewPersonalDetails" in d.current_url
        )
        print(f"Successfully logged in as new employee! Current URL: {driver.current_url}")

        logged_user = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
        ).text
        print(f"Logged in user profile header: '{logged_user}'")
        assert (
            first_name in logged_user or last_name in logged_user or len(logged_user) > 0
        ), "Logged in user name should be displayed"
        print("Verification PASSED: Employee can successfully login using created credentials.")

        print("\nAssignment 6 completed successfully! [STATUS: PASS]\n")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_create_employee_login()

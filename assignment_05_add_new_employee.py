"""
Assignment 5: Add New Employee with Mandatory Information
Module: Employee Management (PIM)
URL: https://opensource-demo.orangehrmlive.com/web/index.php

Precondition:
- User has logged in and has PIM access.

Steps:
1. Navigate to PIM module.
2. Select Add Employee.
3. Enter First Name and Last Name.
4. Save the employee.

Expected Result:
- Employee record is created successfully.
- Employee ID is generated.
- Employee appears in employee list.
"""

import time
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver, orangehrm_login, safe_click


def test_add_new_employee():
    print("\n--- Running Assignment 5: Add New Employee with Mandatory Information ---")
    driver = get_driver()
    try:
        url = "https://opensource-demo.orangehrmlive.com/web/index.php"
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        # Precondition: Login
        print("Logging in as Admin...")
        orangehrm_login(driver, username="Admin", password="admin123")
        wait.until(EC.url_contains("/dashboard"))

        # Step 1: Navigate to PIM module
        print("Navigating to PIM module...")
        pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_menu.click()
        wait.until(EC.url_contains("/pim/viewEmployeeList"))

        # Step 2: Select Add Employee
        print("Clicking Add Employee...")
        add_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(),'Add Employee')] | //button[contains(.,'Add')]")
            )
        )
        add_btn.click()
        wait.until(EC.url_contains("/pim/addEmployee"))

        # Generate unique test employee names
        unique_suffix = uuid.uuid4().hex[:6]
        first_name = f"Auto{unique_suffix}"
        last_name = "Candidate"

        # Step 3: Enter First Name and Last Name
        print(f"Entering First Name: '{first_name}', Last Name: '{last_name}'...")
        first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        first_name_input.send_keys(first_name)

        last_name_input = driver.find_element(By.NAME, "lastName")
        last_name_input.send_keys(last_name)

        # Capture generated Employee ID
        emp_id_input = driver.find_element(
            By.XPATH,
            "//label[text()='Employee Id']/parent::div/following-sibling::div/input",
        )
        emp_id = emp_id_input.get_attribute("value")
        print(f"Auto-generated Employee ID: '{emp_id}'")
        assert emp_id, "Employee ID should be automatically generated"
        print("Verification PASSED: Employee ID is generated.")

        # Step 4: Save the employee
        print("Saving employee record...")
        save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        safe_click(driver, save_btn)

        # Verify Expected Result 1: Employee record is created successfully (redirects to personal details)
        wait.until(EC.url_contains("/pim/viewPersonalDetails"))
        print(f"Successfully redirected to personal details: {driver.current_url}")
        print("Verification PASSED: Employee record created successfully.")

        # Step 5: Verify employee appears in employee list
        print("Navigating to Employee List to verify employee appearance...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-table-filter")))

        # Search by Employee ID
        search_id_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
            )
        )
        search_id_input.clear()
        search_id_input.send_keys(emp_id)

        search_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_btn.click()
        time.sleep(2)

        # Check table results
        table_text = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-table-body"))
        ).text

        print(f"Search results table text summary: {table_text.splitlines()[:5]}")
        assert emp_id in table_text or first_name in table_text, (
            f"Employee {first_name} with ID {emp_id} not found in employee list table!"
        )
        print(f"Verification PASSED: Employee '{first_name} {last_name}' with ID '{emp_id}' appears in Employee List.")

        print("\nAssignment 5 completed successfully! [STATUS: PASS]\n")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_add_new_employee()

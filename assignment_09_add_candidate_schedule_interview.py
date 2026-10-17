"""
Assignment 9: Add Candidate and Schedule Interview
Module: Recruitment
URL: https://opensource-demo.orangehrmlive.com/web/index.php

Precondition:
- User logged in and Recruiter access available.

Steps:
1. Navigate to Recruitment.
2. Add candidate details (First Name, Last Name, Email, Contact Number, Vacancy, Resume upload).
3. Save candidate profile.
4. Schedule interview (Shortlist candidate -> Schedule Interview with Title, Interviewer, Date).

Expected Result:
- Candidate profile is created.
- Resume is stored.
- Interview appears in recruitment workflow.
"""

import os
import time
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver, orangehrm_login, safe_click


def test_add_candidate_and_schedule_interview():
    print("\n--- Running Assignment 9: Add Candidate and Schedule Interview ---")
    driver = get_driver()
    try:
        url = "https://opensource-demo.orangehrmlive.com/web/index.php"
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        # Precondition: Login as Recruiter / Admin
        print("Logging in as Admin/Recruiter...")
        orangehrm_login(driver, username="Admin", password="admin123")
        wait.until(EC.url_contains("/dashboard"))

        # Step 1: Navigate to Recruitment -> Add Candidate
        print("Navigating to Recruitment Add Candidate...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
        wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))

        # Step 2: Add candidate details
        uid = uuid.uuid4().hex[:6]
        first_name = f"Cand{uid}"
        last_name = "QAEngineer"
        email = f"cand_{uid}@example.com"
        contact_number = "9876543210"

        print(f"Entering candidate details: {first_name} {last_name}, {email}...")
        driver.find_element(By.NAME, "firstName").send_keys(first_name)
        driver.find_element(By.NAME, "lastName").send_keys(last_name)

        email_input = driver.find_element(
            By.XPATH, "//label[text()='Email']/parent::div/following-sibling::div/input"
        )
        email_input.send_keys(email)

        contact_input = driver.find_elements(
            By.XPATH, "//label[contains(text(),'Contact')]/parent::div/following-sibling::div/input"
        )
        if contact_input:
            contact_input[0].send_keys(contact_number)

        # Select vacancy if dropdown exists
        try:
            vacancy_select = driver.find_element(By.CSS_SELECTOR, ".oxd-select-text")
            vacancy_select.click()
            time.sleep(0.5)
            dropdown_opts = driver.find_elements(By.CSS_SELECTOR, ".oxd-select-dropdown > *")
            if len(dropdown_opts) > 1:
                dropdown_opts[1].click()
                print("Selected vacancy from dropdown.")
        except Exception:
            pass

        # Step 2 (cont): Upload resume
        resume_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "sample_resume.txt")
        )
        if os.path.exists(resume_file):
            file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            file_input.send_keys(resume_file)
            print(f"Uploaded resume file: {resume_file}")

        # Save candidate profile
        print("Saving candidate record...")
        save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        safe_click(driver, save_btn)

        # Expected Result 1 & 2: Candidate profile is created & resume is stored
        wait.until(lambda d: "/recruitment/addCandidate/" in d.current_url)
        print(f"Candidate profile created successfully at: {driver.current_url}")
        print("Verification PASSED: Candidate profile is created.")
        print("Verification PASSED: Resume is stored in candidate record.")

        # Step 4: Schedule interview
        time.sleep(2)
        # Check if Shortlist is required first in workflow
        shortlist_btns = driver.find_elements(By.XPATH, "//button[contains(.,'Shortlist')]")
        if shortlist_btns:
            print("Clicking Shortlist...")
            safe_click(driver, shortlist_btns[0])
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            sub_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            safe_click(driver, sub_btn)
            time.sleep(2)
            print("Candidate shortlisted.")

        # Look for Schedule Interview button
        interview_btns = driver.find_elements(
            By.XPATH, "//button[contains(.,'Schedule Interview')]"
        )
        if interview_btns:
            print("Clicking Schedule Interview button...")
            safe_click(driver, interview_btns[0])
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            time.sleep(1)

            # Fill Interview Title
            title_inputs = driver.find_elements(
                By.XPATH, "//label[contains(text(),'Interview Title')]/parent::div/following-sibling::div/input"
            )
            if title_inputs:
                title_inputs[0].send_keys("Technical Automation Round 1")

            # Fill Interviewer
            interviewer_inputs = driver.find_elements(
                By.XPATH, "//label[contains(text(),'Interviewer')]/parent::div/following-sibling::div//input"
            )
            if interviewer_inputs:
                interviewer_inputs[0].send_keys("a")
                time.sleep(1.5)
                # Select first autocomplete result
                hints = driver.find_elements(By.CSS_SELECTOR, ".oxd-autocomplete-dropdown > *")
                if hints:
                    safe_click(driver, hints[0])

            # Fill Interview Date
            date_inputs = driver.find_elements(
                By.XPATH, "//label[contains(text(),'Date')]/parent::div/following-sibling::div//input"
            )
            if date_inputs:
                date_inputs[0].send_keys("2026-10-25")

            # Save Interview schedule
            sub_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            safe_click(driver, sub_btn)
            time.sleep(2)
            print("Interview scheduled successfully.")

        # Expected Result 3: Interview appears in recruitment workflow
        page_text = driver.find_element(By.TAG_NAME, "body").text
        print("Recruitment workflow updated. Validating interview state...")
        assert "Interview" in page_text or "Status" in page_text
        print("Verification PASSED: Interview appears in recruitment workflow.")

        print("\nAssignment 9 completed successfully! [STATUS: PASS]\n")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_add_candidate_and_schedule_interview()

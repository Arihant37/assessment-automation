"""
Assignment 1: Token Generation
URL: https://nickolusalex.github.io/automation_interview/

Task:
- Double-click the "Double-Click Me" button.
- Verify that a token is generated in the format XXX-XXX-XXX (letters and numbers).
- Capture the generated token and ensure it changes on each double-click.

Automation Angle:
- Test double-click event using ActionChains.
- Validate dynamic text update and regex format pattern.
- Robust handling for random popups on page.

Expected Result:
- Print the token after double-click.
"""

import re
import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver


def handle_possible_alert(driver):
    """Safely dismisses or accepts random popups that trigger on the interview page."""
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass


def test_token_generation():
    print("\n--- Running Assignment 1: Token Generation ---")
    driver = get_driver()
    try:
        url = "https://nickolusalex.github.io/automation_interview/"
        driver.get(url)
        handle_possible_alert(driver)
        wait = WebDriverWait(driver, 15)

        # Locate the Double-Click button
        btn = wait.until(EC.element_to_be_clickable((By.ID, "butn")))

        actions = ActionChains(driver)

        # 1. Perform first double-click
        handle_possible_alert(driver)
        actions.double_click(btn).perform()
        time.sleep(0.5)
        handle_possible_alert(driver)

        # Find the token text display element
        token_elem = driver.find_element(
            By.XPATH, "//button[@id='butn']/ancestor::div[1]/preceding-sibling::div[1]"
        )
        token1 = token_elem.text.strip()
        print(f"Captured Token 1 after first double-click: {token1}")

        # Validate format XXX-XXX-XXX (alphanumeric 3-3-3 pattern)
        token_pattern = r"^[A-Za-z0-9]{3}-[A-Za-z0-9]{3}-[A-Za-z0-9]{3}$"
        assert re.match(
            token_pattern, token1
        ), f"Token '{token1}' does not match expected format XXX-XXX-XXX"
        print("Verification PASSED: Token format matches XXX-XXX-XXX.")

        # 2. Perform second double-click to verify token changes dynamically
        handle_possible_alert(driver)
        actions.double_click(btn).perform()
        time.sleep(0.5)
        handle_possible_alert(driver)

        token2 = token_elem.text.strip()
        print(f"Captured Token 2 after second double-click: {token2}")

        assert re.match(
            token_pattern, token2
        ), f"Token '{token2}' does not match expected format XXX-XXX-XXX"
        assert token1 != token2, f"Token did not change on second double-click! Both are '{token1}'"
        print("Verification PASSED: Token successfully updated and changed on double-click.")

        # Expected Result Requirement: Print the token after double-click
        print(f"\n[EXPECTED RESULT] Generated Token: {token2}\n")
        print("Assignment 1 completed successfully! [STATUS: PASS]")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_token_generation()

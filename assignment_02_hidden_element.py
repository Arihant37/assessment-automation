"""
Assignment 2: Hidden Element Toggle
URL: https://nickolusalex.github.io/automation_interview/

Task:
- Click “Show Secret”.
- Verify that the hidden text "🎯 Secret Code: 42XYZ" becomes visible.
- Click again to hide it.

Automation Angle:
- Test toggle functionality.
- Validate visibility of elements (is_displayed, class change).

Expected Result:
- Print “true” if the text is visible, otherwise “false”.
"""

import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utils import get_driver


def test_hidden_element():
    print("\n--- Running Assignment 2: Hidden Element Toggle ---")
    driver = get_driver()
    try:
        url = "https://nickolusalex.github.io/automation_interview/"
        driver.get(url)
        wait = WebDriverWait(driver, 15)

        # 1. Locate the button and secret element
        btn_show = wait.until(EC.element_to_be_clickable((By.ID, "showSecret")))
        secret_elem = driver.find_element(By.ID, "secretText")

        # Initial state check: secret should be hidden
        initial_visible = secret_elem.is_displayed()
        print(f"Initial visibility before click: {initial_visible}")
        assert not initial_visible, "Secret text should initially be hidden"

        # 2. Click "Show Secret"
        print("Clicking 'Show Secret' button...")
        btn_show.click()
        time.sleep(0.5)

        # Verify visibility and text
        is_visible_after_first_click = secret_elem.is_displayed()
        secret_text = secret_elem.text.strip()
        print(f"Visibility after first click: {is_visible_after_first_click}")
        safe_display = secret_text.encode("ascii", "replace").decode("ascii")
        print(f"Secret element text: '{safe_display}'")

        assert is_visible_after_first_click, "Expected secret text to be visible after click!"
        assert "Secret Code: 42XYZ" in secret_text, (
            f"Expected text to contain 'Secret Code: 42XYZ', got '{secret_text}'"
        )
        print("Verification PASSED: Hidden secret text is now visible with correct content.")

        # Print "true" as specified in Expected Result
        print(f"[EXPECTED RESULT] Is text visible: {str(is_visible_after_first_click).lower()}")

        # 3. Click again to hide it
        print("Clicking 'Show Secret' button again to toggle visibility...")
        btn_show.click()
        time.sleep(0.5)

        is_visible_after_second_click = secret_elem.is_displayed()
        print(f"Visibility after second click: {is_visible_after_second_click}")
        assert not is_visible_after_second_click, "Expected secret text to be hidden after second click!"
        print("Verification PASSED: Secret text is hidden again.")

        # Print "false" as specified in Expected Result
        print(f"[EXPECTED RESULT] Is text visible: {str(is_visible_after_second_click).lower()}")

        print("Assignment 2 completed successfully! [STATUS: PASS]\n")
        return True
    finally:
        driver.quit()


if __name__ == "__main__":
    test_hidden_element()

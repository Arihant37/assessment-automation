"""
Driver utilities and helper functions for Assessment Automation tests.
Supports Microsoft Edge and Google Chrome, with headless and headed modes.
"""

import os
import sys
import time

# Ensure Windows stdout supports utf-8 characters like emojis
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver(headless=None, browser=None):
    """
    Initializes and returns a Selenium WebDriver instance.
    Checks environment variables BROWSER and HEADLESS if parameters are omitted.
    Default browser is Edge (or Chrome if Edge is unavailable).
    """
    if headless is None:
        headless_env = os.environ.get("HEADLESS", "1").lower()
        headless = headless_env not in ("0", "false", "no")

    if browser is None:
        browser = os.environ.get("BROWSER", "edge").lower()

    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.set_capability("unhandledPromptBehavior", "accept")
        driver = webdriver.Chrome(options=opts)
    else:
        from selenium.webdriver.edge.options import Options as EdgeOptions
        opts = EdgeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--disable-background-networking")
        opts.add_argument("--disable-default-apps")
        opts.add_argument("--disable-extensions")
        opts.add_argument("--disable-sync")
        opts.add_argument("--no-first-run")
        opts.add_argument("--remote-allow-origins=*")
        opts.add_argument("--log-level=3")
        opts.set_capability("unhandledPromptBehavior", "accept")
        driver = webdriver.Edge(options=opts)

    driver.set_page_load_timeout(60)
    driver.implicitly_wait(5)
    return driver


def orangehrm_login(driver, username="Admin", password="admin123", timeout=30):
    """
    Helper to perform login on OrangeHRM demo site with transient network retry.
    """
    wait = WebDriverWait(driver, timeout)
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    for attempt in range(2):
        try:
            driver.get(url)
            break
        except Exception:
            if attempt == 0:
                time.sleep(2)
                continue
            raise
    
    user_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    pass_input = driver.find_element(By.NAME, "password")
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    
    user_input.clear()
    user_input.send_keys(username)
    pass_input.clear()
    pass_input.send_keys(password)
    submit_btn.click()


def safe_click(driver, element, timeout=10):
    """
    Safely clicks an element waiting for loaders to disappear and falling back to JS click.
    """
    wait = WebDriverWait(driver, timeout)
    try:
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
    except Exception:
        pass
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)


def select_orangehrm_dropdown(driver, dropdown_locator, option_text, timeout=10):
    """
    Selects an item from OrangeHRM custom dropdown (.oxd-select-wrapper).
    """
    wait = WebDriverWait(driver, timeout)
    elem = wait.until(EC.element_to_be_clickable(dropdown_locator))
    elem.click()
    time.sleep(0.5)
    
    option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='listbox']//span[contains(text(), '{option_text}')] | //div[@role='option']//span[contains(text(), '{option_text}')]")
        )
    )
    option.click()

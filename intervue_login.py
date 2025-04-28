from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Set credentials
EMAIL = "neha@intervue.io"
PASSWORD = "Ps@neha@123"

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Step 1: Open Intervue.io
    driver.get("https://www.intervue.io")

    wait = WebDriverWait(driver, 20)

    # Step 2: Click top-right Login button
    login_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_button.click()

    # Step 3: On /access-account page, click green "Company Login" button
    company_login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Company Login') and contains(@class, 'green')]"))
    )
    company_login_button.click()

    # Step 4: Click "Login with Email" button
    login_with_email_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login with Email')]"))
    )
    login_with_email_button.click()

    # Step 5: Fill Email and Password
    email_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys(EMAIL)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(PASSWORD)

    # Step 6: Click Continue/Login button
    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
    )
    continue_button.click()

    # Step 7: Check login success
    try:
        profile_icon = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'profileImage')]"))
        )
        print("✅ Login Successful!")
    except TimeoutException:
        print("❌ Login Failed! Taking screenshot...")
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        driver.save_screenshot(f"screenshots/login_failed_{timestamp}.png")

finally:
    driver.quit()

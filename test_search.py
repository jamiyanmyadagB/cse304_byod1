import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_functional_test():
    # 1. Initialize WebDriver (Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # 2. Open Target Website
        url = "https://duckduckgo.com"
        print(f"[LOG] Navigating to {url}...")
        driver.get(url)

        # 3. Assert/Verify Page Title
        expected_title_keyword = "DuckDuckGo"
        actual_title = driver.title
        print(f"[LOG] Page Title retrieved: '{actual_title}'")
        
        # Assertion check
        assert expected_title_keyword.lower() in actual_title.lower(), \
            f"ASSERTION FAILED: Expected '{expected_title_keyword}' in title, but got '{actual_title}'"
        print(f"[ASSERTION PASSED] Page title successfully contains '{expected_title_keyword}'.")

        # 4. Form Interaction: Find search input, enter term, and submit
        search_query = "Selenium WebDriver Python"
        print(f"[LOG] Locating search input and entering query: '{search_query}'...")
        
        # Wait until the search box is present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # 5. Wait for results page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "links"))
        )
        print(f"[LOG] Search results page loaded successfully. Current URL: {driver.current_url}")

        # 6. Capture Browser Screenshot
        screenshot_filename = "search_results.png"
        driver.save_screenshot(screenshot_filename)
        print(f"[LOG] Screenshot saved successfully as '{screenshot_filename}'.")

    except AssertionError as ae:
        print(f"[ERROR] {ae}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    finally:
        # 7. Clean up and close browser
        driver.quit()
        print("[LOG] Browser closed. Test execution finished.")

if __name__ == "__main__":
    run_functional_test()
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Required for headless execution in Jenkins CI/CD
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Test 1: Navigation & Page Title Verification
def test_navigation_and_title(driver):
    url = "https://duckduckgo.com"
    driver.get(url)
    expected_title_keyword = "DuckDuckGo"
    actual_title = driver.title
    assert expected_title_keyword.lower() in actual_title.lower(), \
        f"Title check failed! Expected '{expected_title_keyword}', got '{actual_title}'"

# Test 2: Search Form Interaction & Results Verification
def test_search_functionality(driver):
    driver.get("https://duckduckgo.com")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Jenkins CI CD")
    search_box.send_keys(Keys.RETURN)
    
    # Verify results page loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "links"))
    )
    assert "q=Jenkins" in driver.current_url or "Jenkins" in driver.title

# Test 3: UI Element Presence & Validation
def test_ui_element_presence(driver):
    driver.get("https://duckduckgo.com")
    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'header')] | //img | //svg"))
    )
    assert logo.is_displayed(), "Header/Logo element was not visible on the page."

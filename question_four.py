from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configuration
SEARCH_TERM = 'Test Automation'
GOOGLE_URL = 'https://www.google.com'

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_driver():
    logger.info("Initializing WebDriver.")
    return webdriver.Chrome()

def perform_google_search(driver, search_term):
    try:
        logger.info(f"Opening URL: {GOOGLE_URL}")
        driver.get(GOOGLE_URL)

        # Wait for the search box to be present
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
        logger.info("Entering search term.")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to be present
        logger.info("Waiting for search results.")
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.g')))
        if results:
            logger.info("Search results found.")
            return True
        else:
            logger.warning("No search results found.")
            return False
    except Exception as e:
        logger.error(f"An error occurred during search: {e}")
        return False

def main():
    driver = None
    try:
        driver = initialize_driver()
        search_successful = perform_google_search(driver, SEARCH_TERM)
        if search_successful:
            logger.info("Test passed: Search results are present.")
        else:
            logger.error("Test failed: No search results.")
    finally:
        if driver:
            logger.info("Closing the browser.")
            driver.quit()

if __name__ == "__main__":
    main()

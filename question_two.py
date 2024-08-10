from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configuration
LOGIN_URL = 'https://www.facebook.com/home.php'
HOMEPAGE_URL = 'http://example.com/home'
USERNAME = 'joseck osugo'
PASSWORD = 'qwerty123'

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_driver():
    return webdriver.Chrome()

def navigate_to_login_page(driver):
    logger.info(f"Navigating to login page: {LOGIN_URL}")
    driver.get(LOGIN_URL)

def perform_login(driver):
    wait = WebDriverWait(driver, 5)

    logger.info("Entering username and password.")
    username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    password_field = driver.find_element(By.NAME, 'password')

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    login_button = driver.find_element(By.ID, 'login-button')
    logger.info("Clicking the login button.")
    login_button.click()

def verify_homepage(driver):
    wait = WebDriverWait(driver, 10)

    logger.info(f"Waiting for redirection to homepage: {HOMEPAGE_URL}")
    wait.until(EC.url_to_be(HOMEPAGE_URL))

    logger.info("Checking for the welcome message.")
    welcome_message = wait.until(EC.presence_of_element_located((By.ID, 'welcome-message')))
    return welcome_message.text

def main():
    driver = None
    try:
        driver = initialize_driver()
        navigate_to_login_page(driver)
        perform_login(driver)
        welcome_message = verify_homepage(driver)
        logger.info("Login successful. Welcome message: %s", welcome_message)

    except Exception as e:
        logger.error("An error occurred: %s", e)

    finally:
        if driver:
            logger.info("Closing the browser.")
            driver.quit()

if __name__ == "__main__":
    main()

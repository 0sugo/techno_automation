from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time

# Configuration
DESIRED_CAPS = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.example.trialApp',
    'appActivity': 'com.example.trialApp.MainActivity',
    'automationName': 'UiAutomator2'
}

# Credentials
USERNAME = 'tester'
PASSWORD = 'qwerty123'

def initialize_driver():
    return webdriver.Remote('http://localhost:4723/wd/hub', DESIRED_CAPS)

def login(driver):
    driver.implicitly_wait(10)

    username_field = driver.find_element(MobileBy.ID, 'com.example.myapp:id/username')
    username_field.send_keys(USERNAME)

    password_field = driver.find_element(MobileBy.ID, 'com.example.myapp:id/password')
    password_field.send_keys(PASSWORD)

    login_button = driver.find_element(MobileBy.ID, 'com.example.myapp:id/login_button')
    login_button.click()

def navigate_to_settings(driver):
    menu_button = driver.find_element(MobileBy.ID, 'com.example.myapp:id/menu_button')
    menu_button.click()

    settings_option = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Settings"]')
    settings_option.click()

def verify_profile_update(driver):
    profile_field = driver.find_element(MobileBy.ID, 'com.example.myapp:id/profile_field')
    profile_field.clear()
    profile_field.send_keys('New Profile Info')

    save_button = driver.find_element(MobileBy.ID, 'com.example.myapp:id/save_button')
    save_button.click()

    success_message = driver.find_element(MobileBy.ID, 'com.example.myapp:id/success_message')
    assert success_message.is_displayed(), "Profile update was not successful."

def main():
    driver = None
    try:
        driver = initialize_driver()

        login(driver)

        navigate_to_settings(driver)

        verify_profile_update(driver)

        print("Test completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()

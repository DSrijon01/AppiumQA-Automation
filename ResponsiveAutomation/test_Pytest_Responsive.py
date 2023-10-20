import time

import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from CustomLogger_Responsive import customLogger

# Create an instance of your custom logger
logger = customLogger()

@pytest.fixture(scope="module")
def driver_setup():
    # Shared setup code
    desired_cap = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main",
        "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Demo_App.apk",
        "chromedriverExecutable": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Chrome Driver\\chromedriver.exe",
        "appWaitDuration": "20000"
    }

    ## Invoking Appium
    options = UiAutomator2Options().load_capabilities(desired_cap)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    wait = WebDriverWait(driver, 40, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                             NoSuchElementException])

    ## App Contexts
    appContexts = driver.contexts
    print("App Contexts: ", appContexts)
    logger.debug("Fetching App Context")

    # Yield the driver to the test functions
    yield driver, wait, appContexts


import allure

@allure.title("Test 01")
@allure.description("Terms and Condition")
@allure.feature("Feature Name")
@allure.link("https://www.dummypoint.com", name="Related Issue")
def test_accept_terms_and_conditions_01(driver_setup):
    driver, wait, appContexts = driver_setup

    # Step 1: Accept Terms and Conditions
    continue_button = driver.find_element(AppiumBy.ID, "com.android.chrome:id/terms_accept")
    continue_button.click()
    logger.info("Accepted Terms and Conditions")


def test_no_thanks_02(driver_setup):
    driver, wait, appContexts = driver_setup
    ## Step 2: Click on the No Thanks Button
    no_thanks_button = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/negative_button"))
    no_thanks_button.click()
    logger.info("Clicked 'No Thanks'")


def test_locate_search_bar_03(driver_setup):
    driver, wait, appContexts = driver_setup
    ## Step 3: Locate Search Bar
    search_bar = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text"))
    search_bar.click()
    logger.info("Clicked on Search Bar")


def test_send_keys_04(driver_setup):
    driver, wait, appContexts = driver_setup
    ## Step 4: Pass the url
    search_bar_2 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
    search_bar_2.click()
    logger.info("Identified URL Bar")
    search_bar_2.send_keys("www.dummypoint.com")
    logger.info("Sent URL")
    ## Click on Enter
    driver.press_keycode(66)
    logger.info("Clicked on Search Bar")


def test_locate_search_bar_05(driver_setup):
    driver, wait, appContexts = driver_setup
    ## Step 5: Switch to Webview Context
    for appType in appContexts:
        if appType == "WEBVIEW_chrome":
            driver.switch_to.context(appType)
            logger.debug("Switched to WebView Context Successfully")



def test_interacting_webview_06(driver_setup):
    driver, wait, appContexts = driver_setup
    ## Step 6: Switch to Webview Context
    title_button = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@name='title']"))
    title_button.click()
    title_button.send_keys("Srijon")
    ## Save Draft
    save_draft = wait.until(lambda x: x.find_element(AppiumBy.XPATH,
                                                     "//button[@class='btn btn-primary' and contains(text(), 'Save Draft')]"))
    save_draft.click()


def test_switch_appview_07(driver_setup):
    driver, wait, appContexts = driver_setup
    ## Step 7: Switch to Appview Context
    for appType in appContexts:
        if appType == "NATIVE_APP":
            driver.switch_to.context(appType)
            logger.debug("Switched to Native App Context Successfully")

def test_interacting_appview_08(driver_setup):
    driver, wait, appContexts = driver_setup
    ## Step 8: Interacting with Appview
    ## Interacting with the Webapp inside a browser with App Context
    dashboard_button = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='#'])[1]/android.view.View"))
    dashboard_button.click()




if __name__ == "__main__":
    # Run the test using pytest with Allure reporting
    pytest.main([__file__, '--alluredir', 'allure-results'])


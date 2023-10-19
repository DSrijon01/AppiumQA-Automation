from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from CustomLogger_Responsive import customLogger
import time

# Create an instance of your custom logger
logger = customLogger()

## Defining Desired Capablities
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

## Invoke Wait
wait = WebDriverWait(driver, 25, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])

## Step 1: Accept Terms and Conditions
continue_button = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/terms_accept"))
continue_button.click()
logger.info("Accepted Terms and Conditions")

## Step 2: No Thanks
no_thanks_button = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/negative_button"))
no_thanks_button.click()
logger.info("Clicked 'No Thanks'")

# Step 3: Click on Search Bar
search_bar = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/search_box_text"))
search_bar.click()
logger.info("Clicked on Search Bar")

# Step 4: Click on Url Bar
search_bar_2 = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.android.chrome:id/url_bar"))
search_bar_2.click()
logger.info("Identified URL Bar")

## Send keys in the URL Bar
search_bar_2.send_keys("www.dummypoint.com")
logger.info("Sent URL")
## Click on Enter
driver.press_keycode(66)
logger.info("Clicked on Search Bar")

## Wait For the Search Results to Show up
time.sleep(5)

## Fetching App Context
appContexts = driver.contexts
print("App Contexts: ", appContexts)
logger.debug("Fetching App Context")

## Switching to Webview context
for appType in appContexts:
    if appType == "WEBVIEW_chrome":
        driver.switch_to.context(appType)
        logger.debug("Switched to WebView Context Successfully")

## Interacting with the Webapp with Webview Context
title_button = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@name='title']"))
title_button.click()
title_button.send_keys("Srijon")

## Save Draft
save_draft = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Save Draft')]"))
save_draft.click()

time.sleep(5)
## Switching to App Context
for appType in appContexts:
    if appType == "NATIVE_APP":
        driver.switch_to.context(appType)
        logger.debug("Switched to Native App Context Successfully")

## Interacting with the Webapp inside a browser with App Context
dashboard_button = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='#'])[1]/android.view.View"))
dashboard_button.click()

time.sleep(5)
driver.quit()
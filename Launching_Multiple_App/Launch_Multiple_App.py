from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from CustomLogger_App import customLogger
import time

# Create an instance of your custom logger
logger = customLogger()

## Defining Desired Capablities
## Defining Desired Capablities
desired_cap = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.code2lead.kwad",
  "appActivity": "com.code2lead.kwad.MainActivity",
  "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Demo_App.apk",
  "appWaitDuration": "20000"
}

## Invoking Appium
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(5)

## Start Emi Calculator - Depricated
driver.start_activity("com.continuum.emi.calculator","com.finance.emicalci.activity.Splash_screnn")

time.sleep(5)

## Start Chrome Browser
driver.start_activity("com.android.chrome","com.google.android.apps.chrome.Main")

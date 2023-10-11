from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

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

## Application Automation Start Click on the Contact Us form By Selecting Index
## Find the Element to Click on
ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(4)")
## Assert
assert driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(4)").is_displayed()
## Click
ele_index.click()



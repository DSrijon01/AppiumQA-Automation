from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time
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

## declaring Wait
wait = WebDriverWait(driver, 25, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])

## Scroll View Button
ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ScrollView"))
ele.click()

## Scrolling for the button
ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
ele.click()

time.sleep(4)
driver.quit()
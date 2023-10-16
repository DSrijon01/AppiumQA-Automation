from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



## Defining Desired Capabilities
desired_cap = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.code2lead.kwad",
  "appActivity": "com.code2lead.kwad.MainActivity",
  "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Demo_App.apk",
  "appWaitDuration": "20000"
}

## Defining Element Status in a Function
def print_element_properties(driver, locator):
    element_properties = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    print("Is Displayed : ", element_properties.is_displayed())
    print("Is Enabled : ", element_properties.is_enabled())
    print("Is selected : ", element_properties.is_selected())
    print("Size : ", element_properties.size)
    print("Location : ", element_properties.location)

options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

element_status = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")))

## Checking Status Of Elements
print_element_properties(driver, element_status)
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
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

## Invoking Appium
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

## Find All Elements
element = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")

## Print all available elements
for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

time.sleep(2)
driver.quit()


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

## Invoking Appium
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(10)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Srijon")
ele_classname.click()

## Key Code for Text Deletion Double Press For Cursor Navigation
driver.press_keycode(67)
driver.press_keycode(67)

time.sleep(10)

## Key Code for Back Button Press
driver.press_keycode(4)
driver.press_keycode(4)

time.sleep(10)
driver.quit()
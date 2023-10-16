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

options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the Button ", ele_id.text)
print("Text on the Button ", ele_id.get_attribute("text"))
print("Content Description of the Button ", ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Srijon")
time.sleep(2)
## Alternative Way to Clear Screen
ele_classname.clear()
time.sleep(2)
## Send keys again to validate
ele_classname.send_keys("Srijon")

time.sleep(2)
driver.quit()
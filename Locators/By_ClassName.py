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

## Application Automation Start Click on the Enter Some Value button
element_Class_1 = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
## Assertion
assert driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button").is_displayed()


# Get the text of the element
element_text = element_Class_1.text


# Define the expected text you want to assert
expected_text_0 = "Enter Some Value"

# Use the assert statement to compare the element's text with the expected text
assert element_text.lower() == expected_text_0.lower(), f"Enter Some Value '{element_text}' does not match expected text '{expected_text_0}'"

## Time Gap
wait = WebDriverWait(driver, 20)
## Click
element_Class_1.click()
time.sleep(10)
## Phase 2 Pass Values
element_Class_2 = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
element_Class_2.click()
## Pass the Values into the text
time.sleep(10)
element_Class_2.send_keys("Srijon")
## Click on submit button
element_Class_3 = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
## Click
element_Class_3.click()
## text Assertion
# Wait for the element holding the text to be visible

# text_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(3)")
text_element = wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, "android.widget.TextView")))
time.sleep(40)
# Get the text from the element
actual_text = text_element.text
print(actual_text)
# Define the expected text
expected_text_1 = "Srijon"

## Time Sleep
time.sleep(40)
# Use the assert statement to compare the actual text with the expected text
# Use the assert statement to check if the actual text contains the expected text
assert expected_text_1.lower() in actual_text.lower(), f"'{actual_text}' does not contain the expected text '{expected_text_1}'"





from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time
def calculate_tap_coordinates(element):
    # Calculate the tap coordinates based on the location and size of the element
    tap_x = element.location['x'] + element.size['width'] // 2
    tap_y = element.location['y'] + element.size['height'] // 2
    return tap_x, tap_y


def perform_tap_action(driver, element):
    tap_x, tap_y = calculate_tap_coordinates(element)

    # Perform a tap using TouchAction
    action = TouchAction(driver)
    action.tap(None, tap_x, tap_y).perform()

    return tap_x, tap_y


# Define your desired capabilities
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

# Scroll to the "LOGIN" button
scrollable = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LOGIN"))')

# Ensure that the "LOGIN" button is within the view
login_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("LOGIN")')

# Calculate and print the tap coordinates
tap_x, tap_y = calculate_tap_coordinates(login_button)
print("Tap Coordinates (x, y):", tap_x, tap_y)

# Perform the tap action and get the tap coordinates
tapped_x, tapped_y = perform_tap_action(driver, login_button)
print("Tapped at (x, y):", tapped_x, tapped_y)

# Add a sleep for demonstration purposes
time.sleep(30)

# Quit the driver
driver.quit()

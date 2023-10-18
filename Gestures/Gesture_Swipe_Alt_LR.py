from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

# Defining the swipe action
def perform_swipe(driver, start_x, end_x, start_y, end_y, swipe_count):
    actions = TouchAction(driver)
    for _ in range(swipe_count):
        actions.long_press(None, start_x, start_y).move_to(None, end_x, end_y).release().perform()
        time.sleep(2)  # Add a wait if needed

# Define your desired capabilities
desired_cap = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.code2lead.kwad",
  "appActivity": "com.code2lead.kwad.MainActivity",
  "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Demo_App.apk",
  "appWaitDuration": "20000"
}

# Initialize the driver and pass your desired capabilities
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

# Scroll to the button
scrollable = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("TAB ACTIVITY"))')

# Navigate to the button
tab_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("TAB ACTIVITY")')
tab_button.click()

# Fetching Device Width and Height
print("Device Width and Height : ", driver.get_window_size())

# Assign deviceSize screenWidth screenHeight
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

# Right to Left
start_x = screenWidth*8/9
end_x = screenWidth/9
start_y = screenHeight/2
end_y = screenHeight/2

# Left to Right
start_x_2 = screenWidth/9
end_x_2 = screenWidth*8/9
start_y_2 = screenHeight/2
end_y_2 = screenHeight/2

# Specify the number of swipes you want to perform
swipe_count = int(input("Provide Swipe Count: "))

# Perform Right to Left swipes
perform_swipe(driver, start_x, end_x, start_y, end_y, swipe_count)

# Perform Left to Right swipes
perform_swipe(driver, start_x_2, end_x_2, start_y_2, end_y_2, swipe_count)

# Save Screenshots to Verify
screenshot_path = r"C:\Users\BS726\Desktop\AppiumQA-Automation\ScreenShot\Swipe_right_to_Left_Alt.png"
driver.save_screenshot(screenshot_path)

screenshot_path = r"C:\Users\BS726\Desktop\AppiumQA-Automation\ScreenShot\Swipe_left_to_right_Alt.png"
driver.save_screenshot(screenshot_path)

driver.quit()

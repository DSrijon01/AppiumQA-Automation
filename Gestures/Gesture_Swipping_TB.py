from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

## Function For Swiping Top to Bottom
def calculate_tap_coordinates(element):
  # Calculate the tap coordinates based on the location and size of the element
  tap_x = element.location['x'] + element.size['width'] // 2
  tap_y = element.location['y'] + element.size['height'] // 2
  return tap_x, tap_y

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

# Scroll to the "LOGIN" button
scrollable = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("ScrollView"))')

# Ensure that the "LOGIN" button is within the view
scroll_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("ScrollView")')
scroll_button.click()

# Fetching Device Width and Height
print("Device Width and Height : ", driver.get_window_size())

# Assign deviceSize screenWidth screenHeight
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

###### Swipe from Top to Bottom  #######
start_x = screenWidth/2
end_x = screenWidth/2
start_y = screenHeight*8/9
end_y = screenHeight/9

###### Swipe from Bottom to Top #######
start_x_2 = screenWidth/2
end_x_2 = screenWidth/2
start_y_2 = screenHeight*2/9
end_y_2 = screenHeight*8/9

# Initiate Action
actions = TouchAction(driver)

# Top to Bottom
actions.long_press(None,start_x,start_y).move_to(None,end_x,end_y).release().perform()

time.sleep(2)

# Bottom to Top
actions.long_press(None,start_x_2,start_y_2).move_to(None,end_x_2,end_y_2).release().perform()

driver.quit()

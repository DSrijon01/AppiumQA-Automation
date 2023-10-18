from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
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


# Scroll to the element
scrollable = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("DRAGANDDROP"))')

#Clicking on the Drag and Drop Button
drag_drop_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("DRAGANDDROP")')
drag_drop_button.click()

## Wait
time.sleep(30)

# Locating Element
element_image = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw")
element_text = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/lbl")
element_button = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/btnDrag")

# Definig Layouts
layout_orange = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout1")
layout_blue = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2")
layout_green = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout3")

# Invoking Action
action = TouchAction(driver)

# Move the Image Element
action.long_press(element_image).move_to(layout_green).release().perform()

# Move the Text
action.long_press(element_text).move_to(layout_blue).release().perform()

# Remain static if the button is already in its place.
action.long_press(element_button).move_to(layout_orange).release().perform()

screenshot_path = r"C:\Users\BS726\Desktop\AppiumQA-Automation\ScreenShot\Drag_&_Drop.png"
driver.save_screenshot(screenshot_path)
driver.quit()
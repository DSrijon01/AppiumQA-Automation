from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
# LaunchAppium.py
from capabilities import desired_cap

# Now you can use the desired_cap dictionary as needed in this file.


# Step 1 : Import Appium Service class
from appium.webdriver.appium_service import AppiumService

# Step 2 : Create object for Appium Service class
appium_service = AppiumService()

# Step 3 : Call Start method by using Appium Service class object
appium_service.start()



options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

## Click on the Enter Some Value button
element_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
wait = WebDriverWait(driver, 20)
element_id.click()

# Step 5 : Call stop method by using Appium Service class object
appium_service.stop()
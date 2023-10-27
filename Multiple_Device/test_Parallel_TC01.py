from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
def deviceDriver(deviceId,sysport):
    desired_cap = {
      "deviceName": "Android Emulator",
      "platformName": "Android",
      "appPackage": "com.code2lead.kwad",
      "systemPort": sysport,
      "udid": deviceId,
      "appActivity": "com.code2lead.kwad.MainActivity",
      "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Demo_App.apk",
      "appWaitDuration": "20000"
    }

    options = UiAutomator2Options().load_capabilities(desired_cap)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

    return driver

def enterText(driver):
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()

def test_device_test():
    d1 = deviceDriver('emulator-5554', 8200)
    d2 = deviceDriver('physical Device', 8400)

    enterText(d1)
    enterText(d2)



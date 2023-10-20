from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest

@pytest.mark.flaky(reruns=5)
def test_runAppiumTest():
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

    ## Wrong Value Entered for test rerun demonstration
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterVal")
    ele_id.click()

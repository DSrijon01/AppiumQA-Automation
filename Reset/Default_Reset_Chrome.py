from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
import time

## Nothing to add to the desired Capabilities
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'Pixel',
    'app': 'C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Demo_App.apk',
    'appPackage': 'com.android.chrome',
    'appActivity': 'com.google.android.apps.chrome.Main'
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)


time.sleep(5)

driver.quit()
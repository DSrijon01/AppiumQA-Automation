from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_cap = {
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "appPackage": "com.continuum.emi.calculator",
    "appActivity": "com.finance.emicalci.activity.Splash_screnn",  # Use "appActivity" instead of "appWaitActivity"
    "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\emi-calculator.apk",
    "appWaitDuration": "20000"
}

options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

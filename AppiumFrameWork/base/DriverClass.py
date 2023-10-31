from appium import webdriver
from appium.options.android import UiAutomator2Options
class Driver:

    def getDriverMethod(self):
        # Shared setup code
        desired_cap = {
            "deviceName": "Android Emulator",
            "platformName": "Android",
            "appPackage": "com.skill2lead.appiumdemo",
            "appActivity": "com.skill2lead.appiumdemo.MainActivity",
            "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Appium_Demo.apk",
            "chromedriverExecutable": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Chrome Driver\\chromedriver.exe",
            "appWaitDuration": "20000"
        }

        options = UiAutomator2Options().load_capabilities(desired_cap)
        driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

        return driver

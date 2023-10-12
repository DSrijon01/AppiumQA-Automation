from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
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

## Find Element by Xpath
ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')

# By using xpath and Con-des
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]') Xpath and Res-id
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]') Xpath and text
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[3]') xpath and Index value

ele_xpath.click()
time.sleep(2)

## Send Keys Using Xpath
ele_xpath2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
ele_xpath2.send_keys("Srijon")

time.sleep(2)

driver.quit()





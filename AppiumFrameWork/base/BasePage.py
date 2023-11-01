from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFrameWork.utilities.logger as cl
import time

class BasePage:

    ## Setup Logger for logging Events
    log = cl.customLogger()

    ## Setup Driver
    def __init__(self,driver):
        self.driver = driver

    ## Setup Wait Period for Element Identifier
    def waitforElement(self, locatorvalue, locatortype):
        locatortype = locatortype.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])

        ## By ID
        if locatortype == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
            return element

        ## By Class
        elif locatortype == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorvalue))
            return element

        ## By description
        elif locatortype == "des":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("%s")' % locatorvalue))
            return element

        ## By Index Number
        elif locatortype == "index":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().index("%d")' % int(locatorvalue)))
            return element

        ## By Text
        elif locatortype == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("%s")' % locatorvalue))
            return element

        ## By Xpath
        elif locatortype == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorvalue)))
            return element

        ## Log for troubleshooting
        else:
            self.log.info("Locator Value " + locatorvalue + " not found")

        return element

    ## Element Found/Not Found Logging
    def getElement(self, locatorvalue, locatortype):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.waitforElement(locatorvalue, locatortype)
            self.log.info("Locator Type Found: " + locatortype + " With Locator Value: " + locatorvalue)
        except:
            self.log.info("Locator Type Not Found " + locatortype + " With Locator Value" + locatortype)

        return element

    ## Setup Click Events
    def clickElement(self, locatorvalue, locatortype):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.getElement(locatorvalue, locatortype)
            element.click()
            self.log.info("Clicked on Element with Locator Type Found: " + locatortype + " With Locator Value: " + locatorvalue)

        except:
            self.log.info("Unable to Click on Locator: " + locatortype + " With Locator Value:" + locatorvalue)

        return element

    ## Send Text
    def sendText(self, text, locatorvalue, locatortype):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.getElement(locatorvalue, locatortype)
            element.send_keys(text)
            self.log.info("Send Text to Element with Locator Type Found: " + locatortype + " With Locator Value: " + locatorvalue)

        except:
            self.log.info("Unable to Send Text on Locator: " + locatortype + "With Locator Value:" + locatorvalue)

        return element

    ## Is Displayed
    def isDisplayed(self, locatorvalue, locatortype):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.getElement(locatorvalue, locatortype)
            element.is_displayed()
            self.log.info("Send Text to Element with Locator Type Found: " + locatortype + " With Locator Value: " + locatorvalue)
            return True
        except:
            self.log.info("Unable to Send Text on Locator: " + locatortype + "With Locator Value:" + locatorvalue)
            return False

        return element

    ## Screenshots
    def screenShot (self, screenshotName):
        fileName = screenshotName + "_" +(time.strftime("%d_%m_%y_%H_%M_%S"))+".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot saved to path : "+ screenshotPath)
        except:
            self.log.info("Unable save screenshot to the path : " + screenshotPath)



from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.logger as cl

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        ## Xpath and Index won't work with the given context
        self._loginButton = "com.skill2lead.appiumdemo:id/Login"  # id
        self._enterEmail = "Enter Email"  # index
        self._enterPassword = "Enter Password"  # text
        self._clickLoginButton = "LOGIN"  # text
        self._wrongCredentials = "Wrong Credentials"  # text
        self._pageTitle = "Enter Admin"  # text
        self._enterText = "com.skill2lead.appiumdemo:id/Edt_admin"  # id
        self._submitButton = "SUBMIT"  # text

    def clickLoginButton(self):
        self.clickElement(self._loginButton, "id")
        cl.allureLogs("Click on Login Button")

    def enterEmail(self):
        self.sendText("admin@gmail.com", self._enterEmail, "text")
        cl.allureLogs("Entered email id")

    def enterPassword(self):
        self.sendText("admin123", self._enterPassword, "text")
        cl.allureLogs("Entered Password")

    def enterPassword2(self):
        self.sendText("admin12344", self._enterPassword, "text")
        cl.allureLogs("Entered Password")

    def clickLoginButton2(self):
        self.clickElement(self._clickLoginButton, "text")
        cl.allureLogs("Clicked on Login Button in Login Screen")

    def verifyWrongCredential(self):
        wrongCredentials = self.isDisplayed(self._wrongCredentials, "text")
        assert wrongCredentials == True
        cl.allureLogs("Wrong Credentials Handling Successfull")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle, "text")
        assert adminScreen == True
        cl.allureLogs("Opened Admin Screen")

    def enterText(self):
        self.sendText("Srijon", self._enterText, "id")
        cl.allureLogs("Entered Text")

    def clickOnSubmit(self):
        self.clickElement(self._submitButton, "text")
        cl.allureLogs("Clicked on Submit Button")

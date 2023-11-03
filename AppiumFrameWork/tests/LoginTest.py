import unittest
import pytest
import AppiumFrameWork.utilities.logger as cl
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.LoginPage import LoginPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=5)
    def test_enterDataInEditBox(self):
        self.gt.enterText()
        self.gt.clickOnSubmit()

    @pytest.mark.run(order=4)
    def test_openLoginScreen(self):
        self.bp.keyCode(4)
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickLoginButton2()
        self.gt.verifyAdminScreen()

    ## Failed Scenario Identification
    @pytest.mark.run(order=3)
    def test_loginFailMethod(self):
        cl.allureLogs("App Opened")
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickLoginButton2()
        self.gt.verifyWrongCredential()
        self.gt.verifyAdminScreen()

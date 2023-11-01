import unittest
import pytest
from AppiumFrameWork.pages.ContactUSTrouble import ContactUsFormPage
import AppiumFrameWork.utilities.logger as cl


@pytest.mark.usefixture("beforeClass","beforeMethod")
class contactUsFromTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self,request):
        self.driver = request.getfixturevalue("beforeClass")
        self.cf = ContactUsFormPage(self.driver)

    @pytest.mark.run(order=1)
    def test_openContactUsForm(self):
        cl.allureLogs("App Launched Successfull")
        self.cf.clickContactUsForm()
        self.cf.verifyContactPage()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterNumber()
        self.cf.clickSubmitButton()





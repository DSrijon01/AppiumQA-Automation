from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.logger as cl

class ContactUsFormPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        ## Xpath And Index won't work
        self._contactFromButton = "com.skill2lead.appiumdemo:id/ContactUs" # id
        self._pageTitle = "Contact Us form" # text
        self._enterName = "android.widget.EditText" # class
        self._enterEmail = "Enter Email" # text
        self._enterAddress = "Enter Address" # text
        self._enterMobileNumber = "Enter Mobile No" # text
        self._submitButton = "SUBMIT" # text

    def clickContactUsForm(self):
        self.clickElement(self._contactFromButton, "id")
        cl.allureLogs("Clicked on Contact Us from Button")
    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitle, "text")
        assert element == True
        cl.allureLogs("Verified Page Open")
    def enterName(self):
        self.sendText("Srijon",self._enterName,"class")
        cl.allureLogs("Entered Name")
    def enterEmail(self):
        self.sendText("srijonbiswas17@gmail.com",self._enterEmail,"text")
        cl.allureLogs("Entered Email")
    def enterAddress(self):
        self.sendText("Road 09 Dhaka",self._enterAddress,"text")
        cl.allureLogs("Entered Address")
    def enterNumber(self):
        self.sendText("0000011111", self._enterMobileNumber, "text")
        cl.allureLogs("Entered Mobile Number")
    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked On Submit Button")
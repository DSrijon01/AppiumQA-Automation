from AppiumFrameWork.base.BasePage import BasePage

class ContactUsFormPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        self._contactFromButton = "com.skill2lead.appiumdemo:id/ContactUs" # id
        self._pageTitle = "Contact Us form" # text
        self._enterName = "Enter Name" # text
        self._enterEmail = "Enter Email" # text
        self._enterAddress = "Enter Address" # text
        self._enterMobileNumber = "4" # index
        self._submitButton = "SUBMIT" # text

    def clickContactUsForm(self):
        self.clickElement(self._contactFromButton, "id")
    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitle, "text")
        assert element == True
    def enterName(self):
        self.sendText("Srijon",self._enterName,"text")
    def enterEmail(self):
        self.sendText("srijonbiswas17@gmail.com",self._enterEmail,"text")
    def enterAddress(self):
        self.sendText("Road 09 Dhaka",self._enterAddress,"text")
    def enterNumber(self):
        self.sendText("0000011111",self._enterMobileNumber,"index")
    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
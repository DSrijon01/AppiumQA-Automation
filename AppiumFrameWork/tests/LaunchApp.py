from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.logger as cl
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.ContactUsFormPage import ContactUsFormPage

driver1 = Driver()
log = cl.customLogger()
driver = driver1.getDriverMethod()
log.info("App Launch Successful")
bp = BasePage(driver)
cf = ContactUsFormPage(driver)

cf.clickContactUsForm()
cf.verifyContactPage()
cf.enterName()
cf.enterEmail()
cf.enterNumber()
cf.enterAddress()
cf.clickSubmitButton()





# element = bp.waitforElement("com.skill2lead.appiumdemo:id/ContactUs", "id")
# element.click()
# log.info("Base Page Initiation Successful")
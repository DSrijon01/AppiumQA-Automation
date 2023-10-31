from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.logger as cl
from AppiumFrameWork.base.BasePage import BasePage

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
log.info("App Launch Successful")

bp = BasePage(driver)

element = bp.waitforElement("com.skill2lead.appiumdemo:id/ContactUs", "id")
element.click()
log.info("Base Page Initiation Successful")
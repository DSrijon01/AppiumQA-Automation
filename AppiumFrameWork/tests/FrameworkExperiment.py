from AppiumFrameWork.base.DriverClass import Driver
from AppiumFrameWork.base.BasePage import BasePage

driver1 = Driver()
driver = driver1.getDriverMethod()

bp = BasePage(driver)
bp.screenShot("Launched App")
element = bp.isDisplayed("com.skill2lead.appiumdemo:id/ContactUs", "id")
bp.screenShot("Value is displayed")
bp.clickElement("com.skill2lead.appiumdemo:id/ContactUs", "id")
bp.clickElement("Enter Name", "text")
bp.sendText("Srijon", "Enter Name", "text")
bp.screenShot("Entered text to the field")
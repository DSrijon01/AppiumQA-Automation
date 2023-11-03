## Import Unit test
import unittest
## Import Test Page Files Login
from AppiumFrameWork.tests.LoginTest import LoginTest
## Import Test Page Files ContactUsFormTest
from AppiumFrameWork.tests.ContactUsFormTest import contactUsFormTest

## Create Class Objects Using Unit Test
cf = unittest.TestLoader().loadTestsFromTestCase(contactUsFormTest)
gt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

## Initiate The TestSuite
regressionTest = unittest.TestSuite([cf,gt])

## Run the Test
unittest.TextTestRunner(verbosity=1).run(regressionTest)

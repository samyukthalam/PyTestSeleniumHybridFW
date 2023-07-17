import inspect
import os
import time
from pathlib import Path

from PageObjects.NopCommerceLoginPage import NopCommerceLoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfigFile
from TestCases.conftest import setup, browser
from TestCases.LoginPageTests.test_nopcommerce_login_page import Test_001_NopeCommerceLogin
from PageObjects.AddCustomerPage import AddCustomerPage


class Test_002_AddCustomer:
    appURL = ReadConfigFile.getApplicationURL("nop commerce")
    username = ReadConfigFile.getUserName("nop commerce")
    password = ReadConfigFile.getAPassword("nop commerce")
    logger = LogGen.logGen()

    def test_addNewCustomer(self, setup):
        self.logger.info("Executing the test" + inspect.getframeinfo(inspect.currentframe()).function)
        self.driver = setup
        self.driver.get(self.appURL)
        self.driver.maximize_window()
        self.npLP = NopCommerceLoginPage(self.driver)
        self.npLP.setUserName(self.username)
        self.npLP.setPassword(self.password)
        self.npLP.clickLogin()
        self.logger.info("Login is Successful")
        self.npAddCust = AddCustomerPage(self.driver)
        self.npAddCust.clickCustomerMenu()
        self.npAddCust.clickCustomerMenuItem()
        time.sleep(5)
        if self.driver.find_element("xpath", self.npAddCust.lbl_Customer_xpath).text.strip() == "Customers":
            assert True
            self.logger.info("*********** Testing Customers Label is passed **************")
            self.driver.close()
        else:
            screenshotpath = os.path.join(os.path.sep, Path(__file__).parent.parent.parent, 'Screenshots' + os.sep)
            self.driver.save_screenshot(screenshotpath + "test_label_customer.png")
            self.driver.close()
            self.logger.info("************** Testing Customers Label is failed *************")
            assert False
        self.logger.info("Navigated to Customers Page")
        self.npAddCust.clickCustomerAddNewBtn()
        self.npAddCust.setEmail(self.username)


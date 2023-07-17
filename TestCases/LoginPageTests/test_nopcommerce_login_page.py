import inspect

from PageObjects.NopCommerceLoginPage import NopCommerceLoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfigFile


class Test_001_NopeCommerceLogin:
    appURL = ReadConfigFile.getApplicationURL("nop commerce")
    username = ReadConfigFile.getUserName("nop commerce")
    password = ReadConfigFile.getAPassword("nop commerce")
    logger = LogGen.logGen()


    def test_noplogin(self, setup):
        self.logger.info("Executing the test" + inspect.getframeinfo(inspect.currentframe()).function)
        self.driver = setup
        self.driver.get(self.appURL)
        self.lpNC = NopCommerceLoginPage(self.driver)
        self.lpNC.setUserName(self.username)
        self.lpNC.setPassword(self.password)
        self.lpNC.clickLogin()
        self.logger.info("************** Verifying login functionality *****************")
        if self.driver.title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************* Login test is passed ***************")
        else:
            self.logger.info("************* Login test is failed ************")
            assert False

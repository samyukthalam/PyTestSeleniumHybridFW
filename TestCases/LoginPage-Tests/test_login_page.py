import inspect
import os
from pathlib import Path
from Utilities.readProperties import ReadConfigFile
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen


class Test_001_Login:
    appURL = ReadConfigFile.getApplicationURL()
    username = ReadConfigFile.getUserName()
    password = ReadConfigFile.getAPassword()
    logger = LogGen.logGen()

    def test_page_title(self, setup):
        self.logger.info("Executing the test" + inspect.getframeinfo(inspect.currentframe()).function)
        self.driver = setup
        self.driver.get(self.appURL)
        self.logger.info("****************** Verifying home page title **************")
        if self.driver.title == "ParaBank | Welcome | Online Banking":
            assert True
            self.logger.info("*********** Home page title test is passed **************")
            self.driver.close()
        else:
            screenshotpath = os.path.join(os.path.sep, Path(__file__).parent.parent.parent, 'Screenshots' + os.sep)
            self.driver.save_screenshot(screenshotpath + "test_page_title.png")
            self.driver.close()
            self.logger.info("************** Home page title test is failed *************")
            assert False

    def test_login(self, setup):
        self.logger.info("Executing the test" + inspect.getframeinfo(inspect.currentframe()).function)
        self.driver = setup
        self.driver.get(self.appURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************** Verifying login functionality *****************")
        if self.driver.title == "ParaBank | Accounts Overview":
            assert True
            self.logger.info("************* Login test is passed ***************")
            self.lp.clickLogOut()
        else:
            self.logger.info("************* Login test is failed ************")
            assert False

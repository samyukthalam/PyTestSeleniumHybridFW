import inspect
import os
from pathlib import Path
from Utilities.readProperties import ReadConfigFile
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_001_Login:
    appURL = ReadConfigFile.getApplicationURL()
    testDataFilePath=os.path.join(os.path.sep, Path(__file__).parent.parent.parent, 'TestData/TestData.xlsx')
    logger = LogGen.logGen()

    def test_login(self, setup):
        self.logger.info("Executing the test" + inspect.getframeinfo(inspect.currentframe()).function)
        self.driver = setup
        self.driver.get(self.appURL)
        self.lp = LoginPage(self.driver)
        rowCount=XLUtils.getRowCount(self.testDataFilePath, 'Logins')
        
        colCount = XLUtils.getColumnCount()
        username = XLUtils.readExcelData(testDataFilePath,"Logins",rowCount,colCount,)
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

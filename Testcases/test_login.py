import pytest
from selenium import webdriver
from pageObjects.Login import Login
from Utilities.readProperities import ReadConfig
from Utilities.customLogger import LogGen


class Test_case_001_login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()
    logger =LogGen.loggen()

    def test_home_paget_itle(self, setup):
        self.logger.info("*********Test_001_Login*************")
        self.logger.info("*********Verifyng login page title***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.driver.maximize_window()
        self.lp.clickSignin()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickloginbutton()
        act_title=self.driver.title
        if act_title == 'My account - My Store':
            assert True
            #self.driver.close()
            self.logger.info("*********Verifying login title passed***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+" test_home_paget_itle.png")
            #self.driver.close()
            self.logger.info("******** loginpage title Failed***")
            assert False



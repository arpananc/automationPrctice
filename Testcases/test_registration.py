import pytest
from selenium import webdriver
from pageObjects.Login import Login
from pageObjects.RegistrationPage import Registration
from Utilities.readProperities import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
from CommonFunctions.commomfunctions import commonFunctions
import time

class Test_case_001_registration:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
   #path = ".\\TestData\registration.xlsx"
    logger = LogGen.loggen()


    def test_home_paget_itle ( self, setup ):
      self.logger.info("*********Test_001_Registration*************")
      self.logger.info("*********Verifyng Registration page title***")
      self.driver = setup
      self.driver.get(self.baseurl)
      self.rp = Registration(self.driver)
      self.cf = commonFunctions(self.driver)
      self.driver.maximize_window()
      self.rp.clickSignin()
      self.rp.setemailCreate("abcabc123@gmail.com")
      self.rp.clickcreateAccount()
      act_title = self.driver.title
      if act_title == 'Login - My Store':
          assert True
          self.logger.info("*********Verifying RegistrationPage title passed***")
      else:
          assert False
          self.logger.info("******** RegistrationPage title Failed***")

      #Registartion
      time.sleep(4)
      self.rp.clickradiobutton()
      self.rp.setcustfirstname(firstname='anna')
      self.rp.setcustlastname(lastname='goll')
      self.rp.setemailid(email='')
      self.rp.setpassword(password='abc@13423')
      self.rp.setcompany(company='abcv')
      self.cf.select_dropdown_by_visiable_text("//*[@id='days']",12)
      self.cf.select_dropdown_by_visiable_text('//*[@id="months"]',January )
      self.cf.select_dropdown_by_visiable_text('//*[@id="years"]',1984)
      self.rp.setAddress(Address='1st floor')
      self.rp.setAddress2(Address2='s v towers')
      self.rp.setcity(city='New Jersy')
      self.cf.select_dropdown_by_visiable_text('//*[@id="id_state"]',Alaska)
      self.rp.setPostcode(Postcode='00000')
      self.rp.setMobileNum(MobileNum='1234567889')
      self.rp.setRegisButton()






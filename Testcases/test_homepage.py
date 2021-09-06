import pytest
from selenium import webdriver
from pageObjects.Login import Login
from Utilities.readProperities import ReadConfig
from Utilities.customLogger import LogGen
from CommonFunctions.commomfunctions import commonFunctions
from pageObjects.Homepage import HomePage
from pageObjects.productpage import ProductPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC


class Test_case_003_homepage:
    baseurl = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_home_paget ( self, setup ):
        self.logger.info("*********Test_001_Login*************")
        self.logger.info("*********searching in home page product***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.hp = HomePage(self.driver)
        self.cf = commonFunctions(self.driver)
        self.driver.maximize_window()
        #self.lp.clickSignin()

        # search product
        self.hp.search_product('dress')
        time.sleep(2)
        self.cf.pressEnter()
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.logger.info("*********Product Displayed***")
        self.driver.save_screenshot(".\\Screenshots\\" + " test_home_products.png")
        time.sleep(2)
        image = '2'
        searchimage = self.driver.find_element_by_xpath("//*[@id='center_column']/ul/li['+image+']/div/div[1]/div/a[1]/img")
        ActionChains(self.driver).move_to_element(searchimage).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]/span').click()
        self.driver.save_screenshot(".\\Screenshots\\" + " test_home_paget_cart.png")
        #self.cf.clickusingjavascript(btn)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()
        searchimage1 = self.driver.find_element_by_xpath("//*[@id='""header']/div[3]/div/div/div[3]/div/a")
        ActionChains(self.driver).move_to_element(searchimage1).perform()
        self.driver.find_element_by_xpath('//*[@id="button_order_cart"]/span').click()
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]/span').click()
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys("admin@yourstore.com")
        self.driver.find_element_by_xpath("//*[@id='passwd']").send_keys("abc@123")
        self.driver.find_element_by_xpath("//*[@id='SubmitLogin']/span/i").click()
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button/span').click()
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="cgv"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="form"]/p/button/span').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a').click()
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.driver.find_element_by_xpath('//*[@id="cart_navigation"]/button/span').click()
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.driver.close()












import pytest
from selenium import webdriver
import time

url="http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_id('email_create').send_keys('abcasd4123@gmail.com')
driver.find_element_by_xpath('//*[@id="SubmitCreate"]/span').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="id_gender2"]').click()
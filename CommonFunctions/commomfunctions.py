import logging
import os
import time
import re
from datetime import datetime
import random
import string
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class commonFunctions:
    path = Path(__file__).parents[2]

    def __init__ ( self, driver ):
        self.driver = driver

    def pressEnter( self,):
         a =ActionChains(self.driver)
         a.send_keys( Keys.ENTER).perform()

    def scrollDown(self ,driver):
        driver.execute_script("window.scrollBy(0,500)","")

    def get_text_and_handle_alert ( self, vaild_alert_text ):
        alert_obj = self.driver.switch_to.alert
        time.sleep(2)
        alert_text = alert_obj.text
        if alert_text == vaild_alert_text:
            alert_obj.accept()
            assert True  # Alert box handled successfully
            return alert_text
        else:
            assert False  # Alert box Not handled successfully

    def handleAlertbox ( self ):
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

    def closeAllWindows ( self ):
        handles = self.driver.window_handles
        size = len(handles)
        parent_handles = self.driver.current_window_handle
        for handle in range(size):
            if handles[handle] != parent_handles:
                self.driver.switch_to.window(handles[handle])
                self.driver.close()

    def handlebrowsers ( self ):
        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle
        for handle in range(size):
            if handles[handle] != parent_handle:
                self.driver.switch_to.window(handles[handle])

    def get_current_window_handle ( self ):
        current_window_handle = self.driver.current_window_handle
        return current_window_handle

    def switch_to_current_window ( self ):
        parenthandle = self.driver.current_window_handle
        self.driver.switch_to.window(parenthandle)

    def switchFrames ( self, frameId ):
        self.driver.switch_to.frame(frameId)

    def switchDefaultFrame ( self ):
        self.driver.switch_to.default_content()

    def screenshots ( self, sc_path ):
        testcase_details = os.environ.get('PYEST_CURRENT_TEST')
        testcase_name = testcase_details.split('::')[1]
        now = datetime.now()
        timeinstance = now.strftime("%d%m%y_%H%M%S")
        file_name = testcase_name + "_" + timeinstance + ".png"
        img_path = self.join_path(sc_path, file_name)
        self.driver.get_screenshot_as_file(img_path)

    def select_dropdown_by_visiable_text ( self, locator, visiable_text ):
        try:
            self.wait_for_element(locator, 10)
            ele_dropdown = self.driver.find_element_by_xpath(locator)
            time.sleep(3)
            select_ele = Select(ele_dropdown)
            select_ele.select_by_visible_text(visiable_text)
        except Exception as e:
            assert False, f"Exception occurred.\n{e}"

    def performMouseover( self,locator):
        try:
            a = ActionChains(self.driver)
            a.move_to_element(locator).perform()
        except Exception as e:
            assert False, f"Exception occurred.\n{e}"

    def clickusingjavascript( self ,driver,element):
        driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator, locator_type)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception as e:
            assert False, f"Exception occurred.\n{e}"
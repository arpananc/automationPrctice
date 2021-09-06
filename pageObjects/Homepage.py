

from Utilities.ui import home_page
class HomePage:
    textbox_search_xpath = '//*[@id="search_query_top"]'
    button_search_css = "[name='submit_search']"
    button_AddtoCart_xpath = '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span'


    def __init__ ( self, driver ):
        self.driver = driver

    def search_product(self, searched_product):
        #self.send_keys_to(home_page.get("searchFieldByID"), searched_product)
        self.driver.find_element_by_xpath(self.textbox_search_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_search_xpath).send_keys(searched_product)

    def search_button(self):
        #self.click_on_element(home_page.get("searchButtonByName"), "name")
        self.driver.find_element_by_css(self.button_search_css).click()

    def cart_button(self):
        self.click_on_element(home_page.get("cartButtonCSSSelector"), "css")

    def dresses_button_click_on(self):
        self.click_on_element(home_page.get("dressesButtonByXpath"), "xpath")

    def dresses_summer_dresses_click_on(self):
        pass
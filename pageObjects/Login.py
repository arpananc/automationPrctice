


class Login:
    link_SiginLink_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    textbox_username_xpath = "//*[@id='email']"
    textbox_password_xpath = "//*[@id='passwd']"
    button_login_xpath = "//*[@id='SubmitLogin']/span/i"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clickSignin( self ):
       self.driver.find_element_by_xpath(self.link_SiginLink_xpath).click()

    def setusername(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickloginbutton(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


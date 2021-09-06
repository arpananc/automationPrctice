


class Registration:
    link_SiginLink_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    textbox_email_create_id = 'email_create'
    button_createButton_xpath = '//*[@id="SubmitCreate"]/span'
    radiobutton_gender_xpath ='//*[@id="id_gender2"]'
    textbox_Customer_firstname_id ='customer_firstname'
    textbox_Customer_lastname_id = 'customer_lastname'
    textbox_Customer_email_id = 'customer_lastname'
    textbox_Customer_password_id = 'customer_lastname'
    textbox_Customer_firstname1_id = 'firstname'
    textbox_Customer_lastname1_id = 'lastname'
    textbox_Customer_company_id = 'company'
    textbox_Customer_Address_id = 'address1'
    textbox_Customer_Address2_id = 'address2'
    textbox_Customer_city_id = 'city'
    textbox_Customer_state_id = 'id_state'
    textbox_Customer_postcode_id = 'postcode'
    textbox_Customer_homephone_id ='phone'
    textbox_Customer_mobilephone_id = 'phone_mobile'
    textbox_Customer_alias_address_id = 'alias'
    button_register_xpath ='//*[@id="submitAccount"]/span'


    def __init__(self, driver ):
      self.driver = driver

    def clickSignin( self ):
       self.driver.find_element_by_xpath(self.link_SiginLink_xpath).click()

    def setemailCreate ( self, email_create ):
       self.driver.find_element_by_id(self.textbox_email_create_id).send_keys(email_create)

    def clickcreateAccount ( self ):
       self.driver.find_element_by_xpath(self.button_createButton_xpath).click()


    def clickradiobutton ( self):
       self.driver.find_element_by_xpath(self.radiobutton_gender_xpath).click()

    def setcustfirstname(self, firstname):
        self.driver.find_element_by_id(self.textbox_Customer_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_firstname_id).send_keys(firstname)

    def setcustlastname ( self, lastname ):
        self.driver.find_element_by_id(self.textbox_Customer_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_lastname_id).send_keys(lastname)

    def setemailid ( self, email ):
        self.driver.find_element_by_id(self.textbox_Customer_email_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_email_id).send_keys(email)

    def setpassword ( self, password ):
        self.driver.find_element_by_id(self.textbox_Customer_password_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_password_id).send_keys(password)

    def setcompany ( self, company ):
        self.driver.find_element_by_id(self.textbox_Customer_company_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_company_id).send_keys(company)

    def setAddress ( self, Address ):
        self.driver.find_element_by_id(self.textbox_Customer_Address_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_company_id).send_keys(Address)

    def setAddress2 ( self, Address2 ):
       self.driver.find_element_by_id(self.textbox_Customer_company_id).clear()
       self.driver.find_element_by_id(self.textbox_Customer_company_id).send_keys(Address2)

    def setcity ( self, city ):
        self.driver.find_element_by_id(self.textbox_Customer_city_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_city_id).send_keys(city)

    def setState ( self, State ):
        self.driver.find_element_by_id(self.textbox_Customer_state_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_city_id).send_keys(State)

    def setPostcode ( self, Postcode ):
        self.driver.find_element_by_id(self.textbox_Customer_postcode_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_postcode_id).send_keys(Postcode)

    def setMobileNum ( self, MobileNum ):
       self.driver.find_element_by_id(self.textbox_Customer_mobilephone_id).clear()
       self.driver.find_element_by_id(self.textbox_Customer_mobilephone_id).send_keys(MobileNum)

    def setRegisButton ( self, RegisButton ):
        self.driver.find_element_by_id(self.textbox_Customer_postcode_id).clear()
        self.driver.find_element_by_id(self.textbox_Customer_postcode_id).send_keys(RegisButton)






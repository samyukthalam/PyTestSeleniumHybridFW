class NopCommerceLoginPage:
    # Login Page Element Locators
    textbox_userName_name = "Email"
    textbox_password_name = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_logout_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("name",self.textbox_userName_name).clear()
        self.driver.find_element("name",self.textbox_userName_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("name",self.textbox_password_name).clear()
        self.driver.find_element("name",self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath",self.button_login_xpath).click()

    def clickLogOut(self):
        self.driver.find_element("xpath",self.link_logout_xpath).click()

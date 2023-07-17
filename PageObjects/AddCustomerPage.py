from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomerPage:
    lnk_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_customer_menuItem_xpath ="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    lbl_Customer_xpath = "//h1[contains(text(),'Customers')]"
    btn_addNew_class="btn btn-primary"
    input_Email_name="Email"
    input_Password_name = "Password"
    input_FirstName_name = "FirstName"
    input_LastName_name = "LastName"
    radioBtn_gender_id="Gender_Female"
    input_DOB_id="DateOfBirth"
    input_CompanyName_id="Company"
    chkBox_isTaxExempt_id="IsTaxExempt"
    drpdown_NewsLetter_id="SelectedNewsletterSubscriptionStoreIds_taglist"
    list_newsletterElements_id="SelectedNewsletterSubscriptionStoreIds_listbox"
    listItem_newsletter_xpath="//li[text()='Your store name']"

    def __init__(self,driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element("xpath",self.lnk_customer_menu_xpath).click()

    def clickCustomerMenuItem(self):
        self.driver.find_element("xpath", self.lnk_customer_menuItem_xpath).click()

    def clickCustomerAddNewBtn(self):
        self.driver.find_element("xpath", self.btn_addNew_class).click()

    def setEmail(self, email):
        self.driver.find_element("name", self.input_Email_name).clear()
        self.driver.find_element("name", self.input_Email_name).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element("name", self.input_Password_name).clear()
        self.driver.find_element("name", self.input_Password_name).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element("name", self.input_FirstName_name).clear()
        self.driver.find_element("name", self.input_FirstName_name).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element("name", self.input_LastName_name).clear()
        self.driver.find_element("name", self.input_LastName_name).send_keys(lastName)

    def setDOB(self, DOB):
        self.driver.find_element("id", self.input_DOB_id).clear()
        self.driver.find_element("id", self.input_DOB_id).send_keys(DOB)

    def setCompanyName(self, companyName):
        self.driver.find_element("id", self.input_CompanyName_id).clear()
        self.driver.find_element("id", self.input_CompanyName_id).send_keys(companyName)

    def clickIsTaxExempt(self):
        self.driver.find_element("id", self.chkBox_isTaxExempt_id).click()

    def selectNewsletter(self,newsletterValue):
        self.driver.find_element("id", self.drpdown_NewsLetter_id).click()
        WebDriverWait(self.driver,60).until(EC.presence_of_elements_located(By.ID, self.list_newsletterElements_id))
        self.driver.find_element("xpath", self.listItem_newsletter_xpath).click()

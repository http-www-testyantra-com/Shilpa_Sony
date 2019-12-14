""" 1.	open browser
    2.	enter URL(blustone)
    3.	click on goldmine 10+1 Sceheme
    4.	enter  monthly amount and email address and click on start now
    5.	verify wheather monthly amount and email address entered is reflected in next  page
    6.	Enter all details & select payment option as 'Cash'. click on 'Confirmation button'
    7.  close the browser
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Bluestone_Scenario29:
    def test_Scenario29(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bluestone.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        gold_mine = self.driver.find_element_by_xpath("//div[@class = 'gms-banner-inner']")
        gold_mine.click()
        amount_txtfield = self.driver.find_element_by_id("amount")
        amount_txtfield.send_keys(10000)
        amount_entered = 10000
        email_txtfld = self.driver.find_element_by_id("Email")
        email_txtfld.send_keys("shil@gmail.com")
        email_entered = "shil@gmail.com"
        btn_start = self.driver.find_element_by_id("gmsStart")
        btn_start.click()
        email_value = self.driver.find_element_by_id("email")

        email = email_value.get_attribute("value")
        print(email)

        subscription_amount = self.driver.find_element_by_name("subscriptionAmount")
        amount_value = subscription_amount.text

        print(amount_value)
        # assert amount_entered == amount_value,"amount entered not reflected"
        # print("amount entered is reflected")
        assert email_entered == email,"email entered not reflected"
        print("email entered is reflected")
        name_txfld = self.driver.find_element_by_id("fullname")
        name_txfld.send_keys("shilpa")
        mobile_number_txt = self.driver.find_element_by_id("contactNumber")
        mobile_number_txt.send_keys("9538183318")
        address_txtfield = self.driver.find_element_by_id("address")
        address_txtfield.send_keys("Rajajinagar,Bangalore")
        pincode = self.driver.find_element_by_name("postcode_delivery")
        pincode.send_keys("560010")
        submit_btn = self.driver.find_element_by_xpath("//input[@type = 'submit']")
        submit_btn.click()
        nominee_txt = self.driver.find_element_by_id("nomineeName")
        nominee_txt.send_keys("rbpatil")
        nominee_relation = self.driver.find_element_by_id("nomineeRelationship")
        select = Select(nominee_relation)
        select.select_by_visible_text("Spouse")
        nationality = self.driver.find_element_by_id("nomineeNationality")
        select_nationality = Select(nationality)
        select_nationality.select_by_visible_text("Indian")
        submit_btn = self.driver.find_element_by_name("_eventId_checkoutSaveAddressDetails")
        submit_btn.click()
        payby_cash = self.driver.find_element_by_id("cashondeliverygms")
        payby_cash.click()
        cash_confirm_btn = self.driver.find_element_by_id("airpayEmiPopup-trigger")
        cash_confirm_btn.click()
        ok_btn = self.driver.find_element_by_xpath("//a[@class = 'btn btn-s cod-button']")
        ok_btn.click()
        self.driver.quit()




o = Bluestone_Scenario29()
o.test_Scenario29()
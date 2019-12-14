""" 1.	open browser
    2.	enter URL(blustone)
    3.	click on goldmine 10+1 Sceheme
    4.	enter  monthly amount and email address and click on start now
    5.	verify wheather monthly amount and email address entered is reflected in next  page
    6.	close browser
"""

from selenium import webdriver
class Bluestone_Scenario28:
    def test_Scenario28(self):
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
        email_txtfld.send_keys("shilparpatil86@gmail.com")
        email_entered = "shilparpatil86@gmail.com"
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
        self.driver.quit()


o = Bluestone_Scenario28()
o.test_Scenario28()
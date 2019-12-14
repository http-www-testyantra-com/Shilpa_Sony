""" 1.	open browser
    2.	enter url(https://jqueryui.com/slider/)
    3.	Slide the slider upto end in multiples times  it should come in reverse order in multiple times.
    4.	close Browser.

"""

from selenium import webdriver
from selenium.webdriver import ActionChains


class Jquery_Scenario35:
    def test_Jquery_Scenario35(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://jqueryui.com/slider/")
        self.driver.maximize_window()
        frame = self.driver.find_element_by_xpath("//iframe[@class = 'demo-frame']")
        self.driver.switch_to.frame(frame)
        slider = self.driver.find_element_by_id("slider")
        act = ActionChains(self.driver)

        #Move the slider in forward direction multiple times

        for i in range(3):
            act.click_and_hold(slider).move_by_offset(100,0).perform()

        print("slider moved in forward direction")

        # Move the slider in reverse direction multiple times

        for i in range(3):
            act.click_and_hold(slider).move_by_offset(-100, 0).perform()
            print(i)
        print("slider moved in reverse  direction")

        self.driver.quit()

o = Jquery_Scenario35()
o.test_Jquery_Scenario35()


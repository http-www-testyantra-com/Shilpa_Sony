from selenium import webdriver
class WebDriverFactory():
    def __init__(self, driver):
        self.driver = driver

    def getWebDriverInstance(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        # if self.browser == 'firefox':
        #     driver = webdriver.Firefox(
        #         executable_path="/Users/anushreeprakash/Documents/final/f1/base/geckodriver")
        # else:
        driver = webdriver.Chrome()

            # driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)
        return driver

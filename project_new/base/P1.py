from selenium import webdriver

def setUp(func):
    def inner():
        driver = webdriver.Chrome()
        func(driver)
    return inner



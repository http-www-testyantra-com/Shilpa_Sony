#handling stale element exception
#using flipkart
from selenium import webdriver

def m1():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    # login_signup = driver.find_element_by_xpath("//a[. = 'Login & Signup']")
    # login_signup.click()
    #driver.switch_to.active_element()
    try:

        username = driver.find_element_by_xpath("//input[@class = '_2zrpKA _1dBPDZ']")
        username.send_keys("9345678910")
        password = driver.find_element_by_xpath("//input[@class = '_2zrpKA _3v41xv _1dBPDZ']")
        password.send_keys("shilpa")
        submit_btn = driver.find_element_by_xpath("//button[@class = '_2AkmmA _1LctnI _7UHT_c']")
        submit_btn.click()

        username.send_keys("9538183318")
        
        password.send_keys("Hellohaihowareyou?")

        submit_btn.click()
    except Exception as e:
        print(e)
        print("Exception handled")

m1()


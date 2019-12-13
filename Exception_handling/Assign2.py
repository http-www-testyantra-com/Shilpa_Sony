# USING ICICI
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#element not interactable exception


def test_m1():
    driver = webdriver.Chrome()
    driver.get("https://www.guru99.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    try:
        testing = driver.find_element_by_xpath("//span[text() = 'Testing']")
        act = ActionChains(driver)
        act.move_to_element(testing).perform()
    except Exception as e:
        print(e)
        print("exception handled")


    finally:
        driver.close()
if __name__ == '__main__':
    test_m1()



import time

from selenium import webdriver

from selenium.webdriver.common.by import By


def testing_case():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        required_input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        required_input2 = browser.find_element(By.CSS_SELECTOR,
                                                'input.second[required]')
        required_input3 = browser.find_element(By.CSS_SELECTOR,
                                                'input.third[required]')
        for input_ in required_input1,required_input2,required_input3:
            input_.send_keys('Test')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        time.sleep(1)
        welcome_alert_elt = browser.find_element(By.TAG_NAME,'h1')
        welcome_alert=welcome_alert_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_alert
    finally:
        time.sleep(20)
        browser.quit()

if __name__ == '__main__':
    testing_case()
import time

from selenium import webdriver

from selenium.webdriver.common.by import By


def testing_case():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        inputs = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
        for input_ in inputs:
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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_case():
    try:
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/huge_form.html')
        forms = browser.find_elements(By.CSS_SELECTOR, 'input')
        for form in forms:
            form.send_keys('string')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
    finally:
        time.sleep(20)
        browser.quit()

if __name__ == '__main__':
    test_case()
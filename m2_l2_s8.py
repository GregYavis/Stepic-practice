import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

data = iter(['Greg', 'Kozlov', 'mail@gmail.com'])


def test_case():
    try:
        link = 'http://suninjuly.github.io/file_input.html'
        browser = webdriver.Chrome()
        browser.get(link)
        text_inputs = browser.find_elements(By.CSS_SELECTOR,
                                            'input[type="text"]')
        for input_ in text_inputs:
            input_.send_keys(next(data))
        file_input = browser.find_element(By.CSS_SELECTOR, '#file')
        current_directory = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_directory, 'file.txt')
        file_input.send_keys(file_path)
        submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        submit_button.click()
        # to m2_l3_s1
        alert = browser.switch_to.alert
        print(alert.text)
        alert.accept()
    finally:
        time.sleep(15)
        browser.quit()


if __name__ == '__main__':
    test_case()

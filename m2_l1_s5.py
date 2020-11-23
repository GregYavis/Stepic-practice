import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_case():
    try:
        link = 'http://suninjuly.github.io/math.html'
        browser = webdriver.Chrome()
        browser.get(link)
        value = browser.find_element(By.CSS_SELECTOR, 'label #input_value')
        text = value.text
        answer = calc(text)
        print(answer)
        input_ = browser.find_element(By.CSS_SELECTOR,'#answer')
        input_.send_keys(answer)
        check_box = browser.find_element(By.CSS_SELECTOR,'#robotCheckbox')
        check_box.click()
        radio_button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
        radio_button.click()
        submit = browser.find_element(By.CSS_SELECTOR,'button.btn')
        submit.click()
    finally:
        time.sleep(15)
        browser.quit()

if __name__ == '__main__':
    test_case()
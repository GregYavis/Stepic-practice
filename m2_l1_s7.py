import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_case():
    try:
        link = 'http://suninjuly.github.io/get_attribute.html'
        browser = webdriver.Chrome()
        browser.get(link)
        value = browser.find_element(By.CSS_SELECTOR,'#treasure')
        print(value.get_attribute('valuex'))
        x = value.get_attribute('valuex')
        answer = calc(x=x)
        input_=browser.find_element(By.CSS_SELECTOR,'#answer')
        input_.send_keys(answer)
        check_box = browser.find_element(By.CSS_SELECTOR,'#robotCheckbox')
        check_box.click()
        radio_button = browser.find_element(By.CSS_SELECTOR,'#robotsRule')
        radio_button.click()
        submit = browser.find_element(By.CSS_SELECTOR,'button.btn')
        submit.click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == '__main__':
    test_case()
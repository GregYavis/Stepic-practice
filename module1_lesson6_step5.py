import time
import math
from selenium import webdriver

from selenium.webdriver.common.by import By


def testing_case_2():
    try:
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/find_link_text')
        search = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(
            math.pi, math.e) * 10000)))
        search.click()
        input1 = browser.find_element(By.NAME, 'first_name')

        input1.send_keys('Grigoriy')
        input2 = browser.find_element(By.NAME, 'last_name')
        input2.send_keys('KOZLOW')
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("MOSKOW")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    finally:
        time.sleep(20)
        browser.quit()

if __name__ == '__main__':
    testing_case_2()
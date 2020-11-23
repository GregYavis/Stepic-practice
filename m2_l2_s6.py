import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_case():
    try:
        link = 'http://suninjuly.github.io/execute_script.html'
        browser = webdriver.Chrome()
        browser.get(link)
        value = browser.find_element(By.CSS_SELECTOR, '#input_value')
        x = value.text
        answer = calc(x)

        input_answer = browser.find_element(By.CSS_SELECTOR,'#answer')
        input_answer.send_keys(answer)
        checkbox = browser.find_element(By.CSS_SELECTOR,'[type="checkbox"]')
        checkbox.click()
        radio = browser.find_element(By.CSS_SELECTOR,'[value="robots"]')
        browser.execute_script('return arguments[0].scrollIntoView(true);',
                               radio)
        radio.click()
        button = browser.find_element(By.CSS_SELECTOR,'button.btn')

        button.click()
    finally:
        time.sleep(15)
        browser.quit()

if __name__ == '__main__':
    test_case()

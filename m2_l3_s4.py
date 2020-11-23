import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test():
    try:
        link = 'http://suninjuly.github.io/alert_accept.html'
        browser = webdriver.Chrome()
        browser.get(link)
        start_button = browser.find_element(By.CSS_SELECTOR, 'button')
        start_button.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        value = browser.find_element(By.CSS_SELECTOR, '#input_value')
        x = value.text
        answer = calc(x)
        answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
        answer_input.send_keys(answer)
        submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        submit.click()
        stepic_alert = browser.switch_to.alert
        print(stepic_alert.text)
    finally:
        browser.quit()

if __name__ == '__main__':
    test()
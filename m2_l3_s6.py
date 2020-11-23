import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test():
    try:
        link = 'http://suninjuly.github.io/redirect_accept.html'
        browser = webdriver.Chrome()
        #browser.implicitly_wait(5)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'button').click()
        new_page = browser.window_handles[1]
        browser.switch_to.window(new_page)
        value = browser.find_element(By.CSS_SELECTOR, '#input_value')

        x = value.text
        answer = calc(x)
        input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
        input_answer.send_keys(answer)
        submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        submit.click()
        stepic_answer = browser.switch_to.alert
        print(stepic_answer.text)
    finally:
        browser.quit()


if __name__ == '__main__':
    test()

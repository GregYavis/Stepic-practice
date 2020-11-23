import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def test():
    try:
        link = 'http://suninjuly.github.io/explicit_wait2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        price_100 = WebDriverWait(
            browser, 12).until(
            expected_conditions.text_to_be_present_in_element((
                By.CSS_SELECTOR,'#price'), '100')
        )
        button = browser.find_element(By.ID, 'book')
        button.click()
        value = browser.find_element(By.CSS_SELECTOR, '#input_value')
        x = value.text
        print(x)
        answer = calc(x)
        input_answer = browser.find_element(By.ID, 'answer')
        input_answer.send_keys(answer)
        submit = browser.find_element(By.CSS_SELECTOR, 'solve')
        submit.click()

    finally:
        time.sleep(10)


if __name__ == '__main__':
    test()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_case():
    try:
        link = 'http://suninjuly.github.io/selects1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        value1 = browser.find_element(By.CSS_SELECTOR,'#num1')
        value2 = browser.find_element(By.CSS_SELECTOR, '#num2')
        selection = browser.find_element(By.CSS_SELECTOR, '#dropdown')
        select_answer = Select(selection)
        summa = int(value1.text)+int(value2.text)
        select_answer.select_by_value(str(summa))
        submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        submit.click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == '__main__':
    test_case()
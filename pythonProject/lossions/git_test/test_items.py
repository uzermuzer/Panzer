import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_window_buttow(browser):
    browser.get(link)

    time.sleep(5)

    button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert button.is_displayed() == True, "Кнопки нет на экране"
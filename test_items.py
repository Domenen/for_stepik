import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_on_site(browser):
    browser.get(link)
    text_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert text_basket, "Кнопки нет"
    print(f"Используемый язык: '{browser.language}'")
    time.sleep(30)

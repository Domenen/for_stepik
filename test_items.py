import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_on_site(browser):
    browser.get(link)
    text_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    if text_basket.text == "Добавить в корзину":
        assert "Используется Русский язык"
    elif text_basket.text == "Add to basket":
        assert "Используется Английский язык"
    elif text_basket.text == "Ajouter au panier":
        assert "Используется Французский язык"
    else:
        assert "Другие языки пока не понимаю"
    time.sleep(30)

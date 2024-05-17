from selenium import webdriver
# Класс Keys предоставляет клавиши клавиатуры (ENTER, F1, ALT и другие).
from selenium.webdriver.common.keys import Keys
# Класс By используется для определения местоположения элементов в документе
from selenium.webdriver.common.by import By

# создается экземпляр класса
driver = webdriver.Chrome()
# переход на страницу
driver.get("https://www.ozon.ru")

search_box = driver.find_element(By.XPATH, '//input[@type="text"]')
# ввод текста в поисковую строку
search_box.send_keys("ноутбуки")
# нажатие кнопки поиск
search_box.submit()

assert "ноутбуки" in driver.title


div_element = driver.find_element(By.ID, "cmp")
print(div_element.text())
print()
print(div_element.get_attribute('class'))
print()










# product = driver.find_element(By.XPATH, "//a[@href='/products/shirt']")
# product.click()
# add_to_cart = driver.find_element(By.XPATH, "//button[text()='Добавить в корзину']")
# add_to_cart.click()
# cart_items = driver.find_elements(By.XPATH, "//td[@class='cart-item-name']")
# assert len(cart_items) == 1, "В корзине должен быть только 1 товар"
# assert cart_items[0].text == "Рубашка", "В корзину добавлен неправильный товар"
# driver.quit()
'''Строка поиска '''


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

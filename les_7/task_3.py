'''Пагинация - переход на следующую страницу 

current_page = 1
# пагинация
while True:
    print(f'Происходит скрапинг {current_page} cnhfybws')
    # поиск кнопку
    try:
        # поиск кнопки на странице
        next_button = driver.find_element(*next_button_locator)
        # нажатие кнопки, если она есть
        next_button.click()
        # номер страницы
        current_page += 1
    # если кнопки нет, поиск заканчивается
    except NoSuchElementException:
        break


'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
# переход на сайт с несколькими страницами
driver.get("https://quotes.toscrape.com/page/1/")


quotes = []
page = 1

while True:
    quote_elements = driver.find_elements(By.XPATH, '//div[@class="quote"]')

    for quote_element in quote_elements:
        quote = quote_element.find_element(By.XPATH, './/span[@class="text"]').text
        author = quote_element.find_element(By.XPATH, './/small[@class="author"]').text

        quotes.append({
            'quote': quote,
            'author': author
        })

    next_button = driver.find_element(By.XPATH, '//li[@class="next"]/a')

    if not next_button:
        break

    next_button.click()

    time.sleep(2)
    page += 1
    if page > 5:
        break
    
with open('quotes.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['quote', 'author'])
    writer.writeheader()
    writer.writerows(quotes)

driver.quit()



# вывод в терминал

# for el in quotes:
#     print(f"{el['quote']} by {el['author']}")

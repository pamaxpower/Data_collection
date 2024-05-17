''' Пример обхода защиты '''

import time
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# использование Headless-браузера
options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

# загрузка сайта
driver.get('url')

# решение задачи каптчи
captcha_element = driver.find_element(By.ID, 'captcha')
captcha_image_scr = captcha_element.get_attribute('src')
captcha_image_data = requests.get(captcha_image_scr).content


# использование OCR(оптическое распознавание символов) для извлечения текста из изображения
captcha_text = "CAPTCHA_SOLUTION"

# ввод текста в форму каптчи
captcha_input = driver.find_element(By.ID, 'captcha_input')
captcha_input.send_keys(captcha_text)

# отправка формы
captcha_button = driver.find_element(By.ID, 'submit_button')
captcha_button.click()

time.sleep(5)

data = driver.find_elements(By.XPATH, 'tags')
data_list = []
for item in data:
    data_list.append(item.text)


driver.quit()

print(data_list)









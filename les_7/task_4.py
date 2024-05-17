''' Скрепинг динамических страниц 

# возвращение текущего заголовка
result = driver.execute_script('return document.title')
print(result)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint


driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/page/1/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quote")))

# quote = [el.text for el in element] # для метода _all-elements_located
quote = element.text

driver.quit()


pprint(quote)
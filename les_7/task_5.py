''' Работа с выпадающим меню '''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.example.com")



# tag dropdown_menu - тег меню
dropdown = driver.find_element(By.ID, 'tag dropdown_menu')
select = Select(dropdown)

# Option 2 - что искать
select.select_by_visible_text('Option 2')


''' Работа с модальным окном '''


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# нахождение триггера модального окна и клик на нем
modal_trigger = driver.find_element(By.ID, 'tags modal-trigger')
modal_trigger.click()

# ожидание загрузки окна
modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'modal')))

# взаимодействие с окном (например, ввод текста)
modal_input = modal.find_element(By.ID, '')
modal_input.send_keys('Hello World!')

# закрытие модального окна
modal_close = modal.find_element(By.ID, '')
modal_close.click()


driver.quit()
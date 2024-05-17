from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top")

movie_title = driver.find_elements(By.CSS_SELECTOR, 'a h3')
movie_rating = driver.find_elements(By.XPATH, '//span/@aria-label')

titles = [el.text for el in movie_title]
rating = [el.text for el in movie_rating]
print(titles)
for i in range(10):
    print(f'{i+1} - {titles[i]} - {rating[i]}')

driver.quit()

21:24






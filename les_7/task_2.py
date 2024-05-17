''' Топ-250 фильмов на IMDb'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint


driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top")

movie_title = driver.find_elements(By.CSS_SELECTOR, 'a h3')
movie_rating = driver.find_elements(By.XPATH, '//span[@data-testid="ratingGroup--imdb-rating"]')

titles = [el.text for el in movie_title]
rating = [el.text for el in movie_rating]


# pprint(rating)

for i in range(10):
    print(f"{i+1} - {titles[i][3:].strip()} - {rating[i].split(' ')[0]} " )

driver.quit()






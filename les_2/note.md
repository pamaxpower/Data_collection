Библиотека BeautifulSoap


# МЕТОДЫ

# find() - возвращает первый совпадающий тег или жлемент
a = soup.find('a')
print(a)

# find_all() - возвращает список всех тегов

# Доступ к атрибутам - для получения доступа к атрибутам тега, найденного методом find()
link = soup.find('a')
href = link['href']
print(link, href)

# get() - доступ к атрибутам со значением по умолчанию, если не найден
link = soup.find('a')
href = link['href', None]
print(href)

# string и text - досуп к содержимому тега без форматирования html
link = soup.find('a')
text = link.text
print(text)

# МЕТОДЫ ПО НАВИГАЦИИ ПО ДЕРЕВУ ПАРСИНГА

# contents - список прямых дочерник объектов тена в виде тогов и текста
html = soup.find('html')
children = html.contents

# descendants - возвращает генератор, который рекурсивно выдает всех потомков тега
html = soup.find('html')
descendants = html.descendants

# parent/parents - получение доступа к родителю тега и всем его потомкам

# next_siblink/previous_siblink - получение доступа к следующему или предыдущему тега соответственно

# find/find_all() - поиск тега в пределах поддерева, корнем которого является тег
div = soup.find('div')
links = div.find_all('a')












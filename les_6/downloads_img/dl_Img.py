'''Скачивание файлов'''

# # 1. Загрузка через requests
# import requests

url = 'https://gas-kvas.com/uploads/posts/2023-02/1675420055_gas-kvas-com-p-fonovii-risunok-les-22.jpg'

# # получаем ответ от сайта
# response = requests.get(url)
# # и записываем в файл
# with open('tree.jpg', 'wb') as f:
#     f.write(response.content)
# # из минусов: файл предварительно хранится в оперативке перед тем, как записаться в файл
    

# 2. Специальной библиотекой wget
import wget
# записывает картинку с названием из ссылки. При повторном запуске кода, создает копию картинки
wget.download(url)
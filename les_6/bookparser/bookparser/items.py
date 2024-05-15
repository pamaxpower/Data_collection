# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose


def process_name(value):
    '''на вход принимает "грязный" список вида
    [' Барсуков Ярослав Владимирович: Башня из грязи и веток '], а 
    вовзращает обработанную строку'''
    value = value[0].strip()
    return value

def process_price(value):
    '''на вход получает список вида [' 259\xa0₽ '],
    yd выходе будет список двух элементов: первой - число, второй - символ рубля'''
    # удаляем пробелы в начале и конце, меняем символы на ' ', разделяем на части по пробелу
    value = value[0].strip().replace('\xa0', ' ').split()
    # преобразовываем первое знаечние в формат int
    if value[0].isdigit():
        value[0] = int(value[0])
    # возвращем список вида [259, '₽']
    return value

def process_photo(value: str):
    # обработка ссылки типа ['//ndc.book24.ru/resize/820x1180/iblock/253/253ccf0fcbb1548ed42a0b2ad0dc1db1/d13b3af4d700a1c2027d955d5b356e02.jpeg 2x']
    if value.startswith('//'):
        # Убираем 2x и добавляем https:
        value = 'https:' + value.split()[0]
    else:
    # для ссылок типа 
    # ['https://cdn.book24.ru/v2/ITD000000001223562/COVER/dopfoto01__w410.webp, '
    # 'https://cdn.book24.ru/v2/ITD000000001223562/COVER/dopfoto01__w820.webp '
    # '2x']
        # берем центральный элемент, тк он большего размера
        value = value.split()[1]

    # удаление из списка элемента '2x'
    # value = [el for el in value if el != '2x']
    
    return value

class BookparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(process_price))
    photos = scrapy.Field(input_processor=MapCompose(process_photo))
    _id = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose


def process_name(value):
    value = value[0].strip()
    return value


def process_date(value):
    # делим строку по T (разделяем дату и время)
    value = value[0].split('T')
    # у времени убираем лишние элементы справа после точки
    value[1] = value[1].split('.')[0]
    # соединяем в строку
    value = ' '.join(value)
    return value


def process_photos(value):
    #value = value[-1]
    value = value.split(",")[-1].split()[0]
    return value



class UnsplashItem(scrapy.Item):
    # удалить лишние пробелы и взять первый  элемент
    name = scrapy.Field(input_processor=Compose(process_name))
    # взять только первый элемент
    img_url = scrapy.Field(output_processor=TakeFirst())
    # взять только первый элемент
    discription = scrapy.Field(output_processor=TakeFirst())
    # разделить дату и время пробелом, привести к нормальному виду и склеить в одну строчку
    date = scrapy.Field(input_processor=Compose(process_date))
    # отделить ссылку от информации
    photos = scrapy.Field(input_processor=MapCompose(process_photos))
    _id = scrapy.Field()

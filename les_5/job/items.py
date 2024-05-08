# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# ПОЛУЧЕНИЕ ЗНАЧЕНИЙ ИЗ ПАУКА

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    print('*************************************************************************************')
    name = scrapy.Field()
    salary = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()

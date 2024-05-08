# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# ОБРАБОТКА ЗНАЧЕНИЙ

from itemadapter import ItemAdapter
from pymongo import MongoClient

class JobPipeline:
    def __init__(self):
        client = MongoClient(host='localhost', port=27017)
        self.mongo_base = client.vacancies080524

    def process_item(self, item, spider):
        print()

        # КОД ДЛЯ ОБРАБОТКИ

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        
        return item
    


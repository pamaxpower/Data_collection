# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
import csv
# from pymongo import MongoClient


class LigaparserPipeline:
    # def __init__(self):
    #     client = MongoClient('localhost', 27017)
    #     self.mongo_base = client.ligapro

    def process_item(self, item, spider):

        # print(item.get('player1'))

        tours_list = []
        for i in range(len(item['player1'])):
            new_dict = {}
            for key in item.keys():
                new_dict[key] = item[key][i]

            # collection = self.mongo_base[spider.name]
            # collection.insert_one(new_dict)

            tours_list.append(new_dict)



        with open('./ligapro.csv', 'a+', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=tours_list[0].keys())
            #writer.writeheader()
            for row in tours_list:
                writer.writerow(row)

        return item
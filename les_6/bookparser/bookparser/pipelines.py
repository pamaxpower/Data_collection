# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# (files - для всех файлов, media - звук, картинки, images - только картинки)
from scrapy.pipelines.images import ImagesPipeline

from scrapy.http import Request


class BookparserPipeline:
    # точка входа
    def process_item(self, item, spider):
        print(item)
        return item


class BookPhotosPipeline(ImagesPipeline):
    # точка входа
    def get_media_requests(self, item, info):
        if item['photos']:
            for img_url in item['photos']:
                try:
                    yield Request(img_url)
                except Exception as e:
                    print(e)


    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
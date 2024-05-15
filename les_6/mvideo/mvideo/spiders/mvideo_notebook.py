import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MvideoNotebookSpider(CrawlSpider):
    name = "mvideo_notebook"
    allowed_domains = ["www.mvideo.ru"]
    start_urls = ["https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118"]

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths='//div[@class="product-title product-title--grid"]//a'),
            # LinkExtractor(allow=r"Items/"), # извлекает ссылки с веб-страницы содержащей Items/
            # LinkExtractor(deny =r"Items/")  # не переходить по ссылкам с Items/
            callback="parse_item", # функция для анализа посещенных страниц
            follow=True),)  # рекурсивное извлечение файлов до тех пор пока не будет ни одной подходящей ссылки

    def parse_item(self, response):
        print(response.url)














        # item = {}
        # #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # #item["name"] = response.xpath('//div[@id="name"]').get()
        # #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item



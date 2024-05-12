import scrapy


class LigaProSpider(scrapy.Spider):
    name = "liga_pro"
    allowed_domains = ["tt.sport-liga.pro"]
    start_urls = ["https://tt.sport-liga.pro"]

    def parse(self, response):
        pass

import scrapy
from scrapy.http import HtmlResponse


class LigaProSpider(scrapy.Spider):
    name = "liga_pro"
    allowed_domains = ["tt.sport-liga.pro"]

    # date = input('Введите дату в формате DD:MM:YYYY ')
    # day, month, year = date.split('.')
    
    start_urls = ["https://tt.sport-liga.pro/tours/?year=2024&month=05&day=10"]

    def parse(self, response: HtmlResponse):
        print(response.url)
        print(response.status)

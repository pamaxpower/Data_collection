# from typing import Any
import scrapy
from scrapy.http import HtmlResponse
from items import BookparserItem
from scrapy.loader import ItemLoader

class Book24Spider(scrapy.Spider):
    name = "book24"
    allowed_domains = ["book24.ru"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://book24.ru/search/?q={kwargs.get('query')}"]


    def parse(self, response):
        links = response.xpath('//div[@class="product-list__item"]//a[@class="product-card__image-link"]')
        for link in links:
            yield response.follow(link, callback=self.parse_book)
        

    def parse_book(self, response: HtmlResponse):
        # # классический вариант парсинга
        # name = response.xpath('//h1/text()').get()
        # price = response.xpath('//span[@class="app-price product-sidebar-price__price"]/text()').get()
        # url = response.url
        # # print(name, price, url)
        # photos = response.xpath('//picture[@class="product-poster__main-picture"]//@srcset | '
        #                         '//picture[@class="product-poster__main-picture"]//@data-srcset ').getall()
        # # print(photos)
        # # print(len(photos))
        # yield (BookparserItem(name=name, price=price, url=url, photos=photos))
        
        # парсинг с помощью класса ItemLoader
        loader = ItemLoader(item=BookparserItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('price', '//span[@class="app-price product-sidebar-price__price"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('photos', '//picture[@class="product-poster__main-picture"]//@srcset | '
                         '//picture[@class="product-poster__main-picture"]//@data-srcset')

        yield loader.load_item()


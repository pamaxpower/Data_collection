import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from ..items import CitilinkItem
from itemloaders.processors import MapCompose
from urllib.parse import urljoin
 

class CitilinkNotebooksSpider(CrawlSpider):
    name = "citilink_notebooks"

    # allowed_domains = ["www.citilink.ru"]
    # start_urls = ["https://www.citilink.ru/catalog/noutbuki/"]

    allowed_domains = ["www.zebrs.com"]
    start_urls = ["https://www.zebrs.com/categories/smartphones"]

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths=('//div[@class="app-catalog-oacxam e1ekfd3u0"]/a')), callback="parse_item", follow=True),
    #     Rule(LinkExtractor(restrict_xpaths=('//button[@class="e4uhfkv0 app-catalog-ki69qx e4mggex0"]'))),
    #     )
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="teaser-name"]')), callback="parse_item", follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//a[@rel="next"]'))),
        )



    def parse_item(self, response):
        print(response.url)

        # loader = ItemLoader(item=CitilinkItem(), response=response)
        # # определяем входной процессор - функции обрабатывающие получаемые данные
        # # в данном случае MapCompose принимает только одну функцию str.strip (убирает лишние пробелы)
        # loader.default_input_processor = MapCompose(str.strip)
        # loader.add_xpath('name', '//h1')

        # price_text = response.xpath('//span[@class="e1j9birj0 e106ikdt0 app-catalog-8hy98m e1gjr6xo0"]/text()')
        # absolute_img_urls = response.xpath('//div[@class="app-catalog-1igv0r1 e19l9blg0"]/img/@src').getall()
        
        # # # проверка на цену со скидкой (если разные выражения)
        # # if price_text:  # если переменная не пустая
        # #     # записываем ее
        # #     loader.add_value('price', price_text)
        # # else:
        # #     # если пустая, то записываем цену без скидки
        # #     loader.add_xpath('price', '')
        
        # # price_text = response.xpath('//div[contains(@class, "me-2 product-price")]/text()')
        # # relative_img_urls = response.xpath('//ul[@id="product-zoom"]/li/img').getall()
        # # absolute_img_urls = [urljoin('https://www.zebrs.com', img_url) for img_url in relative_img_urls]
        
        # loader.add_value('price', price_text)
        # loader.add_value('image_urls', absolute_img_urls)

        # yield loader.load_item()




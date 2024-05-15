import scrapy
from scrapy.http import HtmlResponse
from items import UnsplashItem
from scrapy.loader import ItemLoader


class SplashSpider(scrapy.Spider):
    name = "splash"
    allowed_domains = ["www.unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]


    def parse(self, response: HtmlResponse):
        links = response.xpath('//a[@itemprop="contentUrl"]/@href').getall()
        for link in links:
            link = 'https://' + self.allowed_domains[0] + link
            yield response.follow(link, callback=self.image_info)


    def image_info(self, response: HtmlResponse):
        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_value('img_url', response.url)
        loader.add_xpath('discription', '//p[@style="--truncatedTextToggleLines:2"]/text()')
        loader.add_xpath('date', '//time/@datetime')
        loader.add_xpath('photos', '//button//img/@srcset')
        yield loader.load_item()

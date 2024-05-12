# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LigaparserItem(scrapy.Item):
    # define the fields for your item here like:
    data = scrapy.Field()
    time = scrapy.Field()
    stol = scrapy.Field()
    rating = scrapy.Field()
    player1 = scrapy.Field()
    player2 = scrapy.Field()
    score = scrapy.Field()
    score_set = scrapy.Field()
    url_match = scrapy.Field()
    tours_info = scrapy.Field()
    _id = scrapy.Field()
    #pass
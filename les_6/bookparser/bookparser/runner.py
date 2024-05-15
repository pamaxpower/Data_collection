from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.book24 import Book24Spider

if __name__ == "__main__":
    configure_logging()
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    process = CrawlerProcess(get_project_settings())
    #query = input("Введите жанр: ") -> query=query
    process.crawl(Book24Spider, query='фантастика')
    process.start()




# ['https://ndc.book24.ru/resize/820x1180/iblock/710/7106dd9e113f0dd99214a802e3ba9968/a8479cbcd00f8dd9f7b3a4acd45d3c1e.jpg',
# 'https://cdn.book24.ru/v2/ITD000000001223562/COVER/cover4__w820.webp',
#             '2x',
# 'https://cdn.book24.ru/v2/ITD000000001223562/COVER/dopfoto00__w820.webp',
#             '2x',
# 'https://cdn.book24.ru/v2/ITD000000001223562/COVER/dopfoto01__w820.webp',
#             '2x',
# 'https://cdn.book24.ru/v2/ITD000000001223562/COVER/dopfoto02__w820.webp',
#             '2x',
# 'https://ndc.book24.ru/resize/820x1180/iblock/537/53764fc665e2a16621209d4f13ac6526/41659af282d8da5262821ba788cf19df.jpg',
# 'https://cdn.book24.ru/v2/ITD000000001223562/COVER/cover3d__w820.webp',
#             '2x']
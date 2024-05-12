''' Файл для запуска Scrapy '''
# импортируем модуль для связки всех составляющих программы
from scrapy.crawler import CrawlerProcess
# импортируем движок (внутреннее взаимодействие компонентов)
from scrapy.utils.reactor import install_reactor
# система логов
from scrapy.utils.log import configure_logging 
# чтение настроек и запись их в свойства паука
from scrapy.utils.project import get_project_settings

from spiders.hhru import HhruSpider

if __name__ == "__main__":
    configure_logging()
    settings = get_project_settings()
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    process = CrawlerProcess(settings)
    process.crawl(HhruSpider)
    process.start()



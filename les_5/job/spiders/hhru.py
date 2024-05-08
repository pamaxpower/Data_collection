import scrapy
from scrapy.http import HtmlResponse
from items import JobItem 

class HhruSpider(scrapy.Spider):
    name = "hhru"       # имя паука
    allowed_domains = ["hh.ru"]     # фильтр ресурсов (куда паук может "ходить")
    start_urls = ["https://hh.ru/search/vacancy?from=suggest_post&hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&text=Python+junior"]  # точка входа

    # рекурсивная генератор-функция
    def parse(self, response: HtmlResponse):
        
        # проверяем ссылку на следующую страницу
        next_page = response.xpath('//a[@data-qa="pager-next"]/@href').get()
        if next_page:
            # если она есть, переходим на следующую итерацию рекурсии
            yield response.follow(next_page, callback=self.parse)

        # сбор данных на первой странице
        links = response.xpath('//span[@class="serp-item__title-link-wrapper"]/a/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath('//h1/text()').getall()
        salary = response.xpath('//div[@data-qa="vacancy-salary"]//text()').getall()
        url = response.url
        yield JobItem(name=name, salary=salary, url=url)
        





    
import scrapy
from scrapy.http import HtmlResponse
from ligaparser.items import LigaparserItem


class LigaProSpider(scrapy.Spider):
    name = "liga_pro"
    allowed_domains = ["tt.sport-liga.pro"]
    url = 'https://tt.sport-liga.pro/'
    date = '11.05.2024'
    # date = input('Введите дату в формате DD:MM:YYYY ')
    # day, month, year = date.split('.')
    # start_urls = [url+f"tours/?year={year}&month={month}&day={day}"]
    start_urls = [url+"tours/?year=2024&month=05&day=11"]


    def parse(self, response: HtmlResponse):
        
        # data = [self.date for _ in range(len(time))]

        # возвращает ссылку вида href="tours/34259"
        r = response.xpath('//td[@class="tournament-icon"]/a/@href').getall()
        # приведем ссылку в рабочий вид
        links = [self.url + el for el in r]
        for link in links:
            yield response.follow(link, callback=self.tours_info)

    def tours_info(self, response: HtmlResponse):

        full_date = response.xpath('//div[@class="main-column"]//span[@class="day"]/text()').getall()
        full_name = response.xpath('//h1/text()').get()
        player1 = response.xpath('.//td[@class="right"]/a/text()').getall()
        player2 = response.xpath('.//td[@class="left"]/a/text()').getall()
        score = response.xpath('.//td[@class="score"]//a/text()').getall()
        um = response.xpath('.//td[@class="score"]//a/@href').getall()
        date = [full_date[0] for _ in range(len(score))]
        time = [full_date[1] for _ in range(len(score))]
        stol = [full_name.split('.')[0].split(' ')[-1] for _ in range(len(score))]
        rating = [full_name.split('.')[1].split(' ')[-1] for _ in range(len(score))]

        url_match = [self.url + el for el in um]
        if len(response.xpath('//table')) > 3:
            score_set = response.xpath('.//small[@class="nowrap"]/text()').getall()
            for i in range(len(score)):
                if score[i] == "- : -":
                    score_set.insert(i, 'не сыгран')
        else: score_set = ['не сыгран' for _ in range(len(score))]
        
        yield LigaparserItem(data=date, time=time, stol=stol, rating=rating,
                             player1=player1, player2=player2, score=score,
                             score_set=score_set, url_match=url_match)
        
        
        # ЗАБРАТЬ player1, player2, score, url_match, score_set
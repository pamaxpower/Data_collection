import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/country-list/inflation-rate?continent=world"]

    def parse(self, response):
        countries = response.xpath("//td/a")
        for el in countries:
            name = el.xpath(".//text()").get()
            link = el.xpath(".//@href").get()
            # yield{
            #     'country_name': name,
            #     'link': link
            # }
            yield response.follow(url=link, callback = self.parse_country, meta={'country_name': name})

    # def parse_country(self, response):
    #     rows = response.xpath("//tr[contains(@class, 'datatable')]")
    #     for el in rows:
    #         related = el.xpath(".//th[1]/text()").get()
    #         last = float(el.xpath(".//th[2]/text()").get())
    #         previous = float(rows.xpath(".//th[3]/text()").get())
    #         name = response.request.meta['country_name']
    #         yield{
    #             'country_name': name,
    #             'related': related,
    #             'last': last,
    #             'previous': previous
    #         }

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("//tr[contains(@class, 'datatable')]")

        for row in rows:
            related = row.xpath(".//td/a/text()").get().strip()
            last = float(row.xpath(".//td[2]/text()").get())
            previous = float(row.xpath(".//td[3]/text()").get())
        
            yield {
                'country_name' : name,
                'related' : related,
                'last' : last,
                'previous' : previous
            }
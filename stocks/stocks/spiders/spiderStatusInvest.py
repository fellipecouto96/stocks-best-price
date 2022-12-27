import scrapy


class SpiderstatusinvestSpider(scrapy.Spider):
    name = 'spiderStatusInvest'
    allowed_domains = ['statusinvest.com.br']
    start_urls = ['http://statusinvest.com.br/']

    def parse(self, response):
        pass

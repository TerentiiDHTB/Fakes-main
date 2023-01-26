import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScraperSpider(CrawlSpider):
    name = 'scraper'

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        ScraperSpider.rules = [
           Rule(LinkExtractor(unique=True), callback='parse_item'),
        ]
        super(ScraperSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        i = {}
        i['url'] = response.url
        return i
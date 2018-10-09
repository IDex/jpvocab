# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IotnewsSpider(CrawlSpider):
    name = 'iotnews'
    allowed_domains = ['ainow.ai']
    start_urls = ['http://ainow.ai/tag/machine-learning/']

    rules = (
        Rule(LinkExtractor(allow=r'2017'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['title'] = response.css('.single-title::text').extract()
        i['body'] = response.css('p::text').extract()
        return i

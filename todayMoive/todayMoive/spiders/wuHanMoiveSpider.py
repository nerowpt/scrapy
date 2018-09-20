# -*- coding: utf-8 -*-
import scrapy


class WuhanmoivespiderSpider(scrapy.Spider):
    name = 'wuHanMoiveSpider'
    allowed_domains = ['jycinema.com']
    start_urls = ['http://jycinema.com/']

    def parse(self, response):
        pass

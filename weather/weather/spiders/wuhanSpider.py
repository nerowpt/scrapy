# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class WuhanspiderSpider(scrapy.Spider):
    name = 'wuhanSpider'
    allowed_domains = ['https://www.tianqi.com/wuhan/']
    start_urls = []
    citys = ['shenzhen','shanghai','wuhan']
    for city in citys:
        start_urls.append('https://www.tianqi.com/' + city + '/')

    def parse(self, response):
        subSelector = response.xpath('//dl[@class="weather_info"]')
        items = []
        item = WeatherItem()
        item['img'] = subSelector.xpath('./dt/img/@src').extract()[0]
        item['cityName'] = subSelector.xpath('./dd[@class="name"]/h2/text()').extract()[0]
        item['week'] = subSelector.xpath('./dd[@class="week"]/text()').extract()[0]
        item['weather'] = subSelector.xpath('./dd[@class="weather"]/span/b/text()').extract()[0] + subSelector.xpath('./dd[@class="weather"]/span/text()').extract()[0]
        item['shidu'] = subSelector.xpath('./dd[@class="shidu"]/b[1]/text()').extract()[0] + " " + subSelector.xpath('./dd[@class="shidu"]/b[2]/text()').extract()[0]
        item['air'] = subSelector.xpath('./dd[@class="kongqi"]/h5/text()').extract()[0] + " " + subSelector.xpath('./dd[@class="kongqi"]/h6/text()').extract()[0]
        items.append(item)
        return items

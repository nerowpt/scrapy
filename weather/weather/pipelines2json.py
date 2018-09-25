# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import json
import codecs

from myLog import MyLog

class WeatherPipeline(object):
    def process_item(self, item, spider):
        m1 = MyLog()
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = 'weather' + today + '.json'
        m1.error('转换json开始')
        with codecs.open(fileName, 'a', encoding='utf8') as fp:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            fp.write(line)
        m1.warn('转换json结束')
        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import os.path
import urllib2
from myLog import MyLog

class WeatherPipeline(object):
    def process_item(self, item, spider):
        m1 = MyLog()
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = 'weather' + today + '.txt'
        m1.info('同步开始')
        with open(fileName, 'a') as fp:
            fp.write(item['cityName'].encode('utf-8')+'\t')
            fp.write(item['weather'].encode('utf-8')+'\t')
            imgName = os.path.basename(item['img'])
            fp.write(imgName+'\t')
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName,'wb') as fp:
                    response = urllib2.urlopen(item['img'])
                    fp.write(response.read())
            fp.write(item['shidu'].encode('utf-8')+'\t')
            fp.write(item['air'].encode('utf-8')+'\n\n')
            time.sleep(1)
        m1.info('同步结束')
        return item

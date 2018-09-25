# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import os.path

from myLog import MyLog

class WeatherPipeline(object):
    def process_item(self, item, spider):
        m1 = MyLog()
        cityName = item['cityName'].encode('utf8')
        img = os.path.basename(item['img'])
        week = item['week'].encode('utf8')
        weather = item['weather'].encode('utf8')
        shidu = item['shidu'].encode('utf8')
        air = item['air'].encode('utf8')

        m1.info('进行mysql存储')
        
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='spider',
            password='spider123',
            db='scrapyDB',
            charset='utf8'
        )
        cur = conn.cursor()
        cur.execute("insert into weather(cityName,img,week,weather,shidu,air) values(%s,%s,%s,%s,%s,%s)", (cityName,img,week,weather,shidu,air))
        cur.close()
        conn.commit()
        conn.close()

        m1.info('mysql存储完成')
        return item

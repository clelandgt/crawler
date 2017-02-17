# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from crawler.items import WeatherItem


HOST = 'localhost'
PORT = 27017


class WeatherPipeline(object):
    def __init__(self):
        session = pymongo.MongoClient(host=HOST, port=PORT)
        db = session['weather']
        self.data = db['data']

    def process_item(self, item, spider):
        if isinstance(item, WeatherItem):
            self.data.insert(dict(item))
        return item

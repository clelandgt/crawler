# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HifldSpiderItem(scrapy.Item):
    """ hifld 爬虫定义需要爬取的字段
    字段：
        category_name： 分类名
        dataset_name： 数据集名
        dateset_url： 数据下载链接
    """
    category_name = scrapy.Field()
    dataset_name = scrapy.Field()
    dataset_url = scrapy.Field()


class WeatherItem(scrapy.Item):
    """ 气象 爬虫定义需要爬取的字段
    字段:
        city: 城市名
        date: 日期
        time: 时间（CST)
        temp: 气温
        wind_chil: 风冷温
        dew_point: 露点
        humidity: 湿度
        pressure: 气压
        visibility: 能见度
        wind_dir: wind dir
        wind_speed: 风速
        gust_speed: 瞬间风速
        precip: precip
        event: 活动
        conditions: 状况
    """
    city = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    temp = scrapy.Field()
    wind_chill = scrapy.Field()
    dew_point = scrapy.Field()
    humidity = scrapy.Field()
    pressure = scrapy.Field()
    visibility = scrapy.Field()
    wind_dir = scrapy.Field()
    wind_speed = scrapy.Field()
    gust_speed = scrapy.Field()
    precip = scrapy.Field()
    event = scrapy.Field()
    conditions = scrapy.Field()










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
        temp: 气温（单位：°C）
        wind_chil: 风冷温（（单位：°C））
        dew_point: 露点（单位：°C）
        humidity: 湿度（单位：%）
        pressure: 气压（单位：hPa）
        visibility: 能见度
        wind_dir: 风向。   北（N）、东北东（NNE）、东北（NE）、东东北（ENE）、东（E）、东东南（ESE）、东南（SE）南东南（SSE）、南（S）、南西南（SSW）、西南（SW）、西西南（WSW）、西（W）、西西北（WNW）、西北（NW）、北西北（NNW）
        wind_speed: 风速（单位：km/h）
        gust_speed: 瞬间风速（单位：km/h）
        precip: 降雨量
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










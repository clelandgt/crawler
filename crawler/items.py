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
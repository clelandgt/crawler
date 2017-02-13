# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request
from crawler.items import HifldSpiderItem


class HifldSpider(scrapy.Spider):
    name = "hifld"
    allowed_domains = ["hifld-dhs-gii.opendata.arcgis.com"]
    start_urls = ['http://hifld-dhs-gii.opendata.arcgis.com/']

    def parse(self, response):
        elements = response.xpath("//div[@class='categoryIconList']/a")
        for element in elements:
            category_name = element.xpath("div/text()").extract_first().strip()
            category_url = 'https://hifld-dhs-gii.opendata.arcgis.com' + element.xpath('./@href').extract_first().strip()
            yield Request(url=category_url, callback=self.parse_results, meta={'category_name': category_name, 'page': 1})

    def parse_results(self, response):
        category_name = response.meta.get('category_name', 'untitled')
        page = int(response.meta.get('page', 0))
        elements = response.xpath("//li[@class='card card-summary item item-type-feature_service']")
        for element in elements:
            item = HifldSpiderItem()
            id = element.xpath("./div/@data-itemid").extract_first().strip()
            item['category_name'] = category_name
            item['dataset_name'] = element.xpath(".//div[@class='card-title']/a/text()").extract_first().strip()
            item['dataset_url'] = 'https://hifld-dhs-gii.opendata.arcgis.com/datasets/{}.csv'.format(id)
            yield item
        # 分页
        if len(elements) != 0:
            page += 1
            url = re.sub('page=[\d]*', '', response.url)
            url = '{0}&page={1}'.format(url, page)
            yield Request(url=url, callback=self.parse_results, meta={'category_name': category_name})




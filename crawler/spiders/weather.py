# -*- coding: utf-8 -*-
""" 爬取中国主要城市气象历史数据
构造爬取的下载url https://www.wunderground.com/history/airport/ZBAA/2000/2/15/DailyHistory.html?req_city=Beijing&req_statename=China
需要以下几个参数：
    - 地区识别码: ZBAA
    - 城市： Beijing
    - 国家： China
    - 时间： 2000/2/15/

"""
import scrapy
import datetime
from scrapy.http import Request
from crawler.items import WeatherItem


CITYS = [
    {'city': 'Beijing', 'state_name': 'China', 'code': 'ZBAA', 'start_date': '2000-01-01', 'end_date': '2017-02-16'}
]


class WeatherSpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["www.wunderground.com"]

    def start_requests(self):
        for city in CITYS:
            city_name = city['city']
            state_name = city['state_name']
            code = city['code']
            start_date = city['start_date']
            end_date = city['end_date']
            dates = date_range(start_date, end_date)
            for date in dates:
                url = 'https://www.wunderground.com/history/airport/{code}/{date}/DailyHistory.html?req_city={city_name}&req_statename={state_name}'.format(
                    code=code,
                    date=date,
                    city_name=city_name,
                    state_name=state_name
                )
                yield Request(url, callback=self.parse, meta={'city': city_name, 'date': date})

    def parse(self, response):
        city = response.meta.get('city', '')
        date = response.meta.get('date', '')
        records = response.xpath("//table[@class='obs-table responsive']/tbody/tr")
        for record in records:
            item = WeatherItem()
            item['city'] = city
            item['date'] = date
            item['time'] = record.xpath("td[1]/text()").extract_first()
            item['temp'] = record.xpath("td[2]/span/span[1]/text()").extract_first()
            item['wind_chill'] = record.xpath("td[3]/span/span[1]/text()").extract_first()
            item['dew_point'] = record.xpath("td[4]/span/span[1]/text()").extract_first()
            item['humidity'] = record.xpath("td[5]/text()").extract_first()
            item['pressure'] = record.xpath("td[6]/span/span[1]/text()").extract_first()
            item['visibility'] = record.xpath("td[7]/text()").extract_first()
            item['wind_dir'] = record.xpath("td[8]/text()").extract_first()
            item['wind_speed'] = record.xpath("td[9]/span/span[1]/text()").extract_first()
            item['gust_speed'] = record.xpath("td[10]/text()").extract_first()
            item['precip'] = record.xpath("td[11]/text()").extract_first()
            item['event'] = record.xpath("td[12]/text()").extract_first()
            item['conditions'] = record.xpath("td[13]/text()").extract_first()
            yield item
        pass


def date_range(begin_date, end_date):
     dates = []
     dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
     dates.append(dt.strftime("%Y/%m/%d/"))
     date = begin_date[:]
     while date < end_date:
         dt = dt + datetime.timedelta(1)
         dates.append(dt.strftime("%Y/%m/%d"))
         date = dt.strftime("%Y-%m-%d")
     return dates


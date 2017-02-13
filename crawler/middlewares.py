# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from crawler.settings import USER_AGENT_LIST


class UserAgentMiddleware(object):
    """ 更新 user agent """
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent
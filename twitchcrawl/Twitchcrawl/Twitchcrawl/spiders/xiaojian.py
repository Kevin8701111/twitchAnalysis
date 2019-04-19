# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json
import datetime

class SullygnomeSpider(scrapy.Spider):
    name = 'xiaojian'
    allowed_domains = ['sullygnome.com']
    start_urls = ['https://sullygnome.com/api/tables/channeltables/streams/365/5086136/%20/1/2/desc/0/100',
    'https://sullygnome.com/api/tables/channeltables/streams/365/5086136/%20/1/2/desc/101/100',
    'https://sullygnome.com/api/tables/channeltables/streams/365/5086136/%20/1/2/desc/200/100']
    
    def parse(self, response):
        url = response.url
        soup = BeautifulSoup(response.text, "lxml")
        pre = soup.select('p')[0].text
        prej = json.loads(pre)
        for data in range(0,101):
            yield{
                'id' : prej['data'][data]['channelurl'],
                'viewers' : prej['data'][data]['starttime'],
                'rownum' : prej['data'][data]['endtime'],

            }
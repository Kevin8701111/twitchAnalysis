# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json
import datetime

class SullygnomeSpider(scrapy.Spider):
    name = 'sullygnome'
    allowed_domains = ['sullygnome.com']
    url = 'https://sullygnome.com/api/general/directorybrowser/getgames/2019-04-18T20:00:00.000Z/50/0'
    start_urls = ['https://sullygnome.com/api/general/directorybrowser/getgames/2019-04-18T20:00:00.000Z/50/0']
    url = url.split('/')[7]
    url = url.split('T')[0]
    url = url.split('-')
    year = int(url[0])
    month = int(url[1])
    day = int(url[2])
    stopadd = 0

    dat = datetime.datetime(year, month, day)
    d = datetime.timedelta(days=1)
    ymd = '2019-04-18'
    while(ymd != '2019-04-18'):
        dat = dat + d
        ymd = str(dat).split(' ')[0]
        urls = 'https://sullygnome.com/api/general/directorybrowser/getgames/' + ymd + 'T20:00:00.000Z/50/0'
        start_urls.append(urls)

    # while stopadd <= 31:
    #     day = day+1
    #     stopadd = stopadd + 1
    #     print(stopadd)
    #     print(day)
        # if year <= 2019:
        #     if month <=12:

    # print(year, month, day)

    def parse(self, response):
        url = response.url
        print(url)
        url = url.split('/')[7]
        url = url.split('.')[0]
        url = url.split('T')
        ymd = url[0]
        hms = url[1]
        soup = BeautifulSoup(response.text, "lxml")
        pre = soup.select('p')[0].text
        prej = json.loads(pre)
        for data in range(0,10):
            yield{
                'viewers' : prej['data'][data]['viewers'],
                'rownum' : prej['data'][data]['rownum'],
                'id' : prej['data'][data]['id'],
                'channels' : prej['data'][data]['channels'],
                'name' : prej['data'][data]['name'],
                'date' : ymd,
                'time' : hms,
            }
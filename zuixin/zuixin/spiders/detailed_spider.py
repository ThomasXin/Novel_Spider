# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import  Selector
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
quanshu = client['quanshu']
detailed = quanshu['detailed']
urls = quanshu['urls']

class DetailedSpider(Spider):
    name = 'detailed'
    allowed_domain = []
    start_urls = []
    for Total_url in urls.find():
        start_urls.append(Total_url['url'])

    def parse(self, response):
        sel = Selector(response)
        urlm = response.url
        sites = sel.xpath('//div[@class="clearfix dirconone"]/li/a')
        time.sleep(1)
        for site in sites:
            for url in site.xpath('@href').extract():
                urlz = urlm.replace('index.html', url)
                data = {
                    'url': urlz,
                    'title': site.xpath('text()').extract(),
                    'sign': urlm.split('/')[-2]
                }
                # detailed.insert_one(data)

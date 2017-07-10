# -*- coding:utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
import pymongo
client = pymongo.MongoClient('localhost', 27017)
quanshu = client['quanshu']
urls = quanshu['urls']
class DmozSpider(Spider):
    # 这是爬虫的名字（必须唯一）
    name = 'dmoz11'
    # 这是爬取的范围
    allowed_domains = ['quanshuwang.com']
    # 这是我们要爬取的地址
    start_urls = [

    ]
    for page in range(1, 10):
        start_urls.append('http://www.quanshuwang.com/map/%s.html' % page)
    def parse(self, response):
       sel = Selector(response)
       # 这是查找到所有a标签
       sites = sel.xpath('//a')
       for site in sites:
            #  这是查找到每一个a标签的href属性
            for urlt in site.xpath('@href').extract():
                # 用'/'进行分组
               sign = urlt.split('/')
               if sign[-1]== 'index.html':
                   data = {
                       # 这是每一本小说的链接地址
                       'url': 'http://www.quanshuwang.com'+ urlt,
                       # 这是每一本小说的地址
                       'name': site.xpath('text()').extract(),
                       # 这是每一本小说的标签
                       'sign': sign[-2]
                   }
                   #  将数据保存到库中
                   urls.insert_one(data)
               else:
                   pass
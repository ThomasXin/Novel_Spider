# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ZuixinItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DmozItem(Item):
    '''这是获取详细信息 '''
    # 获取书名
    name = Field()
    # 获取链接地址
    url = Field()
    # 获取详情
    description = Field()

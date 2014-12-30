# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class BseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol=Field()
    name=Field()
class RupeeTalkItem(scrapy.Item):
    cname=Field()
    sector=Field()
    bse_code=Field()
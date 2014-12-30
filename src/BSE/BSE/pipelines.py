# -*- coding: utf-8 -*-
from scrapy.contrib.exporter import CsvItemExporter


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class BsePipeline(object):
    def __init__(self):
#         self.modelsCsv = csv.writer(codecs.open('aaaaaaaaaaa.csv', mode='w',encoding='utf-8'))
#         self.modelsCsv.writerow((['company'],['revenue']))
        self.ex=['symbol','company']
    def spider_opened(self,spider):
        self.modelsCsv = CsvItemExporter(open('sym_com.csv','a'))
        self.modelsCsv.start_exporting()
#         self.modelsCsv.writerow((['company'],['revenue']))
        
        self.lst=[]
    def process_item(self, item, spider):
#         if isinstance(item, LastItem): 
        item['symbol'] = item['symbol'].encode('utf-8')
        item['name'] = item['name'].encode('utf-8')
#             self.modelsCsv.writerow(([item['company']],[item['revenue']]))
#         self.modelsCsv.export_item(([item['company']],[item['revenue']]))
        try:
            self.modelsCsv.export_item(item)
        except:
            print item
#         print 'check 1'
#         self.lst.append(([item['company']],[item['revenue']])) 
        
        return item
    def spider_closed(self, spider):
        self.modelsCsv.finish_exporting()
class RupeeTalkPipeline(object):
    def __init__(self):
#         self.modelsCsv = csv.writer(codecs.open('aaaaaaaaaaa.csv', mode='w',encoding='utf-8'))
#         self.modelsCsv.writerow((['company'],['revenue']))
        self.ex=['Name','Sector','BSE Code']
    def spider_opened(self,spider):
        self.modelsCsv = CsvItemExporter(open('rupeetalk.csv','a'))
        self.modelsCsv.start_exporting()
#         self.modelsCsv.writerow((['company'],['revenue']))
        
        self.lst=[]
    def process_item(self, item, spider):
#         if isinstance(item, LastItem): 
#         print item,"====="
#         item['cname'] = item['cname'].encode('utf-8')
#         item['sector'] = item['sector'].encode('utf-8')
#         item['bse_code'] = item['bse_code'].encode('utf-8')
#             self.modelsCsv.writerow(([item['company']],[item['revenue']]))
#         self.modelsCsv.export_item(([item['company']],[item['revenue']]))
        try:
            self.modelsCsv.export_item(item)
        except:
            print item
#         print 'check 1'
#         self.lst.append(([item['company']],[item['revenue']])) 
        
        return item
    def spider_closed(self, spider):
        self.modelsCsv.finish_exporting()
'''
Created on 22-Dec-2014

@author: VAIBHAV JAIN
'''
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector

class BSESpider(CrawlSpider):
    name='bsespider'
    allowed_domains=['www.topstockresearch.com']
    start_urls=['http://www.topstockresearch.com/index/BSE_500.html']
    def parse(self,response):
        sel=Selector(response)
        data=sel.xpath("//div[@class='datagrid']//table//*//td//a//text()").extract()
        print data
        step=1
        lst=[]
        for i in range(0,len(data),step):
#             while data[i]== ' ':
#                 i=i+1 
#             print data[i]
#             while data[i+1]==' ':
#                 i=i+1
#             print data[i]
            print data[i]
            lst.append(data[i])
        print len(lst)
        comp=[]
        data=sel.xpath("//div[@class='datagrid']//table//*//td//text()").extract()
        for i in range(0,len(lst)):
            for j in range(0,len(data)):
                if lst[i]==data[j]:
                    while(data[j]==" "):
                        j+=1
                    comp.append(data[j])
                    break
        for row in comp:
            print "--->",row        
        print len(comp)
'''
Created on 23-Dec-2014

@author: VAIBHAV JAIN
'''
from scrapy.contrib.spiders.crawl import CrawlSpider
from scrapy.selector import Selector
from BSE.pipelines import RupeeTalkPipeline
from BSE.items import RupeeTalkItem

class RupeeTalkSpider(CrawlSpider):
    name='rupeetalkspider'
    allowed_domains=['www.rupeetalk.com']
    st_url='http://www.rupeetalk.com/stocks/search-index.php?search=3&alphabet='
    en_url='&title=Aplhabatical-list-of-companies-listed-in-nse-bse-stock-exchange'
    start_urls=[]
    for i in range(0,26):
        s=st_url+chr(i+65)+en_url
        start_urls.append(s)
    cnme=[]
    csec=[]
    bsecode=[]
    j=0    
    def parse(self,response):
        sel=Selector(response)
#         data=sel.xpath('//*//table//tr//td//text()').extract()
        divs=sel.xpath("//div[@class='stock-search-result-div']//p//text()").extract()
#         print divs
        c=3
        pipeline=RupeeTalkPipeline()
        pipeline.spider_opened(RupeeTalkSpider)
        it=RupeeTalkItem()
        i=0
        for i in range(0,len(divs)):
            if c<len(divs) and not divs[c]=='NA':
                print divs[c]
                if i%4==0:
                    self.cnme.append(divs[i]) 
                    it['cname']=divs[i]
                elif i%4==1:
                    self.csec.append(divs[i])
                    it['sector']=divs[i]
                elif i%4==2:
                    self.bsecode.append(divs[i])s
                    it['bse_code']=divs[i]
                    pipeline.process_item(it,RupeeTalkSpider)
                    c+=4
                else:
                    c=c+4
            else:
                    c=c+4
#         for self.j in range(0,len(self.cnme)):
#             print self.cnme[self.j],'--->',self.csec[self.j],'---->',self.bsecode[self.j]
#             it['cname']=self.cnme[self.j]
#             it['sector']=self.csec[self.j]
#             it['bse_code']=self.bsecode[self.j]
#             pipeline.process_item(it,RupeeTalkSpider)
        pipeline.spider_closed(RupeeTalkSpider)    
#         print len(self.cnme),self.cnme
#         print len(self.csec),self.csec
#         print len(self.bsecode)   
            
#         for div in divs:
#             table=div.xpath("//table/text()")
#             for tab in table:
#                 print tab
#                 data=tab.extract()
#                 for row in data:
#                     try:
#                         print row.decode("utf-8")
#                     except:
#                         print "passing"
#                         pass
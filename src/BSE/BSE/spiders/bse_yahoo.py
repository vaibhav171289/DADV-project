'''
Created on 22-Dec-2014

@author: VAIBHAV JAIN
'''
from scrapy.contrib.spiders.crawl import CrawlSpider
from scrapy.selector import Selector
from BSE.pipelines import BsePipeline
from BSE.items import BseItem

class bseyahoospider(CrawlSpider):
    name='bseyahoospider'
    allowed_domains=['in.finance.yahoo.com']
    start_urls=['https://in.finance.yahoo.com/gainers?e=bo','https://in.finance.yahoo.com/losers?e=bo','https://in.finance.yahoo.com/actives?e=bo']
    lst=[]    
    comp=[]
    count=0
    def parse(self,response):
        sel=Selector(response)
        data=sel.xpath("//div[@id='yfitp']//table//*//td//a//text()").extract()
#         print data
        step=1
        for i in range(0,len(data),step):
            if not('Chart'==data[i] or 'More'==data[i] or 'Profile'==data[i]):
#                 print data[i]
                if data[i] not in self.lst:
                    self.lst.append(data[i])
                    
        data=sel.xpath("//*//p[@class='headlinelinks']//a//text()").extract()
#         print data   
        for i in range(0,len(data),step):
#             print (data[i])[:len(data[i])-3]
            if data[i] not in self.lst:
                self.lst.append(data[i])
        data=sel.xpath("//div[@id='yfitp']//table//*//td//text()").extract()
#         print data
        print len(self.lst)
        pipeline=BsePipeline()
        pipeline.spider_opened(bseyahoospider)
        it=BseItem()
        i=1
        for row in self.lst:
            for j in range(0,len(data)):
                if row==data[j]:
#                     print data[j]
                    while(data[j+1]==" "):
                        j=j+1
#                     print '--->',data[j+1]
                    self.comp.append(data[j+1])
                    it['symbol']=row
                    it['name']=data[j+1]
                    i+=1
                    pipeline.process_item(it,bseyahoospider)
        self.count=self.count+1
#         if self.count==3:
        pipeline.spider_closed(bseyahoospider)
        print 'pipeline closed--->',i
#         else:
        print self.count                        
        print self.comp
        
        for row in self.lst:
#             i=0
#             j=1
#             start_Date='2010-01-01' 
#             end_Date='2014-12-22'
#             
#             
#             while i<len(self.lst):
#                 current_Date=start_Date
#                 print "***Company***",self.lst[i]
#                 while(start_Date != end_Date):
#                     current_Date=start_Date
#                     date1 =current_Date.split('-')     # spliting to date suitable format 
#                     date = datetime.date(int(date1[0]),int(date1[1]),int(date1[2]))
#                     date += datetime.timedelta(days=1)   # incrementing date      
#                     date2=str(date)
#                     next_Date=date2
#                     #print "currrent date",current_Date
#                     #print "next date",next_Date
#                     try:
#                         data= ystockquote.get_historical_prices(self.lst[i],current_Date,next_Date) # returns historical data of that company 
#                     except urllib2.HTTPError, e:
#                         print e.code
#                         print e.msg
#                     if current_Date in data:
#                         details = data[current_Date]
#                         open_price = details['Open']
#                         print "Open price",open_price
#                         start_Date=next_Date
#                     else:
#                         print next_Date
#                         start_Date=next_Date
#                 start_Date='2013-07-15'
#                 i+=1

#             fullpath=os.path.join("",row[:len(row)-3]+".csv")
            link="http://real-chart.finance.yahoo.com/table.csv?s="+row+"&d=12&e=22&f=2014&g=d&a=01&b=01&c=2009&ignore=.csv"
#             opener=urllib.FancyURLopener({})
#             d=""
#             data=opener.open(link,d)
#             print d
            
#             try:    
#                 urllib.urlretrieve(link,filename="BSE//stock//"+row[:len(row)-3]+".csv")#"finance Data\\%s.csv" %row[:len(row)-3])
#             except:
#                 pass    

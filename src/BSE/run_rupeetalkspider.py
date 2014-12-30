'''
Created on 23-Dec-2014

@author: VAIBHAV JAIN
'''

from scrapy import cmdline


cmdline.execute("scrapy crawl rupeetalkspider".split())

# def bse_company():
#     proxy={"http":"http://proxy.iiit.ac.in:8080"}
#     opener=urllib.FancyURLopener({})
# #     data = opener.open('http://economictimes.indiatimes.com/archivelist/year-2014,month-8,starttime-41852.cms')
# #     data=opener.open('https://in.finance.yahoo.com/actives?e=bo')
#     data=opener.open("http://www.bseindia.com/corporates/List_Scrips.aspx?expandable=1")
#     html=data.read().decode("utf-8").encode("utf-8")
# #     try:
#     soup = BeautifulSoup(html,from_encoding=data.info().get_charset())
#     print soup.prettify()
# #         print soup 
# #         tables=soup.span
#     tables = soup.find_all("table")#,{"id":"ctl00_ContentPlaceHolder1_gvData"})
#     print tables
#     for row in tables:
#         print row.tdb.string
# #     except:
# #         print "passing"
# #         pass        
# if __name__=='__main__':
#     bse_company()
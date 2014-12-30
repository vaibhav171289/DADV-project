'''
Created on 21-Dec-2014

@author: VAIBHAV JAIN
'''
from calendar import Calendar
import calendar
import csv
import urllib

from bs4 import BeautifulSoup


def scrapEconomicTimes():
    proxy={"http":"http://proxy.iiit.ac.in:8080"}
    opener=urllib.FancyURLopener({})
    data = opener.open('http://economictimes.indiatimes.com/archivelist/year-2014,month-8,starttime-41852.cms')
    html=data.read()
    soup = BeautifulSoup(html)
    soup.prettify()
    print soup 
    tables = soup.find_all('table')
    for table in tables:
    #     print table.section
        t_row = table.find_all('a')
        for t in t_row:
            try:
                print t.string
            except:
                pass
        print'-----------------------------------------'
if __name__=="__main__":
#     scrapEconomicTimes()
    print calendar.firstweekday
#     for i in Calendar.itermonthdays( self,2014, 12):
#         print i
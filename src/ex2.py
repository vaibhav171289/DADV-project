'''
Created on 22-Dec-2014

@author: VAIBHAV JAIN
'''
import urllib

from bs4 import BeautifulSoup


def bse_company():
    proxy={"http":"http://proxy.iiit.ac.in:8080"}
    opener=urllib.FancyURLopener(proxy)
#     data = opener.open('http://economictimes.indiatimes.com/archivelist/year-2014,month-8,starttime-41852.cms')
#     data=opener.open('https://in.finance.yahoo.com/actives?e=bo')
    data=opener.open("http://www.topstockresearch.com/index/BSE_500.html")
    html=data.read()
    soup = BeautifulSoup(html)
    soup.prettify()
#     print soup 
    tables = soup.find_all('div')
#     tables=table1.find_all("tr")
#     print tables
    lst=[]
    for table in tables:
    #     print table.section
        t_row = table.find_all('td')
        for t in t_row:
            try:
#                 if not t.string == 'Chart' and not t.string=='Profile' and not t.string=='More':
                if not t.a.string==None:  
                    lst.append(t.string)
                    print t.a.string
#                 print t.string
            except:
                pass
    print len(lst)        
    print'-----------------------------------------'
'''    pr=soup.find_all('div',{"class":"mod yfi_quote_headline symbol-links"})
    print pr
    for row in pr:
        r=row.p
        print r
        try:
            if r.string not in lst:
                print r.string
                lst.append(r.string)
        except:
            pass
    print len(lst)'''
if __name__ == '__main__':
    bse_company()
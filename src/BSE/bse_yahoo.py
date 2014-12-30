'''
Created on 22-Dec-2014

@author: VAIBHAV JAIN
'''
import os

from scrapy import cmdline


if not os.path.isdir("BSE//stock") or not os.path.exists("BSE//stock"):
    os.mkdir("BSE//stock//")
    print "created"
else:
    print os.path.abspath(("stock"))
print "xxx"
cmdline.execute("scrapy crawl bseyahoospider".split())
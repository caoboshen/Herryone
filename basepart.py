# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:26:06 2019

@author: lenovo
"""

import requests
from bs4 import BeautifulSoup

class datalist:
    def __init__(self,name,fraction,kind):
        self.name=name
        self.fraction=fraction
        #self.kind=kind
        

def getsubject(txt):
    url1 = "https://www.douban.com/search?q=" + txt
    r = requests.get(url1, timeout=20)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text

def dealurl(html):
    soup = BeautifulSoup(html,"html.parser")
    contentlist = soup.find_all("div","content")
    ndatalist=[]
    for i in contentlist[0:5]:
        try:
            j=i.find("span","rating_nums")
            x=datalist(i.div.a.string,j.string)
            ndatalist.append(x)
        except:
            x=datalist(i.div.a.string,'尚未上映')
            ndatalist.append(x)
    return ndatalist

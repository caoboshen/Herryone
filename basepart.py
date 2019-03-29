# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:26:06 2019

@author: lenovo
"""
import os
import requests
from bs4 import BeautifulSoup

class datalist:
    def __init__(self,name,fraction,kind):
        self.name=name
        self.fraction=fraction
        self.kind=kind
        

def getsubject(txt):
    url1 = "https://www.douban.com/search?q=" + txt
    r = requests.get(url1, timeout=20)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text

def getpic(j,picp):
    root="D://doubanpics//"
    path=root + str(j)+".jpg"
    if not os.path.exists(root):
        os.mkdir(root)
    p=requests.get(picp)
    with open(path,'wb') as f:
        f.write(p.content)

def dealurl(html):
    soup = BeautifulSoup(html,"html.parser")
    contentlist = soup.find_all("div","result")
    ndatalist=[]
    for j in range(0,5):
        i=contentlist[j]
        k=i.find("div",class_="title")
        l=i.find("img")
        picp=l.attrs['src']
        getpic(j,picp)
        try:
            j=i.find("span","rating_nums")
            x=datalist(k.a.string,j.string,k.span.string)
            ndatalist.append(x)
        except:
            x=datalist(k.a.string,'尚未上映',k.span.string)
            ndatalist.append(x)
        
    return ndatalist

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:26:06 2019

@author: lenovo
"""
import os
import requests
from bs4 import BeautifulSoup

class datalist:#数据类-保存搜索结果的三样
    def __init__(self,name,fraction,kind):
        self.name=name
        self.fraction=fraction
        self.kind=kind
        

def getsubject(txt):#获取页面信息
    try:
        url1 = "https://www.douban.com/search?q=" + txt
        r = requests.get(url1, timeout=20)
        r.raise_for_status()#若访问失败，将产生相应信号，使程序返回空串
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def getpic(j,picp):#保存图片到本地
    root="D://doubanpics//"
    path=root + str(j)+".jpg"
    if not os.path.exists(root):
        os.mkdir(root)#如果不存在该路径 就创建该路径
    p=requests.get(picp)
    with open(path,'wb') as f:
        f.write(p.content)

def dealurl(html):#分析页面内容
    soup = BeautifulSoup(html,"html.parser")
    contentlist = soup.find_all("div","result")
    ndatalist=[]
    for j in range(0,5):
        i=contentlist[j]
        k=i.find("div",class_="title")
        l=i.find("img")#解析名字、分数
        picp=l.attrs['src']
        getpic(j,picp)#获得图片的url 调用函数将其保存下来
        try:
            j=i.find("span","rating_nums")
            x=datalist(k.a.string,j.string,k.span.string)
            ndatalist.append(x)
        except:
            x=datalist(k.a.string,'尚未上映',k.span.string)
            ndatalist.append(x)#利用try-except结构应对尚未上映而评分不存在的情况
        
    return ndatalist

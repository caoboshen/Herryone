# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:23:53 2019

@author: lenovo
"""
import os
from basepart import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import requests
from bs4 import BeautifulSoup

window=tk.Tk()
window.title('search-douban')
window.geometry('600x500')

e=tk.Entry(window,show=None)
e.place(x=100,y=20)

var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
t=[]
i=0

def setpic(j):
    global imagen
    file = Image.open("D://doubanpics//"+str(j)+".jpg")
    imagen=ImageTk.PhotoImage(file)
    k=tk.Label(window,image=imagen)    
    k.place(x=50,y=80)

def search():
    f=e.get()
    if(f is None):
        var1.set('')
        var2.set('')
        var3.set('')
    else:
        html=getsubject(f)
        global ndatalist
        ndatalist=dealurl(html)
        global i
        i=0
        var1.set(ndatalist[0].name)
        var2.set(ndatalist[0].fraction)
        var3.set(ndatalist[0].kind)
        setpic(0)

def gonext():
    try:
        global i
        i=(i+1)%5
        var1.set(ndatalist[i].name)
        var2.set(ndatalist[i].fraction)
        var3.set(ndatalist[i].kind)
        setpic(i)
    except:
        var1.set('')
        var2.set('')
        var3.set('')

def golast():
    try:
        global i
        if(i==0):
            i=4
        else:
            i=i-1
        var1.set(ndatalist[i].name)
        var2.set(ndatalist[i].fraction)
        var3.set(ndatalist[i].kind)
        setpic(i)
    except:
        var1.set('')
        var2.set('')
        var3.set('')

a1=tk.Label(window,textvariable=var1,width=30,height=1)
a1.place(x=400,y=150)
a2=tk.Label(window,textvariable=var2,width=30,height=1)
a2.place(x=400,y=170)
a3=tk.Label(window,textvariable=var3,width=30,height=1)
a3.place(x=400,y=190)
f1=tk.Label(window,text='Key World:',width=10,height=1)
f1.place(x=20,y=18)
f2=tk.Label(window,text='   Name:',width=9,height=1)
f2.place(x=380,y=150)
f3=tk.Label(window,text='Farction:',width=9,height=1)
f3.place(x=380,y=170)
f4=tk.Label(window,text='     Kind:',width=9,height=1)
f4.place(x=380,y=190)
b=tk.Button(window,text='search',width=7,height=1,command=search)
b.place(x=250,y=15)
b1=tk.Button(window,text='last',width=7,height=1,command=golast)
b1.place(x=420,y=350)
b2=tk.Button(window,text='next',width=7,height=1,command=gonext)
b2.place(x=500,y=350)

window.mainloop()
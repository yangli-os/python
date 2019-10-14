# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:05:41 2018

@author: liyang
"""

f=open("data.txt","r",encoding="utf-8")
for l in f:
    l = l.split(',')
    s=0.0
    for i in l:
       items=i.split(":")
       s+=eval(items[1])
    print("总和是：{}，平均值是{:.2f}".format(s,s/len(l)))
f.close()
    
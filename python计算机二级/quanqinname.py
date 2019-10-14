# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:24:13 2018

@author: liyang
"""
ls = []
for name in range(1,11):
    fo=open(str(name)+".csv","r",encoding="utf-8")
    for line in fo:
        line = line.replace("\n","")
        ls.append(line.split(",")[0])
    fo.close()
counts={}
for word in ls:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
print("全勤的同学有：",end="")
for i in range(1,74):
    word,counts=items[i]
    if counts==10:
        print(word,end=".")
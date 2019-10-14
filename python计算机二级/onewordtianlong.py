# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:39:58 2018

@author: liyang
"""
fi=open("天龙八部-网络版.txt","r",encoding="utf-8")
fo=open("天龙八部-提取版.txt","w",encoding="utf-8")
txt=fi.read()
counts={}
for word in txt:
    counts[word]=counts.get(word,0)+1
del counts[' ']
del counts['\n']
ls=[]
for key in counts:
    ls.append("{}:{}".format(key,counts[key]))
fo.write(",".join(ls))
fi.close()
fo.close()
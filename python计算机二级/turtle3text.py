# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:35:05 2018

@author: liyang
"""

d={"数学":101,"语文":202,"英语":203,"物理":204,"生物":206}
d["化学"]=205
del d["生物"]
for key in d:
    print("{}:{}".format(d[key],key))
print(d)
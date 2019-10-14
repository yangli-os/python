# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 10:52:31 2018

@author: liyang
"""

def getIntput():
    try:
        s=input("请输入一个整数")
        while eval(s)!=int(s):
            s=input("再次输入")
    except:
        return getIntput()
    return int(s)
print(getIntput())
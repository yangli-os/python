# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 11:12:44 2018

@author: liyang
"""

num=eval(input("请输入一个整数"))
for a in range(2,num):
    k = 0
    for i in range(2,a):
        if a % i == 0 :
            k += 1
            break
    if k == 0 :
        print(a,end=" ")
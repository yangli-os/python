# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:51:51 2018
输出斐波那契数列
@author: liyang
"""

a,b=0,1
while a<1000:
    print(a,end=',')
    a,b=b,a+b
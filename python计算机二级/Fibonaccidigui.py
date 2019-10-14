# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:36:43 2018

@author: liyang
"""

def rabbit2(n):
    if (n==1 or n==2):
        return 1
    else:
        return rabbit2(n-1)+rabbit2(n-2)
n=eval(input("请输入需要计算第几个菲波那切数？"))
print(rabbit2(n))
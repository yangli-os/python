# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 22:02:41 2018

@author: liyang
"""

# 定义一个函数
#辗转相除法：
def gcd(m, n):
    if m<n:
        m,n=n,m
    while n:
        m, n = n, m % n
    return m


num1 = int(input("请输入一个整数"))
num2 = int(input("请输入另一个整数"))

gcd_int = gcd(num1, num2)
print(num1, "和", num2, "的最大公约数为", gcd_int)
print(num1, "和", num2, "的最小公倍数为", int(num1*num2/gcd_int))
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:31:30 2018

@author: liyang
"""

def get_1_digits(n):
    if n <= 0:
        return 0
    if n == 2:
        return 1
    current = 9 * get_1_digits(n-1) + 10 ** (n-1)
    return get_1_digits(n-1) + current
def get_digits(n):
    ret = 0
    while n:
        ret += 1
        n /= 10
    return ret
def main():
    sun=0
    n=eval(input()) 
    if get_1_digits(n)==1:
        sun+=1
    print(sun)
main()
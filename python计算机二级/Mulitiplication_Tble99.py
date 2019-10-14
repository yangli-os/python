# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:11:43 2018

@author: liyang
"""

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end='')
    print('')
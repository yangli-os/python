# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:34:09 2018

@author: liyang
"""

import time
limit=10*1000*1000
start=time.perf_counter()
while True:
    limit-=1
    if limit<=0:
        break
delta=time.perf_counter()-start
print("程序运行时间是：{}秒".format(delta))
print(time.ctime())
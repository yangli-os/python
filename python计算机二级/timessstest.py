# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:40:22 2018

@author: liyang
"""

import time
timestr = "2020-10-10 10:10:10"
t = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(time.strftime("%Y年%m月%d日%H时%M分%S秒", t))

# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:28:25 2018

@author: liyang
"""

import jieba
s="今天晚上我吃了意大利面"
qiefen=jieba.lcut_for_search(s)
print(qiefen)
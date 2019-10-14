# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:46:59 2018

@author: liyang
"""

import jieba as j
s="工业互联网”实施的方式是通过通信、控制和计算技术的交叉应用，建造一个信息物理系统，促进物理系统和数字系统的融合。"
s = s.replace("，","").replace('。','').replace('、','').replace('“','').replace('”','')
txt=j.lcut(s)
d1 = {}
maxc = 0
wo = ''
for i in txt:
   print(i, end= "/ ")
   d1[i] = d1.get(i,0) + 1
print("\n中文词语数是：{}".format(len(txt)))
for key in d1:
    if maxc < d1[key]:
        wo = key
        maxc = d1[key]
    elif maxc == d1[key]:
        wo += ' ' + key
    print("{}: {}".format(key,d1[key]))
print("出现最多的词是（{}）：{} 次".format(wo, maxc))
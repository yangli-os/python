# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:29:59 2018

@author: liyang
"""
fo = open("sgldout.txt","r",encoding ="utf-8")
words = fo.readlines()
fo.close()
exclude = "；。，“”： "
counts = {}
for word in words:
    if word[:-1] not in exclude:
        counts[word[:-1]] = counts.get(word[:-1], 0) + 1
        L = list(counts.items())
        L.sort(key = lambda s:s[1],reverse=True)
# 输出到文件
fo = open("sgldstatistics.txt", "w", encoding="utf-8")      
for i in range(5):
    fo.write(L[i][0] + ":" + str(L[i][1]) + "\n")
fo.close()
# print 输出
for i in range(5):
    print(L[i][0] + ":" + str(L[i][1]))

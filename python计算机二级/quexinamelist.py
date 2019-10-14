# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 09:29:31 2018

@author: liyang
"""

# 从1.csv文件中读取考勤数据
fo=open("1.csv","r",encoding = "utf-8")
foR =fo.readlines()
fo.close()
ls = []
for line in foR:
    line = line.replace("\n","")
    ls.append(line.split(","))
# 从name.txt文件中读取所有同学的名单
foName=open("Name.txt","r",encoding = "utf-8")
foNameR = foName.readlines()
lsAll = []
for line in foNameR:
    line = line.replace("\n","")
    lsAll.append(line)
#求出第一次缺勤同学的名单
for l in ls:
    if l[0] in lsAll:
        lsAll.remove(l[0])
print("第一次缺勤同学有：",end ="")
for l in lsAll:
    print(l,end=" ")

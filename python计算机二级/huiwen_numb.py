# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:27:24 2018
判断输入是不是回文数或者字符
@author: liyang
"""
a=input('your enter:\n')
b=[]
l=len(a)
for i in range(0,l):
    m=a[l-i-1]
    b.append(m)

for j in range(l):
   mark=True
   if a[j]!=b[j]:
       print ("no")
       mark=False
       break
if mark==True:
    print ("yes")
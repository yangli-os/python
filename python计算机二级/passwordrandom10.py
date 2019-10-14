# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:12:00 2018

@author: liyang
"""

import random as rd
rd.seed(0x1010)
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
ls=[]
exclude=""
while len(ls)<10:
    pwd=""
    for i in range(10):
        pwd+=s[rd.randint(0,len(s)-1)]
#        print(pwd)
    if pwd[0] in exclude:
        continue
    else:
        ls.append(pwd)
        exclude+=pwd[0]
#        print(i,(ls),exclude)
print("\n".join(ls))
fo=open("随机密码.txt","w")
fo.write("\n".join(ls))
fo.close()
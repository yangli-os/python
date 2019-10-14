# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:32:20 2018
有3扇关闭的门，一扇门后面停着汽车，其余门后是山羊，
只有主持人知道每扇门后面是什么。参赛者可以选择一扇门，在开启它之前，
主持人会开启另外一扇门，露出门后的山羊，然后允许参赛者更换自己的选择。
更换或者不更换选择，猜中汽车的概率是多少？
@author: liyang
"""

import random
x=random.randint(5000,10000)
change=0
nochange=0
for i in range(1,x+1):
  a=random.randrange(1,4)
  b=random.randrange(1,4)
  if a==b:
    nochange=nochange+1
  else:
    change=change+1      #换或者不换，两者必有一个能得到车
print("不更改选择得到汽车的概率为{}".format(nochange/x))
print("更改选择得到汽车的概率为{}".format(change/x))
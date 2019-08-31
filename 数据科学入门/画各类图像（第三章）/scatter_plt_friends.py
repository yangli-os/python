# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 10:07:31 2018

画散点图

@author: liyang
"""
from matplotlib import pyplot as plt
friends=[70,65,72,63,71,64,60,64,67]
minutes=[175,170,205,120,220,130,105,145,190]
labels=['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes)

#给每个点加标记
for label,friend_count,minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
        xy=(friend_count, minute_count),   #把标记放在对应的点上
        xytext=(5, -5),                     #但要有轻微的偏离
        textcoords='offset points')
    
plt.title("日分钟数与朋友数")
plt.xlabel("朋友数")
plt.ylabel("花在网站上的日分钟数")
plt.show()

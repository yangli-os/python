# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:16:19 2018

生成电影获得奥斯卡金奖数目的柱状图

@author: liyang
"""

from matplotlib import pyplot as plt
movies=["Annie Hall","Ben-Hur","Casablanca","Gandhi","West Side Story"]
num_oscars=[5,11,3,8,10]

#条形的默认宽度是0.8，因此我们队左侧图标加上0.1
xs=[i+0.1 for i,_ in enumerate(movies)]

#使用左侧x坐标{xs]和高速【num_oscars】画条形图
plt.bar(xs, num_oscars)

plt.ylabel("所获奥斯卡金像奖数量")
plt.title("我最喜爱的电影")

#使用电影的名字标记x轴，位置在x轴上线条中心
plt.xticks([i+0.5 for i,_ in enumerate(movies)],movies)
plt.show

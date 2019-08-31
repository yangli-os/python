# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:58:30 2018

生成有关于年份和GDP的点线图

@author: liyang
"""

from matplotlib import pyplot as plt
years=[1950,1960,1970,1980,1990,2000,2010]
GDP=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

#无法显示汉字和负号的配置
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']    #字体雅黑
mpl.rcParams['axes.unicode_minus'] = False      #正常显示负号

#创建一幅线图，X轴是年份,y轴是GDP
plt.plot(years,GDP,color='green',marker='o',linestyle='solid')
 #添加一个标题
plt.title('名义GDP')
#给y轴添加标记
plt.ylabel("十亿美元")
plt.show()
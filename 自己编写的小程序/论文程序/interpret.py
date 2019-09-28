# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:48:56 2018

@author: liyang
"""

import pandas as pd
from scipy.interpolate import lagrange #导入拉格朗日插值函数
#参数初始化
filename = r'C:\Users\liyang\Desktop\桌面文件\铝电解\资料整理\铝电解数据分析\5046（240KA)\10.xlsx'
outputfile = r'C:\Users\liyang\Desktop\桌面文件\铝电解\资料整理\铝电解数据分析\5046（240KA)\101.xlsx' #输出数据路径
data = pd.read_excel(filename)
data= data.iloc[:,0:2]
print(data)
print(data.iloc[2:3,1:2])
data.iloc[2:3,1:2] = None #过滤异常值，将其变为空值

#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=30):
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
  y = y[y.notnull()] #剔除空值
  return lagrange(y.index, list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]: #如果为空即插值。
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile) #输出结果，写入文件

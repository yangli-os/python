#-*- coding: utf-8 -*-
#逻辑回归 自动建模
import pandas as pd
#参数初始化
filename = '../data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].value
y = data.iloc[:,8].value

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR 
rlr = RLR() #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y) #训练模型
rlr.get_support() #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
print ('通过随机逻辑回归模型筛选特征结束')
print (u'有效特征为：%s' % ','.join(data.loc[:,rlr.get_support()]))
x = data.loc[:,rlr.get_support()].value #筛选好特征

lr = LR() #建立逻辑货柜模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
print ('逻辑回归模型训练结束')
print ('模型的平均正确率为:',lr.score(x, y)) #给出模型的平均正确率，本例为81.4%

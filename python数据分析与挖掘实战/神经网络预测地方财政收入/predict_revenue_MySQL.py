# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:27:20 2018

@author: liyang
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:03:22 2018

@author: liyang
"""
#-*- coding: utf-8 -*-
import pymysql
import pandas as pd
import numpy as np
#打开数据库连接（ip/数据库用户名/登录密码/数据库名）
conn=pymysql.connect("localhost","liyang","123456","mysql",charset="utf8")
data=pd.read_sql('select * from data1_gm11',conn)#选择数据库表
conn.close()                        #关闭数据库，这是一个好习惯
feature = ['x1', 'x2', 'x3', 'x4', 'x5', 'x7']     #特征所在列
data_train = data.iloc[0:20].copy()          #取前20个数据建模
data_mean = np.mean(data_train,0)            #按列取均值，1是按行
data_std = data_train.std()                  #计算标准差
data_train = (data_train - data_mean)/data_std #数据标准化
x_train = data_train[feature].as_matrix()       #特征数据
y_train = data_train['y'].as_matrix()           #输出数据

from keras.models import Sequential
from keras.layers.core import Dense, Activation
model = Sequential() #建立模型
model.add(Dense(input_dim=6,output_dim=12)) #对多输入和多输出进行指定输入个数和隐含层
model.add(Activation('relu')) #用relu函数作为激活函数，能够大幅提供准确度
model.add(Dense(input_dim=12,output_dim=1)) #隐含层神经元个数和输出层个数
model.compile(loss='mean_squared_error', optimizer='adam')    #编译模型
model.fit(x_train, y_train, epochs = 10000, batch_size = 16) #训练模型，学习一万次

#预测，并还原结果。
x = ((data[feature] - data_mean[feature])/data_std[feature]).as_matrix()
data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']

import matplotlib.pyplot as plt #画出预测结果图
p = data[['y','y_pred']].plot(subplots = True, style=['b-o','r-*'])
plt.show()



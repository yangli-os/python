# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:10:40 2018

@author: liyang
"""
from keras.utils import np_utils       #后续将label标签转换成One-Hot Encoding
import numpy as np
np.random.seed(10)                     #设置seed可以产生的随机数
#加载Minist数据集
from keras.datasets import mnist        
(x_Train,y_Train),(x_Test,y_Test)=mnist.load_data()

#数据预处理，选取60000个数据作为训练集，10000个作为测试集
x_Train4D=x_Train.reshape(x_Train.shape[0],28,28,1).astype('float32') 
x_Test4D=x_Test.reshape(x_Test.shape[0],28,28,1).astype('float32')
#28*28转换为一维向量784，float方便标准化
x_Train4D_normalize=x_Train4D/255      #数据标准化,images数字化后的数字为0~255
x_Test4D_normalize=x_Test4D/255
#分别传入y_train_label和y_test_labelde label标签字段，进行One-Hot Encoding转换
y_TrainOneHot=np_utils.to_categorical(y_Train)
y_TestOneHot=np_utils.to_categorical(y_Test)

#建立神经网络模型
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
model=Sequential()           #建立神经网络的蛋糕架
#建立卷积层，filters滤镜个数，kernel_size滤镜大小，padding卷积图像大小不变，输入维数第三维是单色为1
model.add(Conv2D(filters=16,kernel_size=(5,5),padding='same',
                 input_shape=(28,28,1),activation='relu'))
#建立池化层,以2*2矩阵转为单值缩小图片，也就是缩减为原来的一半
model.add(MaxPooling2D(pool_size=(2,2)))
#建立卷积层，filters滤镜个数，kernel_size滤镜大小，padding卷积图像大小不变，输入维数第三维是单色为1
model.add(Conv2D(filters=36,kernel_size=(5,5),padding='same',
                 input_shape=(28,28,1),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))#建立池化层,以2*2矩阵转为单值缩小图片，也就是缩减为原来的一半
model.add(Dropout(0.25))       #添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Flatten())           #建立平坦层
model.add(Dense(128,activation='relu'))  #建立隐含层，设置神经元个数
model.add(Dropout(0.5))        #添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Dense(10,activation='softmax'))#softmax将每一个神经元的输出转换为预测每一个数字的概率
#设置训练参数loss使用交叉熵，优化器adam，评估方式为准确率
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
train_history=model.fit(x=x_Train4D_normalize,y=y_TrainOneHot,
                        validation_split=0.2,epochs=15,batch_size=300,verbose=2)
#反向传播时validation_split验证数据的比例，训练次数，每一批次训练的项数verbose显示训练过程

#图形显示训练过程
import matplotlib.pyplot as plt
#显示训练过程loss和accuracy的函数，输入参数为train_history
def show_train_history(train_history,train,validation): #训练参数
    plt.plot(train_history.history[train])              #训练数据的执行结果
    plt.plot(train_history.history[validation])         #训练数据的测试结果
    plt.title('Train History')
    plt.ylabel(train)             #y轴准确率
    plt.xlabel('Epoch')           #x轴训练次数
    plt.legend(['train','validation'],loc='upper left') #图例'train','validation'显示在左上角
    plt.show()
#调用函数显示训练准确率,acc为训练集准确率，val_acc为验证集准确率，无测试集    
show_train_history(train_history,'acc','val_acc')   
show_train_history(train_history,'loss','val_loss')#调用函数显示训练误差

prediction=model.predict_classes(x_Test4D_normalize)            #使用测试数据进行预测

#显示测试集中的图
def plot_images_labels_prediction(images,labels,prediction,idx,num):#查看多项训练数据
    fig=plt.gcf()                              #设置要显示图像的大小
    fig.set_size_inches(12,14)
    if num>25:                                 #显示的图片张数尽量不超过25
        num=25
    for i in range(0,num):
        ax=plt.subplot(5,5,1+i)                #每行显示5张图片 
        ax.imshow(images[idx],cmap='binary')   #cmap为binary显示黑白灰度图像
        title="label="+str(labels[idx])        #设置标题为label的标签
        if len(prediction)>0:                  #如果是预测图，则显示预测的标签predict
            title+=",predict="+str(prediction[idx])
        ax.set_title(title,fontsize=10)        #设置子图的标题
        ax.set_xticks([]);ax.set_yticks([])    #设置不显示刻度
        idx+=1                                 #读取下一项
    plt.show()
#传入预测结果函数的参数，显示测试集中预测的前n个结果
plot_images_labels_prediction(x_Test,y_Test,prediction,idx=0,num=10) 

##使用混淆矩阵显示预测结果    
#import pandas as pd
##crosstab建立混淆矩阵，设置行列名
#print(pd.crosstab(y_test_label,prediction,rownames=['label'],colnames=['prediction']))

scores=model.evaluate(x_Test4D_normalize,y_TestOneHot)#显示预测模型的准确率
print('accuracy=',scores[1])

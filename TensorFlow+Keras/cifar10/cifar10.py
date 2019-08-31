# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 14:38:23 2018

@author: liyang
"""
from keras.datasets import cifar10
from keras.utils import np_utils       #后续将label标签转换成One-Hot Encoding
import numpy as np
np.random.seed(10)     
(x_train_image,y_train_label),\
(x_test_image,y_test_label)=cifar10.load_data()
#print('train:',len(x_train_image))
#print('test:',len(x_test_image))
#print(x_train_image.shape)
x_Train=x_train_image.astype('float32')  #28*28转换为一维向量784，float方便标准化
x_Test=x_test_image.astype('float32')    
x_Train_normalize=x_Train/255.0         #数据标准化,images数字化后的数字为0~255
x_Test_narmalize=x_Test/255.0  
y_Train_OneHot=np_utils.to_categorical(y_train_label)      
y_Test_OneHot=np_utils.to_categorical(y_test_label)

#建立神经网络模型
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D,Activation,ZeroPadding2D
model=Sequential()           #建立神经网络的蛋糕架
#建立卷积层，filters滤镜个数，kernel_size滤镜大小，padding卷积图像大小不变，输入维数彩色为3
model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',
                 input_shape=(32,32,3),activation='relu'))
#建立池化层,以2*2矩阵转为单值缩小图片，也就是缩减为原来的一半
model.add(Dropout(0.3))       #添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu'))
#建立池化层,以2*2矩阵转为单值缩小图片，也就是缩减为原来的一半
model.add(MaxPooling2D(pool_size=(2,2)))           #添加池化层，缩减一半
#建立卷积层，filters滤镜个数，kernel_size滤镜大小，padding卷积图像大小不变，输入维数第三维是单色为1
model.add(Conv2D(filters=64,kernel_size=(3,3),padding='same',activation='relu'))
model.add(Dropout(0.3))       #添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Conv2D(filters=64,kernel_size=(3,3),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))#建立池化层,以2*2矩阵转为单值缩小图片，也就是缩减为原来的一半
model.add(Conv2D(filters=128,kernel_size=(3,3),padding='same',activation='relu'))
model.add(Dropout(0.3))       #添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Conv2D(filters=128,kernel_size=(3,3),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))#建立池化层,以2*2矩阵转为单值缩小图片，也就是缩减为原来的一半
model.add(Flatten())           #建立平坦层
model.add(Dropout(0.3))       #添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Dense(1024,activation='relu'))  #建立隐含层，设置神经元个数
model.add(Dropout(0.3))        #添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Dense(10,activation='softmax'))#softmax将每一个神经元的输出转换为预测每一个数字的概率
#设置训练参数loss使用交叉熵，优化器adam，评估方式为准确率
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
try:
    model.load_weights("SaveModel/cifarCnnModel.h5")
    print('模型加载成功，继续训练模型')
except:
    print("加载模型失败，开始训练新模型")
train_history=model.fit(x=x_Train_normalize,y=y_Train_OneHot,
                        validation_split=0.2,epochs=10,batch_size=128,verbose=1)
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

prediction=model.predict_classes(x_Test_narmalize)            #使用测试数据进行预测

model.save_weights("SaveModel/cifarCnnModel.h5")
print("Saved model to disk")

#显示测试集中的图
label_dict={0:"airplane",1:"automobile",2:"bird",3:"cat",4:"deer",
            5:"dog",6:"frog",7:"horse",8:"ship",9:"truck"}
def plot_images_labels_prediction(images,labels,prediction,idx,num):#查看多项训练数据
    fig=plt.gcf()                              #设置要显示图像的大小
    fig.set_size_inches(12,14)
    if num>25:                                 #显示的图片张数尽量不超过25
        num=25
    for i in range(0,num):
        ax=plt.subplot(5,5,1+i)                #每行显示5张图片 
        ax.imshow(images[idx],cmap='binary')   #cmap为binary显示黑白灰度图像
        title=str(i)+','+label_dict[labels[i][0]]       #设置标题为label的标签
        if len(prediction)>0:                  #如果是预测图，则显示预测的标签predict
            title+='=>'+label_dict[prediction[i]] 
        ax.set_title(title,fontsize=10)        #设置子图的标题
        ax.set_xticks([]);ax.set_yticks([])    #设置不显示刻度
        idx+=1                                 #读取下一项
    plt.show()
#传入预测结果函数的参数，显示测试集中预测的前10个结果
plot_images_labels_prediction(x_test_image,y_test_label,prediction,idx=0,num=10)
##使用混淆矩阵显示预测结果    
#import pandas as pd
##crosstab建立混淆矩阵，设置行列名
#print(pd.crosstab(y_test_label,prediction,rownames=['label'],colnames=['prediction']))

scores=model.evaluate(x_Test_narmalize,y_Test_OneHot,verbose=0)#显示预测模型的准确率,不更新日志
print('accuracy=',scores[1])

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:33:41 2018

@author: liyang
"""

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist=input_data.read_data_sets("MNIST_data/", one_hot=True)

##查看数据
#print('train data=',len(x_train_image))
#print('test data=',len(x_test_image))
#x_train_image:(60000,28,28)
#y_train_label:(60000,)

#数据预处理，选取60000个数据作为训练集，10000个作为测试集

def layer(output_dim,input_dim,inputs,activation=None):
    W=tf.Variable(tf.random_normal([input_dim,output_dim]))
    b=tf.Variable(tf.random_normal([1,output_dim]))
    XWb=tf.matmul(inputs,W)+b
    if activation is None:
        outputs=XWb
    else:
        outputs=activation(XWb)
        return outputs
x=tf.placeholder("float",[None,784])   #建立输入层
h1=layer(output_dim=256,input_dim=784,inputs=x,activation=tf.nn.relu)
y_predict=layer(output_dim=10,input_dim=256,inputs=h1,activation=None)
y_label=tf.placeholder("float",[None,10])
loss_function=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits
                             (logits=y_predict,labels=y_label))   
optimizer=tf.train.AdamOptimizer(learning_rate=0.001)\minimize(loss_function)
correct_prediction=tf.equal(tf.argmax(y_label ,1),tf.argmax(y_predict, 1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,"float"))
trainEpochs=15
batchSize=100
loss_list=[];epoch_list=[];accuracy_list=[]
startTime=time()

sess=tf.Session()
sess.run(tf.global_variables_initializer())
    
x_Train=x_train_image.reshape(60000,784).astype('float32')  #28*28转换为一维向量784，float方便标准化
x_Test=x_test_image.reshape(10000,784).astype('float32')    
x_Train_normalize=x_Train/255         #数据标准化,images数字化后的数字为0~255
x_Test_narmalize=x_Test/255  
#分别传入y_train_label和y_test_labelde label标签字段，进行One-Hot Encoding转换
y_Train_OneHot=np_utils.to_categorical(y_train_label)      
y_Test_OneHot=np_utils.to_categorical(y_test_label)

batch_images_xs,batcha_labels_ys=mnist.train.next_batch(batch_size=100)
print(len(batch_images_xs),len(batcha_labels_ys))
#建立神经网络模型
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
model=Sequential()           #建立神经网络的蛋糕架
#建立输入层与隐藏层units隐含层神经网络256个，输入层784个（一维向量）正态分布的随机数初始化权重和偏差
model.add(Dense(units=1000,input_dim=784,kernel_initializer='normal',activation='relu'))
#添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Dropout(0.3))
#添加第二个隐含层
model.add(Dense(units=1000,kernel_initializer='normal',activation='relu'))
#添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Dropout(0.5))
#建立输出层，输出层10个神经元表示数字，输出层的激活函数选择softmax
model.add(Dense(units=10,kernel_initializer='normal',activation='softmax'))
#设置训练参数loss使用交叉熵，优化器adam，评估方式为准确率
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
#开始训练，并记录准确的和误差
train_history=model.fit(x=x_Train_normalize,y=y_Train_OneHot,
                        validation_split=0.2,epochs=12,batch_size=2000,verbose=2)
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
#show_train_history(train_history,'loss','val_loss')#调用函数显示训练误差

prediction=model.predict_classes(x_Test)            #使用测试数据进行预测

#显示测试集中的图
def plot_images_labels_prediction(images,labels,prediction,idx,num):#查看多项训练数据
    fig=plt.gcf()                              #设置要显示图像的大小
    fig.set_size_inches(12,14)
    if num>25:                                 #显示的图片张数尽量不超过25
        num=25
    for i in range(0,num):
        ax=plt.subplot(5,5,1+i)                #每行显示5张图片 
        ax.imshow(np.reshape(images[idx],(28,28)),cmap='binary')   #cmap为binary显示黑白灰度图像
        title="label="+str(np.argmax(labels[idx]))        #设置标题为label的标签
        if len(prediction)>0:                  #如果是预测图，则显示预测的标签predict
            title+=",predict="+str(prediction[idx])
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

scores=model.evaluate(x_Test_narmalize,y_Test_OneHot)#显示预测模型的准确率
print('accuracy=',scores[1])

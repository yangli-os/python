# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:41:20 2018

@author: liyang
"""

import urllib.request
import os 
import tarfile
filepath="data/aclImdb_v1.tar.gz"                      #文件保存路径
if not os.path.isfile(filepath):                       #判断文件不在就下载文件
    url="http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
    result=urllib.request.urlretrieve(url,filepath)
    print('downloaded:',result)
if not os.path.exists("data/aclImdb"):                 #判断文件不存在就解压
    tfile=tarfile.open(filepath,'r:gz')
    result=tfile.extractall('data/')                   #解压文件到data目录下

from keras.preprocessing import sequence        #sequence用于截长补短所有数字列表，长度固定
from keras.preprocessing.text import Tokenizer  #Tokenizer 用于建立字典

import re                                       #导入Regular Expression模块
def rm_tags(text):                              #创建函数，输入参数为text
    re_tag=re.compile(r'<[^>]+>')               #创建正规表达式变量，且赋值为‘<[^>]+>’
    return re_tag.sub('',text)                  #将符合正则表达式条件的字符替换成空字符串

#输入参数为filetype，读取训练参数时会传入train，测试数据时传输test
import os
def read_files(filetype):        
    path= "data/aclImdb/"          #设置存取路径
    file_list=[]                   #创建文件列表    
    positive_path=path+filetype+'/pos/'           #设置正面评价路径
    for f in os.listdir(positive_path):           #将路径下所有文件加入到file_list
        file_list+=[positive_path+f]                 
    negative_path=path+filetype+'/neg/'           #设置负面评价路径
    for f in os.listdir(negative_path):           #将路径下所有文件加入到file_list
        file_list+=[negative_path+f]        
    print('read',filetype,'files:',len(file_list))#显示当前读取的filetye目录下文件个数    
    all_labels=([1]*12500+[0]*12500)   #产生all_label，前12500项是正面，产生1，后12500是负面，产生0
    all_texts=[]                                  #设置all_text为空列表
    for fi in file_list:                          #fi读取file_list所有文件
        with open(fi,encoding='utf8') as file_input:#打开文件为file_input
            all_texts+=[rm_tags("".join(file_input.readlines()))]
            #读取文件，使用join连接所有文件内容，然后使用rm_tags删除tag，最后加入all_texts list
    return all_labels,all_texts   #返回all_label_texts
y_train,train_text=read_files("train")        #调用read_files函数读取训练集数据
y_test,test_text=read_files("test")           #调用read_files函数读取训练集数据

token=Tokenizer(num_words=3800)  #建立token,输入参数num_words=2000，也就是一个2000个单词的字典
token.fit_on_texts(train_text)   #读取所有训练数据的影评，按照每一个单词出现的次数排序，前2000名
x_train_seq=token.texts_to_sequences(train_text)    #将影评文字转换成数字列表
x_test_seq=token.texts_to_sequences(test_text)
x_train=sequence.pad_sequences(x_train_seq,maxlen=380)#截长补短，让每一个数字列表长度为100
x_test=sequence.pad_sequences(x_test_seq,maxlen=380)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)


#建立神经网络模型,多层感知器模型
from keras.models import Sequential
from keras.layers.core import Dense,Dropout
from keras.layers.embeddings import Embedding            #加入嵌入层的库
from keras.layers.recurrent import LSTM
model=Sequential()           #建立神经网络的蛋糕架
#建立嵌入层，将数字列表转换成线性列表,转换成32维向量，每一项有380个数字
model.add(Embedding(output_dim=32,input_dim=3800,input_length=380))
#添加Dropout层,避免过拟合，设置去取消权值的神经元比例
model.add(Dropout(0.2))
model.add(LSTM(32))                 #建立LSTM层
model.add(Dense(units=256,activation='relu'))  #建立隐含层，设置神经元个数
model.add(Dropout(0.2))        #添加Dropout层,避免过拟合，设置去取消权值的神经元比
model.add(Dense(units=1,activation='sigmoid'))  #建立输出层，1表示正面评价，0表示负面评价
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.summary()  # 模型概述
#开始训练，并记录准确的和误差,注意这里的误差函数
train_history=model.fit(x=x_train,y=y_train,
                        validation_split=0.2,epochs=10,batch_size=380,verbose=2)
#反向传播时validation_split验证数据的比例，训练次数，每一批次训练的项数verbose显示训练过程

predict=model.predict_classes(x_test)            #使用测试数据进行预测

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

#评估模型准确性
scores=model.evaluate(x_test,y_test,verbose=1)#显示预测模型的准确率
print('accuracy=',scores[1])

predict_classes=predict.reshape(-1) #将二维数组的prediction转换成1维数组
predict_classes[:10]
SentimentDict={1:'正面的',0:'负面的'}    #定义字典1为正面的，0为负面的
def display_test_SentimentDict(i):      #输出参数i为要显示第几项数据
    print(test_text[i])
    print('label真实值:',SentimentDict[y_test[i]],'预测结果：',SentimentDict[predict_classes[i]])
display_test_SentimentDict(0)    #输出显示第几项数据

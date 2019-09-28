%% MySQL数据库导入数据示例代码
% 初始化参数
clear;
%% 连接数据库并转化数据
conn = database('mysql', 'liyang', '123456', 'com.mysql.jdbc.Driver', 'jdbc:mysql://localhost:3306/mysql');
%连接数据库，数据库名，用户名，用户密码，jdbc驱动，localhost本地计算机，数据库名称
data_mange = exec(conn, 'select * from data1_gm11');     % 连接数据库表
data_mange = fetch(data_mange);                          % 获取数据表
setdbprefs('DataReturnFormat','cellarray');   %定义获取的变量类型..默认返回类型也是cellarray的元胞数组形式
close(conn);                                  %关闭数据库连接
datafile= data_mange.Data                     % 获取数据（元胞数组的形式，类似于指针）
%将元胞数组转化成正常矩阵，元胞数组相当于指针的形式
data=cell2mat(datafile)           %数据类型为float或int，而不是str类型
%data=cellfun(@str2num,data1)     %元胞数组类型为str，数据库的默认形式varchar也是str   

%%参数设置
netfile = 'C:\Users\liyang\Desktop\程序\MATLAB\net.mat'; % 训练好的神经网络保存路径
nlayer=12;                                               %设置隐含层神经元个数

%% 读取数据，设置神经网络参数，并训练网络
inputdata = data(1:20,2:7)';          %读入训练数据
outputdata=data(1:20,8:8)';           %输出数据
predict_input=data(19:20,2:7)';       %取最后两行验证
predict_output=data(19:20,8:8)'       %取最后两行验证
%%数据归一化
input=mapminmax(inputdata);           %最大最小归一化
output=mapminmax(outputdata);         

net = newff(input,output,nlayer);     %新建神经网络
net.trainParam.epochs=100;            %最大训练次数
net.trainParam.show=10;               %每隔多少步显示一次训练结果
net.trainParam.goal=1e-5;             %最小误差
net.trainParam.lr=0.05;               %学习速率
disp('训练BP神经网络中...')
net=train(net,input,output);          %注意tr有所需的训练信息，此处为一个输出

%% 保存训练好的BP神经网络
save(netfile,'net');                  %将训练好的神经网络保存到net.mat中
disp('训练好的BP神经网络模型存入到net.mat中！')

%%使用训练好的模型进行预测
mse=sim(net,predict_input)            %输出最后两行的误差
disp('预测完成')

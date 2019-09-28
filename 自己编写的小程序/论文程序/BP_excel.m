%% MySQL数据库导入数据示例代码

% 初始化参数
clear;
%% 连接数据库并查询
inputfile = '/data_mange.xls';   % 训练数据
data=xlsread(inputfile)
inputdata = data(:,2:12)' % 读入训练数据
outputdata=data(:,13:16)'

net = newff(inputdata,outputdata,4);
net.trainParam.epochs=100;
net.trainParam.show=10;
net.trainParam.goal=1e-5;
% net.trainParam.lr=0.05;
disp('训练BP神经网络中...')
net=train(net,inputdata,outputdata);      % 注意tr有所需的训练信息，此处为一个输出


%% MySQL数据库导入数据示例代码

% 初始化参数
clear;
datafile='C:\Users\liyang\Desktop\程序\MATLAB\data_mange.xls';    %导出数据的保存路径
%% 连接数据库并查询
conn = database('mysql', 'liyang', '123456', 'com.mysql.jdbc.Driver', 'jdbc:mysql://localhost:3306/mysql');
%连接数据库，数据库名，用户名，用户密码，jdbc驱动，localhost本地计算机，数据库名称
data_mange = exec(conn, 'select * from data_mange'); % 数据库表名
setdbprefs('DataReturnFormat','cellarray');          %设置读取方式为元胞数组形式
data_mange = fetch(data_mange); % 获取数据

%% 保存数据
data = data_mange.Data; % 获取数据
xlswrite(datafile,data);%写入到xls文件
fprintf('导出成功')   %显示导出成功
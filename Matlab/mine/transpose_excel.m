%% 将Excel表的矩阵转置
outputfile = xlsread('C:\Users\liyang\Desktop\bianli2/data.xls');      %第一步读取要写入的excel文件
rangefile = [outputfile'];
xlswrite('C:\Users\liyang\Desktop\bianli2/data2.xls',rangefile);       %转置后的新表
disp('处理完成');
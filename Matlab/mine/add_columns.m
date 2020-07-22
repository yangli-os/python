%%添加矩阵数据的表头
A = {'one','two'};
B = num2cell([1 2]);    %%数字转cell类型才能保存
AB = [A;B];
xlswrite('save_path.xlsx',AB);

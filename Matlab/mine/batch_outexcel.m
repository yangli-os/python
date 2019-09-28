%%批量处理文件夹中的文件并将处理后的数据按列导出到Excel表

source_address = 'C:\Users\liyang\Desktop\bianli';     %设置需要处理的文件地址 
source_list = dir(source_address);                     % 遍历源文件夹下的文件
for numlist=1:length(source_list)  
    alldirfile = fullfile(source_address,source_list(numlist).name,'*.jpg');   % 选取后缀名为“jpg”的文件
    all_select = dir(alldirfile);                                              % 提取所有后缀为.jpg的文件 
    for select_use=1:length(all_select)   
       select_name = fullfile(source_address,source_list(numlist).name,all_select(select_use).name);
       %选取全部符合条件的文件
       %%扩展%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       select_data = imread(select_name);             % 依次读取图像
       %%扩展%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     
       outputfile = xlsread('C:\Users\liyang\Desktop\bianli2/data.xls');      %第一步读取要写入的excel文件
       rangelong = size(outputfile,1)+1;      %读取文件中行数，+1是因为第一行中文无法读出，实际读出5行，+1后表示另起一行
       xlswrite('C:\Users\liyang\Desktop\bianli2/data.xls',select_use,1,num2str(rangelong))         
   end  
end 
disp('处理完成');
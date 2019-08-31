# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:46:43 2018

@author: liyang
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 16 07:56:20 2018
通过文件名对文件筛选
@author: liyang
"""
# -*- coding: utf-8 -*-   
import os 
import shutil
source_address = r'C:\Users\liyang\Desktop\bianli'     #源文件路径
name_address = r'C:\Users\liyang\Desktop\bianli3'     #文件名地址
save_address = r'C:\Users\liyang\Desktop\bianli2'        #筛选后的文件路径
namelist=os.listdir(source_address)
rename=os.listdir(name_address)                      #要命名的名字
print(rename)
for numlist in namelist:                               #遍历文件
    oldname=os.path.join(source_address,numlist)       #组合源名字
for rena in rename:
    newname=os.path.join(save_address,rena)         #组合源名字
    shutil.copyfile(oldname,newname)
print('更改完成')

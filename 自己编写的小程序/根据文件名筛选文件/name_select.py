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
save_address = r'C:\Users\liyang\Desktop\bianli2'        #筛选后的文件路径
namelist=os.listdir(source_address)
for numlist in namelist:                               #遍历文件
    oldname=os.path.join(source_address,numlist)       #组合源名字
    newname=os.path.join(save_address,numlist)         #组合源名字
    numright = numlist.rfind(']')                     #找到最右边]的下标
    sele_name=numlist[:numright-3]                    #去掉后缀，取文件名
    sele_name=int(sele_name)                  #字符型转换成整形
    if sele_name>=20130905181139890 and sele_name<=20130905181140375:      #筛选条件
       shutil.copyfile(oldname,newname)
print('筛选完成')

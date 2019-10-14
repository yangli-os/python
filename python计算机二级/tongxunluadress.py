menu=["1. 显示所有信息","2. 追加信息","3. 删除信息"]
flag = 1
while flag:
   for m in menu:
       print(m)
   try:
       ch = int(input("请输入数字1-3选择功能：") )
       flag =0
   except:
       flag = 1
   if    ch <1 or ch > 3:
       flag = 1
print("您选择了功能", ch)
#P301-2##-*- coding=utf-8 -*-
def display():
   fi = open("text.csv",'r')
   for l in fi:
       l=l.replace('\n','')
       print(l)
   fi.close()
#        
menu=["1. 显示所有信息","2. 追加信息","3. 删除信息"]
flag = 1
while flag:
   for m in menu:
       print(m)
   try:
       ch = int(input("请输入数字1-3选择功能：") )
       flag =0
   except:
       flag = 1
   if    ch <1 or ch > 3:
       flag = 1
if ch ==1:
   display()
elif ch==2:
   pass
elif ch ==3:
   pass
# P301-3def display():
   fi = open("address.txt",'r')
   for l in fi:
       l=l.replace('\n','')
       print(l)
   fi.close()        
def insertrec():
   fi = open("address.txt",'r')
   fo = open("new_address.txt",'w')
   la=[]
   for l in fi:
       la.append(l.replace('\n',''))
   rec = input("请输入要插入的信息，以逗号隔开，示例：103, cc, 34567812, tianjing:")
   la.append(rec)
   for l in la:
       fo.write(l)
       fo.write('\n')
   fi.close()
   fo.close()

menu=["1. 显示所有信息","2. 追加信息","3. 删除信息"]
flag = 1
while flag:
   for m in menu:
       print(m)
   try:
       ch = int(input("请输入数字1-3选择功能：") )
       flag =0
   except:
       flag = 1
   if    ch <1 or ch > 3:
       flag = 1
if ch ==1:
   display() 
elif ch==2:
   insertrec()
elif ch ==3:
   pass#      
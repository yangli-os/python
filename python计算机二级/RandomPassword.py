# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:51:41 2018

@author: liyang
"""

import random,string
src = string.ascii_letters + string.digits
count = input('请确认要生成几条密码： ')
list_passwds = []   #初始化包含了所有字符串的数组
for i in range(int(count)):
    list_passwd_all = random.sample(src, 5) #从字母和数字中随机取5位
    list_passwd_all.extend(random.sample(string.digits, 1))  #让密码中一定包含数字
    list_passwd_all.extend(random.sample(string.ascii_lowercase, 1)) #让密码中一定包含小写字母
    list_passwd_all.extend(random.sample(string.ascii_uppercase, 1)) #让密码中一定包含大写字母
    random.shuffle(list_passwd_all) #打乱列表顺序
    str_passwd = ''.join(list_passwd_all) #将列表转化为字符串
    if str_passwd not in list_passwds: #判断是否生成重复密码
        list_passwds.append(str_passwd)
print(list_passwds)
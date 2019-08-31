# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:46:04 2018

将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R

之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);

示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"

示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I

@author: liyang
"""

class Solution:
    def convert(self, s, numRows):
        data_groups =[[] for i in range(numRows)]#建立一个有numRows行的二维列表
        j=0                 #初始化
        cc=""               #初始化返回值数组cc
        for i in range(int(len(s))): 
            if numRows==1:
                data_groups=s
                break
            shang=i//(numRows-1)
            yushu=i%(numRows-1)
            if shang%2==0 and yushu<(numRows-1) or shang%2==1 and yushu==0:       
                data_groups[j].append(s[i])
                j=j+1
                if j==numRows:
                    j=numRows-2
            elif shang%2==1 and yushu<(numRows-1) or shang%2==0 and yushu==0:
                
                data_groups[j].append(s[i])
                j=j-1
        for i in range(len(data_groups)):
           for j in range(len(data_groups[i])):
               cc += str(data_groups[i][j])
        return cc
a=Solution()
print(a.convert(s="PINALSIGYAHRPI",numRows = 3))









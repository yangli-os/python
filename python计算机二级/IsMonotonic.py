# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 09:52:44 2018
判断一个数列是否是单调数列，只有一个数字的也算是单调数列
@author: liyang
"""

class Solution:
    def isMonotonic(self, A):
#        if len(A)==1:
#            Flag=1
#        for i in range(len(A)-1):
#            if A[i+1]-A[i]>0:
#                Flag=0
#                break
#            elif A[i+1]-A[i]<0:
#                Flag=1
#                break
#            elif A[i+1]==A[i]:
#                Flag=0
#            else:
#                Flag=2
#                break
#        zengjian=True
#        if Flag==0:
#            for i in range(len(A)-1):
#                if A[i+1]-A[i]>=0:
#                    continue
#                else:
#                    zengjian=False
#                    break
#        elif Flag==1:
#            for i in range(len(A)-1):
#                if A[i+1]-A[i]<=0:
#                    continue
#                else:
#                    zengjian=False
#                    break
#        else:
#            zengjian=False
#            
#        return zengjian
         return sorted(A) == A or sorted(A, reverse=True) == A
a=Solution()
print(a.isMonotonic([9]))
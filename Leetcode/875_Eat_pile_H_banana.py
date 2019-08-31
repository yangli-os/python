# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 09:51:23 2018

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4

示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30

示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23

@author: liyang
"""

class Solution:
    def minEatingSpeed(self, piles, H):
        assert len(piles) <= H        #assert如果piles长度超过H则终止执行程序
        a = 0
        b = max(piles)                #找到所给序列的最大值
        while a + 1 < b:              #循环最大值次
            c = (a + b) // 2          
#c为从最大值的一半到最大值之间的整数，这样可以减少至少一半的计算量  
            if sum(1+(p-1)//c for p in piles) <= H: #所给数组中的元素挨个除以C，求和不大于H
                b = c                                #寻找C的最大值
            else: a = c
        return b
a=Solution()
print(a.minEatingSpeed(piles = [30, 11, 23, 4, 20], H = 6))
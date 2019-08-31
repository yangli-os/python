# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:59:26 2018

如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：

    n >= 3
    对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}

给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

（回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

 

示例 1：

输入: [1,2,3,4,5,6,7,8]
输出: 5
解释:
最长的斐波那契式子序列为：[1,2,3,5,8] 。
1+2~3+5<=8，称为斐波那契子序列

示例 2：

输入: [1,3,7,11,12,14,18]
输出: 3
解释:
最长的斐波那契式子序列有：
[1,11,12]，[3,11,14] 以及 [7,11,18]

@author: liyang
"""
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0        #如果长度小于3就没有
        s = set(A)                     #将A处理成一个集合，也就是没有重复元素
        def f(i, j):     
            r = 2
            a = A[i]           
            b = A[j]
            while a + b in s: a, b, r = b, a + b, r + 1 #判断是否是斐波那契子序列
            return r
        r = max(f(i, j) for j in range(1, len(A)) for i in range(j))#返回序列长度
        return r if r >= 3 else 0
a=Solution()
print(a.lenLongestFibSubseq(A = [1,2,3,4,5,6,7,8]))

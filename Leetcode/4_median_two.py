# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:36:41 2018

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

@author: liyang
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums=sorted(nums1+nums2)       #合并两个数组并排序
        print(nums)
        m=len(nums)                    #提取长大衣
        print(m)
        if m%2==0:
            median=(nums[m//2-1]+nums[m//2])/2  #如果是偶数个求中间两个数的平均数
        else:
            median=nums[m//2]          #如果总数是单数个，就输出中间的那个值，注意是从0开始的
        return median
a=Solution()
print(a.findMedianSortedArrays(nums1=[],nums2=[2,3]))
#输入两个数组

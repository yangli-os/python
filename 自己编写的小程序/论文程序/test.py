# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:55:45 2018

@author: liyang
"""
N=input()
numbers=input().split(' ')
ls=""
numbers.sort(reverse=True)
print(numbers)
for i in range(len(numbers)):
    flag=0
    if i<(len(numbers)-1):
        if len(numbers[i])>len(numbers[i+1]):
            dec=min(len(numbers[i]),len(numbers[i+1]))
            for j in range(dec-1): 
                if numbers[i][j]!=numbers[i+1][j]:
                    break
                else:
                    if (numbers[i]+numbers[i+1])<(numbers[i+1]+numbers[i]):
                        numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
        elif (numbers[i])==(numbers[i+1]):
            flag+=1
            if (numbers[i]+numbers[i+flag])<(numbers[i+flag]+numbers[i]):
                        numbers[i],numbers[i+flag]=numbers[i+flag],numbers[i]
    ls+=numbers[i]
print(int(ls))
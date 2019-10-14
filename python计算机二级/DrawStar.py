# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:16:44 2018
画一个五角星
@author: liyang
"""

from turtle import*
color('red','red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
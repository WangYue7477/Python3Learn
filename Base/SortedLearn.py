#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 23:35
# @Author  : WangYue
# @File    : SortedLearn.py
# @Software: PyCharm
l = [21,54,-98,32,-5]
print(sorted(l))
print(sorted(l,key=abs))

name = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(name))
print(sorted(name,key=str.lower))
print(sorted(name,key=str.lower,reverse=True))
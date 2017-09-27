#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/11 22:37
# @Author  : WangYue
# @File    : ListLearn.py
# @Software: PyCharm Community Edition
import os

print(list(range(1,11)))

L=[]
for x in range(1,11):
    L.append(x*x)
print(list(L))

print([x*x for x in range(1,11)])

print([x*x for x in range(1,11) if x%2==0])

print([m+n for m in 'QWE' for n in 'IOPL'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

print(os.listdir())
print(os.listdir("."))

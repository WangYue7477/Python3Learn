#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/26 12:42
# @Author  : WangYue
# @File    : reducelearn.py
# @Software: PyCharm Community Edition

from functools import reduce
#
def add(x,y):
    return x+y

def fn(x,y):
    return 10*x+y

def chr2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn,map(chr2num,'13579')))
# print(reduce(add,[1,3,5,7,9]))

# print(reduce(fn,[1,3,5,7,9]))



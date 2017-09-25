#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/25 23:16
# @Author  : WangYue
# @File    : maptest.py
# @Software: PyCharm Community Edition
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
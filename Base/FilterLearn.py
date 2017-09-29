#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 16:39
# @Author  : WangYue
# @File    : FilterLearn.py
# @Software: PyCharm Community Edition
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,3,4,5,6,7,8,9,11])))

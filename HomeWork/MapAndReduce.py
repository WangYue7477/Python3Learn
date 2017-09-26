#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/26 12:58
# @Author  : WangYue
# @File    : MapAndReduce.py
# @Software: PyCharm Community Edition

from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
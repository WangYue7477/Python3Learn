#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 16:50
# @Author  : WangYue
# @File    : GeneratorLearn.py
# @Software: PyCharm Community Edition
L = [x *x for x in range(10)]
print(L)
g = (x *x for x in range(10))
for n in g:
    print(n)

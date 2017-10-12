#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 22:42
# @Author  : WangYue
# @File    : DecoratorLearn.py
# @Software: PyCharm

from datetime import date
def now():
    print(date.today())
f = now
print(f.__name__)

#剩下的看不懂了
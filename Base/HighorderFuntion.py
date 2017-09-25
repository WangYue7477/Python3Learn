#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/11 22:59
# @Author  : WangYue
# @File    : HighorderFuntion.py
# @Software: PyCharm Community Edition
def poewr2(x, y):
    return x+y


def add1(f, k_1, k_2=2, *num, **kw):
    s = 0
    print('k_1 power=', k_1+k_2)
    for k in num:
        s = s + f(k, 3)
    for v, k in kw.items():
        print("key=", v, "value=", k)
    print('s=', s)
    return s


f = poewr2
ss = list(range(10, 100, 10))
dic = {'one': 12, "two": 34, "three": 45, "four": '65'}
print(add1(f, 2, 5, *ss, **dic))

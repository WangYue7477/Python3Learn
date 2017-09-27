#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/26 12:58
# @Author  : WangYue
# @File    : MapAndReduceHomeWork.py
# @Software: PyCharm Community Edition

from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def normalize(name):
    if isinstance(name, str):
        #        return str.upper(name[0])+str.lower(name[1:])
        return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def str2float(s):
    n = s.index('.')
    f_temp = s[:n] + s[n + 1:]

    def char2num(str_temp):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str_temp]

    def str2int(int_temp):
        return reduce(lambda x, y: 10 * x + y, map(char2num, int_temp))

    return str2int(f_temp) / (10 ** n)


L = '123.456'
print(str2float(L))

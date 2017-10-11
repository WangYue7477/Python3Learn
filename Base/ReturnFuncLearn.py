#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 23:42
# @Author  : WangYue
# @File    : ReturnFuncLearn.py
# @Software: PyCharm
def calc_sum(*args): #加*号的意思为可变参数
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1() == f2())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

fs1, fs2, fs3 = count()
print(fs1(),fs2(),fs3())

def count_():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

fs1_, fs2_, fs3_ = count_()
print(fs1_(),fs2_(),fs3_())
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 23:44
# @Author  : WangYue
# @File    : GeneratorWork.py
# @Software: PyCharm
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]

n=0
a = input("请输入杨辉三角的行数：")
for t in triangles():
    print(t)
    n = n+1
    if n == int(a):
        break

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 23:29
# @Author  : WangYue
# @File    : ListHomeWork.py
# @Software: PyCharm
L = ['Hello', 'World', 18, 'Apple', None]
print([x.lower() for x in L if isinstance(x,str)])
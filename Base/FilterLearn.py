#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 16:39
# @Author  : WangYue
# @File    : FilterLearn.py
# @Software: PyCharm Community Edition
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,3,4,5,6,7,8,9,11])))

def _odd_iter():
    n=1
    while True:
        n = n + 2
        yield n
def not_divisible(n):
    return lambda x : x % n > 0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)
for n in primes():
    print(n)
    if n > 1000:
        break
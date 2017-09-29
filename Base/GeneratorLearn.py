#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 16:50
# @Author  : WangYue
# @File    : GeneratorLearn.py
# @Software: PyCharm Community Edition

"""
L = [x *x for x in range(10)]
print(L)
g = (x *x for x in range(10))
for n in g:
    print(n)
"""

"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
"""

"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
print(fib(6))
"""

'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()
next(o)
next(o)
next(o)
next(o)
'''

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

# for n in fib(6):
#     try:
#         print(n)
#     except StopIteration as e:
#         print(e.value)
#         break
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
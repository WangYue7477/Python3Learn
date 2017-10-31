#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 23:13
# @Author  : WangYue
# @File    : Student_ClassLearn.py
# @Software: PyCharm

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_age(self):
        print("%s:%s" % (self.name,self.age))

    def get_age(self):
        if self.age >= 30:
            return "Old"
        else:
            return "Young"

jim = Student('jim',23)

print(jim.name)
print(jim.age)
jim.print_age()
print(jim.get_age())

jim.name = 'JIM'
print(jim.name)



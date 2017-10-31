#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 23:39
# @Author  : WangYue
# @File    : protected_Student.py
# @Software: PyCharm
class Student(object):
    def __init__(self,name,age,number):
        self.name = name
        self.age = age
        self.__number = number

    def print_age(self):
        print("%s:%s,%s" % (self.name,self.age,self.__number))

    def get_number(self):
        return self.__number

    def set_number(self,number):
        self.__number = number


Jim = Student("jim",23,98)
Jim.print_age()

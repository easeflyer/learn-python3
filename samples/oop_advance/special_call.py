#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义了 __call__ 后，就可以使用 实例() 这样的方式调用对象。
class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

class Stu(object):
    # def __call__(self):print("callable")
    pass


v1 = Student("zhangsan")
v2 = Stu()
print(callable(v1))
print(callable(v2))
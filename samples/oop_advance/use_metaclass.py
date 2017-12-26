#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 指示使用ListMetaclass来定制类
# MyList 虽然继承自 list 并且没有添加任何功能。但是因为：metaclass=ListMetaclass 因此要通过 ListMetaclass 的 __new__ 方法创建
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L1 = list()
L1.append(1)
L1.append(2)
# L1.add(3)
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)
print(L1)
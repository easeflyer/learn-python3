#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print(cls)      # <class '__main__.ListMetaclass'>
        print(name)     # MyList
        print(bases)    # (<class 'list'>,)  注意这里是个元组,是 list 说明创建 MyList 的时候执行的这里
        print(attrs)    # {'__module__': '__main__', '__qualname__': 'MyList'}

        attrs['add'] = lambda self, value: self.append(value)  # 增加了 add 方法
        return type.__new__(cls, name, bases, attrs)    # 调用的父类的 __new__

# 指示使用ListMetaclass来定制类
# MyList 虽然继承自 list 并且没有添加任何功能。但是因为：metaclass=ListMetaclass 因此要通过 ListMetaclass 的 __new__ 方法创建
class MyList(list, metaclass=ListMetaclass):
    print("22222222")
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
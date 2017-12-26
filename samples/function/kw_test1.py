#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fun(*number):
    for v in number:
        print(v)

# print (fun(1,2,3))  # 一个小坑 print fun 除了函数输出外 本语句最后输出 none
fun(1,2,3)
v1 = (4,5,6)
fun(v1)         # 这里输出了一个元素：元组 v1
fun(*v1)        # 这样才是把 元组的三个值 作为三个参数传入

print("-"*80)

# 关键字参数

# 可变参数 vs 关键字参数
# 可变参数       允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 关键字参数     允许你传入0个或任意个 含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

# 关键字参数 vs 命名关键字参数
# 关键字参数：        只要是含有参数命的参数即可，多少不限，命名不限
# 命名关键字参数：     如果要限制关键字参数的名字，就可以用命名关键字参数

def kwfun(**kw):
    print(kw)

# kwfun(1,2,3)          #  takes 0 positional arguments but 3 were given
kwfun(a =1,b=2,c=3)     # {'a': 1, 'b': 2, 'c': 3}


# 几种参数 可以组合但是顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
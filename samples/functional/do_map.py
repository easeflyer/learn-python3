#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x

'''
map(Fun,Iterable)   Fun 一个函数，Iterable 可迭代数据，比如list tuple
return Iterator     返回一个迭代器，迭代器是惰性的，不next 不计算。 list(Iterator) 返回所有结果 list

'''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(f, l)))

print("-"*80)

print (list(map(str,l)))

print("-"*80)


'''
下面的代码完成同样的事情。但是可读性要差很多。
map 属于高阶函数，有的时候程序设计的关键就是增强程序的可读性。降低代码的层级和难度。
简化设计，是程序设计重要的思维。 层级和复杂度越高，不利于解决问题。
'''
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
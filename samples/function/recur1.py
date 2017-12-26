#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 尾递归方式。 递归调用，return 仅仅调用函数本身，不能含有表达式
# python 并没有对 尾递归做优化，因此仍然会导致溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print (fact(100))   # 1000 溢出
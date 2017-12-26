#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


# 把 int 函数的 base 参数 设置默认值为2 并返回一个新函数 int2 相当于：
'''
def int2(x):
    return int(x,base=2)
'''
int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
# 参考：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000
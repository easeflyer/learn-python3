#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# 尝试下面 可能有错误的代码
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
# 捕获 分母为0的错误，并且输出错误信息
except ZeroDivisionError as e:
    print('except:', e)
# 
finally:
    print('finally...')
print('END')

'''
try:
    可能会报错的代码段
except 错误类型1 as e:
    捕获错误类型1 后执行的代码段
except 错误类型2 as e:
    捕获错误类型2 后执行的代码段
else:
    如果没有捕获到错误执行
finally:
    最后都要执行的代码

'''
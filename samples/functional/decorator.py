#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    #@functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
print(now.__name__)

print("-"*80)

'''
解析：

@log 装饰器 放在 def now 前面。 相当于执行了 now = log(now) ,再调用 now() 的时候，实际上执行的是：
log(now) 返回的：wrapper 函数。
'''



def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)  #注意装饰器中的 @functools.wraps(func) 否则结果为：wrapper

'''
解析：
三层嵌套的装饰器函数是这样的
now = log('execute')(now)
'''
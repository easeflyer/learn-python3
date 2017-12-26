#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L = range(100)

# 解析：filter(is_odd, L)
# 用 is_odd 过滤 L 如果 is_odd 为true 则留下，否则丢弃 返回剩余的结果 
# 注意返回结果也是一个 Iterator 迭代器。用 list 转换成 列表。

print(list (filter(is_odd, L) ))

def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))





def is_su(n):
    for i in range(2,n-1):
        if n % i == 0 :
            #if i > 1000:print("{}/{}={}".format(n,i,n/i))
            return False
        else: pass
    return True

#L = range(10000000,10001000)
L = range(3,100000)
print("-"*80)
# print(list(filter(is_su,L)))

for i in filter(is_su,L):
    print(i)


# print("-"*80)



# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def _not_divisible(n):
#     return lambda x: x % n > 0

# def is_su1(n):
#     for i in _odd_iter():
#         filter(_not_divisible,)
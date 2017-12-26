#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 可变参数 numbers  *numbers 允许传入不确定的参数个数
# 见calc1

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
c = calc([1, 2, 3])
c1 = calc((1,2,3,4))
print(c)  # 14
print(c1) # 14 + 16 = 30
# c2 = calc(1,2,3,4)
# print(c2) # 报错

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
c = calc1(1,2,3,4)

d = [1,2,3,4]
# c1 = calc1(d) # 修改为下面的语法，告诉函数 d 是一个可变参数
# 注意以上两种使用方法都可以。
c1 = calc1(*d)
print(c)
print(c1)
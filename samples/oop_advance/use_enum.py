#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon  # 注意这里返回的并不是 1 由Enum 定义 返回的是 Weekday.Mon 成员

print('day1 =', day1)   #
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)   # 这才是返回 数值 2
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

print("=========================================================")

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 注意 Enum 的 遍历 语法
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    # print(dir(member))

# 可以看到 Month 有 __members__ 属性，具体查阅手册
print(dir (Month))
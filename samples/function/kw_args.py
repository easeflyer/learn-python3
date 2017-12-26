#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这里的 **kw 只是一个关键词参数的“形参”
# 比可变参数的 一个 * 号 多一个 * 号，可以理解为既可变又是关键词参数
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))  # python 的格式化输出真是太方便了
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)


# 注意这个函数的定义
# * 号是个分隔符，代表后面的参数为命名关键词参数
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)     # 把 name 替换 %s
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

# 注意命名关键词参数 给出实参的时候 关键词要一致
print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)

#!/usr/bin/python3
# -*- coding: utf-8 -*-  

def gen1():
    v1 = 0
    while True:
        v = yield v1
        v1 = v1 + 1
        v1 = v1 - 1
        v1 = v1 + 1

# for i in gen1():
#     if i < 20:
#         print(i)
#     else:
#         break


def gen2():

    print("[")
    v = yield from gen1()  # yield from 会使程序 在此开始在此结束，除非 gen1 没有可以迭代的值 才会执行下面的语句。
    print(v)               # 换句话说：因为是from gen1 因此 整个逻辑都转到 gen1 来处理。
    print("]")             # 生成器 依然可以 yield 值，因此后面的语句没有被执行。


for i in gen2():
    if i < 5:
        print(i)
    else:
        break

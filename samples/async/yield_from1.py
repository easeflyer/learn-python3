#!/usr/bin/python3
# -*- coding: utf-8 -*-  

def g(x):
     yield from range(x, 0, -1)     # 5 4 3 2 1
     yield from range(x)            # 0 1 2 3 4
     print ("end")

print( list(g(5)) )
# [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]


for i in g(5):
    print(i)


print("2-"*80)


def gen1():

    for i in range(5):
        v = yield i*2


# print(list(gen1()))

def gen2():
    print("start....")
    v = yield from gen1()
    print("end.....",v)


g = gen2()
g.send(None)
for j in range(5):
    v1 = g.send(j)
    print(v1)


''' 结果解析：
g = gen2()  获得一个生成器 对象 g
g.send(None)    相当于调用 next(g)  
进入 gen2 开始执行（输出 start...），直到 yield from gen1()
gen1() 开始执行 i为0直到 yield 0 * 2 返回0 暂时挂起
gen2() 返回 gen1 的返回值 0 也暂时挂起
回到 g.send(None) 执行后面的语句
j为0 开始循环

v1 = g.send(0)  恢复到挂起的 gen2 yield from gen1() 并把0 传递给 gen1()
恢复到挂起的 gen1() 的 yield 接收到 0 赋值给 v 循环继续 i取值1 yield 1 * 2  返回到 gen2()
gen2()返回给 g.send 赋值给  v1为2 print(2) 输出
以此类推


start....
2
4
6
8
end..... None
StopIteration
'''
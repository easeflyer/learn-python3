#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

# produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
# 请看下面的详细执行过程


# consumer 消费者
# 因为包含 yield 因此他是一个生成器generator，因此具有 send 方法。
# send方法 修改 上一次 yield 的返回值，生成器继续执行，如果没有则报错

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:return
        #print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'



# produce 生产者 
def produce(c):
    c.send(None)    # 注意这里第一次 send 的时候必须是 None 因为还没有 yield 返回，相当于启动了 迭代器
    n = 0           # 也就是说 上面的 consumer 执行到 yield r 返回一个空字符串。程序推进到这里，没有其他意义。
    while n < 50000000:    # n 模拟被生产出的东西。
        n = n + 1
        #print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 把产品 n 发送给消费者，程序再次暂时挂起。知道 生成器c yield 返回值，赋值给r 继续
        #print('[PRODUCER] Consumer return: %s' % r)
    c.close()
    # generator.close() 在生成器函数暂停的点处引发GeneratorExit。

t = time.time()
c = consumer()   # c 是一个生成器 并非 yield 的返回值 生成器
produce(c)
print("耗时：",time.time() - t)

'''结果分析：
produce(c)
    c.send(None)  启动了生成器consumer 程序执行到 yield r 返回'' 暂时挂起
    回到 c.send(None) 没有赋值给任何变量，因此程序继续
    直到下一句被输出


[PRODUCER] Producing 1...                n==1 本输出后：r = c.send(n) 回到生成器 yield '' 被替代为 yield 1 继续执行
[CONSUMER] Consuming 1...                本行被输出 而后 r='200 ok' 重新循环，遇到yield r 返回到 r = c.send(n) r 被赋值为 '200 ok' 继续
[PRODUCER] Consumer return: 200 OK       输出本行后，循环继续 n 被赋值为 2
[PRODUCER] Producing 2...                输出本行，r = c.send(2) 回到生成器 n = yield 2 继续，n==2
[CONSUMER] Consuming 2...                输出本行后，r = '200 ok'  重新循环，遇到 yield r 返回到 r = c.send(n) r 被复制为 '200 ok' 继续
[PRODUCER] Consumer return: 200 OK       输出本行， 循环继续 n 被赋值为 3
[PRODUCER] Producing 3...                下面以此类推
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 4...
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 5...
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 OK
'''

print("--"*80)

'''尝试用 普通函数模拟上一过程
'''
def co(p):

    #print('[CONSUMER] Consuming %s...' % p)
    return '200 OK'

def pro():
    n = 0
    while n < 50000000:
        n = n + 1
        #print('[PRODUCER] Producing %s...' % n)
        r = co(n)
        #print('[PRODUCER] Consumer return: %s' % r)

t = time.time()
pro()
print("耗时：",time.time() - t)

print(time.time())
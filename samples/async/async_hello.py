#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio
import time

# 此代码仍然有很大疑问。如何并发？


@asyncio.coroutine
def sleep1():           # 这里 sleep1 只能 yield 一次。因为sleep1 不是被 next 一次。而是被迭代到结束。
    print("我是否被并发执行了？")
    #yield from asyncio.sleep(3)
    time.sleep(1)       # 如果这里 while True 则会造成程序 死循环。
    yield

#@asyncio.coroutine
def hello(n):
    # print("-----")
    # time.sleep(3)
    # print("======")
    print(n,'Hello world! (%s)' % threading.currentThread())
    #yield from asyncio.sleep(3) # 异步调用asyncio.sleep(1):  
    yield from sleep1()
    print(n,'Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()  # 获取EventLoop:
h1 = hello(1)
h2 = hello(2)
h3 = hello(3)
h4 = hello(4)
print("h1:",h1)     # 他们是 4个不同的生成器对象，保存在不同的内存地址
print("h2:",h2)
print("h3:",h3)
print("h4:",h4)
tasks = [h1,h2,h3,h4]
loop.run_until_complete(asyncio.wait(tasks)) # 执行coroutine
loop.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio
import time

@asyncio.coroutine
def hello(n):
    print("-----")
    time.sleep(3)
    print("======")
    print(n,'Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1) # 异步调用asyncio.sleep(1):  
    print(n,'Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()  # 获取EventLoop:
h1 = hello(1)
h2 = hello(2)
tasks = [h1,h2]
loop.run_until_complete(asyncio.wait(tasks)) # 执行coroutine
loop.close()

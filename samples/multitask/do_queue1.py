#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        time.sleep(random.random()*10)
        print('Put %s to queue...' % value)
        q.put(value)
        

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        time.sleep(1)
        #value = q.get(False)
        try:                                    # 尝试以非阻塞方式q.get(False)获取数据，获得后输出
            value = q.get(False)
            print('Get %s from queue.' % value)
        except Exception:                       # 如果没有获得数据则抛出异常
            print('#',end="",flush=True)
        

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # 等待 3秒 使得 pr 进程捕获最后一个数据
    time.sleep(3)
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
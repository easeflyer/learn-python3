#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading

# 新线程执行的代码:延迟输出一段数列
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))    # current_thread().name 当前线程的名字
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)          # 主线程开始
t = threading.Thread(target=loop, name='LoopThread')                        # 新线程开始
t.start()
t.join()                                                                    # 主线程被阻塞，直到新线程执行完毕
print('thread %s ended.' % threading.current_thread().name)

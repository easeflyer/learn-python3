#!/usr/bin/python3
# -*- coding: utf-8 -*-


import threading
import time

def clock(interval):
    while True:
        print("The time is %s" % time.ctime())
        time.sleep(interval)
        
t = threading.Thread(target=clock, args=(1,))
                                    # 在新的线程中运行 clock 函数，参数为 args所给出的元组
t.daemon = True                     # 后台线程
t.start()                           # 线程启动

time.sleep(15)                      # 主线程等待15秒
                                    # 主线程结束，则后台线程跟随结束


'''
可以看到 多线程 基本语法与多进程极为相似。具有类似功能的方法命名也是相同的。
'''
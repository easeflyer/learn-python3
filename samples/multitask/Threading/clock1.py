#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
clock.py 用自定义线程类的方式来改写
'''


import threading
import time

class ClockThread(threading.Thread):        # 继承自 Thread
    '''
    自定义线程注释事项：
        1）构造函数中要调用基类的构造函数
        2）多线程代码都是通过 run()方法调用的，因此自定义线程，主要就是改写这个方法。
        3）除了 run()方法外，其他基类的方法，尽量不要动。
    '''
    def __init__(self,interval):
        #threading.Thread.__init__(self)     # 调用父类的 构造函数
        super(ClockThread,self).__init__()  # 调用父类的 构造函数
        self.daemon = True                  # 设定为 后台线程
        self.interval = interval            # 设置属性

    def run(self):                          # run 就是在新线程中要执行的核心函数
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)

#t = ClockProcess(15)  书中写错了。
t = ClockThread(1)
t.start()

time.sleep(15)                              # 暂停15秒，否则后台线程也会立即退出。
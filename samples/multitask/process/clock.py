#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing
import time


'''
# 创建进程方法 1
# 1）建立函数（计划在新进程执行）
# 2）开启进程，并把函数和参数放进去。

def clock(interval):
    while True:
        print("The time is %s" % time.ctime())
        time.sleep(interval)

if __name__ == '__main__':
    # 定义一个进程，执行目标是 clock 函数，参数 15
    p = multiprocessing.Process(target=clock, args=(15,))
    p.start()   # 启动进程

'''

# 建立进程 方法2
# 继承 Process 类，并重写run方法（需要执行的任务）
# 实例化新进程类，启动进程对象
class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        #multiprocessing.Process.__init__(self)  # 调用父类的构造法
        super(ClockProcess,self).__init__()      # 这种方式也可以
        self.interval = interval
    def run(self):
        while True:
            print('the time is %s' % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(5)
    p.start()


'''
从两种方法我们可以看到进程的核心函数是 run 方法。
方法一：就是把自定义的函数 抛给 Process，实质上就是交给 run 去执行。
方法二：就是自定义 run 方法，然后实例化新进程类，运行。
'''
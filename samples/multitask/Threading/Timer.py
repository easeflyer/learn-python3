#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Timer
import time

def clock(n):
    print("%s The time is %s" % (n,time.ctime()))


t = Timer(5,clock,args=(3,))        # 5 秒后
t.start()
print("结束...")                    # 注意这里 先被执行，然后等待 定时器函数的执行结果
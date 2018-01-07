#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# windows 系统的多进程支持 multiprocessing 是跨平台的

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())       # current process id
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()   # 子进程开启
    p.join()    # 子进程暂时 阻塞 父进程的运行，也就是父进程等待子进程完毕后，再继续执行。
    print('Child process end.')



'''
多核心处理器 python 多线程效率并不高。
原因是：http://blog.csdn.net/you_are_my_dream/article/details/56316826
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())     # pid   process Id
# Only works on Unix/Linux/Mac:
pid = os.fork()                                  # 程序运行到这里 被自动复制到 成2个进程并返回两个 pid 继续执行
if pid == 0:                                     # 子进程 pid == 0
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:                                            # 父进程 pid == 子进程的 id, 注意理解，程序被复制为两个进程继续的
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


'''
分析：
可以看到在 linux 系统中  os.fork() 很轻松的建立了多进程。

并且在 父子进程中都可以通过 pid ppid 确定彼此的 id
'''
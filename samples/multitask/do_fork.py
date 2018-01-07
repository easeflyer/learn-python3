#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())     # pid   process Id
# Only works on Unix/Linux/Mac:
pid = os.fork()                                  # 程序运行到这里 被自动复制出一个子 进程并返回两个 pid 继续执行
                                                 # 父进程也就是当前进程 pid 返回子进程的 id
if pid == 0:                                     # 那么子进程，因为没有子进程因此 pid 为0
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))  # getpid()返回当前进程id  getppid() 返回父进程id
else:
    os.wait() # 等一下子进程，否则子进程退出后，无法返回。
    print('pid:',pid)                                            # 父进程 pid == 子进程的 id, 注意理解，程序被复制为两个进程继续的
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

exit()

'''
分析：
可以看到在 linux 系统中  os.fork() 很轻松的建立了多进程。

并且在 父子进程中都可以通过 pid ppid 确定彼此的 id
'''
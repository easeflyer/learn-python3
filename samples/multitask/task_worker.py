#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)


# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()


# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)                 # 工作进程 理论上比主进程后启动，并且提前判断应该有任务分配了，因此这里 timeout=1
        print('run task %d * %d...' % (n, n))   # n 是任务队列的任务，也就是一个整数
        r = '%d * %d = %d' % (n, n, n*n)        # r 是处理结果 这里的处理工作就是 计算 n*n 的结果
        time.sleep(1)                           
        result.put(r)                           # 把结果保存到 结果队列
    except Queue.Empty:                         # 如果任务队列 为空则抛出异常处理
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

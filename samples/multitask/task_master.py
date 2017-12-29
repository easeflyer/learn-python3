#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# register 参考 3.6.2 手册  他是一个 类方法 classmethod
# register(typeid[, callable[, proxytype[, exposed[, method_to_typeid[, create_method]]]]]) 
# typeid:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':   BaseManager([address[, authkey]]) 
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:   在一个子进程启动 manager
manager.start()         

# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()


# 放几个任务进去:                          # 任务： 就是从0-10000 的整数进入队列
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)                           # 放入队列中


# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)            # 从结果队列中读取结果。如果读不到结果，10秒后抛出异常。
    print('Result: %s' % r)               # 这个主进程中 并没有对 任务进行处理，只是分配了任务。


# 关闭:
manager.shutdown()  
print('master exit.')

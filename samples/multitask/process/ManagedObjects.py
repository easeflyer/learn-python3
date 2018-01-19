#!/usr/bin/python3
# -*- coding: utf-8 -*-
import multiprocessing
import time


# print out d whenever the passed event gets set
# 在事件发生时 打印d 否则暂时挂起 等待
def watch(d, evt):
    while True:
        evt.wait()                  # 等待 信号。 等待 evt.set()
        print(d)
        evt.clear()                 # 事件清空


if __name__ == '__main__':
    m = multiprocessing.Manager()   # 定义一个 返回一个 SyncManager 对象
    d = m.dict()                    # 建立一个共享 dict
    evt = m.Event()                 # 建立一个共享事件对象     # Create a shared Event

                                    # Launch a process that watches the dictionary    
                                    # 启动一个进程 监视共享字典
    p = multiprocessing.Process(target=watch, args=(d, evt))
    p.daemon = True                 # daemon 后台进程，随主线程关闭
    p.start()                       # watch 进程启动就绪
    
    d['foo'] = 42                   # 增加一个字典 键值 # Update the dictionary and notify the watcher
    evt.set()                       # 通知事件
    time.sleep(2)                   # 阻塞等待5秒
    
    d['bar'] = 37                   # 增加另一个字典 键值 # Update the dictionary and notify the watcher
    evt.set()                       # 通知事件
    time.sleep(2)                   # 阻塞等待5秒

    print("m.address:",m.address)

                                    # 强制终止进程 Terminate the process and manager
    p.terminate()                   # 进程结束
    m.shutdown()                    # 管理器结束
'''
输出：
{'foo': 42}
{'foo': 42, 'bar': 37}

我们可以看到 m.dict() 返回的是 访问共享对象 dict 的代理。但是使用方法和 dict 没有区别。


Server process managers are more flexible than using shared memory objects 
because they can be made to support arbitrary object types. 
Also, a single manager can be shared by processes on different computers over a network. 
They are, however, slower than using shared memory. 
服务器进程管理器比使用共享内存对象更灵活，
因为它们可以用来支持任意对象类型。
另外，单个管理器可以通过网络上不同计算机上的进程共享。
但是，它们比使用共享内存要慢
'''
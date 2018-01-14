#!/usr/bin/python3
# -*- coding: utf-8 -*-
import multiprocessing
import time


# print out d whenever the passed event gets set
# 在事件发生时 打印d 否则暂时挂起 等待
def watch(d, evt):
    while True:
        evt.wait()
        print(d)
        evt.clear()


if __name__ == '__main__':
    m = multiprocessing.Manager()  # 定义一个 返回一个 SyncManager 对象
    d = m.dict()  # 建立一个共享 dict
    # Create a shared dict
    evt = m.Event()  # 建立一个共享事件对象
    # Create a shared Event
    # Launch a process that watches the dictionary
    p = multiprocessing.Process(target=watch, args=(d, evt))
    p.daemon = True  # daemon 后台进程，随主线程关闭
    p.start()  # watch 进程启动就绪
    # Update the dictionary and notify the watcher
    d['foo'] = 42  # 增加一个字典 键值
    evt.set()  # 通知事件
    time.sleep(5)  # 阻塞等待5秒
    # Update the dictionary and notify the watcher
    d['bar'] = 37  # 增加另一个字典 键值
    evt.set()  # 通知事件
    time.sleep(5)  # 阻塞等待5秒
    # Terminate the process and manager
    p.terminate()  # 进程结束
    m.shutdown()  # 管理器结束
'''
输出：
{'foo': 42}
{'foo': 42, 'bar': 37}

我们可以看到 m.dict() 返回的是 访问共享对象 dict 的代理。但是使用方法和 dict 没有区别。
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from multiprocessing.managers import SyncManager

'''
自定义的 类型 A
自定义的 管理器 MyManager 继承自 BaseManager 没有添加任何代码
自定义 代理 AProxy 用于 调用者对 A 的访问
(进程间共享对象的管理器，要想共享自定义的对象，就要使用管理器)
'''


class A(object):
    def __init__(self, value):
        self.x = value
    def __repr__(self):
        return "A(%s)" % self.x
    def getX(self):
        return self.x
    def setX(self, value):
        self.x = value
    def __iadd__(self, value):
        self.x += value
        return self


from multiprocessing.managers import BaseProxy
class AProxy(BaseProxy):
    # A list of all methods exposed on the referent
    _exposed_ = ['__iadd__','getX','setX']
    # Implement the public interface of the proxy
    def __iadd__(self,value):
        self._callmethod('__iadd__',(value,))       # 调用 代理引用对象的 __iadd__ 访问
        return self
    @property
    def x(self):
        return self._callmethod('getX',())          # 调用 代理引用对象的 getX 方法
    @x.setter
    def x(self,value):
        self._callmethod('setX',(value,))           # 调用 setX 方法

class MyManager(SyncManager): pass
'''
若果要运行 ManagedObjects2.py 则需要 SyncManager 的 Event 对象，所以要继承 SyncManager 
否则 继承 BaseManager 即可
'''

MyManager.register("A", A, proxytype=AProxy)        # 管理器 注册 A 类对象。并不是 A 的实例



'''
注意：这个部分，必须写到一个模块里，如果写在 __main__ 文件中可能会报错。
这个问题好像和多核处理器有关，参考：http://blog.csdn.net/geekleee/article/details/77838288
'''
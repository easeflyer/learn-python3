#!/usr/bin/python3
# -*- coding: utf-8 -*-  

# 链式调用 解决 REST api 动态url的情况

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        #return Chain('%s/%s' % (self._path, path))         # 旧语法
        #return Chain('{0}/{1}'.format(self._path,path))    # 新语法
        return Chain('{}/{}'.format(self._path,path))       # 同样

    def __str__(self):
        return self._path

    __repr__ = __str__

print (Chain().status.user.timeline.list)
# 解析
# Chain().status                  返回：Chain("/status")
# Chain("/status").user           返回: Chain("/status/user")
# Chain("/status/user").timeline  返回：Chain("/status/user/timeline")
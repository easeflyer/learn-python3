#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# 定义 Dict 的目的是利用 __setattr__ 和 __getattr__ 让 字典对象可以用 dict.attr 的方式访问
# 这里增加一些“文档测试”代码，来验证这个过程。
class Dict(dict):
    ''' 注意文档测试 只能出现在这个位置。
    >>> d = Dict(a=1,b='bb',c='cc')
    >>> d.b
    'bb'
    >>> d.d = "ddd"
    >>> d.d
    'ddd'
        '''
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value   # 给 对象增加属性。给用属性的方式来访问。
        #self.key = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
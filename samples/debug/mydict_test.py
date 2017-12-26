#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest                                 # 引入单元测试包

from mydict import Dict                         # 引入要测试的模块

class TestDict(unittest.TestCase):              # 编写单元测试 类 代码

    def test_init(self):                        # 以 test 开头的方法 是测试方法
        self.funname = "test_init"
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)                # 相等 断言 d.a == 1 则通过
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))    # 参数表达式为 True 通过

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']                  # d['empty']  访问不存在的key时

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty                     # d.empty  访问不存在的key时

    def setUp(self):
        print("setUp.....")
    def tearDown(self):

        print("teardown....")

if __name__ == '__main__':
    unittest.main()


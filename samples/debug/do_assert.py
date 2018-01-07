#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  # n !=0  应该是 True, 否则后面肯定会出错。 如果出错则提示 n is zero
    return 10 / n

def main():
    foo('0')

main()

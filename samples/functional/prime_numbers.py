#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    for n in primes():
        if n < 100000:
            print(n)
        else:
            break

# 输出 从1 开始的所有奇数 惰性迭代
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 函数作为返回值 返回 意义为：
# 返回一个函数，函数的功能是： 参数x如果除以 n 能除尽则返回True
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        # 返回一个迭代器，这个迭代器以it 为基础，排除掉除以n 能出尽的数（n是上次得出的素数）
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()

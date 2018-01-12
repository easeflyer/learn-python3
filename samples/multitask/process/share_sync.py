#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing


class FloatChannel(object):
    def __init__(self, maxsize):
        self.buffer     = multiprocessing.RawArray('d', maxsize)
        self.buffer_len = multiprocessing.Value('i')
        self.empty      = multiprocessing.Semaphore(1)
        self.full       = multiprocessing.Semaphore(0)
    def send(self,values):
        self.empty.acquire()    # 获取信号量，如果没有则阻塞 参考多线程代码
        nitems = len(values)
        self.buffer_len = nitems
        self.buffer[:nitems] = values
        self.full.release()
    def recv(self):
        self.full.acquire()
        values = self.buffer[:self.buffer_len.value]
        self.empty.release()
        return values

# 性能测试，接收多条消息
def consume_test(count,ch):
    for i in range(count):
        values = ch.recv()

# 性能测试，发送多条消息
def produce_test(count,values,ch):
    for i in range(count):  # 一共发送 1000次 每次 10万个浮点数
        ch.send(values)

if __name__ == '__main__':
    ch = FloatChannel(100000)
    p = multiprocessing.Process(target=consume_test,
                                args=(1000,ch))
    p.start()
    values = [float(x) for x in range(100000)] # 10万个浮点数
    produce_test(1000,values,ch)
    print("Done")
    p.join()

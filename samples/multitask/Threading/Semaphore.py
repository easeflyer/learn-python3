#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading

produced = threading.Semaphore(0)           # 创建 produced 信号对象 初始值为 0
consumed = threading.Semaphore(1)           # 串讲 consumed 信号对象 初始值为 1

def producer():                             # 生产 循环
    while True: 
        consumed.acquire()                  # 等待获得信号量，如果信号量为0 则阻塞等待，上面初始为1 则首先会执行
        produce_item()                      # 生产产品
        produced.release()                  # 释放 produced 信号量 +1
def consumer(): 
    while True: 
        produced.acquire()                  # 获取 produced 信号量 如果为0 则 阻塞
        item = get_item()                   # 获得产品 消费
        consumed.release()                  # 释放 consumed 信号量。


''' 简要解析

produced = threading.Semaphore(0) 
consumed = threading.Semaphore(1)
def producer(): 
    while True: 
        consumed.acquire()          # 申请生产（有消费完毕吗？consumed > 0 吗？）只要有消费完毕，就继续生产  消费者 - 1
        produce_item()              # 生产
        produced.release()          # 生产完毕（produced 信号量+1， 也可以理解为，产品 > 0 个）
def consumer(): 
    while True: 
        produced.acquire()          # 有产品吗？（produced 信号量 > 0, 说明有产品被生产出来） 产品 - 1
        item = get_item()           # 消费
        consumed.release()          # 消费者 + 1 进入队列等待生产



'''
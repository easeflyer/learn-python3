#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading,time

produced = threading.Semaphore(0)           # 创建 produced 信号对象 初始值为 0     程序开始还没有产品
consumed = threading.Semaphore(2)           # 串讲 consumed 信号对象 初始值为 1     可以理解为：开始时有一个消费者

def producer(material,product):             # 生产 循环
    for m in material:
        consumed.acquire()                  # 等待获得信号量，如果信号量为0 则阻塞等待，上面初始为1 则首先会执行
        product.append("#"*m)
        time.sleep(0.1)
        produced.release()                  # 释放 produced 信号量 +1
def consumer(product,id): 
    while True: 
        produced.acquire()                  # 获取 produced 信号量 如果为0 则 阻塞  （没有产品则阻塞等待）
        p = product.pop()                   # 获得产品 消费
        print(id,p)
        time.sleep(1)
        consumed.release()                  # 释放 consumed 信号量。


material = [i for i in range(1,20)]
product = []

t = threading.Thread(target=consumer, args=(product,1))
t.daemon = True
t.start()

t1 = threading.Thread(target=consumer, args=(product,2))
t1.daemon = True
t1.start()


producer(material,product)




''' 简要解析

注意本程序，信号量决定了生产几个，然后开始消费，尝试修改消费者信号量为1 或者 2







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
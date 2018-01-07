#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
此案例演示了 管道的任何一端，都是可读可写的。
我们在消费端 保留了 conn1, 在生产端 保留了 conn2

然后分别让他们进行读写操作。
'''

import multiprocessing, time

def consumer(pipe):
    conn1,conn2 = pipe
    conn2.close()
    while True:                  # 首先做消费者
        try:
            item = conn1.recv()
            if item == None:
                break
            print("cons消费：",item)
        except EOFError:
            break
        print("#")

    for item in range(10,20):    # 然后转为生者
        print('cons生产：',item)
        conn1.send(item)

    conn1.close()                # 生产完毕关闭



def producer(pipe):
    conn1,conn2 = pipe
    conn1.close()
    for item in range(10):       # 首先做为生产者
        print('prod生产:',item)
        conn2.send(item)
        time.sleep(1)
    
    conn2.send(None)             # 发送一个信号

    while True:                  # 变为消费者
        try:
            item = conn2.recv()
            print("prod消费：",item)
        except EOFError:
            break

if __name__ == '__main__':
    conn1,conn2 = multiprocessing.Pipe()

    cons_p = multiprocessing.Process(target=consumer,args=((conn1,conn2),))
    cons_p.start()

    producer((conn1,conn2))
    cons_p.join()
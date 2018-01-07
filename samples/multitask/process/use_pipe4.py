#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 计划演示 全双工 确实是全双工的
此案例演示了 管道的任何一端，都是可读可写的。
我们在消费端 保留了 conn1, 在生产端 保留了 conn2

然后分别让他们进行读写操作。
'''

import multiprocessing, time, random

def consumer(pipe):
    conn1,conn2 = pipe
    conn2.close()
    t = 0
    while True:                  # 首先做消费者
        if t < 10:
            n = random.randrange(1,7)
            if n < 4:
                for item in range(n+1):
                    t = t + 1
                    print("--------------------cons生产：",t)
                    conn1.send(t)
               
        else:
            conn1.send(None) # 不再生产

        try:
            item = conn1.recv()
            if item == None:
                break
            print("cons消费：",item)
        except EOFError:
            break        

def producer(pipe):
    conn1,conn2 = pipe
    conn1.close()
    t = 0
    while True:                  # 首先做消费者

        if t < 10:
            n = random.randrange(1,7)
            if n < 4:
                for item in range(n+1):
                    t = t + 1
                    print("prod生产：",t)
                    conn2.send(t)
                
        else:
            conn2.send(None) # 不再生产    
        try:
            item = conn2.recv()
            if item == None:
                break
            print("----------------------------------prod消费：",item)
        except EOFError:
            break






















if __name__ == '__main__':
    conn1,conn2 = multiprocessing.Pipe()

    cons_p = multiprocessing.Process(target=consumer,args=((conn1,conn2),))
    cons_p.start()

    producer((conn1,conn2))
    cons_p.join()
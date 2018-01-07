#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing, time

'''
利用  None 信号，终止消费者进程。
参考：Python参考手册(第4版).pdf  p354

'''



def consumer(input_q,id):
    while True:
        item = input_q.get()
        if item is None:
            break
        print("%s消费：%s" % (id,item))
        time.sleep(5)

    print("消费者break退出.")

def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)
        print("生产：",item)
        time.sleep(2)
        

if __name__ == '__main__':
    q = multiprocessing.Queue()

    cons_p1 = multiprocessing.Process(target=consumer, args=(q,1))
    cons_p2 = multiprocessing.Process(target=consumer, args=(q,2))
    cons_p3 = multiprocessing.Process(target=consumer, args=(q,3))
    cons_p1.start()
    cons_p2.start()
    cons_p3.start()

    sequence = [i for i in range(10)]
    producer(sequence,q)

    q.put(None)     # 这里加入了 3个 None 三个消费者收到后，会自动退出。
    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()
    cons_p3.join()
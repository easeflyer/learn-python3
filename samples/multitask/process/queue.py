#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing

def consumer(input_q):                      # 消费者
    while True:
        item = input_q.get()
        print(item)                         # 具体如何消费,某些具体操作
        input_q.task_done()
def producer(sequence,output_q):            # 生产者
    for item in sequence:
        output_q.put(item)

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.daemon = True
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence,q)
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing, time
'''
本程序详细介绍参考 user_queue.py

本程序只增加了一个 消费者
'''



def consumer(input_q,id):                      # 消费者
    while True:
        print("cons wait for get....")
        item = input_q.get()                # 挂起等待队列
        print("%s消费：%s" % (id,item))                 # 具体如何消费,某些具体操作
        time.sleep(8)
        input_q.task_done()
def producer(sequence,output_q):            # 生产者
    for item in sequence:                   # 从任务列表取出任务
        #time.sleep(3)                      # 做适当处理，尝试调整时间，影响生产的速度
        output_q.put(item)                  # 放入 等待消费的队列，此时消费者就可以get到了。
        print('生产完毕：',item)

if __name__ == '__main__':
    #q = multiprocessing.JoinableQueue()
    q = multiprocessing.JoinableQueue()

    cons_p1 = multiprocessing.Process(target=consumer,args=(q,1))
    cons_p1.daemon = True                    # 设置为后台进程，创建者终止，他自动终止
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer,args=(q,2))
    cons_p2.daemon = True                    # 设置为后台进程，创建者终止，他自动终止
    cons_p2.start()



    sequence = [1,2,3,4,5,6,7,8,9,0]                    # 待处理任务列表
    producer(sequence,q)

    q.join()                                # 等消费者完成之后再退出。
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing, time
'''
程序特点：
    消费者consumer 是后台进程，随主进程退出
    消费者从队列取任务是挂起等待的状态。直到有任务继续。
    生产者producer 和消费者是异步的，消费等待生产，但生产不等待消费。


执行过程：
1 主程序建立队列 q
2 建立新进程cons_p 用于执行消费者操作
3 cons_p 被设定为后台进程，主进程关闭，自动关闭
4 cons_p 开启无限循环，等待从任务队列get
5 定义待执行任务队列 sequence

6 生产函数执行循环处理 任务列表，然后放入待消费队列
7 消费函数get到数据后 消费, 然后使用task_done() 发出信号，已消费完毕

注意：
input_q.get()           暂时阻塞，直到队列有数据为止。
input_q.task_done()     只是通知队列，刚get的项目已经处理完毕

q.join                  阻塞当前进程，直到队列所有项目都task_done()

'''

class MyCls(object):
    def __init__(self,name):
        self.name = name
        self.v1 = "123"
        self.v2 = "456"
        self.v3 = (1,2,3)
    def test(self):
        return self.v2





def consumer(input_q,n):                      # 消费者（阻塞的，等待生产）
    while True:
        print("cons wait for get....")
        item = input_q.get()                # 挂起等待队列
        print(n,"消费：",item.test(),":",item.v1)      # 具体如何消费,某些具体操作
        time.sleep(2)
        input_q.task_done()
def producer(sequence,output_q):            # 生产者（非阻塞，一直生产）
    for item in sequence:                   # 从任务列表取出任务
        #time.sleep(3)                      # 做适当处理，尝试调整时间，影响生产的速度
        output_q.put(item)                  # 放入 等待消费的队列，此时消费者就可以get到了。
        print('生产完毕：',item)

if __name__ == '__main__':
    #q = multiprocessing.Queue()            # 不能用他，不具备 join 功能和 task_done
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer,args=(q,1))
    cons_p.daemon = True                    # 设置为后台进程，创建者终止，他自动终止
    cons_p.start()

    cons_p1 = multiprocessing.Process(target=consumer,args=(q,2))
    cons_p1.daemon = True                    # 设置为后台进程，创建者终止，他自动终止
    cons_p1.start()

    #sequence = [1,2,3,4]                    # 待处理任务列表,模拟了一个任务列表。（可理解为“原材料”）
    sequence = [MyCls(i) for i in range(16)] # 这里没有序列化 。
    sequence[10].v1 = "我被修改了！"           # 经过这里测试，发现数据是共享的。
    producer(sequence,q)                    # “原材料”交给 producter 加工，然后发给消费者

    q.join()                                # 等消费者完成之后再退出。如果不用，主进程将提前终止，子进程，也将随之终止。


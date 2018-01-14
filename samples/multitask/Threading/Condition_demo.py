#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 简单概括： Condition 方式 就是 获得锁之后。 在处理工作之前 进行判断。
# acquire() 获得锁
# if ... wait  如果不满足条件则wait 而不是直接 生产 或者消费。 (中间这一步就是 Condition 的独特之处)
# release 释放锁


import threading,time


cv = threading.Condition()              # 新建一个“条件变量” cv 只是比之前的 同步方式多了一些步骤而已。
                                        # Semaphore 信号量方式，只要 acquire() 获得了信号量，即可生产。
                                        # 而 Condition 方式，在acquire之后，  在release 之前，有机会做判断，然后wait 或者 notify
                                        # notify 将会唤醒其他 wait， 而wait 则是释放 锁，等待notify
def producer(item,n):
    for i in range(10): 
        cv.acquire()                    # 获取底层锁定
        print("p_acquire......")
        item.append(i+n)                  # 生产
        print("生产了：",i+n)
        time.sleep(0.4)
        cv.notify_all()                     # 唤醒等待 cv 的 n个线程，notify(n) n 是唤醒线程的数量
                                        # 调用 notify() 一定在 acquire() 获得锁定之后
        cv.release()                    # 释放底层锁定
        print("p_release.....")


def consumer(item,n): 
    while True: 
        print("-"*15+n+"c等待 acquire.....")
        cv.acquire() 
        print("-"*15+n+"c获得 acquire OK")
        while not len(item):  # 如果 没有产品 就 等通知
            print("-"*15+n+"c_没产品wait")
            cv.wait()                   # 等待 通知（notify），或者超时为止， 调用后 释放底层锁定 相当于release() 并且 睡眠。 获得通知重新获得锁定
                                        # 获得通知，继续判断是否有产品。

                                        # 获得通知 且 有产品 程序绕过此循环继续。
        print("-"*15+n+"消费：",item.pop())               # 消费                                         
        cv.release()                    # 释放锁定
        print("-"*15+n+"c_release")
        time.sleep(0.1)



item = []

t = threading.Thread(target=producer, args=(item,1000))     # 两个生产线程
t.start()
# t3 = threading.Thread(target=producer, args=(item,2000))    
# t3.start()
time.sleep(1)
t1 = threading.Thread(target=consumer, args=(item,"1"))     # 两个消费线程
t1.start()

t2 = threading.Thread(target=consumer, args=(item,"2"))
t2.start()






'''
wait_for(predicate, timeout=None) 相当于上面的
while not predicate():
    cv.wait()

'''
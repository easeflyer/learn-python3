#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 这是一个 condition 的模板


import threading


cv = threading.Condition()              # 新建一个“条件变量” cv
def producer():
    while True: 
        cv.acquire()                    # 获取底层锁定
        produce_item()                  # 生产
        cv.notify()                     # 唤醒等待 cv 的 n个线程，notify(n) n 是唤醒线程的数量
                                        # 调用 notify() 一定在 acquire() 获得锁定之后
        cv.release()                    # 释放底层锁定





def consumer(): 
    while True: 
        cv.acquire() 
        while not item_is_available():  # 如果 没有产品 就 等通知
            cv.wait()                   # 等待 通知（notify），或者超时为止， 调用后 释放底层锁定 相当于release() 并且 睡眠。 获得通知重新获得锁定
                                        # 获得通知，继续判断是否有产品。

                                        # 获得通知 且 有产品 程序绕过此循环继续。
                                         
        cv.release()                    # 释放锁定
        consume_item()                  # 消费



'''
wait_for(predicate, timeout=None) 相当于上面的

while not predicate():
    cv.wait()

'''
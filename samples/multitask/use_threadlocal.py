#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name     # ？？ 给全局对象赋值？ 不用 global 吗？
    process_student()


# threading.Thread(target可以调用的程序，args给target提供的参数列表，name线程的名字)
t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


print("-"*80)

class cla:
    pass

c = cla()
c.v1 = 5
v2 = 55

def fun1():
    c.v1 = 8    # 这里修改 c.v1 成功。因为 c 是全局的，因此 c.v1 也就是引用的全局变量。
    v2 = 66     # 注意这里改写 全局变量 v2 不成功，因为这里的v2 是局部变量

fun1()
print(c.v1)
print(v2)
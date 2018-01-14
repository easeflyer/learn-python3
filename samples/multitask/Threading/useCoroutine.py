
#!/usr/bin/python3
# -*- coding: utf-8 -*-


def foo():
    for n in range(5):
        print("I'm foo %d" % n)
        yield
def bar():
    for n in range(10):
        print("I'm bar %d" % n)
        yield
def spam():
    for n in range(7):
        print("I'm spam %d" % n)
        yield
# Create and populate a task queue
from collections import deque
taskqueue = deque()
taskqueue.append(foo())                # 添加一些任务（都是生成器）也就是可以被调度的任务。
taskqueue.append(bar())
taskqueue.append(spam())
# Run all of the tasks
while taskqueue:                        # 这是一个顺序调度的方式。在 try 语句段，也可以对 任务作出某些判断。后直接放回去，完成轮询的调度方式。
    # Get the next task
    task = taskqueue.pop()              # 取出一个任务（foo,bar,spam 其一）
    try:
        # Run it to the next yield and enqueue
        next(task)                      # 执行任务 next 是获取 task 生成器的下一个值
        taskqueue.appendleft(task)      # 把 任务对象再放回 队列。
    except StopIteration:
        # Task is done
        pass


'''
双向队列（Deque）是栈和队列的一般化（deque发音和‘deck’一样，是‘double-ended queue’的缩写）。Deque是线程安全的。在队列两端添加（append）或弹出（pop）元素的复杂度大约是O(1),所以Deque的效率是很高的。

尽管list 对象支持类似的操作, 但是list是专门为固定长度的操作进行了优化，导致了改变列表长度和数据位置的操作例如 pop(0)和 insert(0, v) 操作的复杂度高达O(n)

'''
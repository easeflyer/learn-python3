#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random


# 模拟一个 执行比较长时间的 进程任务
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid())) # getpid 获得当前进程的 process  id
    start = time.time() # 计时开始
    time.sleep(random.random() * 3)
    end = time.time()   # 计时结束
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply(long_time_task, args=(i,))          # apply 串行
        #p.apply_async(long_time_task, args=(i,))   # apply_async 异步，并行的
    print('Waiting for all subprocesses done...')
    p.close()   # 调用 close 后 就不能再添加子进程了
    p.join()    # 暂时挂起父进程等待进程池执行完毕
    print('All subprocesses done.')

''' 结果解析
Parent process 1732.                    父进程开始执行
Waiting for all subprocesses done...    父进程先继续，进程池中的进程任务需要时间
Run task 0 (6436)...                    p.close p.join 暂时挂起了父进程等待子进程，因此子进程陆续开始
Run task 1 (3376)...
Run task 2 (6684)...
Run task 3 (1508)...
Task 3 runs 0.32 seconds.               我们注意到 task 4 并没有开始，原因是进程池默认同时执行4个进程，因此 task 3 完成后，task 4 才开始
Run task 4 (1508)...
Task 0 runs 1.08 seconds.
Task 2 runs 1.15 seconds.
Task 1 runs 1.60 seconds.
Task 4 runs 1.33 seconds.
All subprocesses done.


'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import multiprocessing, time
# 参考 use_pipe2.py 如果这里子进程没有传过来 input 端，就不需要再关闭了。
def consumer(output,id):
    output_p = output
    #input_p.close()                    # 关闭管道的输入端，因为消费者 只需要输出端 接收数据
    while True:
        try:
            item = output_p.recv()      # 接收c.send()方法返回的对象 如果input 端已经关闭，则抛出错误
        except EOFError:
            break
        # 处理项目
        print("%s消费：%s" % (id,item))             # 接收到以后消费
        time.sleep(3)
    # 关闭
    print('Consumer done')
        
def producer(sequence, input_p):
    for item in sequence:
        print('生产：',item)
        input_p.send(item)              # 发送数据，写入
        # time.sleep(1) #间隔2秒

if __name__ == '__main__':
    (output_p, input_p) = multiprocessing.Pipe()        # 建立管道，返回两个 connection 对象
    # 启动使用者进程1
    cons_p1 = multiprocessing.Process(target=consumer,args=(output_p,1))  # ?? 给一端不就可以了？ 为什么给两端？
    cons_p1.start()                                      # 上面语句创建进程执行 consumer函数 并把管道连接发送给 消费者对象，启动进程
    # 使用者进程2
    cons_p2 = multiprocessing.Process(target=consumer,args=(output_p,2))
    cons_p2.start()                                      # 上面语句创建进程执行 consumer函数 并把管道连接发送给 消费者对象，启动进程


    # 关闭生产者中的输出管道
    output_p.close()
    print("生产者已关闭：output_p")
    
    # 生产项目
    sequence = [i for i in range(10)]
    producer(sequence, input_p)

    # 关闭输入管道，标识完成，生产完毕了，关闭了。
    input_p.close()
    print("生产者已关闭：input_p")

    # 等待使用者进程关闭
    cons_p1.join()
    cons_p2.join()


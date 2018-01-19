#!/usr/bin/python3
# -*- coding: utf-8 -*-


import multiprocessing, time

def consumer(pipe,id):
    output_p, input_p = pipe
    input_p.close()                     # 关闭管道的输入端，因为消费者 只需要输出端 接收数据。
    while True:
        try:
            item = output_p.recv()      # 接收c.send()方法返回的对象 如果input 端已经关闭，则抛出错误
                                        # 注意recv() 是阻塞的，挂起等待，直到接收到数据为止
            item = output_p.recv()                                        
        except EOFError:
            break
        # 处理项目
        print("%s消费：%s" % (id,item))             # 接收到以后消费
    # 关闭
    print('Consumer done')
        
def producer(sequence, input_p):
    print("CPU：",multiprocessing.cpu_count())    # 工具函数参考：Python参考手册(第4版).pdf 20章
    for item in sequence:
        print('生产：',item)
        input_p.send(item)
        time.sleep(2) #间隔2秒

if __name__ == '__main__':
    (output_p, input_p) = multiprocessing.Pipe()        # 建立管道，返回两个 connection 对象,链接管道两端

    cons_p1 = multiprocessing.Process(target=consumer,args=((output_p,input_p),1))
                                                         # 启动使用者进程1
    cons_p1.start()                                      # 上面语句创建进程执行 consumer函数 并把管道连接发送给 消费者对象，启动进程

    # cons_p2 = multiprocessing.Process(target=consumer,args=((output_p,input_p),2))
    #                                                      # 使用者进程2
    # cons_p2.start()                                      # 上面语句创建进程执行 consumer函数 并把管道连接发送给 消费者对象，启动进程

    output_p.close()                                     # 关闭生产者中的输出管道
    
    # 生产项目
    sequence = [i for i in range(10)]
    producer(sequence, input_p)

    # 关闭输入管道，标识完成
    input_p.close()

    # 等待使用者进程关闭
    cons_p1.join()
    cons_p2.join()

'''
代码分析：
(output_p, input_p) = multiprocessing.Pipe()    Pipe 返回的是两个 连接对象。代表管道两端。 都可以进行输入输出。
                                                但程序通常使用一端输入，一端输出。因此这里使用命名的方式，确定输入输出的用途。

注意在子进程中如果复制了对两端的引用， 不使用的一端要进行关闭。因为只要有引用，管道就不会产生 EOFError 错误

注意此代码中存在一个问题：就是当有两个消费者的时候，要对数据进行序列化。参考 use_pipe1.py


'''
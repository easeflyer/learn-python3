
'''
所谓原语，是操作系统内核中，由若干条指令构成、用于完成一个特定的功能的一个过程，
该过程在执行时是不可中断的。如：创建进程原语：create(n)，撤销进程原语：destroy(n)，
阻塞进程原语：block()，唤醒进程原语：wakeup(n)．


当一个进程调用一个send原语时，在消息开始发送后，发送进程便处于阻塞状态，直至消息完全发送完毕，
send原语的后继语句才能继续执行。当一个进程调用一个receive原语时，并不立即返回控制，
而是等到把消息实际接收下来，并把它放入指定的接收区，才返回控制，继续执行该原语的后继指令。
在这段时间它一直处于阻塞状态。上述的send和receive被称为同步通信原语或阻塞通信原语。

A semaphore（信号量） is a synchronization（同步） primitive（原语） based on a counter（基于计数器）
that’s decremented by each acquire() call and incremented by each release() call.If the counter ever reaches zero,the acquire() method blocks until some other thread calls release()
信号量是一种基于计数器的同步原语，调用acquire()减一，调用和release()加一。如果计数器为0 acquire()方法阻塞，直到其他线程调用release()。
'''


import multiprocessing
class FloatChannel(object):
    def __init__(self, maxsize):
        self.buffer     = multiprocessing.RawArray('d',maxsize)
        self.buffer_len = multiprocessing.Value('i')
        self.empty      = multiprocessing.Semaphore(1)  #  设置 empty 信号量对象 初始值 1
        self.full       = multiprocessing.Semaphore(0)  #  设置 full 信号量对象 初始值 0
    def send(self,values):
        self.empty.acquire()             # Only proceed if buffer empty 
        nitems = len(values)
        self.buffer_len = nitems         # Set the buffer size 
        self.buffer[:nitems] = values    # Copy values into the buffer 
        self.full.release()              # Signal that buffer is full 
    def recv(self): 
        self.full.acquire()              # Only proceed if buffer full 
        values = self.buffer[:self.buffer_len.value]   # Copy values 
        self.empty.release()             # Signal that buffer is empty return values

# Performance test.  Receive a bunch of messages 
def consume_test(count, ch): 
    for i in range(count): 
        values = ch.recv()
# Performance test. Send a bunch of messages 
def produce_test(count, values, ch): 
    for i in range(count): 
        ch.send(values)
if __name__ == '__main__': 
    ch = FloatChannel(100000) 
    p = multiprocessing.Process(target=consume_test, 
                                args=(1000,ch)) 
    p.start() 
    values = [float(x) for x in range(100000)] 
    produce_test(1000, values, ch) 
    print("Done") 
    p.join() 
import threading,time
from queue import Queue
class WorkerThread(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self,*args,**kwargs)
        self.input_queue = Queue()                          # 构造函数中
    def send(self,item):
        self.input_queue.put(item)                          # 加入队列，如果队列满，将阻塞，直到有位置为止。（参考队列的 maxsize）
    def close(self):
        self.input_queue.put(None)                          # 调用线程的close方法，队列插入 None 标志
        self.input_queue.join()                             # 阻塞，直到队列中的所有元素都被处理为止。
    def run(self):
        while True:
            item = self.input_queue.get()                   # 获得一个元素，如果没有将阻塞，直到获得为止
            if item is None:                                # 判断 结束线程的方式
                break
            # Process the item (replace with useful work)
            time.sleep(2)
            print(item)                                     # 输出元素
            self.input_queue.task_done()                    # 告知队列 任务处理完毕
        # Done. Indicate that sentinel was received and return
        self.input_queue.task_done()                        # 因为 循环z最后 break 因此这里增加一个 task_done()
        return
# Example use
w = WorkerThread()
w.start()
w.send("hello") # Send items to the worker (via queue)
w.send("world")

for i in range(10):
    w.send(str(i))
    time.sleep(1)
print('w.close')
w.close()               # 这里放进去了 None 因此 None 在最后。队列一定会被处理完。无论是否 join()

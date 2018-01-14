import multiprocessing,time
from multiprocessing.managers import BaseManager
from Amodule import A,MyManager

'''

Amodule 模块中 自定义了一个类型 A 和 管理器 MyManager

'''


def watch(d, evt):
    '''
    仍然定义 watch 函数，用于在子进程中调用 共享自定义对象。
    '''
    while True:
        evt.wait()
        print(d.x)
        evt.clear()

#MyManager.register("A", A)
if __name__ == '__main__':
    m = MyManager()
    m.start()                           # 注意 m 本身就工作在一个单独的进程中
    evt = m.Event()
    a = m.A(37)                         # 实例化共享对象 A 的实例
    p = multiprocessing.Process(target=watch, args=(a, evt))
    p.daemon = True                     # daemon 后台进程，随主线程关闭
    p.start()                           # watch 进程启动就绪    

                         
    # Create a managed object
    #print(a.getX())
    print(a.x)                          # 自定义代理中 设定了 x 属性的装饰器，因此可以直接访问
    a.x = 88                            # 重新

    evt.set()                           # 通知事件
    time.sleep(5)                       # 阻塞等待5秒
    print("主进程：",a.x)               # 主进程再次输出共享对象 a
    # Terminate the process and manager
    p.terminate()                       # 进程结束
    m.shutdown()                        # 管理器结束


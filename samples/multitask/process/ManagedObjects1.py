import multiprocessing
from multiprocessing.managers import BaseManager
from Amodule import A,MyManager

'''

Amodule 模块中 自定义了一个类型 A 和 管理器 MyManager

'''


#MyManager.register("A", A)
if __name__ == '__main__':
    m = MyManager()
    m.start()
    # Create a managed object
    a = m.A(37)                 # 实例化共享对象 A 的实例
    #print(a.getX())
    print(a.x)                  # 自定义代理中 设定了 x 属性的装饰器，因此可以直接访问
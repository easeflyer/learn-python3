#!/usr/bin/python3
# -*- coding: utf-8 -*-  


#  python 2.2 之前的 调用父类构造方法的 方式。
#  缺点：https://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html
#  单继承 适合用 super 多继承 仍然保留这种方法


# 定义 A
class A:
  def __init__(self):   # A 的构造方法
   print("enter A")
   print("leave A")

class B(A):             # B 继承自 A
  def __init__(self):   # B 的构造方法
   print("enter B")     # 输出： enter B
   A.__init__(self)     # 调用 A 的构造方法   
   print("leave B")     # 输出： enter B

b = B()
# print (b)
#  enter B
#  enter A
#  leave A
#  leave B


print("=======================================")

class A(object):    # A must be new-style class
  def __init__(self):
   print("enter A")
   print("leave A")

class C(object):    # A must be new-style class
  def __init__(self):
   print("enter C")
   print("leave C")

# 这里我们注意到：如果 B 不再继承 A 二是改为继承 C 只需要改动一个地方。

class B(C):     # A --> C
  def __init__(self):
   print ("enter B")
   super(B, self).__init__()
   print ("leave B")

b1 = B()
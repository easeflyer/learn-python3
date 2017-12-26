#!/usr/bin/python3
# -*- coding: utf-8 -*-  
class A(object):
  def __init__(self):
   print("enter A")
   print("leave A")

class B(object):
  def __init__(self):
   print("enter B")
   print("leave B")

class C(A):
  def __init__(self):
   print("enter C")
   super(C, self).__init__()
   print("leave C")

class D(A):
  def __init__(self):
   print("enter D")
   super(D, self).__init__()
   print("leave D")
class E(B, C):
  def __init__(self):
   print("enter E")
   B.__init__(self)
   C.__init__(self)
   print("leave E")

class F(E, D):
  def __init__(self):
   print("enter F")
   E.__init__(self)
   D.__init__(self)
   print("leave F")

f = F()

# 1)我们看到结果，比较严重的问题是 super(C, self).__init__()  怎么会调用了 D 的 __init__
# 2)明显地，类A和类D的初始化函数被重复调用了2次，作为 F() 使得父类的初始化被调用2次，似乎也不符合面向对象的逻辑
#      注意 A 被调用2次还可以理解，虽然不符合面向对象的理念。但是D 为什么被调用了？

# enter F
#         enter E
#                 enter B
#                 leave B

#                 enter C
#                     enter D ?
#                     enter A
#                     leave A
#                     leave D ?
#                 leave C
#         leave E

#         enter D
#             enter A
#             leave A
#         leave D
# leave F



class A(object):
  def __init__(self):
   print("enter A")
   super(A, self).__init__()  # new
   print("leave A")

class B(object):
  def __init__(self):
   print("enter B")
   super(B, self).__init__()  # new
   print("leave B")

class C(A):
  def __init__(self):
   print("enter C")
   super(C, self).__init__()
   print("leave C")

class D(A):
  def __init__(self):
   print("enter D")
   super(D, self).__init__()
   print("leave D")
class E(B, C):
  def __init__(self):
   print("enter E")
   super(E, self).__init__()  # change
   print("leave E")

class F(E, D):
  def __init__(self):
   print("enter F")
   super(F, self).__init__()  # change
   print("leave F")

print("======================================")   
f = F()


# 记住这两个例子的继承关系 即可。这里涉及到 python 多重继承的 结果关系 是按照一个 遍历的过程。而不是父子的过程。因此才会出现上例中理解的问题。
# 参考：https://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html
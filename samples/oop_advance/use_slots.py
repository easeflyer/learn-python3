#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'

# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('1AttributeError:', e)


# __slots__ 只限制当前类，子类 不受限制
g = GraduateStudent()
g.score = 99
print('g.score =', g.score)


print("-"*80)

class cls1(object):
    def fun1(self):
        print("func1...")


c1 = cls1()
c2 = cls1()

c1.fun1()
c2.fun1()

c1.fun2 = lambda x: x * x
print (c1.fun2(3))

def func1(self,x):                  # 注意因为要绑定到类，因此注意增加 self 参数，这个参数起其他名字也是可以的。
    self.name = "new name"
    return x + 3


cls1.fun3 = func1                   # 给 类绑定一个新函数，则所有对象都可以访问。注意这里是动态绑定，之前生成的对象，也都有了这个方法。
cls1.fun4 = lambda self,x: x + 10
print (c1.fun3(2))                  # 注意这里因为执行了 fun3 因此所有对象都增加了 name 属性，太变态！
print (c2.fun3(5))
print(c1.name)
print(c2.name)
print()
print (c1.fun4(2))
print (c2.fun4(5))

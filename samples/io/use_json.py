#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
JSON类型	        Python类型
{}	              dict
[]	              list
"string"	      str
1234.56	          int或float
true/false	      True/False
null	          None
'''




import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)                        # json.dumps(d) 对象转换为 json 字符串
print(type(data))
print('JSON Data is a str:', data)
reborn = json.loads(data)                   # json.loads(data) 还原为 对象
print(reborn)
print("reborn.name:",reborn['name'])



print("-"*80)

'''
序列化 自定义类对象的方法：

1 自定义对象类型 默认是不支持直接序列化的
2 json.dumps(序列化对象，default) default 参数可以绑定一个函数，用于把对象转变为可以序列化的类型。即可正常序列化。
3 反序列化也是同样，反序列化之后，得到的是一个可序列化的对象，并不是原对象类型，这时也需要 一个函数负责把他还原成原对象类型。
    json.loads(json_str, object_hook=dict2student)

理解：简单说把一个对象，变成 属性字典，然后序列化，  反序列化回属性字典，然后再调用构造函数重新构造这个对象。
为什么不能直接序列化？因为类的定义相对比较复杂，无法完成一个标准统一的序列化和反序列化过程 js 是特例

'''


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
print("obj.__dict__:",s.__dict__)           # 通常自定义的对象都有一个 __dict__属性 用来保存 属性列表

std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

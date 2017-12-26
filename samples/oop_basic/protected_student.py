#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.__name = name                  # 私有属性 __name
        self.__score = score

    def get_name(self):                     # 访问 属性 __name
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):             # 设置属性 __score 并且做合法性检查 0-100之间
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):                    # 
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

# print(bart.__name) # 私有属性 无法读取
print('DO NOT use bart._Student__name:', bart._Student__name)  # 但实际上可以这样读取，（不建议）

# 如果设置 bart.__name = "某某"，实际上是新增了一个变量
bart.__name = "someone"
print(bart.__name)

# 也就是说 python 并没有真正意义上的私有变量，全靠自觉

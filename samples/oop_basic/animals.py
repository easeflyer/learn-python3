#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):   # 这里 animal 只是一个形参。并不对参数做类型要求
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

class yazi:
    def run(self):
        print("我不是animal，但是看起来像animal")

    
d = yazi()

run_twice(c)
run_twice(d)


# 显示变量的类型用 type
print(type(d)=='yazi')  # False
print(type(d)==yazi)    # True
print(type(c)==Animal)  # False
print(type(c)==Cat)     # True

print("-"*80)
# 判断一个变量是否为 某个类型用 isinstance

# print(isinstance(d,'yazi'))  # False
print(isinstance(d,yazi))    # True
print(isinstance(c,Animal))  # True
print(isinstance(c,Cat))     # True
print(isinstance(d,Animal))  # True

print("Dog or Cat:",isinstance(c,(Dog,Cat)))  # True

print("-"*80)

print("Dog:",dir(Dog))
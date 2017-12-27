#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
序列化：

b = pickle.dumps(d)         把任意对象序列化成一个  bytes
d = pickle.loads(b)         反序列化 bytes 回对象

pickle.dump(d,file-like)    把对象 d 序列化并保存到 file-like object
pickle.load(file-like)      把file-like 读取到的 bytes 反序列化回对象

注意：pickle 序列化 只是 python 自己使用。
而 json 可以异构系统使用。但是 json 序列化，，不能对 python 的自定义对象

'''




import pickle

d = dict(name='Bob', age=20, score=88)      # 定义一个字典
data = pickle.dumps(d)                      # 序列化：pickle.dumps()方法把任意对象序列化成一个  bytes
print(data)

reborn = pickle.loads(data)                 # 反序列化 成对象
print(reborn['name'])


with open('./f.txt','wb') as f:
    pickle.dump(d,f)                        # 序列化：pickle.dumps()方法把任意对象序列化成一个  bytes

with open('./f.txt','rb') as f:
    reborn1 = pickle.load(f)                 # 反序列化 成对象

print(reborn1['age'])

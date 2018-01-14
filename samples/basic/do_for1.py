#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
嵌套 列表生成式的 演示
'''

l = [ [i,j]  for i in range(1,4) for j in range(i)]
print("l1:",l)

l = []
for i in range(1,4):
    for j in range(i):
        l.append([i,j])
print("l2:",l)


# [
#     [1, 0], 
#     [2, 0], 
#     [2, 1], 
#     [3, 0], 
#     [3, 1], 
#     [3, 2]
# ]

import os
l = [[path,name] for path,dirs,files in os.walk("./") for name in files ]
print(l)

allfiles = (os.path.join(path,name) for path,dirs,files in os.walk("./") for name in files )

for n in allfiles:
    print(n)
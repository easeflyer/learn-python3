#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from os.path import join, getsize
# for root, dirs, files in os.walk('./'):
#     print(root, "consumes", end=" ")
#     print(sum(getsize(join(root, name)) for name in files), end=" ")
#     print("bytes in", len(files), "non-directory files")
#     if 'CVS' in dirs:
#         dirs.remove('CVS')  # don't visit CVS directories


from os.path import join, getsize
for root, dirs, files in os.walk('./'):
    print("root:",root)
    print("dirs:",dirs)
    print("files:",files)


'''
walk(目录) ：遍历目录，返回有三个元素的  tuple（root,dirs,files） 三个值分别是：
root 正在遍历的目录
dirs 正在遍历的目录下的目录列表
files 正在遍历目录下的文件列表

'''

print(os.path.join("/",'dir1','dir2','dir3'))
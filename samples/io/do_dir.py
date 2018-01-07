#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

print("os.name:",os.name)
#print("os.name:",os.uname()) # windows 环境不支持
#print("os.environ:",os.environ)            # 所有环境变量
print("PATH:",os.environ.get('PATH'))       # 获得具体某个环境变量

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

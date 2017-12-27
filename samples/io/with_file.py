#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


# 注意默认情况下 encoding 跟着系统走，windows 系统默认采用gbk 编码
#with open('test.txt', 'w') as f:
with open('test.txt', 'w', encoding='utf-8') as f:    
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

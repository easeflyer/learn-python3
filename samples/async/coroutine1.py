#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time

file = ["文件的第1行文字",
        "文件的第2行文字",
        "文件的第3行文字",
        "文件的第4行文字",
        "文件的第5行文字",
        "文件的第6行文字"]



def pline():
    while True:
        line = yield
        time.sleep(1)
        print(line)
        # if pattern in line:
        #     print(line)

next_coroutine = pline()
next_coroutine1 = pline()
next_coroutine.send(None)
next_coroutine1.send(None)
for line in file:
    next_coroutine.send(line)
    next_coroutine1.send(line)
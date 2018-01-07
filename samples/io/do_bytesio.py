#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
#print("f.getvalue():",f.getvalue())
#print("f.read():",f.read().decode('utf-8'))
# f.close()     # 调用close()方法时，文本缓冲区将被丢弃
f.seek(0)
v = f.read().decode("utf-8")
print("v:",v)


# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())     # 读完之后指针指向流末尾。再read()将没有输出
f.seek(0)           # 将流位置更改为给定字节偏移量。seek(offset[, whence])
v1 = f.read()
v1 = v1.decode("utf-8")
print("-"*80)
print(v1)

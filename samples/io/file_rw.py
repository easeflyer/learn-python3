#!/usr/bin/python3
# -*- coding: utf-8 -*-


try:
    #f = open('./file.txt', 'r')                       # 注意如果不给出编码，可能会报错。
    f = open('./file.txt', 'r',encoding='utf8')
    str = f.read()                                    # 如果不给出编码，这里就会报错。
    print(str)                      # 
finally:                            # UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 0: illegal multibyte sequence
    if f:
        f.close()
print("-"*80,"下面用with")

'''
以上写法没有问题，但是有些繁琐，不美观，而python原则就是让代码可读性更好。更优雅，因此替代方案是用with
with 利用上下文管理器协议 在代码段结束后 利用 __exit__ 自动处理收尾工作 f.close()
'''

with open('./file.txt', 'r',encoding='utf8') as f:
    str = f.read()
    print(str)


with open('./file.txt', 'w',encoding='utf8') as f:  # w 方式 覆盖写入
    f.write('Hello, world!')

with open('./file.txt', 'r',encoding='utf8') as f:
    str = f.read()
    print(str)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
print(md5.digest())


sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


'''
hash.digest() 返回字节对象
返回传递给update()方法的数据的摘要。它是一个大小为digest_size的字节对象，包含的字节可以在0到255整个范围。

hash.hexdigest() 返回字符串
类似digest()，但是摘要以2倍长度的字符串对象返回，只包含十六进制数字。这可用于在电子邮件或其它非二进制环境中安全交换数据
'''
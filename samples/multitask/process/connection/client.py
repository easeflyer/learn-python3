#!/usr/bin/python3
# -*- coding: utf-8 -*-
from multiprocessing.connection import Client

'''
案例：服务器 - 客户端 模式的数据共享与消息传送。
conn = Client()         建立一个客户端连接
serv = Listener()       侦听 某个端口 建立一个服务器 
conn = serv.accept()    返回和客户端的连接

conn.send()             发送数据
conn.recv()             接收数据（注意是 recv 是挂起等待状态，如果没数据则会一直挂起）
                        send(),recv() 客户端服务器端都可以使用。
conn.close()            关闭连接

考虑如果要发送一个自定义对象？ 应该进行序列化和反序列化的操作

'''



conn = Client(('localhost',15000), authkey=b"12345")
print("3,4")
conn.send((3,4))
print("3,4....")
r = conn.recv()
print(r) # Prints '7'
conn.send(("Hello","World"))
r = conn.recv()
print(r) # Prints 'HelloWorld'
conn.send(("exit;","World"))
conn.close()
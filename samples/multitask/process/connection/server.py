#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing.connection import Listener

serv = Listener(('localhost', 15000), authkey=b'12345')
while True:
    conn = serv.accept()        # 注意服务器一直处于等待连接状态的 轮询中
    print("服务已连接...")
    while True:
        print('等待接收数据...')
        try:
            x, y = conn.recv()
            print('收到x:%s y:%s' % (x, y))

            if x=='exit;':
                conn.close()
                exit()

        except EOFError:
            print("客户端已经关闭....")
            break

        result = x + y
        conn.send(result)
    conn.close()
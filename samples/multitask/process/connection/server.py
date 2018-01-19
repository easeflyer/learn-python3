#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing.connection import Listener


                                            # 创建一个服务器, 监听域名：localhost 端口：15000  密钥：b'12345' bytes 类型
serv = Listener(('localhost', 15000), authkey=b'12345')
while True:                                 # 主循环
    conn = serv.accept()                    # 注意服务器一直处于等待连接状态的 轮询中，当有连接，返回连接，程序继续
                                            # conn 是一个 Connection 对象
    print("服务已连接...")                   
    while True:                             # 处理循环
        print('等待接收数据...')
        try:
            print('conn.recv等待接收数据...')
            x, y = conn.recv()              # 阻塞等待 conn.send() 发来数据     
            print('收到x:%s y:%s' % (x, y))

            if x=='exit;':                  # 如果发来的 x == ’exit;‘ 则断开链接
                conn.close()
                exit()

        except EOFError:
            print("客户端已经关闭....")
            break

        result = x + y
        conn.send(result)
    conn.close()


'''
分析：连接对象 Connection
之前代码在使用管道的时候，返回的也是链接对象。
因此我们可以知道这里的链接对象就是 管道的链接对象，使用的是管道 作为数据传递的方式。


'''
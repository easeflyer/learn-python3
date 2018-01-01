#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def wget(host):                                             # host 准备要打开的网址
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)             # coroutine asyncio.open_connection 是 create_connection()的包装器返回（rader，writer）对
                                                            # reader返回的是一个StreamReader实例；writer是一个StreamWriter实例。
                                                            # 根据给定的 host 和 port 建立一个流连接，注意他是一个协程
    # print(connect)                                        # 结果可以看到 他是一个 generator <generator object open_connection at
                                                            # 因此注意 connect 并不会立即执行。而是返回对象的引用
    reader, writer = yield from connect                     # 挂起当前，转向协程connect（也是一个生成器）开始执行,当前程序 等待结果
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
利用 Pipe 管道 双向通信的方式 模拟 请求，响应的机制。
参考：Python参考手册(第4版).pdf p357
adder 以类似服务器的形式运行
'''




import multiprocessing

def adder(pipe):                    # server 一直挂起等待请求
    server_p, client_p = pipe
    client_p.close()
    while True:
        try:
            x,y = server_p.recv()   # 接收到请求
        except EOFError:
            break
        result = x + y              # 处理请求
        server_p.send(result)       # 发送反馈响应结果
    print("Server done")


if __name__ == '__main__':
    server_p, client_p = multiprocessing.Pipe()
    
    adder_p = multiprocessing.Process(
        target=adder,args=((server_p,client_p),))
    adder_p.start()                 # 启动服务器进程
    
    server_p.close()                # 关闭客户端中服务器端管道

    client_p.send((3,4))
    res = client_p.recv()
    print(res)

    client_p.send(('Hello',' World'))
    res = client_p.recv()
    print(res)

    
    client_p.close()                # 完成后关闭管道
    adder_p.join()                  # 等待服务器进程关闭
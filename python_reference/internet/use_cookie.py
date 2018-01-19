#!/usr/bin/python3
# -*- coding: utf-8 -*-

try: # py3
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from http.cookies import SimpleCookie
except ImportError: # py2
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        c = SimpleCookie()
        c['name'] = '张三'
        c['cartid'] = '123'
        c['amount'] = '2'

        self.send_response(200)
        self.wfile.write(c.output().encode(encoding='utf_8'))
        self.send_header('content-type','text/plain;charset=utf-8')
        #print(c.output())
        self.end_headers()
        resp = "你好！"
        self.wfile.write(resp.encode('utf-8'))

serv = HTTPServer(("",9000), MyRequestHandler)

import threading
d_mon = threading.Thread(target=serv.serve_forever)
d_mon.start()



# 以下代码 仅做语法参考
# def _ _ init _ _ (self,thedict,*args,**kwargs):
# self.thedict = thedict
# BaseHTTPRequestHandler. _ _ init _ _ (self,*args,**kwargs)
# def do_GET(self):
# key = self.path[1:]
# # Strip the leading '/'
# if not key in self.thedict:
# self.send_error(404, "No such key")
# else:
# self.send_response(200)
# self.send_header('content-type','text/plain')
# self.end_headers()
# resp = "Key : %s\n" % key
# resp += "Value: %s\n" % self.thedict[key]
# self.wfile.write(resp.encode('latin-1'))
# Example use
# d = {
# 'name' : 'Dave',
# 'values' : [1,2,3,4,5],
# 'email' : 'dave@dabeaz.com'
# }
# from functools import partial
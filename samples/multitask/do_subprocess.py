#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


print("-"*80)


print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
'''
p.communicate()
请注意，如果要将数据发送到进程的标准输入，则需要使用stdin=PIPE创建Popen对象。类似地，为了在结果元组中不只得到None，你还需要给予stdout=PIPE和/或stderr=PIPE。
参考 官方手册

'''



output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))     # windows
#print(output.decode('utf-8'))   # linux
print('Exit code:', p.returncode)

print("err.decode:",err.decode('gbk'))

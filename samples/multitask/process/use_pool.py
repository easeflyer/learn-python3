#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import multiprocessing
import hashlib

#BUFERSIZE：读取缓冲区大小
#Poolsize：工作进程数量

BUFSIZE=8192
POOLSIZE=2
def compute_digest(filename):
    try:
        f=open(filename,'rb')
    except IOError:
        return None
    digest=hashlib.sha512()
    while True:
        chunk=f.read(BUFSIZE)
        if not chunk:break
        digest.update(chunk)
    f.close()
    return filename,digest.digest()
def build_digest_map(topdir):
    digest_pool=multiprocessing.Pool(POOLSIZE)
    allfiles=(os.path.join(path,name) for path,dirs,files in os.walk(topdir) for name in files )
    digest_map=dict(digest_pool.imap_unordered(compute_digest,allfiles,20))                                           
    digest_pool.close()
    return digest_map
   
if __name__=='__main__':
    digest_map=build_digest_map(r'F:\Anaconda3\Lib\site-packages\sklearn')
    print(len(digest_map))
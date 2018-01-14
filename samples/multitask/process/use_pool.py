#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import multiprocessing
import hashlib
import time

#BUFERSIZE：读取缓冲区大小
#Poolsize：工作进程数量

BUFSIZE=8192
POOLSIZE=4
def compute_digest(filename):           # compute_digest  计算摘要
    '''
    输入：根据带路径的 文件 filename 
    返回：filename,文件的哈希摘要 散列值
    '''
    print("带路径：",filename)
    try:
        f=open(filename,'rb')           # 注意文件已 bytes 方式打开
    except IOError:
        return None
    digest=hashlib.sha512()             # 获得一个 sha512 的散列算法对象，有很多散列算法  digest 摘要对象（散列算法对象）
    #digest=hashlib.md5()
    while True:
        chunk=f.read(BUFSIZE)           # 分块读取内容，进行散列计算
        if not chunk:break              # 直到没有内容了退出
        digest.update(chunk)            # 更新摘要（安全hash）  m.update(a); m.update(b)相当于m.update(ab)。
    f.close()
    #return filename,digest.digest()
    return filename,digest.hexdigest()  # 返回：路径文件名,哈希值

                                        # hash.digest() 返回字节对象
                                        # 返回传递给update()方法的数据的摘要。它是一个大小为digest_size的字节对象，包含的字节可以在0到255整个范围。

                                        # hash.hexdigest() 返回字符串
                                        # 类似digest()，但是摘要以2倍长度的字符串对象返回，只包含十六进制数字。这可用于在电子邮件或其它非二进制环境中安全交换数据

def build_digest_map(topdir):
    '''

    '''
    digest_pool=multiprocessing.Pool(POOLSIZE)
                                        # Poll([numprocess],initializer],initargs])
                                        # numprocess 要创建的进程数, initializer 进程启动时调用的可调用对象，initargs 传递给 initializer 的参数元组
    allfiles=(os.path.join(path,name) for path,dirs,files in os.walk(topdir) for name in files )

                                        # os.walk(目录) 遍历“目录” 返回 path 当前路径， dirs 所有目录, fils所有文件
                                        #         path 是从 topdir 开始到正在遍历目录的路径
                                        #         dirs 是正在遍历的目录下的所有文件夹
                                        #         files 是正在遍历目录下的所有文件
                                        # os.path.join("/",'dir1','dir2','dir3')  /dir1/dir2/dir3
                                        # allfiles 计算结果为：遍历到的 包含完整路径的所有文件，组成的元组

    digest_map=dict(digest_pool.imap_unordered(compute_digest,allfiles,20))         
                                        # imap_unordered() 无序版本的 imap(), imap() 功能类似 map(fun,interable,chuncksize) 对可迭代对象，逐一应用fun，并生成新的迭代器
                                        #           imap() 返回迭代器， map() 返回结果列表逐一区别, 这里可以替换，数量多避免内存挤爆，采用i开头的
                                        #           chuncksize 指定项目数，拆分后交给进程池进程并行 处理。传统的map 是逐一，这里是并行。
                                        # dist(interable) 转换为 字典。
    digest_pool.close()
    return digest_map                   # 函数最后返回这个字典。注意字典的数据由 compute_digest 决定形如：路径:hashstring
   
if __name__=='__main__':
    t = time.time()

    digest_map=build_digest_map(r'./')  # windows 路径为了用反斜杠可以前面加个 r
    print(len(digest_map))
    print(digest_map)

    print('一共用时：',time.time()-t)



'''
总结：本例中进程池的使用
1）首先明确一个需要并行计算的需求，这里的需求是：对大量文件计算散列值，涉及到了大量io
2）pool=multiprocessing.Pool(POOLSIZE)  开启进程池对象
3) imap_unordered(fun,interable,size)  把由n个数据组成的需要用fun 处理的可迭代对象，分成size大小的块，进行并行处理。pool.map() pool.imap() 类似功能。
'''
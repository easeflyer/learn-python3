#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

s = '1'  # 尝试 0,1  下面的 logging.info 都会有输出 ，但上面的错误等级取消后，则不再输出。
n = int(s)
logging.info('n = %d' % n)              # 普通的信息输出记录，只要等级是 info 就会输出
if n == 0:
    logging.error('n 不能为 0')          # 等级低于等于 error 时记录。 不管是 info 还是 error 本质上都是输出。只是在不同的错误等级才会输出。
print(10 / n)


# 有debug，info，warning，error等几个级别
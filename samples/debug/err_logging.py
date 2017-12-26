# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print("---------------")
        logging.exception(e)  # 这里 显示了错误，但程序并没有终止。


main()
print('END')


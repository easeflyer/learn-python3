def fun():
    i = 0
    def count():
        nonlocal i
        i = i + 1
        return i
    return count


f = fun()   # func 返回了一个闭包函数，次函数 引用着 先前 i 的内存区域，每次执行对此区域 进行递增运算

print(f(),f(),f())
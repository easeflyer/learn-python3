'''
上下文管理协议（Context Management Protocol）： 
    __enter__(), __exit__() 所谓协议，其实就是定义数据交换的接口。
    确定了两个方法，就是确定了接口，也就是协议。

上下文管理协议（Context Management Protocol）：
    也就是实现了，以上两个方法的对象。

上下文表达式（Context Expression）：
    with 语句中跟在关键字 with 之后的表达式，该表达式要返回一个上下文管理器对象。

语句体（with-body）：
    在执行语句体之前会调用上下文管理器的 __enter__() 方法，执行完语句体之后会执行 __exit__() 方法。
'''


class Sample:                               # 支持上下文管理协议的对象， 也叫上下文管理器
    def __enter__(self):
        print ("In__enter__()")
        return "Foo"
 
    def __exit__(self, type,value, trace):
        print ("In__exit__()")
 
 
def get_sample():
    return Sample()
 
 
with get_sample() as sample:                # 执行 get_sample() ，并调用 返回对象的 __enter__() 方法，将__enter__()的返回值赋值给 as 后面的 sample 变量
    print("sample:",sample)

# In__enter__()
# sample: Foo
# In__exit__()


print("-"*80)

f = open("err.py")
print("type(f):",type(f))
print ("type:",type((1,2,3)))
with open("err.py") as file:
    print("type(file):",type(file))
    data = file.read()
    print(data)
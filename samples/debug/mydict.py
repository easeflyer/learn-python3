


# Dict 的目的：
# 通过
class Dict(dict):

    def __init__(self, **kw):       # **kw  任意多个 关键字参数
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value   # 给 对象增加属性。给用属性的方式来访问。
        #self.key = value



if __name__ == "__main__":
    d = Dict(a=1,b="b",c="c")
    print (d.b)

    dd = dict(a=1,b="b",c="c")
    # print(dd.b)
    print(dd["c"])
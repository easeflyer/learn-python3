# err_raise.py


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# foo('0')



try:
    foo('0')
except FooError as e:
    print("fooerror:",e)
finally:
    print("finally...")
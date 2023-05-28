def calc(*args):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    return result

print(calc(a=1, b=2, c=3))

'''
执行上面的代码会引发TypeError错误，
错误消息为calc() got an unexpected keyword argument 'a'，
由此可见，*args并不能处理带参数名的参数。
'''
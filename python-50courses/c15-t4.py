'''
我们在设计函数时，如果既不知道调用者会传入的参数个数，
也不知道调用者会不会指定参数名，那么同时使用可变参数和关键字参数。
关键字参数会将传入的带参数名的参数组装成一个字典，
参数名就是字典中键值对的键，而参数值就是字典中键值对的值，代码如下所示。
'''

def calc(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result

print(calc())
print(calc(1,2,3))
print(calc(a=1, b=2, c=3))
print(calc(1,2,c=3,d=4))

'''
提示：不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前，
否则将会引发异常。
例如，执行calc(1, 2, c=3, d=4, 5)将会引发SyntaxError错误，
错误消息为positional argument follows keyword argument，
翻译成中文意思是“位置参数出现在关键字参数之后”。
'''
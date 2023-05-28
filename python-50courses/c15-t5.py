
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        if type(arg) in (int, float):
            result = op(result,arg)
    for value in kwargs.values():
        if type(value) in (int,float):
            result = op(result,value)
    return result

'''
上面的函数增加了两个参数，
其中init_value代表运算的初始值，
op代表二元运算函数。
经过改造的calc函数不仅仅可以实现多个参数的累加求和，
也可以实现多个参数的累乘运算，代码如下所示。
'''

def add(x,y):
    return x + y

def mul(x,y):
    return x * y

'''通过对高阶函数的运用，calc函数不再和加法运算耦合，
所以灵活性和通用性会变强，这是一种解耦合的编程技巧，
但是最初学者来说可能会稍微有点难以理解。需要注意的是，
将函数作为参数和调用函数是有显著的区别的，调用函数需要在函数名后面跟上圆括号，
而把函数作为参数时只需要函数名即可。'''



print(calc(1,2,3,init_value=0,op=add,x=4,y=5))
print(calc(1,2,x=3,y=4,z=5,init_value=1,op=mul))

#本代码和c15-t4对比来看
a = ()
print(type(a))

b = ('hello')
print(type(b))
c = (100)
print(type(c))
d = ('hello',)
print(type(d))
e = (100,)
print(type(e))
'''
但是如果元组中只有一个元素，
需要加上一个逗号，
否则()就不是代表元组的字面量语法，
而是改变运算优先级的圆括号，
所以('hello', )和(100, )才是一元组，
而('hello')和(100)只是字符串和整数。
'''
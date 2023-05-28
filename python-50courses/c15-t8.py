import operator, functools

fac = lambda num: functools.reduce(operator.mul,range(1,num + 1),1)
#定义阶乘函数
is_prime = lambda x:x > 1 and all(map(lambda f: x % f,range(2,int(x ** 0.5) + 1)))
#定义素数判断函数

print(fac(10))
print(is_prime(9))
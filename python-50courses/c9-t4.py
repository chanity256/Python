# 有一种解决变量个数少于元素的个数方法：使用星号表达式
a = 1,10,100,1000
i,j,*k = a
print(i,j,k)

i,*j,k = a
print(i,j,k)

*i,j,k = a
print(i,j,k)

*i,j = a
print(i,j)
i,*j = a
print(i,j)

i,j,k,*l = a
print(i,j,k,l)

i,j,k,l,*m = a
print(i,j,k,l,m)


'''
解包语法对所有的序列都成立，这就意味着对列表
以及我们之前讲到的range函数返回的范围序列都可以使用解包语法。
'''

b,c,*d = range(1,10)
print(b,c,d)
b,c,d = [1,10,100]
print(b,c,d)
b,*c,d = 'hello'
print(b,c,d)
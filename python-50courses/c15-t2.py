'''
调用函数时，如果希望函数的调用者必须以参数名=参数值的方式传参，
可以用命名关键字参数（keyword-only argument）取代位置参数。
所谓命名关键字参数，是在函数的参数列表中，
写在*之后的参数，代码如下所示。
'''

def is_triangle(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and c + a > b

print(is_triangle(a=3, b=4, c=5))
print(is_triangle(c=5, b=4, a=3))

#注意：上面的is_triangle函数，参数列表中的*是一个分隔符，*前面的参数都是位置参数，而*后面的参数就是命名关键字参数。
def is_triangle(a,b,c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b

print(is_triangle(1,2,3))
#不指定参，直接对号入座

print(is_triangle(a=1, b=2, c=3))
#通过“参数名=参数值”按顺序传入

print(is_triangle(c=3, a=1, b=2))
#通过“参数名=参数值”不按顺序传入调用函数时，如果希望函数的调用者必须以参数名=参数值的方式传参，可以用命名关键字参数（keyword-only argument）取代位置参数。所谓命名关键字参数，是在函数的参数列表中，写在*之后的参数，代码如下所示。
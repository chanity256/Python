a = 321
b = 123
c = a*b
print('{} * {} = {}'.format(a, b, a * b))
print(f'{a} * {b} = {c}')
print('%d * %d = %d' % (a, b, a * b))

#三种输出字符串的语法，都是可以的。但是第一种进行格式化操作更方便。

s = 'hello,world'
print(s.center(20,'*'))
print(s.rjust(20))  #默认填充空格
print(s.ljust(20,'-'))

print('33'.zfill(5))
print('-33'.zfill(5))
#zfill似乎只能左填充，默认填充数据数字0
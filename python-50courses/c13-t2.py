#对c13-t1.py的代码进行重构
def fac(num):
    result = 1
    for n in range(1,num + 1):
        result *= n
    return result  
#定义函数，求阶乘，返回num的阶乘（因变量）

m = int(input('m = '))
n = int(input('n = '))

print(fac(m) // fac(n) // fac(m - n))
def is_even(num):
    return num % 2 == 0

def square(num):
    return num ** 2

numbers1 = [35,12,8,99,52]
numbers2 = list(map(square,filter(is_even,numbers1)))
print(numbers2)

'''
高阶函数，我们前面提到过的filter和map函数就是高阶函数，
前者可以实现对序列中元素的过滤，
后者可以实现对序列中元素的映射
'''
#去掉整数列表中的奇数，并对所有偶数平方求得一个新列表
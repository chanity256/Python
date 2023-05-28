numbers1 = [35,12,8,99,52]
numbers2 = list(map(lambda x: x ** 2,filter(lambda x: x % 2 == 0,numbers1)))
print(numbers2)
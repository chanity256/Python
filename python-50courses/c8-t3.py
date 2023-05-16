items1 = [35,12,99,68,55,87]
items2 = [45,8,29]

#列表拼接
items3 = items1 + items2
print(items3)

#列表重复
items4 = ["hello"] * 3
print(items4)

#列表成员的计算
print(900 in items3)
print("hello" in items4)

#获取列表的长度
size = len(items3)
print(size)

#列表的索引
print(items3[0],items3[-size])
items3[-1] = 100
print(items3[size - 1],items3[-1],items3)

#列表的切片
print(items3[:5])
print(items3[4:])
print(items3[-5:-7:-1])
print(items3[::-2])

#列表的比较运算
items5 = [1,2,3,4]
items6 = list(range(1,5))
#比较列表相等性，对应索引位置上的元素是否相等
print(items5 == items6)
items7 = [3,2,1]
#列表大小比较，对应索引位置上的元素大小
print(items5 <= items7)
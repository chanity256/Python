#for循环创建列表
items1 = []
for x in range(1,10):
    items1.append(x)
print(items1)

items2 = []
for x in 'hello world':
    if x not in 'aeiou':
        items2.append(x)
print(items2)

items3 = []
for x in 'abc':
    for y in '12':
        items3.append(x+y)
print(items3)


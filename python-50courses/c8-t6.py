#添加和删除元素
items = ['python','java','go','kotlin','swifit']

#append在尾部添加元素
items.append('swift')
print(items)
#insert在制定索引位置插入元素
items.insert(-4,'sql')
print(items)

#删除指定元素
items.remove('java')
print(items)
#删除指定索引位置的元素
items.pop(0)
items.pop(len(items) - 1)  #这里是删除位移偏量为-1的元素
print(items)

#清空列表里的元素
items.clear()
print(items)

items = ['Python', 'Java', 'Go', 'Kotlin']
del items[-2]
print(items)    # ['Python', 'Go', 'Kotlin']